# F360

These are a set of classes created with the goal of making it easier to work with the API of fuison 360. These classes simplify the code you have to write and reduce the lines of code you must write to achive your end result

# How to use the Classes 

This section will educate you on the usage of the classes in Fusion 360. Let us begin with the most simple sketch: A SINGULAR LINE

## The Line Class
```python

start_point = adsk.core.Point3D.create(0, 0, 0)
end_point = adsk.core.Point3D.create(10, 0, 0)

xy_plane = app.activeProduct.rootComponent.xYConstructionPlane
       
line_drawer = LineDrawer(start_point, end_point, xy_plane)

line_drawer.create_line()

```

To explain the code: def run(context) is the default runnig function of the Fusion 360 API. Then you set your ui as none due to you not having any ui related functions in your code. Then you simply define your start and end point, construction play and create the LineDrawer class instance. After that you call the create_line function and you have a line on any plane you want.
