FREECADPATH = '/usr/lib/freecad/lib'
import sys
sys.path.append(FREECADPATH)
from collections import defaultdict
import FreeCAD
import Mesh
import shutil
import os

def export_mesh(body_obj,filename):
    __objs__=[]
    __objs__.append(FreeCAD.getDocument("rs_winder").getObject(body_obj))
    Mesh.export(__objs__,filename+".stl")
    Mesh.export(__objs__,filename+".3mf")
    del __objs__

## List of sizes to generate
## Large range  = h=2.8, d=12-18
## Normal range = h=1.6, d=7-12
rs_version = "0.95"
spring1_d = ["7.0", "7.5", "8.0",  "8.5",  "9.0",  "9.5",  "10.0", "10.5", "11.0", "11.5", "12.0", "12.5"]
spring2_d = ["13.0",  "13.5",  "14.0",  "14.5", "15.0", "15.5", "16.0", "16.5", "17.0", "17.5", "18.0", "18.5"]

## Open project file and spreadsheet
FreeCAD.openDocument("rs-winder.FCStd")
doc = App.ActiveDocument
sheet = doc.Spreadsheet002

## Create release file dirs
os.mkdir("Release")
os.mkdir("Release/normal")
os.mkdir("Release/large")
os.mkdir("Release/normal/winder-base")
os.mkdir("Release/normal/housing-barrel")
os.mkdir("Release/normal/bowl-setter")
os.mkdir("Release/normal/plunger")
os.mkdir("Release/large/winder-base")
os.mkdir("Release/large/housing-barrel")
os.mkdir("Release/large/bowl-setter")
os.mkdir("Release/large/plunger")
os.mkdir("Release/staplejig")
shutil.copyfile("misc/staplejig.stl", "Release/staplejig/staplejig.stl")
shutil.copyfile("README.md", "Release/README-v"+rs_version+".md")
shutil.copyfile("LICENSE", "Release/LICENSE")


###############################
## Generate normal winder    ##
###############################
## Setup normal winder params
sheet.set("spr_h",  "1.6")   ## Set max spring height
sheet.set("spr_ex", "0.65")  ## Set setter bowl spring extrude depth
sheet.set("arb_d",  "1.625") ## Fits M1.5 dowel + clearance
sheet.set("hook_d", "0.52")  ## Set hook hole diameter
sheet.set("body_d", "25.0")  ## Set winder body diameter
doc.recompute(None,True,True)

## Generate winder base (M1.5)
export_mesh("Body002", "Release/normal/winder-base/rs-winder-base-normal-1.5mm")

## Generate winder base (M2)
sheet.set("arb_d",  "2.125") ## Fits M2.0 dowel + clearance
doc.recompute(None,True,True)
export_mesh("Body002", "Release/normal/winder-base/rs-winder-base-normal-2.0mm")

## Generate housing/plunger (based on spring diameter)
for n in spring1_d:
    sheet.set("spr_d", n)
    sheet.set("version", "M"+n)
    if len(n) < 4:
        sheet.set("version_x_offs", "-5.40")
    else:
        sheet.set("version_x_offs", "-6.50")
    doc.recompute(None,True,True)
    export_mesh("Body", "Release/normal/plunger/rs-winder-plunger-"+n+"mm")
    export_mesh("Body001", "Release/normal/housing-barrel/rs-winder-housing-"+n+"mm")

## Generate setter bowl
export_mesh("Body003", "Release/normal/bowl-setter/rs-setter-bowl-normal")


###############################
## Generate large winder     ##
###############################
## Reset project file and spreadsheet
doc.restore()
sheet = doc.Spreadsheet002

## Setup large winder params
sheet.set("spr_h",  "2.6")   ## Set max spring height
sheet.set("spr_ex", "0.75")  ## Set setter bowl spring extrude depth
sheet.set("arb_d",  "2.625") ## Fits M2.5 dowel + clearance
sheet.set("hook_d", "0.55")  ## Set hook hole diameter
sheet.set("body_d", "30.0")  ## Set winder body diameter
doc.recompute(None,True,True)

## Generate winder base (M2.5)
export_mesh("Body002", "Release/large/winder-base/rs-winder-base-large-2.5mm")

## Generate winder base (M3)
sheet.set("arb_d",  "3.125") ## Fits M3.0 dowel + clearance
doc.recompute(None,True,True)
export_mesh("Body002", "Release/large/winder-base/rs-winder-base-large-3.0mm")

## Generate housing/plunger (based on spring diameter)
for n in spring2_d:
    sheet.set("spr_d", n)
    sheet.set("version", "M"+n)
    doc.recompute(None,True,True)
    export_mesh("Body", "Release/large/plunger/rs-winder-plunger-"+n+"mm")
    export_mesh("Body001", "Release/large/housing-barrel/rs-winder-housing-"+n+"mm")

## Generate setter bowl
export_mesh("Body003", "Release/large/bowl-setter/rs-setter-bowl-large")

