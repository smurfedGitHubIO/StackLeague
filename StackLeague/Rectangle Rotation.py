import math

def rectangle_rotation(a, b):
    p, r = 0, (a/2)**2+(b/2)**2
    r = int(math.ceil(math.sqrt(r)))
    for i in range(-r,r+1):
        for j in range(-r,r+1):
            x = i*math.cos(math.radians(-45))-j*math.cos(math.radians(-45))
            y = i*math.cos(math.radians(-45))+j*math.cos(math.radians(-45))
            if -a/2<=x<=a/2 and -b/2<=y<=b/2:
                p += 1
    return p