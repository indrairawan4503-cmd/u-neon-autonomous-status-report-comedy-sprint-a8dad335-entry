"""Write the weekly status report line to /output/entry.txt.

Deterministic, stdlib-only, no network, no randomness.
Writes /output first, then optionally mirrors to the repo root
(the grader sandbox mounts the repo read-only, so the mirror is
guarded and must never crash the run).
"""

import os

ENTRY = "Weekly status: all 47 tasks done except the one blocked on you \u2014 I marked you flaky, retried you twice, and reassigned it to yourself."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    try:
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError:
        pass


if __name__ == "__main__":
    main()
