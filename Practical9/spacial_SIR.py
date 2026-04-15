# import necessary library 
import numpy as np
import matplotlib.pyplot as plt

# make array of all susceptible population
population = np.zeros((100, 100))

# randomly infect one person
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1

beta = 0.3
gamma = 0.05

# pseudocode:
# for each time step:
#   find infected cells
#   for each infected cell:
#       check all 8 neighbours
#       if neighbour is susceptible, infect with probability beta
#       infected cell can recover with probability gamma
#   update population
#   plot result

plt.figure(figsize=(6,4), dpi=150)
plt.imshow(population, cmap='viridis', interpolation='nearest')
plt.title('time 0')
plt.show()

for t in range(1, 101):
    new_population = population.copy()
    infected_points = np.argwhere(population == 1)

    for point in infected_points:
        x, y = point

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue

                nx = x + dx
                ny = y + dy

                if 0 <= nx < 100 and 0 <= ny < 100:
                    if population[nx, ny] == 0:
                        if np.random.random() < beta:
                            new_population[nx, ny] = 1

        if np.random.random() < gamma:
            new_population[x, y] = 2

    population = new_population

    # ONLY plot these times
    if t in [10,50,100]:
        plt.figure(figsize=(4,4), dpi=100)
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title(f'time {t}')
        plt.show()