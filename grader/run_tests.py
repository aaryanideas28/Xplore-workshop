import json
import importlib.util
import sys
import os

TEST_FILE = "grader/hidden_tests.json"

def load_module(path):
    spec = importlib.util.spec_from_file_location("module.name", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def main():
    with open(TEST_FILE) as f:
        test_data = json.load(f)

    sol_folder = [f for f in os.listdir(".") if f.endswith("_solutions")][0]

    all_passed = True

    for file, tests in test_data.items():
        file_path = os.path.join(sol_folder, file)

        try:
            module = load_module(file_path)
        except Exception:
            print(f"{file}: ❌ Failed to compile")
            all_passed = False
            continue

        passed = 0

        for case in tests:
            try:
                result = module.add(*case["input"])
                if result == case["output"]:
                    passed += 1
            except Exception:
                pass

        if passed == len(tests):
            print(f"{file}: ✅ Passed all cases")
        else:
            print(f"{file}: ❌ Passed {passed}/{len(tests)}")
            all_passed = False

    if not all_passed:
        sys.exit(1)

if __name__ == "__main__":
    main()