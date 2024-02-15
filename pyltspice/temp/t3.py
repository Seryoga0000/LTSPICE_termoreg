#p
#%%
import sympy as sp

r1=47e3
r2=22e3
c=4.4e-6
r3=100e3
r4=150e3
#%%
(r2/(r1+r2))
s= sp.symbols('s')
expr = (r4*r2/(r1+r2))/(r4+(r1*r2/(r1+r2))+r3+1/(s*c))
numerator = expr.as_numer_denom()[0] /  227272.727272727
denominator = expr.as_numer_denom()[1] /  227272.727272727
# Сборка выражения обратно
expr = numerator / denominator

numerator = expr.as_numer_denom()[0] /  (1.16593623188406*s)
denominator = sp.expand(expr.as_numer_denom()[1] /  (1.16593623188406*s),s)
# Сборка выражения обратно
expr = numerator / denominator
# expr = round(expr, 2)
texpr=expr.xreplace(sp.core.rules.Transform(lambda x: x.round(2), lambda x: isinstance(x, sp.Float)))
# expr=sp.cancel(expr)
print(expr)
expr = (r4*r2/(r1+r2))/(r4+(r1*r2/(r1+r2))+r3)
print(expr)
# %%
r4/(r4+1/(s*c))
(r4+r3)*c

sp.simplify(0.18/(1 + 1/(s*1.17)))
sp.simplify(expr/(1/5.54/(1 + 1/(s*1.17))))

#%%

c*(r4+r3+r2*r1/(r1+r2))
1+r1/r2+(r1+r3)/r4+r1*r3/(r2*r4)