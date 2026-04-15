# import necessary library 
import numpy as np
import matplotlib.pyplot as plt

S = 9999
I = 1
R = 0
N = 10000

beta = 0.3
gamma = 0.05

# make list to store variables 
S_values = [S]
I_values = [I]
R_values = [R]

# for each time step:
#   calculate infection probability = beta * (I / N)
#   randomly decide how many susceptible people become infected
#   randomly decide how many infected people recover
#   update S, I, R
#   store updated values in lists

for t in range(1000):
    infection_prob = beta * (I / N)

    new_infections = np.sum(np.random.choice([0, 1], size=S, p=[1-infection_prob, infection_prob]))
    new_recoveries = np.sum(np.random.choice([0, 1], size=I, p=[1-gamma, gamma]))

    S = S - new_infections
    I = I + new_infections - new_recoveries
    R = R + new_recoveries

    S_values.append(S)
    I_values.append(I)
    R_values.append(R)

plt.figure(figsize=(6,4), dpi=150)
plt.plot(S_values, label='susceptible')
plt.plot(I_values, label='infected')
plt.plot(R_values, label='recovered')

plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model')
plt.legend()

plt.savefig("sir_graph.png")
plt.show()