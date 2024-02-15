
#%%
import numpy as np
import matplotlib.pyplot as plt
import control

# Определение передаточной функции
# numerator = [1.67, 1.67*1.1]
# denominator = [0.44, 0]
# sys = control.TransferFunction(numerator, denominator)
A_list=[300e3,30e3,3e3]
sys_list=[]
s = control.TransferFunction.s
Lpi = 1.67*(1+1/(s*1.1))

for A in A_list:
    G = Lpi/(1+Lpi/A)
    sys=G
    sys_list.append(sys)

# Вычисление АЧХ
omega = np.logspace(-6, 1, 1000)  # Частота в рад/с
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
