#%%
import sympy as sp
#%%
s= sp.symbols('s')

#%%
sys = 4.18*(1+1/(s*1.17))/(4.18/7280*(1+1/(s*1.17))+1)

lim = sp.limit(sys, s, 0)
lim.evalf()