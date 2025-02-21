#!/usr/bin/env python3
"""Script to customize the pypackage_template for a new project."""

import argparse
import os
import re
from pathlib import Path
from typing import Dict, List

def update_file_content(file_path: Path, replacements: Dict[str, str]) -> None:
    """Update file content with given replacements."""
    if not file_path.exists():
        return
    
    content = file_path.read_text()
    for old, new in replacements.items():
        content = content.replace(old, new)
    file_path.write_text(content)

def update_directory_name(old_name: str, new_name: str, base_path: Path) -> None:
    """Rename directory while maintaining its contents."""
    old_dir = base_path / 'src' / old_name
    new_dir = base_path / 'src' / new_name
    if old_dir.exists():
        old_dir.rename(new_dir)

def main() -> None:
    """Main function to customize the template."""
    parser = argparse.ArgumentParser(description="Customize package template")
    parser.add_argument("--name", required=True, help="New package name")
    parser.add_argument("--author", required=True, help="Author name")
    parser.add_argument("--email", required=True, help="Author email")
    parser.add_argument("--description", required=True, help="Package description")
    parser.add_argument("--github-username", required=True, help="GitHub username")
    args = parser.parse_args()

    # Define replacements
    replacements = {
        "pypackage_template": args.name,
        "Marcus Sherman": args.author,
        "m.sherman@northeastern.edu": args.email,
        "A fully featured Python package template": args.description,
        "betteridiot": args.github_username,
    }

    # Files to update
    files_to_update = [
        Path("pyproject.toml"),
        Path("README.md"),
        Path("docs/source/conf.py"),
        Path(".github/workflows/ci.yml"),
        Path(".github/workflows/docs.yml"),
        Path(".github/workflows/publish.yml"),
        Path("CONTRIBUTING.md"),
        Path("LICENSE"),
    ]

    # Update each file
    for file_path in files_to_update:
        update_file_content(file_path, replacements)

    # Rename the package directory
    update_directory_name("pypackage_template", args.name, Path.cwd())

    # Update import statements in Python files
    python_files = list(Path("src").rglob("*.py")) + list(Path("tests").rglob("*.py"))
    for py_file in python_files:
        update_file_content(py_file, replacements)

    print(f"""
Template customization complete!
Next steps:
1. Review the changes
2. Initialize git repository: git init
3. Create initial commit: git add . && git commit -m "feat: initial commit"
4. Create initial tag: git tag v0.1.0
5. Install development dependencies: poetry install --with dev,docs,test,build
6. Setup pre-commit hooks: pre-commit install --install-hooks
""")

if __name__ == "__main__":
    main()
