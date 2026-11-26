#!/usr/bin/env python3
"""Explain effective values across explicitly supplied Git-style config files."""
import argparse
import json
import re
import sys
from pathlib import Path

SECTION = re.compile(r'^\s*\[\s*([A-Za-z0-9.-]+)(?:\s+"((?:\\.|[^"])*)")?\s*\]\s*(?:[#;].*)?$')
KEY = re.compile(r'^\s*([A-Za-z0-9.-]+)\s*(?:=\s*(.*))?$')

def parse_config(path):
    values = {}
    section, subsection = None, None
    for line_number, raw in enumerate(Path(path).read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith(("#", ";")):
            continue
        match = SECTION.match(raw)
        if match:
            section = match.group(1).lower()
            subsection = match.group(2)
            continue
        match = KEY.match(raw)
        if match and section:
            key = match.group(1).lower()
            value = (match.group(2) or "true").strip()
            if len(value) >= 2 and value[0] == value[-1] == '"':
                value = value[1:-1].replace(r'\"', '"').replace(r'\\', '\\')
            identity = (section, subsection, key)
            values[identity] = {"value": value, "line": line_number}
    return values

def analyze(paths):
    effective = {}
    history = []
    for path in paths:
        for identity, item in parse_config(path).items():
            section, subsection, key = identity
            label = section + (f'.{subsection}' if subsection is not None else "") + "." + key
            previous = effective.get(identity)
            if previous:
                history.append({"key": label, "overridden_source": previous["source"], "winning_source": str(path)})
            effective[identity] = {"key": label, "value": item["value"], "source": str(path), "line": item["line"]}
    return sorted(effective.values(), key=lambda item: item["key"]), history

def main():
    parser = argparse.ArgumentParser(description="Compare supplied Git-style config files from low to high precedence.")
    parser.add_argument("files", nargs="+", help="configuration files in precedence order")
    parser.add_argument("--json", action="store_true", help="print JSON")
    args = parser.parse_args()
    try:
        effective, history = analyze(args.files)
    except OSError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps({"effective": effective, "overrides": history}, indent=2))
    else:
        print("Effective Git-style configuration:")
        for item in effective:
            print(f"{item['key']} = {item['value']}  [{item['source']}:{item['line']}]")
        if history:
            print("\nOverrides:")
            for item in history:
                print(f"- {item['key']}: {item['winning_source']} overrides {item['overridden_source']}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
