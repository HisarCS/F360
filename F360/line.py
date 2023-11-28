import adsk.core, adsk.fusion, adsk.cam, traceback
from time import sleep

def run(context):
    ui = None
    try:
        class LineDrawer:
            def __init__(self, start_point, end_point, construction_plane):
                self.start_point = start_point
                self.end_point = end_point
                self.construction_plane = construction_plane

                app = adsk.core.Application.get()
                self.design = app.activeProduct

                self.root_comp = self.design.rootComponent

            def create_line(self):
                sketches = self.root_comp.sketches
                sketch = sketches.add(self.construction_plane)

                lines = sketch.sketchCurves.sketchLines

                line = lines.addByTwoPoints(self.start_point, self.end_point)
