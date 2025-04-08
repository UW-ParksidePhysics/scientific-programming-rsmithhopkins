# Print the table header
print(f"{'°F':>3} {'°C':>6}")

# Initialize the Fahrenheit value
fahrenheit = 0

# Use a while loop to generate the table
while fahrenheit <= 100:
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    print(f"{fahrenheit:>3} {celsius:>6.1f}")
    fahrenheit += 10