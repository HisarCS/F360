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
