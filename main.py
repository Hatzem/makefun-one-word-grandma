"""One Word From Grandma — make.fun entry.

Writes the single word a grandma would text about AI to /output/entry.txt.

The word is "contraption": the warm, slightly baffled name a grandmother
gives any clever machine she does not quite trust but loves anyway. It is
funny standing alone, it only fits a machine, and it is not the obvious pick.
"""

import os

WORD = "contraption"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(WORD)


if __name__ == "__main__":
    main()
