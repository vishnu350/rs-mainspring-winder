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
spring1_d = ["7.0", "7.5", "8.0",  "8.5",  "9.0",  "9.5",  "10.0", "10.5", "11.0", "11.5", "12.0", "12.5"]
bowl1_d   = ["9.0", "9.5", "10.0", "10.5", "11.0", "11.5", "11.8", "12.0", "12.3", "12.5", "13.0", "13.5", "14.0", "14.5"]
spring2_d = ["13.0",  "13.5",  "14.0",  "14.5", "15.0", "15.5", "16.0", "16.5", "17.0", "17.5", "18.0", "18.5"]
bowl2_d   = ["15.0", "15.5", "16.0", "16.5", "17.0", "17.3", "17.5", "18.0", "18.5", "19.0", "19.5", "20.0", "20.5"]

## Open project file and spreadsheet
FreeCAD.openDocument("rs-winder.FCStd")
doc = App.ActiveDocument
sheet = doc.Spreadsheet002

## Create dirs
os.mkdir("Release")
os.mkdir("Release/normal")
os.mkdir("Release/large")
os.mkdir("Release/normal/winder-base")
os.mkdir("Release/normal/housing-barrel")
os.mkdir("Release/normal/barrel-bowl")
os.mkdir("Release/normal/plunger")
os.mkdir("Release/large/winder-base")
os.mkdir("Release/large/housing-barrel")
os.mkdir("Release/large/barrel-bowl")
os.mkdir("Release/large/plunger")


###############################
## Generate normal winder    ##
###############################
## Setup normal winder params
sheet.set("spr_h",  "1.6")
sheet.set("arb_d",  "2.1")
sheet.set("hook_d", "0.5")
sheet.set("body_d", "25.0")
sheet.set("spr_dmax", "12.5")
sheet.set("spr_dmin", "7.0")
doc.recompute(None,True,True)

## Generate winder base
export_stl("Body002", "Release/normal/winder-base/rs-winder-base-normal.stl")

## Generate housing/plunger (based on spring diameter)
for n in spring1_d:
    sheet.set("spr_d", n)
    sheet.set("version", n+"MM")
    if len(n) < 4:
        sheet.set("version_x_offs", "-5.50")
    else:
        sheet.set("version_x_offs", "-6.60")
    doc.recompute(None,True,True)
    export_stl("Body", "Release/normal/plunger/rs-winder-plunger-"+n+"mm.stl")
    export_stl("Body001", "Release/normal/housing-barrel/rs-winder-housing-"+n+"mm.stl")

## Generate bowls (based actual barrel diameter)
for n in bowl1_d:
    sheet.set("barrel_d", n)
    doc.recompute(None,True,True)
    export_stl("Body003", "Release/normal/barrel-bowl/rs-winder-bowl-"+n+"mm.stl")


###############################
## Generate large winder     ##
###############################
## Setup large winder params
sheet.set("spr_h",  "2.8")
sheet.set("arb_d",  "3.0")
sheet.set("hook_d", "0.7")
sheet.set("body_d", "30.0")
sheet.set("spr_dmax", "18.5")
sheet.set("spr_dmin", "13.0")
sheet.set("version_x_offs", "-6.60")
doc.recompute(None,True,True)

## Generate winder base
export_stl("Body002", "Release/large/winder-base/rs-winder-base-large.stl")

## Generate housing/plunger (based on spring diameter)
for n in spring2_d:
    sheet.set("spr_d", n)
    sheet.set("version", n+"MM")
    doc.recompute(None,True,True)
    export_stl("Body", "Release/large/plunger/rs-winder-plunger-"+n+"mm.stl")
    export_stl("Body001", "Release/large/housing-barrel/rs-winder-housing-"+n+"mm.stl")

## Generate bowls (based actual barrel diameter)
for n in bowl2_d:
    sheet.set("barrel_d", n)
    doc.recompute(None,True,True)
    export_stl("Body003", "Release/large/barrel-bowl/rs-winder-bowl-"+n+"mm.stl")

