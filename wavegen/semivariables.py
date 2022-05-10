import numpy.random as rnd

disciplines = ['Simulate', 'Validate', 'ATE']

name_field = 'Name'
units_field = 'Units'
baseUnits_field = 'BaseUnits'

xAxisOptions = [
    {
        name_field: 'Frequency',
        units_field: 'MHz',
        baseUnits_field: 'Hz'
    },
    {
        name_field: 'Voltage',
        units_field: 'mV',
        baseUnits_field: 'V'
    },
    {
        name_field: 'Time',
        units_field: 'ms',
        baseUnits_field: 's'
    },
    {
        name_field: 'Decibels',
        units_field: 'dB',
        baseUnits_field: 'dB'
    },
    {
        name_field: 'Degrees',
        units_field: 'C',
        baseUnits_field: 'C'
    }
]

yAxisOptions = [
    {
        name_field: 'R_SigmaJA',
        units_field: 'CW',
        baseUnits_field: 'CW'
    },
    {
        name_field: 'R_SigmaJCTop',
        units_field: 'CW',
        baseUnits_field: 'CW'
    },
    {
        name_field: 'RSigmaJB',
        units_field: 'CW',
        baseUnits_field: 'CW'
    },
    {
        name_field: 'V_ESD',
        units_field: 'V',
        baseUnits_field: 'V'
    },
    {
        name_field: 'TND+N',
        units_field: 'dB',
        baseUnits_field: 'dB'
    },
    {
        name_field: 'IMD',
        units_field: 'dB',
        baseUnits_field: 'dB'
    },
    {
        name_field: 'GBW',
        units_field: 'MHz',
        baseUnits_field: 'Hz'
    },
    {
        name_field: 'SR',
        units_field: 'V/us',
        baseUnits_field: 'V/us'
    },
    {
        name_field: 'Overload Recovery',
        units_field: 'ns',
        baseUnits_field: 's'
    },
    {
        name_field: 'Channel Separation',
        units_field: 'dB',
        baseUnits_field: 'dB'
    },
    {
        name_field: 'e_n',
        units_field: 'nVpp',
        baseUnits_field: 'Vpp'
    },
    {
        name_field: 'e_n',
        units_field: 'uVpp',
        baseUnits_field: 'Vpp'
    },
    {
        name_field: 'I_n',
        units_field: 'pA/rtHz',
        baseUnits_field: 'A/rtHz'
    },
    {
        name_field: 'V_OS',
        units_field: 'mV',
        baseUnits_field: 'V'
    },
    {
        name_field: 'V_OS',
        units_field: 'uV/C',
        baseUnits_field: 'V/C'
    },
    {
        name_field: 'PSRR',
        units_field: 'uV/V',
        baseUnits_field: 'V/V'
    },
    {
        name_field: 'I_B',
        units_field: 'nA',
        baseUnits_field: 'A'
    }
]
yAxisLabels = [
    'I_OS (nA)',
    'V_CM (V)',
    'CMRR (uV/V)',
    'A_OL (dB)',
    'V_OUT (V)',
    'I_OUT (mA)',
    'Z_Q (ohm)',
    'I_SC (mA)',
    'C_Load (pF)',
    'I_Q (uA)',
    'LSBR (MHz)',
    'BW (MHz)',
    'HD2 (dBc)',
    'HD3 (dBv)',
    'IMD3 (dBc)',
    'OIP3 (dBm)',
    'P1dB (dBm)',
    'NF (dB)',
    'S11 (dB)',
    'S22 (dB)',
    'E_G (dB)',
    'Z_in (ohm)',
    'C_in (pF)',
    'V_ICM (V)',
    'V_IL (V)',
    'V_IH (V)',
    'Z_o (ohm)',
    'V_OL (V)',
    'V_OH (V)',
    'V_OM (V)',
    'CMRR (dB)',
    'V_S (V)',
    'f_sc (MHz)',
    't_PH (ns)',
    't_PL (ns)',
    't_SU (ns)',
    't_H (ns)',
    't_IZ (ns)',
    't_ODZ (ns)',
    't_OD (ns)',
    't_CSS (ns)',
    't_CSH (ns)',
    't_IAG (ns)',
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
    return names[rnd.randint(0, len(names))]

def get_random_xaxis_title():
    info = get_random_xaxis_info()
    return format_axis_title(info)

def get_random_xaxis_info():
    return __get_random_element_from_array(xAxisOptions)

def get_random_yaxis_title():
    info = get_random_yaxis_info()
    return format_axis_title(info)

def get_random_yaxis_info():
    return __get_random_element_from_array(yAxisOptions)

def get_random_discipline():
    return __get_random_element_from_array(disciplines)

def format_axis_title(axis_info):
    return axis_info[name_field] + ' (' + axis_info[units_field] + ')'