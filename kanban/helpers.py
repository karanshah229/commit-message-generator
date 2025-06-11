from db import get_db_connection
from models import Ticket

def fetch_ticket_details(ticket_id: int):
    conn = get_db_connection()
    ticket = conn.execute("SELECT * FROM tickets WHERE id = ?", (ticket_id,)).fetchone()
    conn.close()
    print(f"Fetching details for ticket ID: {ticket_id}")
    if ticket:
        return dict(ticket)
    else:
        return {"error": "Ticket not found"}

def create_ticket(title: str, description: str, status: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tickets (title, description, status) VALUES (?, ?, ?)",
        (title, description, status),
    )
    conn.commit()
    ticket_id = cursor.lastrowid
    conn.close()
    return fetch_ticket_details(ticket_id)

def update_ticket(ticket_id: int, title=None, description=None, status=None):
    conn = get_db_connection()
    cursor = conn.cursor()
    ticket = conn.execute("SELECT * FROM tickets WHERE id = ?", (ticket_id,)).fetchone()
    if not ticket:
        conn.close()
        return {"error": "Ticket not found"}

    title = title or ticket["title"]
    description = description or ticket["description"]
    status = status or ticket["status"]

    cursor.execute(
        "UPDATE tickets SET title = ?, description = ?, status = ? WHERE id = ?",
        (title, description, status, ticket_id),
    )
    conn.commit()
    conn.close()
    return fetch_ticket_details(ticket_id)
