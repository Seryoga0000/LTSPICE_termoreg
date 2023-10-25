#%%
from PyLTSpice import SimCommander
from PyLTSpice import RawRead
from PyLTSpice import SpiceEditor
import numpy as np
import matplotlib.pyplot as plt

#%%
asc_path=r"D:\LTSpice\Termoreg2\LTSPICE_termoreg\pyltspice\for_py.asc"
LTC = SimCommander(asc_path)
seditor=SpiceEditor(asc_path.replace(".asc",".net"))
vstr=seditor.get_component_info("Rbrs")['value']
print(vstr)
# %%
raw, log =LTC.run('for_py.net').wait_results()
LTC.wait_completion()
LTR = RawRead(raw)
vcol = LTR.get_trace("V(collector)")
vcol=np.array(vcol)
print(len(vcol))
# %%
# построение графика

plt.plot(vcol[600:])
plt.show()
# %%
