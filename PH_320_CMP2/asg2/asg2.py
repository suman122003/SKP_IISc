import numpy as np
import matplotlib.pyplot as plt

kF = 1.0

def om1(q, kF):
    '''
    Calculate the minimum and maximum omega values for a given q < 2kF.
    '''
    return q*0, 2*kF*q + q**2

def om2(q, kF):
    '''
    Calculate the minimum and maximum omega values for a given q > 2kF.
    '''
    return - 2*kF*q + q**2, 2*kF*q + q**2

def om3(q, kF):
    '''
    Calculate the minimum and maximum omega values for a given q < 2kF.
    '''
    return 2*kF*q - q**2, 2*kF*q + q**2

def om4(q, kF):
    '''
    Calculate the minimum and maximum omega values for a given q > 2kF.
    '''
    return - 2*kF*q + q**2, 2*kF*q + q**2

q1 = np.linspace(0, 2*kF, 100)
q2 = np.linspace(2*kF, 4*kF, 100)
om1_min, om1_max = om1(q1, kF)
om2_min, om2_max = om2(q2, kF)
om3_min, om3_max = om3(q1, kF)
om4_min, om4_max = om4(q2, kF)

plt.plot(q1, om1_min, label='$\omega$ min ($q \leq 2k_F$)', color='blue')
plt.plot(q1, om1_max, label='$\omega$ max ($q \leq 2k_F$)', color='blue', linestyle='--')
plt.plot(q2, om2_min, label='$\omega$ min ($q > 2k_F$)', color='orange')
plt.plot(q2, om2_max, label='$\omega$ max ($q > 2k_F$)', color='orange', linestyle='--')
plt.xlabel('$q$')
plt.ylabel('$\omega(q)$')
plt.title('$\omega$ vs $q$ for different regimes ($d = 2, 3$)')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(2*kF, color='grey', linewidth=0.5, linestyle='--')
plt.legend()
plt.grid()
plt.savefig('q3a.png')
plt.show()

plt.plot(q1, om3_min, label='$\omega$ min ($q \leq 2k_F$)', color='green')
plt.plot(q1, om3_max, label='$\omega$ max ($q \leq 2k_F$)', color='green', linestyle='--')
plt.plot(q2, om4_min, label='$\omega$ min ($q > 2k_F$)', color='red')
plt.plot(q2, om4_max, label='$\omega$ max ($q > 2k_F$)', color='red', linestyle='--')
plt.xlabel('$q$')
plt.ylabel('$\omega(q)$')
plt.title('$\omega$ vs $q$ for different regimes ($d = 1$)')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(2*kF, color='grey', linewidth=0.5, linestyle='--')
plt.legend()
plt.grid()
plt.savefig('q3b.png')
plt.show()

