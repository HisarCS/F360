import adsk.core
import adsk.fusion
import traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface


        design = app.activeProduct


        rootComp = design.rootComponent
        sketches = rootComp.sketches

  
        sketch1 = sketches.add(rootComp.xYConstructionPlane)
        circles1 = sketch1.sketchCurves.sketchCircles
        circle1 = circles1.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), 10)

        sketch2 = sketches.add(rootComp.xYConstructionPlane)
        circles2 = sketch2.sketchCurves.sketchCircles
        circle2 = circles2.addByCenterRadius(adsk.core.Point3D.create(0, 0, 20), 5)

        
        loftFeatures = rootComp.features.loftFeatures
        loftInput = loftFeatures.createInput(adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        loftSections = loftInput.loftSections
        loftSections.add(circle1)
        loftSections.add(circle2)

    
        loftInput.isSolid = True

        
        loftFeatures.add(loftInput)

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

# Run the script
run(None)
