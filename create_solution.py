from __future__ import annotations

import keyword
import re
from pathlib import Path


SKIP_DIRS = {".git", ".agents", ".codex", "__pycache__"}


def to_kebab_case(name: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", name.lower())
    return slug.strip("-")


def topic_folders(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.iterdir()
        if path.is_dir() and path.name not in SKIP_DIRS
    )


def choose_folder(folders: list[Path]) -> Path:
    print("Choose a folder:")
    for index, folder in enumerate(folders, start=1):
        print(f"{index}. {folder.name}")

    while True:
        choice = input("Folder number or name: ").strip()
        if not choice:
            print("Please enter a folder number or name.")
            continue

        if choice.isdigit():
            index = int(choice)
            if 1 <= index <= len(folders):
                return folders[index - 1]

        for folder in folders:
            if folder.name == choice:
                return folder

        print("Folder not found. Try again.")


def ask_method_name() -> str:
    while True:
        method_name = input("Solution method name: ").strip()
        if method_name.isidentifier() and not keyword.iskeyword(method_name):
            return method_name
        print("Use a valid Python method name, like twoSum or combinationSum.")


def ask_problem_number() -> str:
    while True:
        problem_number = input("LeetCode problem number: ").strip()
        if problem_number.isdigit() and int(problem_number) > 0:
            return str(int(problem_number))
        print("Use a positive problem number, like 39.")


def ask_problem_title() -> str:
    while True:
        problem_title = input("Problem title: ").strip()
        slug = to_kebab_case(problem_title)
        if slug:
            return slug
        print("Use a problem title, like Combination Sum.")


def solution_template(method_name: str) -> str:
    return f"""class Solution:
    def {method_name}(self, *args):
        pass


def main():
    solution = Solution()
    result = solution.{method_name}()
    print(result)


if __name__ == "__main__":
    main()
"""


def main() -> None:
    root = Path.cwd()
    folders = topic_folders(root)
    if not folders:
        print("No topic folders found.")
        return

    folder = choose_folder(folders)
    problem_number = ask_problem_number()
    problem_slug = ask_problem_title()
    method_name = ask_method_name()
    file_name = f"{problem_number}-{problem_slug}.py"
    path = folder / file_name

    if path.exists():
        print(f"{path} already exists. No file was created.")
        return

    path.write_text(solution_template(method_name))
    print(f"Created {path}")


if __name__ == "__main__":
    main()
