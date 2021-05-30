FREECADPATH = '/usr/lib/freecad/lib'
import sys
sys.path.append(FREECADPATH)
from collections import defaultdict
import FreeCAD
import Mesh
import os

def export_stl(body_obj,filename):
    __objs__=[]
    __objs__.append(FreeCAD.getDocument("rs_winder").getObject(body_obj))
    Mesh.export(__objs__,filename)
    del __objs__

## List of sizes to generate
## Large range  = h=2.8, d=12-18
## Normal range = h=1.6, d=7-12
bowl_d   = ["10.0", "10.5", "11.0", "11.5", "11.8", "12.0", "12.5", "13.0", "13.5", "14.0", "14.5", "15.0"]
spring_d = ["8.0",  "8.5",  "9.0",  "9.5",  "10.0", "10.5", "11.0", "11.5", "12.0", "12.5", "13.0"]

## Open project file and spreadsheet
FreeCAD.openDocument("rs-winder.FCStd")
doc = App.ActiveDocument
sheet = doc.Spreadsheet002

## Create dirs
os.mkdir("Release")
os.mkdir("Release/winder-base")
os.mkdir("Release/housing-barrel")
os.mkdir("Release/barrel-bowl")
os.mkdir("Release/plunger")

## Generate winder base
export_stl("Body002", "Release/winder-base/rs-winder-base-stdsize.stl")

## Generate housing/plunger (based on spring diameter)
for n in spring_d:
    sheet.set("spr_d", n)
    sheet.set("version", n+"MM")
    if len(n) < 4:
        sheet.set("version_x_offs", "-5.50")
    else:
        sheet.set("version_x_offs", "-6.60")
    doc.recompute(None,True,True)
    export_stl("Body", "Release/plunger/rs-winder-plunger-"+n+"mm.stl")
    export_stl("Body001", "Release/housing-barrel/rs-winder-housing-"+n+"mm.stl")

## Generate bowls (based actual barrel diameter)
for n in bowl_d:
    sheet.set("barrel_d", n)
    doc.recompute(None,True,True)
    export_stl("Body003", "Release/barrel-bowl/rs-winder-bowl-"+n+"mm.stl")

