import numpy as np
from numpy import vectorize
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def electronEff(pt,eta):
    if pt <= 0.1 :
        Eff = 0.00
    elif (abs(eta) <= 1.5) and (pt > 0.1 and pt <= 1.0) :
        Eff = 0.73
    elif (abs(eta) <= 1.5) and (pt > 1.0 and pt <= 10) :
        Eff = 0.95
    elif (abs(eta) <= 1.5) and (pt > 10) :
        Eff = 0.99
    elif (abs(eta) > 1.5 and abs(eta) <= 2.5) and (pt > 0.1 and pt <= 1.0) :
        Eff = 0.50
    elif (abs(eta) > 1.5 and abs(eta) <= 2.5) and (pt > 1.0 and pt <= 10) : 
        Eff = 0.83 
    elif (abs(eta) > 1.5 and abs(eta) <= 2.5) and (pt > 10) :
        Eff = 0.90

    return Eff

velectronEff = vectorize(electronEff)

def muonEff(pt,eta):
    if pt <= 0.1 :
        Eff = 0.00
    elif (abs(eta) <= 1.5) and (pt > 0.1 and pt <= 1.0) :
        Eff = 0.75
    elif (abs(eta) <= 1.5) and (pt > 1.0) :
        Eff = 0.99
    elif (abs(eta) > 1.5 and abs(eta) <= 2.5) and (pt > 0.1 and pt <= 1.0) :
        Eff = 0.70
    elif (abs(eta) > 1.5 and abs(eta) <= 2.5) and (pt > 1.0 ) :
        Eff = 0.98
    return Eff

vmuonEff = vectorize(muonEff)

def pionEff(pt,eta):
    if pt <= 0.1 :
        Eff = 0.00
    elif (abs(eta) <= 1.5) and (pt > 0.1 and pt <= 1.0) :
        Eff = 0.70
    elif (abs(eta) <= 1.5) and (pt > 1.0) :
        Eff = 0.95
    elif (abs(eta) > 1.5 and abs(eta) <= 2.5) and (pt > 0.1 and pt <= 1.0) :
        Eff = 0.60
    elif (abs(eta) > 1.5 and abs(eta) <= 2.5) and (pt > 1.0 ) :
        Eff = 0.85
    return Eff

vpionEff = vectorize(pionEff)

def effPlotter(eta_parts, ptList, fct, axes, lineStylesList, labelList):
    if len(ptList) != len(lineStylesList) or len(ptList) != len(labelList) :
       print "pt, line style and label lists must have the same length"
       return
    #for part in eta_parts :

    for i in range(len(ptList)):
        j=0
        for part in eta_parts :
            Eff = fct(ptList[i],part)
            if j == 0 :
                axes.plot(part, Eff, linestyle=lineStylesList[i], color='black', label=labelList[i])
            else :
                axes.plot(part, Eff, linestyle=lineStylesList[i], color='black')
            j+=1


eta_barrel = np.linspace(-1.5, 1.5, num=30)
eta_ec1 = np.linspace(-2.5, -1.6, num=9)
eta_ec2 = np.linspace(1.6, 2.5, num=9)

eta_parts = [eta_ec1, eta_barrel, eta_ec2]

fig = plt.figure(figsize=(10,15))

ax = fig.add_subplot(111)
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['right'].set_color('none')
ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')


elec_axes = fig.add_subplot(311)
effPlotter(eta_parts, [100,10,1], velectronEff, elec_axes, ['-','--',':'], [r'$p_T \geq 10$ GeV', r'$1 \leq p_T < 10$ GeV', r'$0.1 \leq p_T < 1$ GeV'])
leg = elec_axes.legend(loc=4, borderaxespad=0.)
leg.get_frame().set_linewidth(0.0)
elec_axes.set_ylim([0,1])
elec_axes.tick_params(labelsize=20)
elec_axes.text(-2.8, 0.1 , r'electrons', fontsize=20)

muon_axes = fig.add_subplot(312)
effPlotter(eta_parts, [10,1], vmuonEff, muon_axes, ['-','--'], [r'$p_T \geq 1$ GeV', r'$0.1 \leq p_T < 1$ GeV'])
leg=muon_axes.legend(loc=4, borderaxespad=0.)
leg.get_frame().set_linewidth(0.0)
muon_axes.set_ylim([0,1])
muon_axes.tick_params(labelsize=20)
muon_axes.text(-2.8, 0.1 , r'muons', fontsize=20)

pion_axes = fig.add_subplot(313)
effPlotter(eta_parts, [10,1], vpionEff, pion_axes, ['-','--'], [r'$p_T \geq 1$ GeV', r'$0.1 \leq p_T < 1$ GeV'])
leg = pion_axes.legend(loc=4, borderaxespad=0.)
leg.get_frame().set_linewidth(0.0)
pion_axes.set_ylim([0,1])
pion_axes.tick_params(labelsize=20)
pion_axes.text(-2.8, 0.1 , r'charged hadrons', fontsize=20)

ax.set_xlabel(r'$\eta$', fontsize=25, labelpad=25)
ax.set_ylabel('Efficiency', fontsize=20, labelpad=20)
#ax.set_xticklabels(labelsize=10)

plt.show()
fig.savefig('efficiencies.png')
