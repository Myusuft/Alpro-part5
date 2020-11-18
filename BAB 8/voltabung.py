import math
#hasil akan integer

def area_circle (r):
    return math.pi * r *r

def vol_tabung (r,t):
    return area_circle(r) * t

def vol_int(r,t):
    return int(vol_tabung(r,t))

hasil_int = vol_int(7 , 9)
print(hasil_int)
