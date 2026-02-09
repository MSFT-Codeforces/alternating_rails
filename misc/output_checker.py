
import os
import re
from typing import Tuple, List


_DIGITS_RE = re.compile(r"^[0-9]+$")


def _normalize_newlines(s: str) -> str:
    return s.replace("\r\n", "\n").replace("\r", "\n")


def _parse_input(input_text: str) -> Tuple[int, List[Tuple[int, int, int]]]:
    toks = _normalize_newlines(input_text).split()
    if not toks:
        raise ValueError("input is empty")

    try:
        t = int(toks[0])
    except Exception:
        raise ValueError("first token (t) is not an integer")

    if t < 1 or t > 10_000:
        raise ValueError(f"t={t} is out of constraints [1..10000]")

    need = 1 + 3 * t
    if len(toks) < need:
        raise ValueError(f"input has too few integers: expected at least {need}, got {len(toks)}")

    cases: List[Tuple[int, int, int]] = []
    idx = 1
    for ci in range(1, t + 1):
        X = int(toks[idx]); Y = int(toks[idx + 1]); K = int(toks[idx + 2])
        idx += 3
        # Input is normally trusted, but constraints are stated, so validate.
        if not (0 <= X <= 10**18):
            raise ValueError(f"case {ci}: X={X} out of constraints [0..1e18]")
        if not (0 <= Y <= 10**18):
            raise ValueError(f"case {ci}: Y={Y} out of constraints [0..1e18]")
        if not (1 <= K <= 10**9):
            raise ValueError(f"case {ci}: K={K} out of constraints [1..1e9]")
        cases.append((X, Y, K))

    return t, cases


def check(input_text: str, output_text: str) -> Tuple[bool, str]:
    """
    Output checker for Alternating Rails.

    Validates:
      - exact number of output lines (t), one per test case
      - each line contains exactly one non-negative integer in base-10 (digits only)
      - strict whitespace: no leading/trailing spaces on any line
      - allows at most one trailing newline at EOF
      - enforces the explicit statement rule: if (X,Y) = (0,0), answer must be 0

    Does NOT validate that the number is the true minimum ticks for general cases.
    """
    try:
        t, cases = _parse_input(input_text)
    except Exception as e:
        return (False, f"Checker error while parsing input: {e}")

    out = _normalize_newlines(output_text)

    # Allow either:
    #   - no trailing newline, or
    #   - exactly one trailing newline
    if out.endswith("\n"):
        out = out[:-1]
        if out.endswith("\n"):
            return (False, "Output has more than one trailing newline (extra empty line at end)")

    if out == "":
        return (False, f"Expected {t} output lines, got empty output")

    lines = out.split("\n")
    if len(lines) != t:
        return (False, f"Expected exactly {t} output lines (one per test case), got {len(lines)} lines")

    for i, line in enumerate(lines, start=1):
        if line == "":
            return (False, f"Case {i}: empty line; expected a non-negative integer")
        if line != line.strip():
            return (False, f"Case {i}: line has leading/trailing whitespace")
        # Enforce exactly one token: digits only, no internal whitespace.
        if not _DIGITS_RE.fullmatch(line):
            return (False, f"Case {i}: expected a non-negative integer (digits only), got '{line}'")

        ans = int(line)
        X, Y, _K = cases[i - 1]

        # Explicitly stated special case.
        if X == 0 and Y == 0 and ans != 0:
            return (False, f"Case {i}: for (X,Y)=(0,0) the answer must be 0, got {ans}")

        # No further correctness/range checking: the statement does not bound the answer.

    return (True, "OK")


if __name__ == "__main__":
    in_path = os.environ.get("INPUT_PATH", "")
    out_path = os.environ.get("OUTPUT_PATH", "")
    if not in_path or not out_path:
        print("False")
    else:
        with open(in_path, "r", encoding="utf-8") as f:
            input_text_ = f.read()
        with open(out_path, "r", encoding="utf-8") as f:
            output_text_ = f.read()
        ok, _ = check(input_text_, output_text_)
        print("True" if ok else "False")
