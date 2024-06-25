import statistics  # Import the statistics module to use built-in functions for calculations

# List of newly infected patients per day during the first 20 days
infection_rates = [174, 335, 278, 214, 422, 513, 737, 672, 489, 412, 1301,
                   1105, 1123, 1376, 1502, 894, 665, 1704, 1656, 1342]

# Find the smallest number in the list
minimum = min(infection_rates)
# Find the largest number in the list
maximum = max(infection_rates)
# Calculate the range by subtracting the minimum from the maximum
range_infections = maximum - minimum
# Calculate the average (mean) of the list
mean = statistics.mean(infection_rates)
# Find the middle value (median) of the list
median = statistics.median(infection_rates)
# Calculate how spread out the numbers are (variance)
variance = statistics.variance(infection_rates)
# Calculate the spread of numbers around the mean (standard deviation)
std_deviation = statistics.stdev(infection_rates)

# Display all the calculated statistics
print(f"Minimum infection rate: {minimum}")
print(f"Maximum infection rate: {maximum}")
print(f"Range of infection rates: {range_infections}")
print(f"Mean infection rate: {mean:.2f}")
print(f"Median infection rate: {median}")
print(f"Variance of infection rates: {variance:.2f}")
print(f"Standard deviation of infection rates: {std_deviation:.2f}")

""" 
    Otuput od the program is:
    
Minimum infection rate: 174
Maximum infection rate: 1704
Range of infection rates: 1530
Mean infection rate: 845.70
Median infection rate: 704.5
Variance of infection rates: 253620.75
Standard deviation of infection rates: 503.61

"""