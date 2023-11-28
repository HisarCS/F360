import adsk.core
import adsk.fusion
import traceback


class FilletManager:
  
    def __init__(self):
        self.app = adsk.core.Application.get()
        self.ui = self.app.userInterface
        self.design = adsk.fusion.Design.cast(self.app.activeProduct)
        self.rootComp = self.design.rootComponent
        self.fillets = self.rootComp.features.filletFeatures

    # Method to create a constant-radius fillet
    def create_constant_radius_fillet(self, edge_collection, radius):
        input1 = self.fillets.createInput()
        input1.isRollingBallCorner = True

        const_radius_input = input1.edgeSetInputs.addConstantRadiusEdgeSet(edge_collection, radius, True)
        const_radius_input.continuity = adsk.fusion.SurfaceContinuityTypes.TangentSurfaceContinuityType

        fillet1 = self.fillets.add(input1)
        fillet1.deleteMe()

    # Method to create a variable-radius fillet
    def create_variable_radius_fillet(self, edge, start_radius, end_radius, mid_radii, positions):
        input2 = self.fillets.createInput()
        input2.isRollingBallCorner = False

        edge_collection2 = adsk.core.ObjectCollection.create()
        edge_collection2.add(edge)

        var_radius_edge_set = input2.edgeSetInputs.addVariableRadiusEdgeSet(edge_collection2, start_radius, end_radius, True)
        var_radius_edge_set.continuity = adsk.fusion.SurfaceContinuityTypes.TangentSurfaceContinuityType

        var_radius_edge_set.setMidRadii(mid_radii, positions)

        fillet2 = self.fillets.add(input2)
        fillet2.deleteMe()

    # Method to create a chord-length fillet
    def create_chord_length_fillet(self, edge_collection, chord_length):
        input3 = self.fillets.createInput()
        input3.isRollingBallCorner = True

        chord_length_edge_set = input3.edgeSetInputs.addChordLengthEdgeSet(edge_collection, chord_length, True)
        chord_length_edge_set.continuity = adsk.fusion.SurfaceContinuityTypes.TangentSurfaceContinuityType

        self.fillets.add(input3)


def run(context):
    try:
        
        fillet_manager = FilletManager()

        # Create constant-radius fillet
        edges1 = fillet_manager.rootComp.bRepBodies.item(0).faces.item(0).edges
        edge_collection1 = adsk.core.ObjectCollection.create()
        for edge in edges1:
            edge_collection1.add(edge)
        radius1 = adsk.core.ValueInput.createByReal(0.3)
        fillet_manager.create_constant_radius_fillet(edge_collection1, radius1)

        # Create variable-radius fillet
        edge2 = fillet_manager.rootComp.bRepBodies.item(0).faces.item(0).edges.item(0)
        start_radius2 = adsk.core.ValueInput.createByReal(1.0)
        end_radius2 = adsk.core.ValueInput.createByReal(5.0)
        positions2 = [adsk.core.ValueInput.createByReal(0.3), adsk.core.ValueInput.createByReal(0.6)]
        radii2 = [adsk.core.ValueInput.createByReal(2.0), adsk.core.ValueInput.createByReal(3.0)]
        fillet_manager.create_variable_radius_fillet(edge2, start_radius2, end_radius2, radii2, positions2)

        # Create chord-length fillet
        edges3 = fillet_manager.rootComp.bRepBodies.item(0).faces.item(0).edges
        edge_collection3 = adsk.core.ObjectCollection.create()
        for edge in edges3:
            edge_collection3.add(edge)
        chord_length3 = adsk.core.ValueInput.createByReal(1.0)
        fillet_manager.create_chord_length_fillet(edge_collection3, chord_length3)


    except Exception as e:
        fillet_manager.ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
