#A tetrahedron is a pyramid with a triangular base and three sides. A tetrahedral number is a number of items within a tetrahedron.
#Create a function that takes an integer n and returns the nth tetrahedral number.

def tetra(n):
    return int((n * (n + 1) * (n + 2)) / 6)

print(tetra(2))
print(tetra(5))
print(tetra(10))