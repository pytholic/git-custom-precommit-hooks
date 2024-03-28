import subprocess
import tempfile


# Define the function to test the commit message format
def test_commit_msg(commit_msg):
    # Write the commit message to a temporary file
    tmp_file = tempfile.NamedTemporaryFile(mode="w", delete=True)
    tmp_file.write(commit_msg)
    tmp_file.flush()  # Ensure the file is written to disk

    # Run the commit-msg hook script with the temporary file as argument
    result = subprocess.run(
        ["../custom-hooks/commit_msg_hook.sh", tmp_file.name], capture_output=True, text=True
    )
    exit_code = result.returncode

    # Check the exit code of the script
    print(f"Commit Message: {commit_msg}")
    if exit_code == 0:
        print("Test PASSED.")
    else:
        print("Test FAILED.")

    print("*" * 50)

    # Clean up the temporary file
    tmp_file.close()


if __name__ == "__main__":

    # Get current git branch
    output = subprocess.check_output(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"], universal_newlines=True
    )
    current_branch = output.strip()
    # Define the commit messages to test
    commit_messages = [
        "[feat][MOPS-123] commit body",
        "[feat][MOPS-321]commit body",
        "[feat][MOPS-123]",
        "[feat]commit body",
        "[test][MOPS] commit body",
        "[abc][MOPS-abx] commit body",
        f"[abc][{current_branch}] commit body",
        f"[feat][{current_branch}]commit body",
        f"[test][{current_branch}] commit body",
        f"[docs][{current_branch}] commit body",
    ]

    # Run the tests for each commit message
    for commit_msg in commit_messages:
        test_commit_msg(commit_msg)
