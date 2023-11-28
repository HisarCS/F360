import adsk.core
import adsk.fusion
import traceback

class ExtrudeCreator:
    def __init__(self, profile, distance, operation_type):
        self.profile = profile
        self.distance = distance
        self.operation_type = operation_type

        app = adsk.core.Application.get()
        self.design = app.activeProduct

        self.root_comp = self.design.rootComponent

    def create_extrusion(self):

        extrusions = self.root_comp.features.extrudeFeatures

        extrusion_input = extrusions.createInput(self.profile, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        extrusion_input.setDistanceExtent(False, adsk.core.ValueInput.createByReal(self.distance))

        if self.operation_type == 'Cut':
            extrusion_input.operation = adsk.fusion.FeatureOperations.CutFeatureOperation
        elif self.operation_type == 'Join':
            extrusion_input.operation = adsk.fusion.FeatureOperations.JoinFeatureOperation
        elif self.operation_type == 'Intersect':
            extrusion_input.operation = adsk.fusion.FeatureOperations.IntersectFeatureOperation

        extrusions.add(extrusion_input)

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface


        sketches = app.activeProduct.rootComponent.sketches
        xy_plane = app.activeProduct.rootComponent.xYConstructionPlane
        sketch = sketches.add(xy_plane)

 
        corner1 = adsk.core.Point3D.create(0, 0, 0)
        corner2 = adsk.core.Point3D.create(10, 5, 0)
        sketch.sketchCurves.sketchLines.addTwoPointRectangle(corner1, corner2)

        
        rectangle_profile = sketch.profiles.item(0)  
        extrude_creator = ExtrudeCreator(rectangle_profile, 5, 'NewBody')#note that newbody is the default extrusion type

     
        extrude_creator.create_extrusion()

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))


run(app.activeDocument)
