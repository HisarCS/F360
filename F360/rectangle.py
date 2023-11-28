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


 
