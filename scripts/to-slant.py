#!/usr/bin/env python

import sys
import fontforge

feature_file = "GaramondNo8.fea"

def slant(file):
    f = fontforge.open(file)
    f.mergeFeature(feature_file)
    f.italicize(italic_angle = -16)
    f.generate(f.fullname + ".otf", flags=("opentype", "TeX-table", "round"))
    f.close()

if __name__ == "__main__":
    for i in sys.argv[1:]:
        slant(i)
