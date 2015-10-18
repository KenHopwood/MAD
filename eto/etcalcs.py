__author__ = 'kenhopwood'

import pyeto

# Get ET0
# 22-SEP-2015
# K.Hopwood

def get_et0(t, tdew, ws, atmos_pres):
    net_radiation = net_rad(ni_sw_rad, no_lw_rad)
    svp = svp_from_t(t)
    avp = avp_from_tdew(tdew)
    delt_svp = delta_svp(t)
    psy = psy_const(atmos_pres)
    et_data = pyeto.fao56_penman_monteith(net_radiation, t, ws, svp, avp, delt_svp, psy)
    return et_data
