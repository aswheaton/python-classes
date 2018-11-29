import math as m

def PDF(time, theta, tau1, tau2, frac):
    
    normalisation1 = (3*m.pi*(1-m.exp(-10.0/tau1))*tau1)**-1
    normalisation2 = (3*m.pi*(1-m.exp(-10.0/tau2))*tau2)**-1
    
    PDF1 = normalisation1 * (1+m.cos(theta)**2) * m.exp(-time/tau1)
    PDF2 = normalisation2 * 3 * m.sin(theta)**2 * m.exp(-time/tau2)

    return(frac*PDF1 + (1-frac)*PDF2)
