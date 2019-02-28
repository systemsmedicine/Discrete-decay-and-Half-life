# -*- coding: utf-8 -*-
"""
Created on Wed 20.02.2019 10:01:50 

@author: Gustavo Hernandez-Mejia
"""

import matplotlib.pyplot as plt
import math   
from mpl_toolkits.mplot3d import axes3d
import numpy as np
import pandas as pd
import random

# Initial array of size N
N=100000
life = np.arange(N)
#life = np.stack((arr,np.zeros(N)), axis=1) 
#life = arr

prop_cycle = plt.rcParams['axes.prop_cycle'] #Colors
colors = prop_cycle.by_key()['color']

# populations
living = np.empty([1, 2])
dying = np.empty([1, 2])

life_count = 0

dead_amount = np.empty([1, 2])
life_amount = np.empty([1, 2])


point_clear = np.empty([1, 1])
point_clear=np.delete(point_clear, 0,0)

# Half-life (hours)
Half_life = 72
days = 20
time_stop = (24/6)*days
step_1 = 1  
step_long = 6
L = np.log(2)/Half_life

prob_dying = 1-np.exp(-L*step_long)   # the step is 6h.

event_list_step = []
event_list_step.append(life)

while step_1 <= time_stop and life.size != 0:
#    The probability is divided by 2 since it is a binary decition (live/die)
    dead_count = 0
     
    #print('Hour',step*6)
    for i in range(len(life)):
        if random.random() <= prob_dying:
            #life=np.delete(life, i,0) 
            point_clear = np.concatenate((point_clear, np.array([[i]])), 
                                                                     axis=None)
            dead_count += 1
    if point_clear.size != 0:
        life = np.delete(life, point_clear, 0) 
        life_count = len(life)
        
    point_clear = np.empty([1, 1])      
    point_clear=np.delete(point_clear, 0,0)
    event_list_step.append(life)  #  Keeps record of individuals
    
    dead_amount=np.concatenate((dead_amount, np.array([[step_1*step_long, 
                                                        dead_count]])), axis=0)
    life_amount=np.concatenate((life_amount, np.array([[step_1*step_long,
                                                        life_count]])), axis=0)

    step_1 += 1  
    
dead_amount=np.delete(dead_amount, 0,0) 
life_amount[0,0]=0
life_amount[0,1]=N

#_____________________       PLOTTING      ____________________________________ 
long = len(life_amount)
times = np.linspace(0.,life_amount[long-1,0],1000)
ax1=plt.figure(2, figsize=(11,7), facecolor='w', edgecolor='k')
plt.plot((life_amount[:,0]), (life_amount[:,1]), '--', color=colors[1])
plt.plot(times,N*np.exp(-L*times), '-', c=colors[2], label='Half-life decay')
plt.bar((life_amount[:,0]), (life_amount[:,1]), 0.7)
plt.scatter((life_amount[:,0]), (life_amount[:,1]), s=38, color=colors[0],
                                       marker='o',alpha=1, label='Life_amount')
plt.grid(True)
plt.xlabel("Time (h)", fontsize=16)
plt.ylabel("Individuals (counts)", fontsize=16)
plt.title('Half-life based on constant probability, time steps (6h)', 
                                                                   fontsize=20)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend(fontsize=12)
#ax1.savefig('Half_life_constant_probability_6h.pdf', format='pdf', dpi=1400)
plt.show()


print('Prob_death: ', prob_dying)




#_____________________       EOF      _________________________________________ 