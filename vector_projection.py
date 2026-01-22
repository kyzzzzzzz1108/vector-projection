import math

def dot(a, b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

def scale(c, v):
    return [c*v[0], c*v[1], c*v[2]]

def sub(a, b):
    return [a[0]-b[0], a[1]-b[1], a[2]-b[2]]

def add(a, b):
    return [a[0]+b[0], a[1]+b[1], a[2]+b[2]]

def norm(v):
    return math.sqrt(dot(v, v))

def project(v, u):
    denom = dot(u, u)
    if denom == 0:
        raise ValueError("u must be nonzero")
    c = dot(v, u) / denom
    return scale(c, u)

u = [1.0, 2.0, 2.0]
v = [2.0, 1.0, 3.0]

p = project(v, u)
r = sub(v, p)

print("u =", u)
print("v =", v)
print("proj_u(v) =", p)
print("residual =", r)
