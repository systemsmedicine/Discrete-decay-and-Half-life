# Discrete decay and Half-life
Discrete-time approach for decay with a certain half-life.

This code is based on the Tau-leaping approximate method which is used for simulations of stochastic systems.
Please see details of Tau-leaping here: https://en.wikipedia.org/wiki/Tau-leaping.
The Half-life is the time required for a quantity to reduce to half its initial value, see https://en.wikipedia.org/wiki/Half-life.

Given the half-life of a population and time-step size for the decay, we set the probability of an individual to be selected. This indicates the probability to either keep or not the selected individual under a Poisson distributed random variable. The time-step can be selected as a resolution parameter, the smaller time-step the higher resolution of decay. The population is any discrete quantity. The initial population size is consistent with the "law of large numbers". The higher the initial population the better behavior of the discrete decay.

The probability of elimination (dying) is given by(code): prob_dying = 1 - np.exp(-L * step_long), where L = np.log(2)/Half_life.

This probability is taken to select individuals to continue for the next time-step or not (live/die).
On each time-step (step_long), individuals are uniformly randomly selected to be eliminated.

In the "Figs" carpet you can see different examples of time-step selection for a half-life of 72h with a population of 100000.


