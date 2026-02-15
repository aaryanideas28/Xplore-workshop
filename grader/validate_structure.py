import os
import sys

ALLOWED_TOP_LEVEL = {"tests", "grader", ".github"}
TESTS_DIR = "tests"


def get_pr_author():
    return os.environ.get("GITHUB_ACTOR")


def validate_top_level():
    items = os.listdir(".")

    for item in items:
        if os.path.isdir(item):
            if item in ALLOWED_TOP_LEVEL:
                continue
            if item.endswith("_solutions"):
                continue
            print(f"❌ Invalid top-level directory: {item}")
            sys.exit(1)
        else:
            # Allow README or workflow files if needed
            if item in {"README.md"}:
                continue
            print(f"❌ Invalid top-level file: {item}")
            sys.exit(1)


def validate_user_solution():
    username = get_pr_author()
    expected_folder = f"{username}_solutions"

    if not os.path.isdir(expected_folder):
        print(f"❌ Expected folder '{expected_folder}' not found")
        sys.exit(1)

    test_files = set(os.listdir(TESTS_DIR))
    sol_files = set(os.listdir(expected_folder))

    if test_files != sol_files:
        print("❌ Files inside solution folder do not match tests/")
        sys.exit(1)

    print("✅ Structure Valid")


def main():
    validate_top_level()
    validate_user_solution()
    print("✅ All structure checks passed")


if __name__ == "__main__":
    main()
