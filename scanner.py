import sys
import re

def scan_solidity(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
        sys.exit(1)

    findings = []

    for line_no, line in enumerate(lines, start=1):
        # 1. Reentrancy risk (low-level call)
        if re.search(r"\.call\s*\{", line) or re.search(r"\.call\s*\(", line):
            findings.append(f"⚠️ Reentrancy risk at line {line_no}")

        # 2. tx.origin usage
        if "tx.origin" in line:
            findings.append(f"⚠️ tx.origin used at line {line_no}")

        # 3. Unchecked external call
        if "call{" in line and "require" not in line:
            findings.append(f"⚠️ Unchecked external call at line {line_no}")

    return findings


def main():
    if len(sys.argv) < 2:
        print("Usage: python scanner.py <solidity_file>")
        sys.exit(1)

    file_path = sys.argv[1]

    print(f"🔍 Scanning: {file_path}\n")

    results = scan_solidity(file_path)

    if results:
        print("⚠️ Vulnerabilities found:\n")
        for r in results:
            print(r)
    else:
        print("✅ No obvious vulnerabilities detected")


if __name__ == "__main__":
    main()
