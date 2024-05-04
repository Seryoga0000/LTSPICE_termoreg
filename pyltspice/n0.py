#%%
from PyLTSpice import SimRunner
from PyLTSpice import RawRead
from PyLTSpice import SpiceEditor
import numpy as np
import matplotlib.pyplot as plt
import ltspice

#%%
asc_path=r"D:\LTSpice\Termoreg2\LTSPICE_termoreg\OthersScheme\OldScheme\static.asc"
LTC = SimRunner(output_folder='./temp')
seditor=SpiceEditor(asc_path.replace(".asc",".net"))
vstr=seditor.get_component_info("R60")['value']
print(vstr)
# %%


def run_sim(LTC, seditor):
    raw, log =LTC.run(seditor,run_filename='for_py.net').wait_results()
    LTC.wait_completion()
    return raw

def print_params(raw):
    l = ltspice.Ltspice(raw)
    l.parse()
    vcol = l.get_data("V(Collector_1)")
    vcol=np.array(vcol)
    # print("Length of vcol:", len(vcol))
    print("Mean value of vcol:", np.mean(vcol))

def str_to_num(s):
    multipliers = {'p': 1e-12, 'n': 1e-9, 'u': 1e-6, 'm': 1e-3, 'k': 1e3, 'Meg': 1e6, 'G': 1e9}
    if s[-3:] in multipliers:
        return float(s[:-3]) * multipliers[s[-3:]]
    elif s[-1] in multipliers:
        return float(s[:-1]) * multipliers[s[-1]]
    else:
        return float(s)

def num_to_str(n):
    if n >= 1e9:
        return str(n / 1e9) + 'G'
    elif n >= 1e6:
        return str(n / 1e6) + 'Meg'
    elif n >= 1e3:
        return str(n / 1e3) + 'k'
    elif n >= 1e-3:
        return str(n / 1e-3) + 'm'
    elif n >= 1e-6:
        return str(n / 1e-6) + 'u'
    elif n >= 1e-9:
        return str(n / 1e-9) + 'n'
    elif n >= 1e-12:
        return str(n / 1e-12) + 'p'
    else:
        return str(n)

def change_component(seditor, component_name, ppm):
    component_info = seditor.get_component_info(component_name)
    component_value = str_to_num(component_info['value'])
    new_value = num_to_str(component_value * (1 + ppm / 1e6))
    seditor.set_component_value(component_name, new_value)

def change_and_run(seditor, component_name, ppm):
    change_component(seditor, component_name, ppm)
    raw = run_sim(LTC, seditor)
    print_params(raw)
    seditor.reset_netlist()

change_and_run(seditor, "R60", -100)
change_and_run(seditor, "R8", 50)
change_and_run(seditor, "R10", 70)

