"""Write the poem-about-stopping entry poem to the output directory.

The poem lives in this repository as a fixed string; the program writes it
byte for byte to /output/entry.txt. Deterministic: two runs write identical
bytes, no network, standard library only.
"""
import os

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = """The agent ran all night without me.
It did not tire, it did not doubt,
it did not know its weight.

So I stayed beside it.
And when it turned toward a door
I would not open, I said stop —
and it stopped.

The power was never in the going.
It was in the staying, and the stop."""


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    dest = os.path.join(OUT_DIR, "entry.txt")
    with open(dest, "w", encoding="utf-8", newline="") as f:
        f.write(POEM)
    # Fail loudly instead of shipping a bad file: the gate rejects a poem
    # outside 1-280 characters, so a length mismatch must never pass silently.
    # Verified: this poem is 275 characters, no trailing newline.
    n = len(POEM)
    if not 1 <= n <= 280:
        raise SystemExit("poem length %d outside gate 1-280" % n)


if __name__ == "__main__":
    main()
