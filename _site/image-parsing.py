#!/usr/bin/env python3

import os


BASE_DIR = "/Users/ak27/programming/personal/anton-khodak.github.io/assets/images/scotland"

JEKYLL_STATIC_BASE = "/assets/images/scotland/"

with open("result.txt", "w") as f:
    files = [os.path.join(BASE_DIR, f) for f in os.listdir(BASE_DIR)]
    files.sort(key=os.path.getmtime)
    for img in files:
        f.write(f"![]({JEKYLL_STATIC_BASE}{os.path.basename(img)})\n")


