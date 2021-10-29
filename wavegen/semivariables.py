import numpy.random as rnd

disciplines = ['Simulate', 'Validate', 'ATE']
xAxisLabels = ['Frequency', 'Voltage', 'Time', 'Decibels (dB)', 'Degrees']
yAxisLabels = ['S_PA_Out_PA_In_Phase (deg)',
'S_PA_Out_PA_In_Mag (dB)',
'S_PA_In_PA_Out_Mag (dB)',
'S_PA_Out_PA_Out_Phase (deg)',
'S_PA_Out_PA_Out_Mag (dB)',
'S_PA_In_PA_In_Phase (deg)',
'S_PA_In_PA_In_Mag (dB)',
'S_PA_In_PA_Out_Phase (deg)',
'Mu2 source',
'K Factor',
'Mu1 load',
'Gain Imbalance (dB)',
'Common-mode rejection ratio (dB)',
'Phase Imbalance (deg)',
'Idc_Vcc1 (mA)',
'Idc_Vcc2 (mA)',
'Gain (dB)',
'Pout (dBm)',
'Irf_Vcc1 (mA)',
'Irf_Vcc2 (mA)',
'OP1dB (dBm)',
'IP1dB (dBm)',
'IP3dB (dBm)',
'OP3dB (dBm)',
'OIP3 Min (dBm)',
'Noise Floor Power (dBm)',
'OIP3 AVG (dBm)',
'OIP3 Delta (dB)',
'OIP3 LSB (dBm)',
'OIP3 Max (dBm)',
'IIP3 Min (dBm)',
'OIP3 USB (dBm)',
'IIP3 USB (dBm)',
'Actual_Pin_at_f2 (dBm)',
'Actual_Pin_at_f1 (dBm)',
'Pout_at_IMH (dBm)',
'Noise Floor Frequency (GHz)',
'Attenuation (dB)',
'Pout_at_IML (dBm)',
'IIP3 Delta (dB)',
'Gain_at_f1 (dB)',
'Pout_at_f2 (dBm)',
'IMH Frequency (GHz)',
'IML Frequency (GHz)',
'Gain_at_f2 (dB)',
'IIP3 Max (dBm)',
'IIP3 LSB (dBm)',
'Pout_at_f1 (dBm)',
'IIP3 AVG (dBm)',
'Gain Flatness (dB)',
'Group Delay (ps)',
'Noise Figure (dB)',
'Noise Temperature (K)',
'Noise Gain (dB)',
'Idc_Vdig (mA)',
'Irf_Vcc (mA)',
'ACLR Adj. Channel Max (dBc)',
'ACLR Alt1. Channel Max (dBc)',
'ACLR Up. Alt1. Channel (dBc)',
'ACLR Up. Adj. Channel (dBc)',
'ACLR Low. Alt1. Channel (dBc)',
'ACLR Low. Adj. Channel (dBc)',
'Idc_Vcc (mA)',
'Vth1 (V)',
'Toff (ns)',
'Ton (ns)',
'Idc_Vcc2 (uA)',
'Idc_Vcc1 (uA)',
'Idc_Vcc (uA)',
'Vth2 (V)']

def __get_random_element_from_array(names):
    return names[rnd.randint(0,len(names))]

def get_random_xaxis():
    return __get_random_element_from_array(xAxisLabels)

def get_random_yaxis():
    return __get_random_element_from_array(yAxisLabels)

def get_random_discipline():
    return __get_random_element_from_array(disciplines)