import adsk.core, adsk.fusion, adsk.cam, traceback

# Define the RectangleDrawer class
class RectangleDrawer:
    def __init__(self, corner1, corner2, plane):
        self.corner1 = corner1
        self.corner2 = corner2
        self.plane = plane

        app = adsk.core.Application.get()
        self.design = app.activeProduct
        self.root_comp = self.design.rootComponent

    def draw_rectangle(self):
        sketches = self.root_comp.sketches
        sketch = sketches.add(self.plane)
        sketch.sketchCurves.sketchLines.addTwoPointRectangle(self.corner1, self.corner2)

# Define the ExtrudeCreator class
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

# Define the ParameterCreator class
class ParameterCreator:
    def __init__(self):
        app = adsk.core.Application.get()
        self.design = app.activeProduct
        self.user_parameters = self.design.userParameters

    def add_parameter(self, name, value, unit, comment):
        existing_param = self.user_parameters.itemByName(name)
        if existing_param:
            return existing_param
        else:
            try:
                return self.user_parameters.add(name, adsk.core.ValueInput.createByReal(value), unit, comment)
            except Exception as e:
                app = adsk.core.Application.get()
                ui = app.userInterface
                ui.messageBox(f'Failed to add parameter {name}:\n{e}')
                raise

# Define the main function to create the desk
def create_desk(params):
    param_creator = ParameterCreator()

    # Create parameters using a loop
    param_dict = {}
    for idx, (key, value) in enumerate(params.items()):
        param_name = f'm{idx + 1}'
        param_dict[key] = param_creator.add_parameter(param_name, value, 'cm', f'{key.replace("_", " ").capitalize()}')

    # Extract parameter values
    desk_len = param_dict['desk_length'].value
    desk_wid = param_dict['desk_width'].value
    desk_thk = param_dict['desk_thickness'].value
    leg_hei = param_dict['leg_height'].value
    leg_thk = param_dict['leg_thickness'].value

    # Create the desk top
    app = adsk.core.Application.get()
    design = app.activeProduct
    root_comp = design.rootComponent
    sketches = root_comp.sketches
    xy_plane = root_comp.xYConstructionPlane

    top_corner1 = adsk.core.Point3D.create(0, 0, 0)
    top_corner2 = adsk.core.Point3D.create(desk_len, desk_wid, 0)
    drawer = RectangleDrawer(top_corner1, top_corner2, xy_plane)
    drawer.draw_rectangle()

    # Get the profile of the desk top
    top_sketch = sketches.item(sketches.count - 1)
    top_profile = top_sketch.profiles.item(0)
    extruder = ExtrudeCreator(top_profile, desk_thk, 'Join')
    extruder.create_extrusion()

    # Create the desk legs
    leg_positions = [
        (0, 0),
        (0, desk_wid - leg_thk),
        (desk_len - leg_thk, 0),
        (desk_len - leg_thk, desk_wid - leg_thk)
    ]
    leg_sketches = []

    for pos in leg_positions:
        leg_corner1 = adsk.core.Point3D.create(pos[0], pos[1], 0)
        leg_corner2 = adsk.core.Point3D.create(pos[0] + leg_thk, pos[1] + leg_thk, 0)
        drawer = RectangleDrawer(leg_corner1, leg_corner2, xy_plane)
        drawer.draw_rectangle()
        leg_sketches.append(sketches.item(sketches.count - 1))

    for leg_sketch in leg_sketches:
        leg_profile = leg_sketch.profiles.item(0)
        extruder = ExtrudeCreator(leg_profile, -leg_hei, 'Join')
        extruder.create_extrusion()

def run(context):
    try:
        # Define the parameters
        params = {
            'desk_length': 100,
            'desk_width': 60,
            'desk_thickness': 2,
            'leg_height': 70,
            'leg_thickness': 2
        }
        
        create_desk(params)
    except Exception as e:
        app = adsk.core.Application.get()
        ui = app.userInterface
        ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

# This function should be called when the script is run
run(adsk.fusion.Design.cast(None))
