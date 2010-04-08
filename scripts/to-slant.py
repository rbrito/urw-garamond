#!/usr/bin/env python

import sys
import fontforge

# Does not work and generates an internal error in fontforge
def slant_not_working(file):
    f = fontforge.open(file)
    f.selection.all()
    f.italicize(italic_angle = -16)
    f.generate(f.fullname + ".otf", flags=("opentype", "TeX-table", "round"))
    f.close()

# Works, but some messages are output
# (perhaps something is being done incorrectly?)
def slant(file):
    f = fontforge.open(file)
    f.selection.all()
    f.copy()
    g = fontforge.font()
    g.selection.all()
    g.paste()
    g.italicize(italic_angle = -16)
    g.generate(f.fullname + ".otf", flags=("opentype", "TeX-table", "round"))
    g.close()
    f.close()

if __name__ == "__main__":
    for i in sys.argv[1:]:
        slant(i)
