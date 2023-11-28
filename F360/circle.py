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
