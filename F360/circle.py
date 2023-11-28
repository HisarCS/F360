#Author-
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback

class CircleCreator:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def create_circle(self, sketch):
        circles = sketch.sketchCurves.sketchCircles
        return circles.addByCenterRadius(self.center, self.radius)

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface


        design = app.activeProduct


        rootComp = design.rootComponent

  
        sketches = rootComp.sketches
        xyPlane = rootComp.xYConstructionPlane
        sketch = sketches.add(xyPlane)


        circle_creator = CircleCreator(adsk.core.Point3D.create(0, 0, 0), 2)


        circle1 = circle_creator.create_circle(sketch)

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
