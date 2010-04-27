#!/usr/bin/env python

import sys
import fontforge

feature_file = "GaramondNo8.fea"

def slant(file):
    f = fontforge.open(file)
    f.mergeFeature(feature_file)
    f.italicize(italic_angle = -16)

    new_fullname = ' '.join(f.fullname.split()[:-1] + ['Slanted'])
    new_fontname = '-'.join(f.fullname.split()[:-1] + ['Slanted'])

    f.fontname = new_fontname
    f.fullname = new_fullname

    # f.simplify(flags=("ignoreslopes", "ignoreextrema", "smoothcurves",
    #                   "choosehv", "forcelines", "nearlyhvlines",
    #                   "mergelines", "setstarttoextremum"))
    # f.round()
    # f.addExtrema()

    f.generate(f.fontname + ".otf", flags=("opentype", "TeX-table", "round"))
    f.close()

if __name__ == "__main__":
    for i in sys.argv[1:]:
        slant(i)
