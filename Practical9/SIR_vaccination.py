import numpy as np
import matplotlib.pyplot as plt

N = 10000
beta = 0.3
gamma = 0.05
time_steps = 1000

vaccination_rates = range(0, 101, 10)

plt.figure(figsize=(6,4), dpi=150)

for v in vaccination_rates:
    vaccinated = int(N * v / 100)

    if vaccinated >= N:
        S = 0
        I = 0
        R = 0
        I_values = [0] * (time_steps + 1)
    else:
        I = 1
        R = 0
        S = N - vaccinated - I

        I_values = [I]

        for t in range(time_steps):
            if I == 0:
                I_values.append(0)
                continue

            infection_prob = beta * (I / N)

            if S > 0:
                new_infections = np.sum(np.random.choice([0, 1], size=S, p=[1-infection_prob, infection_prob]))
            else:
                new_infections = 0

            new_recoveries = np.sum(np.random.choice([0, 1], size=I, p=[1-gamma, gamma]))

            S = S - new_infections
            I = I + new_infections - new_recoveries
            R = R + new_recoveries

            I_values.append(I)

    plt.plot(I_values, label=f'{v}%')

plt.xlabel('time')
plt.ylabel('infected people')
plt.title('SIR model with different vaccination rates')
plt.legend()
plt.show()