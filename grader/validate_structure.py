import os
import sys

TESTS_DIR = "tests"

def get_solution_folder():
    folders = [f for f in os.listdir(".") if os.path.isdir(f)]
    folders = [f for f in folders if f.endswith("_solutions")]
    return folders

def main():
    solution_folders = get_solution_folder()

    if len(solution_folders) != 1:
        print("❌ Invalid: Must contain exactly one *_solutions folder")
        sys.exit(1)

    sol_folder = solution_folders[0]

    test_files = set(os.listdir(TESTS_DIR))
    sol_files = set(os.listdir(sol_folder))

    if test_files != sol_files:
        print("❌ Invalid: Files inside solution folder do not match tests/")
        sys.exit(1)

    print("✅ Structure Valid")

if __name__ == "__main__":
    main()