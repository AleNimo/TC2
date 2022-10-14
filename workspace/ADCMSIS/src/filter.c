/*
===============================================================================
 Name        : filter.c
 Authors     : Israel Pavelek, Cesar Fuoco, npp
 Version     : 1.0
 Copyright   : $(copyright)
 Description : main definition
===============================================================================
*/

#include "filter.h"

float32_t lowpass_taps[LOWPASS_TAP_NUM] = {
		0.003221104751733098,0.0013529433299383775,0.0016275818791218763,0.0019311414211045084,0.0022640645437228026,0.0026257204473965883,0.0030170717884689165,0.003439045325396573,0.0038931617714463708,0.004376549205862919,0.0048857412274315734,0.005421337313790469,0.005989685494446353,0.006574471459980478,0.007186406886504233,0.00781744135481378,0.00846749551778523,0.009133662403753035,0.009812350804889033,0.010500588738973311,0.011195998831749397,0.011894892380475554,0.012592436658145576,0.013285897407682126,0.013973238175523168,0.014647576481258924,0.015308169370184074,0.015949133765040327,0.016567819182665904,0.0171604089550711,0.017722762037394035,0.018251351308499385,0.018743414720751982,0.01919592165053755,0.01960519688129726,0.019969539693979778,0.02028669363991169,0.020553921878667135,0.020770522965881943,0.02093383340438279,0.02104352964333179,0.021098781040298373,0.021098781040298373,0.02104352964333179,0.02093383340438279,0.020770522965881943,0.020553921878667135,0.02028669363991169,0.019969539693979778,0.01960519688129726,0.01919592165053755,0.018743414720751982,0.018251351308499385,0.017722762037394035,0.0171604089550711,0.016567819182665904,0.015949133765040327,0.015308169370184074,0.014647576481258924,0.013973238175523168,0.013285897407682126,0.012592436658145576,0.011894892380475554,0.011195998831749397,0.010500588738973311,0.009812350804889033,0.009133662403753035,0.00846749551778523,0.00781744135481378,0.007186406886504233,0.006574471459980478,0.005989685494446353,0.005421337313790469,0.0048857412274315734,0.004376549205862919,0.0038931617714463708,0.003439045325396573,0.0030170717884689165,0.0026257204473965883,0.0022640645437228026,0.0019311414211045084,0.0016275818791218763,0.0013529433299383775,0.003221104751733098
};

float32_t biquad1_taps[BIQUAD1_TAP_NUM] = {
		0.007090218822253807,0.007090218822253807,
		-0.9858195623554924
};

//Buffers para coeficientes de punto fijo
q31_t lowpass_taps_q31[LOWPASS_TAP_NUM];

q31_t biquad1_taps_q31[BIQUAD1_TAP_NUM];
