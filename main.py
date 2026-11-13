import os

OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as f:
    f.write("My AI coding agent fixed the bug by deleting the feature, the tests, and \u2014 for consistency \u2014 my will to live.")
