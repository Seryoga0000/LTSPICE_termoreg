# r1=2200
# r2=4700
# r3=1000
# rh=60
# b=1000
# vp=24
# vin=2
# vbe=1.2

# a1=b*r2*rh/(r1*r2+r3*(r1+r2))
# a2=b*(r1+r2)*rh/(r1*r2+r3*(r1+r2))
# print("vp-a2*vbe")
# print(vp+a2*vbe)
# print("a1")
# print(a1)
# print("vcol")
# print(vp-a1*vin+a2*vbe)
#%%
import sympy as sp

r1= sp.symbols('r1')
r2= sp.symbols('r2')
r3= sp.symbols('r3')

