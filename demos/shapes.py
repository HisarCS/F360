import adsk.core, adsk.fusion, traceback, math


class LineDrawer:
    def __init__(self, start_point, end_point, plane):
        self.start_point = start_point
        self.end_point = end_point
        self.plane = plane
        app = adsk.core.Application.get()
        self.design = app.activeProduct
        self.root_comp = self.design.rootComponent

    def create_line(self):
        sketches = self.root_comp.sketches
        sketch = sketches.add(self.plane)
        lines = sketch.sketchCurves.sketchLines
        return lines.addByTwoPoints(self.start_point, self.end_point)


class PolygonDrawer:
    def __init__(self, center_point, num_sides, radius, plane):
        self.center_point = center_point
        self.num_sides = num_sides
        self.radius = radius
        self.plane = plane
        app = adsk.core.Application.get()
        self.design = app.activeProduct
        self.root_comp = self.design.rootComponent

    def draw_polygon(self):
        sketches = self.root_comp.sketches
        sketch = sketches.add(self.plane)
        polygon_points = []
        for i in range(self.num_sides):
            angle = 2 * math.pi * i / self.num_sides
            x = self.center_point.x + self.radius * math.cos(angle)
            y = self.center_point.y + self.radius * math.sin(angle)
            polygon_points.append(adsk.core.Point3D.create(x, y, 0))
        for i in range(self.num_sides):
            sketch.sketchCurves.sketchLines.addByTwoPoints(
                polygon_points[i], polygon_points[(i + 1) % self.num_sides]
            )
        return sketch.profiles[0]


class ExtrudeCreator:
    def __init__(self, profile, distance, operation_type="NewBody"):
        self.profile = profile
        self.distance = distance
        self.operation_type = operation_type
        app = adsk.core.Application.get()
        self.design = app.activeProduct
        self.root_comp = self.design.rootComponent

    def create_extrusion(self):
        extrusions = self.root_comp.features.extrudeFeatures
        extrusion_input = extrusions.createInput(
            self.profile, adsk.fusion.FeatureOperations.NewBodyFeatureOperation
        )
        extrusion_input.setDistanceExtent(
            False, adsk.core.ValueInput.createByReal(self.distance)
        )
        if self.operation_type == "Cut":
            extrusion_input.operation = adsk.fusion.FeatureOperations.CutFeatureOperation
        elif self.operation_type == "Join":
            extrusion_input.operation = adsk.fusion.FeatureOperations.JoinFeatureOperation
        elif self.operation_type == "Intersect":
            extrusion_input.operation = (
                adsk.fusion.FeatureOperations.IntersectFeatureOperation
            )
        return extrusions.add(extrusion_input)


def create_shapes():
    app = adsk.core.Application.get()
    ui = app.userInterface
    try:
        design = app.activeProduct
        root_comp = design.rootComponent
        plane = root_comp.xZConstructionPlane

        pentagon_center = adsk.core.Point3D.create(0, 0, 0)
        pentagon = PolygonDrawer(pentagon_center, 5, 10, plane)
        pentagon_profile = pentagon.draw_polygon()
        ExtrudeCreator(pentagon_profile, 5).create_extrusion()

      
        l_sketch = root_comp.sketches.add(plane)
        l_start = adsk.core.Point3D.create(15, 15, 0)
        l_middle1 = adsk.core.Point3D.create(25, 15, 0)
        l_middle2 = adsk.core.Point3D.create(25, 5, 0)
        l_end = adsk.core.Point3D.create(15, 5, 0)
        l_bottom = adsk.core.Point3D.create(15, 10, 0)
        l_sketch.sketchCurves.sketchLines.addByTwoPoints(l_start, l_middle1)
        l_sketch.sketchCurves.sketchLines.addByTwoPoints(l_middle1, l_middle2)
        l_sketch.sketchCurves.sketchLines.addByTwoPoints(l_middle2, l_bottom)
        l_sketch.sketchCurves.sketchLines.addByTwoPoints(l_bottom, l_start)
        ExtrudeCreator(l_sketch.profiles[0], 5).create_extrusion()


        circle_sketch = root_comp.sketches.add(plane)
        circle_center = adsk.core.Point3D.create(50, 0, 0)
        circle_radius = 10
        circle_sketch.sketchCurves.sketchCircles.addByCenterRadius(
            circle_center, circle_radius
        )
        ExtrudeCreator(circle_sketch.profiles[0], 5).create_extrusion()

      
        star_center = adsk.core.Point3D.create(0, 40, 0)
        num_points = 5
        radius_outer = 10
        radius_inner = 5
        star_points = []
        for i in range(num_points * 2):
            angle = i * math.pi / num_points
            radius = radius_outer if i % 2 == 0 else radius_inner
            x = star_center.x + radius * math.cos(angle)
            y = star_center.y + radius * math.sin(angle)
            star_points.append(adsk.core.Point3D.create(x, y, 0))
        star_sketch = root_comp.sketches.add(plane)
        for i in range(len(star_points)):
            star_sketch.sketchCurves.sketchLines.addByTwoPoints(
                star_points[i], star_points[(i + 1) % len(star_points)]
            )
        ExtrudeCreator(star_sketch.profiles[0], 5).create_extrusion()

        ui.messageBox("Shapes created and extruded flat on the floor!")

    except Exception as e:
        if ui:
            ui.messageBox(f"Failed:\n{traceback.format_exc()}")


create_shapes()
