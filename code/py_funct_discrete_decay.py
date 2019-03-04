# -*- coding: utf-8 -*-
"""
Created on Fri 01.03.2019 12:51:45 

@author: Gustavo Hernandez-Mejia
"""

"""
    Function to compute the number individual that remain after a probability of
    selection. The discrete decay follows the half-life concept.
    
 input. 
     N_pop: Array of the population that decay.
     hal_lif: Half-life
     step: Discrete time-step. 
           The smaller time-step the higher resolution of decay. 
     time: Parameter for setting the long of the simulation.
    
 output. 
 event_list_step: List containing the living individuals for each step in the 
                  decay.
 quantity: array with the number of individuals for each step in the decay.

"""

import numpy as np
import random

def py_discrete_decay(N_pop, hal_lif, step, time):
    
    event_list_step = []
    event_list_step.append(N_pop)
    point_clear = np.empty([1, 1])
    point_clear = np.delete(point_clear, 0,0)
    quantity = np.empty([1, 1])
    quantity[0,0] = len(N_pop)
    L = np.log(2)/hal_lif
    prob_dying = 1-np.exp(-L*step)
    
    while step <= time and N_pop.size != 0:
        dead_count = 0
        for i in range(len(N_pop)):
            if random.random() <= prob_dying:
                point_clear = np.concatenate((point_clear, np.array([[i]])), 
                                                                   axis=None)
                dead_count += 1
        if point_clear.size != 0:
            N_pop = np.delete(N_pop, point_clear, 0) 
            
        point_clear = np.empty([1, 1])      
        point_clear=np.delete(point_clear, 0,0)
        event_list_step.append(N_pop)  #  Keeps record of individuals
        quantity = np.concatenate((quantity, np.array([[len(N_pop)]])), 
                                                                   axis=None)
        step += 1  
    
    return event_list_step, quantity
