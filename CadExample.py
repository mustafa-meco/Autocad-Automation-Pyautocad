from pyautocad import Autocad, APoint
import math

acad = Autocad(create_if_not_exists=True)
acad.prompt("Creating a simple tree in Autocad with trianglar canopy\n")

# Create trunk using a polylinee
trunk_start1 = APoint(0, 0)
trunk_end1 = APoint(0, 50)
trunk_start2 = APoint(5, 0)
trunk_end2 = APoint(5, 50)

trunk_line1 = acad.model.AddLine(trunk_start1, trunk_end1)
trunk_line2 = acad.model.AddLine(trunk_start2, trunk_end2)

# Equilateral triangle side length
triangle_side = 40

# Calculate circle centers based on triangle vertices
circle_center1 = APoint(2.5, 60)
circle_center2 = APoint(circle_center1.x + triangle_side, circle_center1.y)
circle_center3 = APoint(circle_center1.x + triangle_side/2, circle_center1.y + math.sqrt(3)/2 * triangle_side )

# Create canopy using circles
radius = 20

canopy_circle1 = acad.model.AddCircle(circle_center1, radius)
canopy_circle2 = acad.model.AddCircle(circle_center2, radius)
canopy_circle3 = acad.model.AddCircle(circle_center3, radius)

# Create canopy using triangles
triangle_vertex1 = APoint(circle_center1.x, circle_center1.y )
triangle_vertex2 = APoint(circle_center2.x, circle_center2.y )
triangle_vertex3 = APoint(circle_center3.x, circle_center3.y )

canopy_triangle1 = acad.model.AddLine(triangle_vertex1, triangle_vertex2)
canopy_triangle2 = acad.model.AddLine(triangle_vertex2, triangle_vertex3)
canopy_triangle3 = acad.model.AddLine(triangle_vertex3, triangle_vertex1)
