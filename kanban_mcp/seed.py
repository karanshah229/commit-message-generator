from kanban.db import get_db_connection, init_db

def seed_db():
    init_db()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tickets WHERE id IN (123,124,125,126,127)")

    tickets = [
        (
            123,
            "Implement dark mode toggle",
            """**Background:**  
Dark mode has become a common feature in modern applications, offering a more visually comfortable experience in low-light environments. Several users have requested the option to switch between light and dark themes in our application. This feature is especially useful for developers and power users who tend to work during late hours or in environments where dark UIs reduce eye strain.

**Task:**  
Design and implement a toggle switch for dark mode within the application settings page. The dark mode preference should be stored persistently so that it remains consistent across sessions. For authenticated users, persist the preference to their profile in the database. For guest users, fallback to storing the setting in local storage.

**Technical Details:**  
- Use CSS custom properties (variables) or a Tailwind theme extension for color management.
- Implement the toggle as a UI switch component.
- Update the layout and major UI components to respect the selected theme.
- Ensure compatibility with both desktop and mobile views.
- Add animations for smooth theme transitions if possible.

**Acceptance Criteria:**  
- Users can toggle between dark and light modes via a settings toggle.
- The selected theme persists across reloads and logins.
- UI components like buttons, modals, and text fields must adapt to the selected theme.
- No visual glitches or accessibility regressions.
""",
            "todo"
        ),
        (
            124,
            "Fix login redirect bug",
            """**Background:**  
Users are expected to be redirected to their originally requested page after logging in. However, users are currently redirected to the home page regardless of the intended destination. This is a usability issue, particularly for users trying to access protected content such as workspace dashboards, document editing pages, or specific tickets from shared URLs.

**Bug Description:**  
When a non-authenticated user attempts to visit a protected route, the app redirects them to the login page. After login, instead of returning them to the originally intended route, the system sends them to the default landing page (`/home`). This happens across both web and mobile views.

**Technical Investigation:**  
Session or route state is likely being lost between redirection flows. Examine how the `redirectTo` state is handled in middleware/auth guards. The value should be captured on the unauthenticated access attempt and carried forward through the login process.

**Expected Behavior:**  
- If a user visits `/projects/42/kanban` without being authenticated, they should log in and be redirected to `/projects/42/kanban`.
- If a user manually visits the login page, they should still be taken to the default home after login.

**Acceptance Criteria:**  
- Fix should work across both SSR and CSR paths.
- Unit tests cover login flow and destination routing.
- Add QA test plan covering protected routes, direct logins, and shared link scenarios.
""",
            "in_progress"
        ),
        (
            125,
            "Integrate GitHub OAuth",
            """**Background:**  
Many of our users are developers and would prefer to sign up and log in using their GitHub accounts rather than creating new credentials. GitHub OAuth integration would lower friction and speed up onboarding.

**Task:**  
Implement GitHub OAuth login flow using GitHub's OAuth 2.0 API. Users who choose this method should be redirected to GitHub’s authorization page. Upon successful authentication, GitHub should redirect them back with a code, which we exchange for an access token and use to fetch the user profile.

**Details:**  
- Create a GitHub OAuth App and configure `client_id`, `client_secret`, and callback URL.
- Add a new "Sign in with GitHub" button on the login page.
- Store GitHub user ID and email in our user profile table.
- If a GitHub user already exists in our system (based on email or GitHub ID), log them in.
- If it’s their first time, create a new account.

**Security:**  
- Ensure that OAuth tokens are not stored beyond what’s necessary.
- Use secure cookies or token-based authentication for our sessions.
- Ensure CSRF protection on the callback handler.

**Acceptance Criteria:**  
- Users can log in via GitHub and are redirected to the app dashboard.
- Existing users with a GitHub email are matched and logged in correctly.
- New users get a profile auto-created and prompted to complete onboarding.
""",
            "todo"
        ),
        (
            126,
            "Improve mobile responsiveness of dashboard",
            """**Background:**  
The dashboard is one of the most visited screens in our product. However, several usability issues have been reported when viewing it on small screens (<400px wide), particularly on older Android devices. Cards overflow the screen width, and action buttons overlap.

**Task:**  
Refactor the dashboard layout and its components to ensure responsive behavior. All elements should resize or stack appropriately depending on the viewport. Use a mobile-first approach.

**Details:**  
- Convert card grid to a column layout below 600px.
- Ensure buttons and links have adequate tap targets (>48px height).
- Avoid fixed widths and use `flex-wrap`, `min-width`, and `overflow` controls where applicable.
- Test on Chrome DevTools with iPhone SE and Galaxy S8 profiles.

**Acceptance Criteria:**  
- The layout works well on devices as small as 360px wide.
- No horizontal scrolling unless in overflow containers.
- Text truncation and button spacing are visually clean.
- Visual QA across all major breakpoints is complete.
""",
            "done"
        ),
        (
            127,
            "Resolve intermittent crash in notification service",
            """**Background:**  
Multiple users have reported that their app occasionally crashes when receiving new notifications. This issue is intermittent, with no clear reproduction steps, but seems more frequent on devices with unstable network connections or high latency.

**Symptoms:**  
- On some occasions, the notification list fails to load or refresh.
- Users see a generic error modal or the app freezes momentarily.
- No logs appear in the UI, but server logs show occasional 500 errors from the notification service.

**Investigation Path:**  
- Review the notification API client — are errors handled properly?
- Audit the backend fetch logic: are we using `await` correctly, and is there any race condition during simultaneous fetch + UI render?
- Test how the service behaves when the database returns null, empty, or malformed records.

**Fix Approach:**  
- Add retry logic for the notification fetch endpoint.
- Validate data formats and sanitize before rendering.
- Improve error logging so future crashes are traceable via telemetry.

**Acceptance Criteria:**  
- No crashes during notification refresh, even under poor network conditions.
- User is shown an informative error if the fetch fails, with a retry option.
- Backend and frontend logs provide full context for future incidents.
""",
            "in_progress"
        ),
    ]

    for id, title, description, status in tickets:
        cursor.execute(
            "INSERT INTO tickets (id, title, description, status) VALUES (?, ?, ?, ?)",
            (id, title, description, status)
        )

    conn.commit()
    conn.close()
    print("Database seeded successfully with 5 detailed developer tickets.")

if __name__ == "__main__":
    seed_db()
