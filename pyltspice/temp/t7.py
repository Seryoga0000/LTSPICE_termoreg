#%%
import sympy as sp
#%%
rd,rs,a,b,u= sp.symbols('rd,rs,a,b,u')
beta, rdo = sp.symbols('beta rdo')


rd = (beta * u + rdo)
u = (rs - rd) * a + b
# eq = sp.Eq(u,(rd - rs) * a + b)
# eq2 = sp.Eq((rd-rdo)/beta,u)    
# solution = sp.solve([eq, eq2], u)

eq1=sp.Eq(u,u.subs(rd,(beta * u + rdo)))

solu=sp.solve(eq1,u)[0]
error=solu/a
print(error)
error = sp.apart(solu,rs)
#%%
