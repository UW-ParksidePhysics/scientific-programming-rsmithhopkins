# Define the densities in g/cm^3
densities = {
    "iron": 7.87,
    "air": 0.0012,
    "gasoline": 0.755,
    "ice": 0.91,
    "human body": 0.86,
    "silver": 10.50,
    "platinum": 21.45
}

# Volume in cm^3 (1 liter = 1000 cm^3)
volume_cm3 = 1000

# Calculate and print the mass for each substance
for substance, density in densities.items():
    mass = density * volume_cm3
    print(f"The mass of one liter of {substance} is {mass} grams.")

# I used copilot for help