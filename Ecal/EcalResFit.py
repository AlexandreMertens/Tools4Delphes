import numpy as np
from numpy import vectorize
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def barrel(x, p):
    return p*(0.8)+(0.8*x*x)

def endCap(x,p):
    return 33.8 - 1.27 + p*(0.8) - 30.8 *x + 7.65*x*x

def etares(x,p):
    if x < 1.5:
        return p*(0.8)+(0.8*x*x)
    else :
        return 33.8 - 1.27 + p*(0.8) - 30.8 *x + 7.65*x*x

def pol2centered(x,a,c):
    return a + c*x*x

def pol2(x,a,b,c):
    return a + b*x + c*x*x

def funcERes(x,a,b):
    return np.sqrt(a*a/(x*x) + b*b/x + 1*1)

def testMich(energy,eta):
    if eta < 1.5:
        resol = (1+0.5*eta*eta) * np.sqrt(energy*energy*0.8*0.8 + energy*11*11 + 40*40)/energy
    else :
        resol = (2.16 + 5.6*(eta-2)*(eta-2)) * np.sqrt(energy*energy*0.8*0.8 + energy*11*11 + 40*40)/energy
    return resol

eta_EB = np.array([0.002552,
0.012758,
0.032321,
0.073147,
0.123329,
0.172661,
0.222843,
0.273876,
0.323208,
0.37339,
0.413366,
#0.432928,
#0.441434,
0.45079,
0.478007,
0.523937,
0.573269,
0.623451,
0.672783,
0.723815,
0.76294,
0.783354,
#0.791859,
#0.798663,
0.825881,
0.873512,
0.923694,
0.973876,
1.022357,
1.074241,
1.113366,
#1.138032,
#1.173755,
1.223937,
1.273269,
1.323451,
1.373633,
1.424666
])

eta_EE = np.array([1.574707,
1.624356,
1.674005,
1.72459,
1.774239,
1.824824,
1.87541,
1.925059,
1.97377,
2.025293,
2.074941,
2.125527,
2.175176,
2.224824,
2.274473,
2.325995,
2.374707,
2.424356,
2.474941
])

sigma_EB = np.array([1.664773,
1.295455,
1.153409,
1.306818,
1.448864,
1.295455,
1.363636,
1.568182,
1.522727,
1.295455,
1.494318,
#1.971591,
#2.880682,
1.443182,
1.477273,
1.409091,
1.477273,
1.477273,
1.482955,
1.732955,
1.397727,
1.619318,
#2.960227,
#2.073864,
1.715909,
1.8125,
1.914773,
1.909091,
1.960227,
2.051136,
2.1875,
#2.829545,
#2.954545,
2.392045,
2.8125,
2.755682,
2.897727,
3.142045
])

sigma_EE = np.array([4.52459,
3.92686,
3.245902,
3.253468,
2.791929,
3.283733,
3.10971,
3.382093,
2.799496,
2.769231,
2.723834,
2.95082,
3.283733,
2.807062,
3.04918,
2.799496,
3.699874,
4.335435,
4.638083])

Energy = np.array([8.862069,
10.827586,
12.793103,
14.862069,
16.827586,
18.793103,
20.862069,
22.827586,
24.896552,
26.965517,
28.931034,
30.793103,
32.965517,
34.931034,
36.896552,
38.862069,
40.931034,
42.793103,
44.965517,
46.827586,
48.896552,
50.758621,
52.724138,
55,
56.965517,
58.931034,
61,
62.965517,
64.931034,
67,
69.068966,
70.827586,
73,
74.965517,
76.827586,
79,
80.862069,
82.827586,
85,
86.965517,
89.034483,
91,
92.965517,
94.931034,
96.896552,
98.862069
])

sigma_Energy = np.array([6.907692,
6.184615,
5.861538,
5.046154,
4.769231,
4.523077,
4.184615,
4.061538,
3.753846,
3.523077,
3.276923,
3.030769,
3.046154,
2.907692,
2.769231,
2.784615,
2.738462,
2.538462,
2.569231,
2.369231,
2.353846,
2.276923,
2.230769,
2.138462,
2.261538,
2.153846,
2.107692,
2.153846,
2.030769,
2.030769,
1.969231,
1.969231,
1.953846,
1.923077,
1.907692,
1.892308,
1.830769,
1.830769,
1.876923,
1.830769,
1.784615,
1.784615,
1.784615,
1.753846,
1.707692,
1.723077
])


fig = plt.figure()
fig.subplots_adjust(left=0.2, wspace=0.6)

# Barrel Eta Fit

ax1 = fig.add_subplot(221)
popt_EB, pcov_EB = curve_fit(pol2centered, eta_EB, sigma_EB)
ax1.plot(eta_EB, sigma_EB, 'b+',linestyle='None')
print "barrel : "+str(popt_EB[0])+" + "+str(popt_EB[1])+"x^2"
fitted_sigma_EB = pol2centered(eta_EB,popt_EB[0],popt_EB[1])
ax1.plot(eta_EB,fitted_sigma_EB,'r')

# EndCap Eta Fit

ax2 = fig.add_subplot(222)
popt_EE, pcov_EE = curve_fit(pol2, eta_EE, sigma_EE)
ax2.plot(eta_EE, sigma_EE, 'b+',linestyle='None')
print "endcap : "+str(popt_EE[0])+" + "+str(popt_EE[1])+"x + " +str(popt_EE[2])+"x^2"
fitted_sigma_EE = pol2(eta_EE,popt_EE[0],popt_EE[1],popt_EE[2])
ax2.plot(eta_EE,fitted_sigma_EE,'r')


# Energy dependence

ax3 = fig.add_subplot(223)
popt_ERes, pcov_ERes = curve_fit(funcERes, Energy, sigma_Energy)
ax3.plot(Energy, sigma_Energy, 'b+',linestyle='None')
print popt_ERes
Energy_fitted = np.arange(10.0, 100.0, 5)
fitted_sigma_EnergyRes = funcERes(Energy_fitted,popt_ERes[0],popt_ERes[1])

ax3.plot(Energy_fitted,fitted_sigma_EnergyRes,'r')

# test

ax4 = fig.add_subplot(224)
eta_range = np.arange(0.,2.6,0.13)

energy_test = [20,40,100]
colors = ['r','b','g']

for i in range(len(energy_test)):
    p = np.empty(20)
    p.fill(funcERes(energy_test[i],popt_ERes[0],popt_ERes[1]))

    vetares = vectorize(etares)
    sigma_range = vetares(eta_range,p)
    ax4.plot(eta_range,sigma_range,colors[i])
    vtestMich = vectorize(testMich)
    res_range = vtestMich(energy_test[i], eta_range)
    ax4.plot(eta_range,res_range,colors[i])

plt.show() 
