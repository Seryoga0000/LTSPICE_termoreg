r1=150e3
r2=100e3
c=4.4e-6

r2/r1

c*r1
c*r2

#%%
import numpy as np
import matplotlib.pyplot as plt
import control
import math
# Определение передаточной функции
s = control.TransferFunction.s
G = 0.67*(1+1/(s*0.44))
sys=G

# Вычисление АЧХ
omega = np.logspace(-6, 2, 1000)  # Частота в рад/с
magnitude, phase, omega = control.bode(sys, omega,Hz=True)

# Построение графика
omega = omega / (2. * math.pi)
# Display the Bode plot
fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.set_title('Bode Plot')
ax1.loglog(omega, magnitude)
ax1.grid()
ax1.set_ylabel('Magnitude (dB)')  # Set y-axis title for magnitude plot
ax2.semilogx(omega, phase)
ax2.grid()
ax2.set_xlabel('Frequency [rad/s]')
ax2.set_ylabel('Phase (degrees)')  # Set y-axis title for phase plot

# Add a horizontal dashed line to indicate a specific value
specific_value = 0.67  # Define the value for the horizontal line
ax1.axhline(y=specific_value, color='r', linestyle='--', label='Specific Value', linewidth=1)
ax1.text(1e-6, specific_value + 3, f'Mag: {specific_value}', color='r',horizontalalignment='left')
# ax2.axhline(y=specific_value, color='r', linestyle='--')

plt.tight_layout()
plt.show()








# %%
