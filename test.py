import numpy as np

a=np.arange(9).reshape((3,3))

b,c=a[1,:], a[:,1]

print(f"a.shape: {a.shape}\n")

print(f"row.shape: {b.shape}\n")
print(f"col.shape: {c.shape}\n")

print(a)
print(b)
print(c)
