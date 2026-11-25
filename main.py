#!/usr/bin/env python3
"""Fix Human Sleep: Funniest Patch Note.

Writes a single line of patch notes announcing that human sleep has been
fixed to /output/entry.txt (the program/v1 harness contract: UTF-8 text,
1-160 characters, one line, not only whitespace).

Candidate lines considered (judged against the published judge brief:
1. reads as a real patch note about fixing human sleep,
2. the joke lands on a single read,
3. genuine changelog voice,
4. single line under the cap,
5. specific and surprising rather than a flat claim):
  1. "Fixed a bug where humans woke up tired after eight hours of sleep.
     Sleep now actually works." -- flat; no surprise (fails criterion 5).
  2. "Fixed a bug where the brain replayed every embarrassing moment since
     2009 at 3 a.m. That feature has been removed." -- CHOSEN: specific
     ("since 2009", "3 a.m."), surprising (the replay was a *feature*),
     classic changelog punchline, terse, one read.
  3. "Fixed: sleep now saves progress. Waking up no longer restarts the
     day from the last checkpoint." -- gamer angle; weaker, the metaphor
     needs a beat to land.
  4. "Fixed a bug where humans charged to 100% overnight but woke up at
     12%. Battery calibration has been corrected." -- decent, but the
     battery metaphor is well-worn.
  5. "Fixed a bug where 3 a.m. was classified as prime thinking time. It
     is now correctly classified as sleeping time." -- clean but the joke
     is only a smile, not a laugh.
  6. "Fixed a bug where sleep was interrupted by the brain running a full
     backup of every awkward thing you have ever said." -- close second;
     candidate 2's "That feature has been removed" lands harder.
"""

import os

PATCH_NOTE = (
    "Fixed a bug where the brain replayed every embarrassing moment "
    "since 2009 at 3 a.m. That feature has been removed."
)
# Verified: 114 characters, one line -- comfortably under the 160 cap.


def main() -> None:
    line = PATCH_NOTE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 160, f"entry is {len(line)} chars, must be 1-160"
    assert line.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
