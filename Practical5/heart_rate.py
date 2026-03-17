import matplotlib.pyplot as plt

heart_rates = [72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64]

num_patients = len(heart_rates)
mean_heart_rate = sum(heart_rates) / len(heart_rates)

print(f"\nThere are {num_patients} patients in the dataset and the mean heart rate is {mean_heart_rate:.2f} bpm.")

low_count = 0
normal_count = 0
high_count = 0

for rate in heart_rates:
    if rate < 60:
        low_count += 1
    elif rate <= 120:
        normal_count += 1
    else:
        high_count += 1

print(f"Low heart rate patients: {low_count}")
print(f"Normal heart rate patients: {normal_count}")
print(f"High heart rate patients: {high_count}")

categories = {
    "Low": low_count,
    "Normal": normal_count,
    "High": high_count
}

largest_category = max(categories, key=categories.get)
print(f"The largest category is {largest_category}.")

labels = ["Low", "Normal", "High"]
sizes = [low_count, normal_count, high_count]

plt.figure()
plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.title("Distribution of Heart Rate Categories")
plt.show()