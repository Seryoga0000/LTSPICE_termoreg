
#%%
r1=150e3
r2=100e3
c=4.4e-6

r2/r1+1

c*(r1+r2)


#%%
import numpy as np
import matplotlib.pyplot as plt
import control

# Определение передаточной функции
# numerator = [1.67, 1.67*1.1]
# denominator = [0.44, 0]
# sys = control.TransferFunction(numerator, denominator)
sys_list=[]
s = control.TransferFunction.s
G = 1.67*(1+1/(s*1.1))
sys=G
sys_list.append(sys)
G = 0.67*(1+1/(s*0.44))
sys=G
sys_list.append(sys)

# Вычисление АЧХ
omega = np.logspace(-2, 2, 1000)  # Частота в рад/с
_, magnitude, _ = control.bode(sys_list, omega,Hz=True)

# Построение графика
# plt.figure()
# plt.semilogx(omega, magnitude)  # Построение в логарифмическом масштабе по оси x
# plt.title('АЧХ передаточной функции')
# plt.xlabel('Частота (рад/с)')
# plt.ylabel('Амплитуда (дБ)')
# plt.grid()
# plt.show()

# %%
