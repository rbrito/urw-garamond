#!/usr/bin/env python

import sys
import fontforge

def ps_to_otf(file):
    f = fontforge.open(file)
    #f.save(f.fullname+".orig")
    #f.addSmallCaps()
    #f.mergeFeature(file_with_extra_info)
    #f.simplify()
    #f.round()
    f.save()
    f.generate(f.fullname + ".new.otf", flags=("opentype", "TeX-table", "round"))
    f.close()

def ttf_to_otf(file):
    f = fontforge.open(file)
    f.save(f.fullname+".orig")
    #f.addSmallCaps()
    f.layers["Fore"].is_quadratic = False
    f.selection.all()
    f.simplify()
    f.autoHint()
    f.selection.none()
    #f.simplify()
    #f.round()
    f.save()
    f.generate(f.fullname + ".otf", flags=("opentype", "TeX-table", "round"))
    f.close()

def ps_to_ttf(file):
    f = fontforge.open(file)
    f.save(f.fullname+".orig")
    #f.addSmallCaps()
    f.layers["Fore"].is_quadratic = True
    f.selection.all()
    f.autoInstr()
    f.selection.none()
    #f.simplify()
    #f.round()
    f.save()
    f.generate(f.fullname + ".ttf")
    f.close()

if __name__ == "__main__":
    for i in sys.argv[1:]:
        ps_to_otf(i)
