#!/bin/bash

cat << 'EOF' > .git/hooks/pre-push
#!/bin/bash

blocked_branches=("feat-311" "feat-317" "fix-359" "feat-452")

while read local_ref local_sha remote_ref remote_sha; do
  [ -z "$local_ref" ] && continue
  branch_name=$(basename "$local_ref")
  for blocked in "${blocked_branches[@]}"; do
    if [[ "$branch_name" == "$blocked" ]]; then
      echo "🚫 Push blocked: Branch '$branch_name' is not allowed to be pushed."
    fi
  done
done

exit 0
EOF

chmod +x .git/hooks/pre-push