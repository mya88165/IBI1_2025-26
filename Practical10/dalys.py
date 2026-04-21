import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Change this to your own folder path
os.chdir("/Users/mee/Downloads/IBI1_materials/IBI1_2025-26/IBI1_2025-26/Practical10")

print(os.getcwd())
print(os.listdir())

# Read CSV file
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# Inspect dataframe
print(dalys_data.head(5))
print(dalys_data.info())
print(dalys_data.describe())

# Third and fourth columns (Year and DALYs) for first 10 rows
first_10 = dalys_data.iloc[0:10, 2:4]
print(first_10)

max_row = first_10.loc[first_10["DALYs"].idxmax()]
print("Max DALYs in first 10 Afghanistan rows:")
print(max_row)

# The year with the maximum DALYs across the first 10 Afghanistan rows is: XXXX

# Zimbabwe years using Boolean + loc
zimbabwe_years = dalys_data.loc[dalys_data["Entity"] == "Zimbabwe", "Year"]
print(zimbabwe_years)

print("First Zimbabwe year:", zimbabwe_years.min())
print("Last Zimbabwe year:", zimbabwe_years.max())

# Zimbabwe data were recorded from XXXX to XXXX

# Find max and min DALYs countries in 2019
recent_data = dalys_data.loc[dalys_data["Year"] == 2019, ["Entity", "DALYs"]]

max_country = recent_data.loc[recent_data["DALYs"].idxmax()]
min_country = recent_data.loc[recent_data["DALYs"].idxmin()]

print("Maximum DALYs in 2019:")
print(max_country)

print("Minimum DALYs in 2019:")
print(min_country)

# Country with maximum DALYs in 2019: XXXX
# Country with minimum DALYs in 2019: XXXX

# Plot DALYs over time for one selected country
country_name = max_country["Entity"]
country_data = dalys_data.loc[dalys_data["Entity"] == country_name, ["Year", "DALYs"]]

plt.figure(figsize=(10, 5))
plt.plot(country_data["Year"], country_data["DALYs"], 'b+')
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.title(f"DALYs over time in {country_name}")
plt.xticks(country_data["Year"], rotation=-90)
plt.tight_layout()
plt.show()

# Question task starts here
dalys_2019 = dalys_data.loc[dalys_data["Year"] == 2019, "DALYs"]

plt.figure(figsize=(8, 5))
plt.boxplot(dalys_2019)
plt.ylabel("DALYs")
plt.title("Distribution of DALYs across all countries in 2019")
plt.tight_layout()
plt.show()

print("Median DALYs in 2019:", dalys_2019.median())
print("Mean DALYs in 2019:", dalys_2019.mean())
print("Minimum DALYs in 2019:", dalys_2019.min())
print("Maximum DALYs in 2019:", dalys_2019.max())