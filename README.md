# F360

These are a set of classes created with the goal of making it easier to work with the API of fuison 360. These classes simplify the code you have to write and reduce the lines of code you must write to achive your end result

# How to use the Classes 

This section will educate you on the usage of the classes in Fusion 360. Let us begin with the most simple sketch: A SINGULAR LINE

## The Line Class

´
import adsk.core, adsk.fusion, adsk.cam, traceback
from time import sleep

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface

        # Get active design
        design = app.activeProduct
        root_comp = design.rootComponent

        # Define start and end points for the line
        start_point = adsk.core.Point3D.create(0, 0, 0)
        end_point = adsk.core.Point3D.create(10, 0, 0)

        # Create an instance of LineDrawer
        line_drawer = LineDrawer(start_point, end_point)

        # Create a line using LineDrawer
        line_drawer.create_line()

        # Optional: Add a delay to visualize the created line
        sleep(2)

    except Exception as e:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
´
