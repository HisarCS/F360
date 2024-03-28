# F360

These are a set of classes created with the goal of making it easier to work with the API of fuison 360. These classes simplify the code you have to write and reduce the lines of code you must write to achive your end result

# How to use the Classes 

This section will educate you on the usage of the classes in Fusion 360. 

## Sketching

Let us begin with the most simple sketch: A SINGULAR LINE

### The Line Class
```python

start_point = adsk.core.Point3D.create(0, 0, 0)
end_point = adsk.core.Point3D.create(10, 0, 0)

xy_plane = app.activeProduct.rootComponent.xYConstructionPlane
       
line_drawer = LineDrawer(start_point, end_point, xy_plane)

line_drawer.create_line()

```

To explain the code: You simply define your start and end point, construction plane and create the LineDrawer class instance. After that you call the create_line function and you have a line on any plane you want. ⎹ 
<img width="628" alt="Ekran Resmi 2023-11-29 18 06 24" src="https://github.com/HisarCS/F360/assets/120194760/78cdb822-9620-487b-8af4-fa7ba08dfc44">

### The Circle Class

Let's look at how to create a circle with the circle class

```python

app = adsk.core.Application.get()
ui = app.userInterface

design = app.activeProduct
rootComp = design.rootComponent

xzPlane = rootComp.xZConstructionPlane
circle_creator = CircleCreator(adsk.core.Point3D.create(0, 0, 0), 2, xyPlane)

circle1 = circle_creator.create_circle()

```
Here you have to define the application and ui(they aren't defined in the class). Then create a variable and assign the construction plane you want to use to it. After that you just have to define your point and radius and pass them into the class along with the plane the circle will be drawn on.  ⃝

<img width="485" alt="Ekran Resmi 2023-11-29 18 06 59" src="https://github.com/HisarCS/F360/assets/120194760/d0f68bcf-a3e2-40e2-94e5-16ffe1ba2e6e">

### The Rectangle Class

```python

app = adsk.core.Application.get()
ui = app.userInterface

       
corner1 = adsk.core.Point3D.create(0, 0, 0)
corner2 = adsk.core.Point3D.create(10, 5, 0)


xy_plane = app.activeProduct.rootComponent.xYConstructionPlane

rectangle_drawer = RectangleDrawer(corner1, corner2, xy_plane)

rectangle_drawer.draw_rectangle()
```
Here you have to define the application and ui(they aren't defined in the class). Then you have to define two points as you are drawing a two point rectangle also you define the plane you use then you pass them into the class. After that you just have to call the draw_rectangle function and you have a rectangle.▭

<img width="483" alt="Ekran Resmi 2023-11-29 18 07 22" src="https://github.com/HisarCS/F360/assets/120194760/7110dab2-7a78-4443-89cf-466fb6fc8cc5">

### The Polygon Class


```python

app = adsk.core.Application.get()
ui = app.userInterface

center_point = adsk.core.Point3D.create(0, 0, 0)
num_sides = 6
radius = 3
xy_plane = app.activeProduct.rootComponent.xYConstructionPlane

polygon_drawer = PolygonDrawer(center_point, num_sides, radius, xy_plane)
polygon_drawer.draw_polygon()
```
Here you have to define the application and ui(they aren't defined in the class). Then you have to define your side number, radius, plane and center point. After that you pass these into the class and then class the draw_polygon function and you have a polygon. ⬠

<img width="487" alt="Ekran Resmi 2023-11-29 18 07 55" src="https://github.com/HisarCS/F360/assets/120194760/20b24308-7bbd-47fe-8e5e-5052183f97c8">

### Three Point Arc

```python

app = adsk.core.Application.get()
ui = app.userInterface

design = app.activeProduct
root_comp = design.rootComponent

xy_plane = root_comp.xYConstructionPlane

arc_creator = ThreePointArcCreator(xy_plane)

point1 = adsk.core.Point3D.create(0, 0, 0)
point2 = adsk.core.Point3D.create(10, 0, 0)
point3 = adsk.core.Point3D.create(10, 10, 0)

arc_creator.create_arc(point1, point2, point3)

```

Here you call/define app and ui also you get the design and root_comp after that you define the xy plane you then create an instance of the class and pass in the plane after that you call the create_arc function and pass in the points. After you've completed these steps you have a three point arc. ⌒

<img width="820" alt="Ekran Resmi 2023-11-30 00 37 06" src="https://github.com/HisarCS/F360/assets/120194760/61a8a6b3-502a-4a75-a046-1ded8636ce46">

## Features

### Extrude 

```python

app = adsk.core.Application.get()
ui = app.userInterface


sketches = app.activeProduct.rootComponent.sketches
xy_plane = app.activeProduct.rootComponent.xYConstructionPlane
sketch = sketches.add(xy_plane)

 
corner1 = adsk.core.Point3D.create(0, 0, 0)
corner2 = adsk.core.Point3D.create(10, 5, 0)
sketch.sketchCurves.sketchLines.addTwoPointRectangle(corner1, corner2)

        
rectangle_profile = sketch.profiles.item(0)  
extrude_creator = ExtrudeCreator(rectangle_profile, 5, 'NewBody')

     
extrude_creator.create_extrusion()

```
Firstly here you create a simple shape(here a rectangle). Then you put your profile the extrusion height and type into the class. After that you just called the creat extrusion function and now you have a 3D body.

<img width="772" alt="Ekran Resmi 2023-12-07 07 24 55" src="https://github.com/HisarCS/F360/assets/120194760/4ada3ae5-abc4-4df5-8d3d-0ffb5e5de9de">

### Fillet

#### Constant Radius Fillet

#### Variable Radius Fillet

#### Chord Length Fillet

### Loft

```python
def run(context):
    try:
        app = adsk.core.Application.get()
        lofter = Lofter(app)

        def sketch_square1(sketch):
            lines = sketch.sketchCurves.sketchLines
            p1 = adsk.core.Point3D.create(-2.5, 2.5, 0)
            p2 = adsk.core.Point3D.create(2.5, 2.5, 0)
            p3 = adsk.core.Point3D.create(2.5, -2.5, 0)
            p4 = adsk.core.Point3D.create(-2.5, -2.5, 0)
            lines.addByTwoPoints(p1, p2)
            lines.addByTwoPoints(p2, p3)
            lines.addByTwoPoints(p3, p4)
            lines.addByTwoPoints(p4, p1)

        xyPlane = lofter.rootComp.xYConstructionPlane
        lofter.add_profile(xyPlane, sketch_square1)

        def sketch_square2(sketch):
            lines = sketch.sketchCurves.sketchLines
            p1 = adsk.core.Point3D.create(-1.5, 1.5, 0)
            p2 = adsk.core.Point3D.create(1.5, 1.5, 0)
            p3 = adsk.core.Point3D.create(1.5, -1.5, 0)
            p4 = adsk.core.Point3D.create(-1.5, -1.5, 0)
            lines.addByTwoPoints(p1, p2)
            lines.addByTwoPoints(p2, p3)
            lines.addByTwoPoints(p3, p4)
            lines.addByTwoPoints(p4, p1)

        offsetPlaneInput = lofter.rootComp.constructionPlanes.createInput()
        offsetDistance = adsk.core.ValueInput.createByReal(10.0)
        offsetPlaneInput.setByOffset(xyPlane, offsetDistance)
        offsetPlane = lofter.rootComp.constructionPlanes.add(offsetPlaneInput)
        lofter.add_profile(offsetPlane, sketch_square2)

        lofter.create_loft()

    except:
        if lofter.ui:
            lofter.ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))


```

<img width="1005" alt="Ekran Resmi 2024-03-28 14 46 19" src="https://github.com/HisarCS/F360/assets/120194760/1b68f405-e126-4022-81f6-fcec6dfe9a3b">
