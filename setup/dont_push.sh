cat << 'EOF' > .git/hooks/pre-push
#!/usr/bin/bash

current_branch=$(git rev-parse --abbrev-ref HEAD)

if [[ "$current_branch" == "feat-311" || "$current_branch" == "feat-317" || "$current_branch" == "fix-359" || "$current_branch" == "feat-452" ]]; then 
  echo "Don't push this branch"
  exit 1
fi
EOF

chmod +x .git/hooks/pre-push
