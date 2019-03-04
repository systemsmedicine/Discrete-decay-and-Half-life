
"""
Created on Fri Mar  1 14:22:53 2019

@author: Gustavo Hernandez-Mejia
"""

"""
 This code is based on the Tau-leaping approximate method which is used for
 simulations of stochastic systems.
 Given the half-life of a population and time-step size for the decay, we 
 set the probability of an individual to be selected. This indicates the 
 probability to either keep or not the selected individual. 
 The time-step can be selected as a resolution parameter, the smaller 
 time-step the higher resolution of decay. 
 The population is any discrete quantity. 
 The initial population size is consistent with the "law of large numbers". The
 hihger the initial population the better behabiour of the discrete decay.
 Please refer to the README file at:
 github.com/GustavoHdezM/Discrete-decay-and-Half-life
 
 time-step = step_long
 Half_life = 72 h. You may set this parameter as needed 
 Population size = N
 
 This file is a guide of how to employ the function "py_discrete_decay(...)"
 with diverse instances. You may tailor this file (or create another) to
 use the function.
 Please refer to the README file at:
 github.com/GustavoHdezM/Discrete-decay-and-Half-life
 
"""
from py_funct_discrete_decay import *
import matplotlib.pyplot as plt
import numpy as np

#____________________    Initial settings       _______________________________

N=10000                     # Initial population of size N
life = np.arange(N)
Half_life = 72               #  72 h (3d)
stop = 40                    # 40*step_long (h)
L = np.log(2)/Half_life      # For Plotting the continous-time approach
prop_cycle = plt.rcParams['axes.prop_cycle']    #   Colors
colors = prop_cycle.by_key()['color']


"""
                            EXAMPLES 
                       Different step-long (h)

  The function returns two structures
 1. evol#, a list containing the living individuals for each step in the decay.
 2. pol#, an array with the number of individuals for each step in the decay.

"""
step_long = 1
evol1, pol1 = py_discrete_decay(life, Half_life, step_long, stop)

step_long = 2
evol2, pol2 = py_discrete_decay(life, Half_life, step_long, stop)

step_long = 4
evol4, pol4 = py_discrete_decay(life, Half_life, step_long, stop)

step_long = 6
evol6, pol6 = py_discrete_decay(life, Half_life, step_long, stop)

step_long = 8
evol8, pol8 = py_discrete_decay(life, Half_life, step_long, stop)




"""
                             PLOTTING

 Warning: You may select the case, depending of the step_long, to be plotted.
 The default case is 6h.
"""
step_long = 6        # 1,2,4,6 or 8 h
case = pol6          # pol1, pol2, pol4, pol6 or pol8 to select the case
base = np.arange(len(case))
long = len(case)*step_long
times = np.linspace(0.,long,1000)

ax1=plt.figure(2, figsize=(11,7), facecolor='w', edgecolor='k')
plt.plot(times,N*np.exp(-L*times), '-', c=colors[2], label='Continous-time')
plt.plot((base*step_long), case, '--', color=colors[1], label='Discrete-time')
plt.bar((base*step_long), case, 0.7)
plt.scatter((base*step_long), case, s=38, color=colors[0],
                                       marker='o',alpha=1, label='Life_amount')
plt.grid(True)
plt.xlabel("Time (h)", fontsize=16)
plt.ylabel("Individuals (counts)", fontsize=16)
plt.title('Discrete decay following the Half-life with time-steps of 6h', 
                                                                   fontsize=20)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend(fontsize=12)
#ax1.savefig('Half_life_decay_6h.pdf', format='pdf', dpi=1400)
plt.show()




#_____________________       EOF      _________________________________________ 