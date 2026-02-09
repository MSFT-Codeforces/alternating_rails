
import sys
import re

LINE1_RE = re.compile(r"\d+")
CASE_RE = re.compile(r"\d+(?: +\d+){2}")  # exactly 3 non-negative integers separated by 1+ spaces

def is_valid() -> bool:
    data = sys.stdin.read()
    if data == "":
        return False

    lines = data.splitlines()

    # No empty lines; no leading/trailing whitespace on any line; no tabs (enforce spaces as separators)
    for ln in lines:
        if ln == "":
            return False
        if ln != ln.strip():
            return False
        if "\t" in ln:
            return False

    if len(lines) < 1:
        return False

    if not LINE1_RE.fullmatch(lines[0]):
        return False
    try:
        t = int(lines[0])
    except Exception:
        return False

    if not (1 <= t <= 10**4):
        return False

    if len(lines) != t + 1:
        return False

    for i in range(1, t + 1):
        s = lines[i]
        if not CASE_RE.fullmatch(s):
            return False

        parts = s.split(" ")
        # Because we allow 1+ spaces, split(" ") can create empty tokens; reject if any.
        if any(p == "" for p in parts):
            return False
        if len(parts) != 3:
            return False

        try:
            X = int(parts[0])
            Y = int(parts[1])
            K = int(parts[2])
        except Exception:
            return False

        if not (0 <= X <= 10**18):
            return False
        if not (0 <= Y <= 10**18):
            return False
        if not (1 <= K <= 10**9):
            return False

    return True

def main():
    sys.stdout.write("True" if is_valid() else "False")

if __name__ == "__main__":
    main()
