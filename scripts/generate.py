#!/usr/bin/env python

import fontforge
import sys

feature_file = "GaramondNo8.fea"

def sfd_to_otf(font):
    font.mergeFeature(feature_file)
    print "generating '%s'" % font.fontname
    font.generate(font.fontname + ".otf", flags=("opentype", "TeX-table", "round"))

if __name__ == "__main__":
    for i in sys.argv[1:]:
        font = fontforge.open(i)
        sfd_to_otf(font)
