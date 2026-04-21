import numpy as np
import matplotlib.pyplot as plt

# set starting values from practical guide
N = 10000
beta = 0.3
gamma = 0.05
time_steps = 1000

# test vaccination rates from 0% to 100%
vaccination_rates = range(0, 101, 10)

plt.figure(figsize=(6,4), dpi=150)

# loop through each vaccination percentage
for v in vaccination_rates:

    # calculate number of vaccinated people
    vaccinated = int(N * v / 100)

    # if everyone vaccinated, nobody can be infected
    if vaccinated >= N:

        # make infected values all zero
        I_values = [0] * (time_steps + 1)

    else:
        # start with 1 infected person
        I = 1

        # nobody recovered yet
        R = 0

        # rest of people are susceptible
        S = N - vaccinated - I

        # store infected numbers over time
        I_values = [I]

        # repeat for 1000 time steps
        for t in range(time_steps):

            # if no infected people remain
            # outbreak has ended
            if I == 0:
                I_values.append(0)
                continue

            # infection chance depends on
            # beta and proportion infected
            infection_prob = min(beta * (I / N), 1)

            # if susceptible people remain
            if S > 0:

                # randomly choose who gets infected
                new_infections = np.sum(
                    np.random.choice(
                        [0,1],
                        size=S,
                        p=[1-infection_prob, infection_prob]
                    )
                )

            else:
                new_infections = 0

            # randomly choose infected people who recover
            new_recoveries = np.sum(
                np.random.choice(
                    [0,1],
                    size=I,
                    p=[1-gamma, gamma]
                )
            )

            # update groups
            S = S - new_infections
            I = I + new_infections - new_recoveries
            R = R + new_recoveries

            # store infected number for graph
            I_values.append(I)

    # plot infected curve for this vaccination %
    plt.plot(I_values, label=f"{v}%")

plt.xlabel("time")
plt.ylabel("infected people")
plt.title("SIR model with different vaccination rates")
plt.legend(loc="upper right", fontsize=8)
plt.show()