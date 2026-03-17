import matplotlib.pyplot as plt

populations = {
    "UK": {"2020": 66.7, "2024": 69.2},
    "China": {"2020": 1426, "2024": 1410},
    "Italy": {"2020": 59.4, "2024": 58.9},
    "Brazil": {"2020": 208.6, "2024": 212.0},
    "USA": {"2020": 331.6, "2024": 340.1}
}

population_changes = {}

for country, data in populations.items():
    pop_2020 = data["2020"]
    pop_2024 = data["2024"]
    percent_change = ((pop_2024 - pop_2020) / pop_2020) * 100
    population_changes[country] = percent_change

print("\nPercentage population changes:")
for country, change in population_changes.items():
    print(f"{country}: {change:.2f}%")

sorted_changes = sorted(population_changes.items(), key=lambda x: x[1], reverse=True)

print("\nPopulation changes from largest increase to largest decrease:")
for country, change in sorted_changes:
    print(f"{country}: {change:.2f}%")

largest_increase_country = sorted_changes[0][0]
largest_decrease_country = sorted_changes[-1][0]

print(f"\nCountry with the largest increase: {largest_increase_country}")
print(f"Country with the largest decrease: {largest_decrease_country}")

countries = list(population_changes.keys())
changes = list(population_changes.values())

plt.figure()
plt.bar(countries, changes)
plt.xlabel("Country")
plt.ylabel("Population Change (%)")
plt.title("Population Change from 2020 to 2024")
plt.show()
