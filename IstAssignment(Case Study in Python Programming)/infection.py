import statistics
import matplotlib.pyplot as plt

# List of newly infected patients per day
infection_rates = [174, 335, 278, 214, 422, 513, 737, 672, 489, 412, 1301, 1105, 1123, 1376, 1502, 894, 665, 1704, 1656, 1342]

# Calculate statistics
min_infections = min(infection_rates)
max_infections = max(infection_rates)
range_infections = max_infections - min_infections
mean_infections = statistics.mean(infection_rates)
median_infections = statistics.median(infection_rates)
variance_infections = statistics.variance(infection_rates)
std_dev_infections = statistics.stdev(infection_rates)

# Print statistics
print("COVID-19 Infection Statistics:")
print(f"Minimum infections per day: {min_infections}")
print(f"Maximum infections per day: {max_infections}")
print(f"Range of infections per day: {range_infections}")
print(f"Mean infections per day: {mean_infections:.2f}")
print(f"Median infections per day: {median_infections}")
print(f"Variance of infections per day: {variance_infections:.2f}")
print(f"Standard deviation of infections per day: {std_dev_infections:.2f}")

# Plot the infection rates over time
plt.plot(infection_rates)
plt.xlabel("Day")
plt.ylabel("Newly Infected Patients")
plt.title("COVID-19 Infection Rates Over Time")
plt.show()

# Calculate the daily change in infection rates
daily_changes = [infection_rates[i] - infection_rates[i-1] for i in range(1, len(infection_rates))]

# Plot the daily changes in infection rates
plt.plot(daily_changes)
plt.xlabel("Day")
plt.ylabel("Daily Change in Infections")
plt.title("Daily Change in COVID-19 Infection Rates")
plt.show()