FREECADPATH = '/usr/lib/freecad/lib'
import sys
sys.path.append(FREECADPATH)
from collections import defaultdict

def convert_model(filename, arclen, radius, width, height):
    try:
        import FreeCAD
        from FreeCAD import Vector
    except ValueError:
        print ('import error\n')
    else:
        FreeCAD.open(filename)

        doc = App.ActiveDocument

        sheet = doc.Spreadsheet
        print("mode = "+str(sheet.getEditorMode("A5")))
        sheet.setEditorMode("A5", 0)
        print("mode' = "+str(sheet.getEditorMode("A5")))
        print("arclen = "+str(sheet.arclen))
        print("radius = "+str(sheet.radius))
        print("angle = "+str(sheet.angle))
        print("width = "+str(sheet.width))
        print("height = "+str(sheet.height))
        sheet.set("arclen", str(arclen))
        sheet.set("radius", str(radius))
        sheet.set("width", str(width))
        sheet.set("height", str(height))
        sheet.recompute()
        # verify that the radius and also the dependent angle have changed after the recomputer
        print("arclen' = "+str(sheet.arclen))
        print("radius' = "+str(sheet.radius))
        print("angle' = "+str(sheet.angle))
        print("width' = "+str(sheet.width))
        print("height' = "+str(sheet.height))

        # recompute the model
        doc.recompute()

        geometry = generate_geometry(doc)
        print("generated geometry: "+str(geometry[0][0]))

        assert geometry[0][0][2] == Vector(width, 0, 0)

def generate_geometry(doc):
    objects = doc.Objects
    return [tessellate_shape(shaped) for shaped in objects if shaped.TypeId == 'PartDesign::Body']

def tessellate_shape(shaped):
    return shaped.Shape.tessellate(0.1)

def main():
    filename=sys.argv[1]
    arclen=float(sys.argv[2])
    radius=float(sys.argv[3])
    width=float(sys.argv[4])
    height=float(sys.argv[5])
    convert_model(filename, arclen, radius, width, height)

if __name__=='__main__':
   main()

