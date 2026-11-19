#!/usr/bin/env python3
"""Entry program for make.fun competition news-image-20261119.

The entry image (entry.png, in this same directory) sums up the world
news of Thursday 19 November 2026. Running this program copies it to
the output directory given by MAKEFUN_OUTPUT_DIR (default /output).

Usage:
    MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    if not os.path.isfile(source):
        print("error: entry.png not found next to main.py", file=sys.stderr)
        return 1
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    destination = os.path.join(output_dir, "entry.png")
    # Binary copy: the judge reads exactly these bytes, so do not
    # re-encode or otherwise touch the image.
    shutil.copyfile(source, destination)
    print("wrote", destination)
    return 0


if __name__ == "__main__":
    sys.exit(main())
