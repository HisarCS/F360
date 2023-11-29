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
ere you have to define the application and ui(they aren't defined in the class). Then you have to define your side number, radius, plane and center point. After that you pass these into the class and then class the draw_polygon function and you have a polygon. ⬠



