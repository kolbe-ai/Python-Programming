"""
Create geometry.py with area_square(s) and perimeter_rectangle(l, b).
In main.py, import them in two different ways (import x and from x import y) and explain the difference.
"""

from geometry import area_square
from geometry import perimeter_rectangle
a = area_square(10)
print(a)

b = perimeter_rectangle(10,3)
print(b)