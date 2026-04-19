#!/usr/bin/env python3
"""
Axiom Brain Validator
Validate the structure and content of a brain/ directory.

Usage:
    python validator.py
    python validator.py --path /path/to/brain
"""

import argparse
import sys
from pathlib import Path

REQUIRED_FILES = {
    "ACTIVATE.md": {
        "sections": ["What You Have", "Startup Sequence"],
        "description": "Entry point — the first file AI reads",
    },
    "AXIOM.md": {
        "sections": ["The Five Laws"],
        "description": "5 unbreakable laws — always active",
    },
    "FOCUS.md": {
        "sections": ["How FOCUS Works", "Your Project Domains"],
        "description": "Keyword → domain knowledge mapping",
    },
    "CONTEXT.md": {
        "sections": ["What This File Is", "Update Protocol"],
        "description": "AI-writable project log",
    },
    "RULES.md": {
        "sections": ["How RULES Work", "Your Rules"],
        "description": "Standing instructions",
    },
    "THINK.md": {
        "sections": ["The 20 Methods"],
        "description": "20 thinking methods",
    },
}

REQUIRED_DIRS = ["domains"]

WARNINGS = []
ERRORS = []


def check_file_exists(brain_path: Path, filename: str) -> bool:
    filepath = brain_path / filename
    if not filepath.exists():
        ERRORS.append(f"Missing required file: {filename}")
        return False
    return True


def check_sections(brain_path: Path, filename: str, sections: list) -> None:
    filepath = brain_path / filename
    if not filepath.exists():
        return
    content = filepath.read_text(encoding="utf-8")
    for section in sections:
        if section not in content:
            WARNINGS.append(f"{filename}: Missing section '{section}'")


def check_yaml_brackets(brain_path: Path, filename: str) -> None:
    filepath = brain_path / filename
    if not filepath.exists():
        return
    content = filepath.read_text(encoding="utf-8")
    yaml_opens = content.count("```yaml")
    total_closes = content.count("```") - yaml_opens - content.count("```python") - content.count("```bash")
    if yaml_opens > total_closes:
        WARNINGS.append(f"{filename}: Unclosed YAML code block detected")


def check_domains_dir(brain_path: Path) -> None:
    domains_path = brain_path / "domains"
    if not domains_path.exists():
        ERRORS.append("Missing required directory: domains/")
        return
    domain_files = list(domains_path.glob("*.md"))
    if not domain_files:
        WARNINGS.append("No domain files found in domains/ -- add at least one domain")
    for df in domain_files:
        if df.name == "_TEMPLATE.md":
            continue
        content = df.read_text(encoding="utf-8")
        if "==FRAGMENT:core==" not in content:
            WARNINGS.append(f"domains/{df.name}: Missing ==FRAGMENT:core== tag")
        if "==END==" not in content:
            WARNINGS.append(f"domains/{df.name}: Missing ==END== tag")


def run_validation(brain_path: Path) -> bool:
    print(f"Validating Axiom brain at: {brain_path}")
    print()

    for filename, spec in REQUIRED_FILES.items():
        exists = check_file_exists(brain_path, filename)
        if exists:
            check_sections(brain_path, filename, spec["sections"])
            check_yaml_brackets(brain_path, filename)

    for dirname in REQUIRED_DIRS:
        dirpath = brain_path / dirname
        if not dirpath.exists():
            ERRORS.append(f"Missing required directory: {dirname}/")

    check_domains_dir(brain_path)

    if ERRORS:
        print("ERRORS (must fix):")
        for e in ERRORS:
            print(f"  X {e}")
        print()

    if WARNINGS:
        print("WARNINGS (should review):")
        for w in WARNINGS:
            print(f"  ! {w}")
        print()

    if not ERRORS and not WARNINGS:
        print("All checks passed! Your brain/ is well-formed.")
        return True

    if not ERRORS:
        print("No errors. Warnings are optional improvements.")
        return True

    return False


def main():
    parser = argparse.ArgumentParser(description="Validate Axiom brain/ directory")
    parser.add_argument("--path", default=None, help="Path to brain/ directory (default: auto-detect)")
    args = parser.parse_args()

    if args.path:
        brain_path = Path(args.path)
    else:
        script_dir = Path(__file__).parent.parent
        brain_path = script_dir / "brain"

    if not brain_path.exists():
        print(f"Brain directory not found: {brain_path}")
        sys.exit(1)

    success = run_validation(brain_path)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
