import sys
from pathlib import Path


def main():
    print("Running Python code quality check...")

    forbidden_text = "debug"
    python_files = list(Path(".").glob("*.py"))

    for file_path in python_files:
        if file_path.name == "check_code.py":
            continue

        content = file_path.read_text()

        if forbidden_text in content:
            print(f"Check failed: found forbidden word '{forbidden_text}' in {file_path}")
            sys.exit(1)

    print("All checks passed.")
    sys.exit(0)


if __name__ == "__main__":
    main()