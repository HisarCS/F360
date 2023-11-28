import adsk.core
import adsk.fusion
import traceback

class RectangleDrawer:
    def __init__(self, corner1, corner2):
        self.corner1 = corner1
        self.corner2 = corner2

        app = adsk.core.Application.get()
        self.design = app.activeProduct

        
        self.root_comp = self.design.rootComponent

    def draw_rectangle(self):
       
        sketches = self.root_comp.sketches
        xy_plane = self.root_comp.xYConstructionPlane
        sketch = sketches.add(xy_plane)

  
        sketch.sketchCurves.sketchLines.addTwoPointRectangle(self.corner1, self.corner2)

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface


        corner1 = adsk.core.Point3D.create(0, 0, 0)
        corner2 = adsk.core.Point3D.create(10, 5, 0)


        rectangle_drawer = RectangleDrawer(corner1, corner2)


        rectangle_drawer.draw_rectangle()

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

# Run the script
run(app.activeDocument)
 