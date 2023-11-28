import adsk.core
import adsk.fusion
import traceback

class Lofty:
    def __init__(self, app):
        self.app = app
        self.ui = app.userInterface
        self.design = app.activeProduct
        self.root_comp = self.design.rootComponent
        self.sketches = self.root_comp.sketches


        try:
            self.create_construction_planes()
            self.create_loft_profiles()
        except RuntimeError as e:
            if self.ui:
                self.ui.messageBox(f'Failed to initialize: {e}')

    def create_construction_planes(self):
        try:

            plane_input1 = self.root_comp.constructionPlanes.createInput()
            plane_input1.setByOffset(self.root_comp.xZConstructionPlane, adsk.core.ValueInput.createByString('10 cm'))
            plane1 = self.root_comp.constructionPlanes.add(plane_input1)

            # Create construction plane 2
            plane_input2 = self.root_comp.constructionPlanes.createInput()
            plane_input2.setByOffset(plane1, adsk.core.ValueInput.createByString('10 cm'))
            self.root_comp.constructionPlanes.add(plane_input2)

        except Exception as e:
            raise RuntimeError(f'Failed to create construction planes: {e}')


    def create_loft_profiles(self):
        try:

            if self.root_comp.constructionPlanes.count < 2:
                self.create_construction_planes()


            profiles = []
            for i in range(min(3, self.root_comp.constructionPlanes.count)):
                sketch = self.sketches.add(self.root_comp.constructionPlanes.item(i))
                circle = sketch.sketchCurves.sketchCircles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), 5.0 * (i + 1))
                profiles.append(sketch.profiles.item(0))

            
            loft_feats = self.root_comp.features.loftFeatures
            loft_input = loft_feats.createInput(adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
            
          
            for profile in profiles:
                loft_input.loftSections.add(profile)

            loft_input.isSolid = False
            loft_input.isClosed = False
            loft_input.isTangentEdgesMerged = True

      
            loft_feats.add(loft_input)
        except Exception as e:
            raise RuntimeError(f'Failed to create loft profiles: {e}')


