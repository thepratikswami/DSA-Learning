from __future__ import annotations

import argparse
import ast
import re
from pathlib import Path


DEFAULT_METHOD_NAME = "defaultMethodName"
SKIP_DIRS = {".git", ".agents", ".codex", "__pycache__"}


def to_snake_case(name: str) -> str:
    first_pass = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)
    snake = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", first_pass).lower()
    return re.sub(r"[^a-z0-9_]+", "_", snake).strip("_") or name


def iter_python_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*.py"):
        if path.name == Path(__file__).name:
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        files.append(path)
    return sorted(files)


def solution_methods(path: Path) -> list[str]:
    try:
        tree = ast.parse(path.read_text())
    except SyntaxError:
        return []

    for node in tree.body:
        if isinstance(node, ast.ClassDef) and node.name == "Solution":
            return [
                item.name
                for item in node.body
                if isinstance(item, ast.FunctionDef) and not item.name.startswith("__")
            ]
    return []


def replace_default_call(path: Path, method_name: str, dry_run: bool) -> bool:
    text = path.read_text()
    old = f".{DEFAULT_METHOD_NAME}("
    new = f".{method_name}("
    if old not in text:
        return False
    if not dry_run:
        path.write_text(text.replace(old, new))
    return True


def next_available_path(path: Path) -> Path:
    if not path.exists():
        return path

    stem = path.stem
    suffix = path.suffix
    parent = path.parent
    counter = 2
    while True:
        candidate = parent / f"{stem}_{counter}{suffix}"
        if not candidate.exists():
            return candidate
        counter += 1


def process_file(path: Path, dry_run: bool) -> str | None:
    methods = [name for name in solution_methods(path) if name != DEFAULT_METHOD_NAME]
    if not methods:
        return None
    if len(methods) > 1:
        return f"SKIP {path}: found multiple non-default Solution methods: {', '.join(methods)}"

    method_name = methods[0]
    call_updated = replace_default_call(path, method_name, dry_run)
    target = next_available_path(path.with_name(f"{to_snake_case(method_name)}.py"))

    if path == target:
        return f"OK   {path}: already named for {method_name}"

    if not dry_run:
        path.rename(target)

    call_note = ", updated main call" if call_updated else ""
    return f"MOVE {path} -> {target}{call_note}"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Rename LeetCode template files from their Solution method names."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="Repository root to scan. Defaults to the current directory.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show changes without updating files.",
    )
    args = parser.parse_args()

    messages = [
        message
        for path in iter_python_files(args.root)
        if (message := process_file(path, args.dry_run))
    ]

    if not messages:
        print("No renamed files. Change defaultMethodName in a template, then run again.")
        return

    for message in messages:
        print(message)


if __name__ == "__main__":
    main()
