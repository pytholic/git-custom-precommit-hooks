#!/bin/sh
# Create by @pytholic on 2024.03.27.

# Reject pushes that contain commits with messages that do not match out requried format.
# e.g. [<semantic-commit-type>][MOPS-XXXX] comment body
#
# Also make sure this issue number and the branch name are same.


set -e

echo "The commit-msg hook is running..."

msg_regex='^\[(feat|fix|docs|style|refactor|test|chore)\]\[MOPS-[0-9]+\] .+$'
COMMIT_MSG_FILE=$1

# Get the current branch name
current_branch=$(git rev-parse --abbrev-ref HEAD)

# Get ticket number from commit message
pattern='MOPS-[0-9]{3}'
ticket_number=$(cat "${COMMIT_MSG_FILE}" | grep -Eo "$pattern" || true)

# Run the check
if ! grep -Eq "${msg_regex}" "${COMMIT_MSG_FILE}" || [ -z "${ticket_number}" ] || [ "${current_branch}" != ${ticket_number} ]; then
    echo "Error: Commit message must follow the format: [<semantic-commit-type>][MOPS-XXXX] comment body"
    echo "Valid semantic commit types are: [feat, fix, docs, style, refactor, test, chore]"
    echo "Branch name should be same as the ticket number."
    echo "e.g., [feat][MOPS-123] Added tests for the function."
    exit 1
fi

echo "Commit message is valid."
exit 0
