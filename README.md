# F360

These are a set of classes created with the goal of making it easier to work with the API of fuison 360. These classes simplify the code you have to write and reduce the lines of code you must write to achive your end result

# How to use the Classes 

This section will educate you on the usage of the classes in Fusion 360. Let us begin with the most simple sketch: A SINGULAR LINE

## The Line Class
```python 

import adsk.core, adsk.fusion, adsk.cam, traceback
from time import sleep

def run(context):
    ui = None
    try:
        class LineDrawer:
            def __init__(self, start_point, end_point):
                self.start_point = start_point
                self.end_point = end_point

                app = adsk.core.Application.get()
                self.design = app.activeProduct

                self.root_comp = self.design.rootComponent

            def create_line(self):

                sketches = self.root_comp.sketches
                xy_plane = self.root_comp.xYConstructionPlane
                sketch = sketches.add(xy_plane)

                lines = sketch.sketchCurves.sketchLines

                line = lines.addByTwoPoints(self.start_point, self.end_point)

```
