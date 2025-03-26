from collections import namedtuple

Points = namedtuple("Points",["x","y","z"])

point1=Points(x = 1.5,y=2.5,z=3.5)
point2=Points(x = 4.5,y=5.5,z=6.5)

print(f"Point 1 = x:{point1.x}, y:{point1.y}, z:{point1.z},")
print(f"Point 2 = x:{point2.x}, y:{point2.y}, z:{point2.z},")


# Point 1 = x:1.5, y:2.5, z:3.5,
# Point 2 = x:4.5, y:5.5, z:6.5,