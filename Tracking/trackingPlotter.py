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

def elecSmearing(pt,eta):
    
    if (abs(eta) <= 0.5) and (pt > 0.1) :
        smear = np.sqrt(pow(0.06,2) + pow(pt,2)*pow(1.3e-3,2))
    elif abs(eta) > 0.5 and abs(eta) <= 1.5 and pt > 0.1 :
        smear = np.sqrt(pow(0.10,2) + pow(pt,2)*pow(1.7e-3,2)) 
    elif abs(eta) > 1.5 and abs(eta) <= 2.5 and pt > 0.1 :
        smear =  np.sqrt(pow(0.25,2) + pow(pt,2)*pow(3.1e-3,2))
    else :
        smear = 0   
    return smear
 
velectronSmearing=vectorize(elecSmearing)

def pionSmearing(pt,eta):

    if (abs(eta) <= 0.5) and (pt > 0.1) :
        smear = np.sqrt(pow(0.06,2) + pow(pt,2)*pow(1.3e-3,2))
    elif abs(eta) > 0.5 and abs(eta) <= 1.5 and pt > 0.1 :
        smear = np.sqrt(pow(0.10,2) + pow(pt,2)*pow(1.7e-3,2))
    elif abs(eta) > 1.5 and abs(eta) <= 2.5 and pt > 0.1 :
        smear =  np.sqrt(pow(0.25,2) + pow(pt,2)*pow(3.1e-3,2))
    else :
        smear = 0
    return smear

vpionSmearing=vectorize(pionSmearing)

def muonSmearing(pt,eta):

    if (abs(eta) <= 0.5) and (pt > 0.1) :
        smear = np.sqrt(pow(0.01,2) + pow(pt,2)*pow(2.0e-4,2))
    elif abs(eta) > 0.5 and abs(eta) <= 1.5 and pt > 0.1 :
        smear = np.sqrt(pow(0.02,2) + pow(pt,2)*pow(3e-4,2))
    elif abs(eta) > 1.5 and abs(eta) <= 2.5 and pt > 0.1 :
        smear =  np.sqrt(pow(0.05,2) + pow(pt,2)*pow(6.0e-4,2))
    else :
        smear = 0
    return smear

vmuonSmearing=vectorize(muonSmearing)


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

def smearPlotter(pt_parts, etaList, fct, axes, lineStylesList, labelList):
    if len(etaList) != len(lineStylesList) or len(etaList) != len(labelList) :
       print "pt, line style and label lists must have the same length"
       return

    for i in range(len(etaList)):
        j=0
        for part in pt_parts :
            Smear = fct(part, etaList[i])
            if j == 0 :
                axes.plot(part, Smear, linestyle=lineStylesList[i], color='black', label=labelList[i])
            else :
                axes.plot(part, Smear, linestyle=lineStylesList[i], color='black')
            j+=1


## eta definitions

eta_barrel = np.linspace(-1.5, 1.5, num=30)
eta_ec1 = np.linspace(-2.5, -1.6, num=9)
eta_ec2 = np.linspace(1.6, 2.5, num=9)

eta_parts = [eta_ec1, eta_barrel, eta_ec2]

## pt definitions

pt_range = np.linspace(0.11,100.11,num=20)

pt_parts = [pt_range]

####################
#### Efficiency ####
####################

fig1 = plt.figure(figsize=(10,15))


# adding an empty subplot at which I will add the common labels
ax = fig1.add_subplot(111)
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['right'].set_color('none')
ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')

# electron plot
elec_axes = fig1.add_subplot(311)
effPlotter(eta_parts, [100,10,1], velectronEff, elec_axes, ['-','--',':'], [r'$p_T \geq 10$ GeV', r'$1 \leq p_T < 10$ GeV', r'$0.1 \leq p_T < 1$ GeV'])
leg = elec_axes.legend(loc=4, borderaxespad=0.)
leg.get_frame().set_linewidth(0.0)
elec_axes.set_ylim([0,1])
elec_axes.tick_params(labelsize=20)
elec_axes.text(-2.8, 0.1 , r'electrons', fontsize=20)

# muon plot
muon_axes = fig1.add_subplot(312)
effPlotter(eta_parts, [10,1], vmuonEff, muon_axes, ['-','--'], [r'$p_T \geq 1$ GeV', r'$0.1 \leq p_T < 1$ GeV'])
leg=muon_axes.legend(loc=4, borderaxespad=0.)
leg.get_frame().set_linewidth(0.0)
muon_axes.set_ylim([0,1])
muon_axes.tick_params(labelsize=20)
muon_axes.text(-2.8, 0.1 , r'muons', fontsize=20)

#pion plot
pion_axes = fig1.add_subplot(313)
effPlotter(eta_parts, [10,1], vpionEff, pion_axes, ['-','--'], [r'$p_T \geq 1$ GeV', r'$0.1 \leq p_T < 1$ GeV'])
leg = pion_axes.legend(loc=4, borderaxespad=0.)
leg.get_frame().set_linewidth(0.0)
pion_axes.set_ylim([0,1])
pion_axes.tick_params(labelsize=20)
pion_axes.text(-2.8, 0.1 , r'charged hadrons', fontsize=20)

# setting common labels, (labelpad is for the offset)
ax.set_xlabel(r'$\eta$', fontsize=25, labelpad=25)
ax.set_ylabel('Efficiency', fontsize=20, labelpad=20)

#plt.show()
fig1.savefig('efficiencies.png')

###########################
#### Momentum smearing ####
###########################

fig2 = plt.figure(figsize=(10,15))


# adding an empty subplot at which I will add the common labels

ax = fig2.add_subplot(111)
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['right'].set_color('none')
ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')

# electron plot
elec_axes = fig2.add_subplot(311)
smearPlotter(pt_parts, [0.5,1.5,2.5], velectronSmearing, elec_axes, ['-','--',':'], [r'$|\eta| \leq 0.5 $', r'$ 0.5 \leq |\eta| < 1.5$', r'$ 1.5 \leq |\eta| < 2.5 $'])
leg = elec_axes.legend(loc=4)
leg.get_frame().set_linewidth(0.0)
elec_axes.tick_params(labelsize=20)
elec_axes.text(5, 0.01 , r'electrons', fontsize=20)
#pion_axes.set_xscale("log")
elec_axes.set_xlim(0.1,100)
elec_axes.set_yscale("log")
elec_axes.set_ylim(0.005,1)

# muon plot
muon_axes = fig2.add_subplot(312)
smearPlotter(pt_parts, [0.5,1.5,2.5], vmuonSmearing, muon_axes, ['-','--',':'], [r'$|\eta| \leq 0.5 $', r'$ 0.5 \leq |\eta| < 1.5$', r'$ 1.5 \leq |\eta| < 2.5 $'])
leg = muon_axes.legend(loc=1)
leg.get_frame().set_linewidth(0.0)
muon_axes.tick_params(labelsize=20)
muon_axes.text(5, 0.3 , r'muons', fontsize=20)
#pion_axes.set_xscale("log")
muon_axes.set_xlim(0.1,100)
muon_axes.set_yscale("log")
muon_axes.set_ylim(0.005,1)

# pion plot
pion_axes = fig2.add_subplot(313)
smearPlotter(pt_parts, [0.5,1.5,2.5], vpionSmearing, pion_axes, ['-','--',':'], [r'$|\eta| \leq 0.5 $', r'$ 0.5 \leq |\eta| < 1.5$', r'$ 1.5 \leq |\eta| < 2.5 $'])
leg = pion_axes.legend(loc=4)
leg.get_frame().set_linewidth(0.0)
pion_axes.tick_params(labelsize=20)
pion_axes.text(5, 0.01 , r'charged hadrons', fontsize=20)

#pion_axes.set_xscale("log")
pion_axes.set_xlim(0.1,100)
pion_axes.set_yscale("log")
pion_axes.set_ylim(0.005,1)

ax.set_xlabel(r'$p_T$ [GeV]', fontsize=25, labelpad=25)
ax.set_ylabel(r'$\sigma(p_T)/p_T$', fontsize=25, labelpad=25)



fig2.savefig('trackerSmearing.png')

