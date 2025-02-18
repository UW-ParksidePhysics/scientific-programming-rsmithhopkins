# Conversion factors
km_to_cm = 100000  # 1 km = 100000 cm
cm_to_inch = 1 / 2.54  # 1 inch = 2.54 cm
inch_to_foot = 1 / 12  # 1 foot = 12 inches
foot_to_yard = 1 / 3  # 1 yard = 3 feet
yard_to_mile = 1 / 1760  # 1 mile = 1760 yards

def convert_km_to_imperial(km):
    cm = km * km_to_cm
    inches = cm * cm_to_inch
    feet = inches * inch_to_foot
    yards = feet * foot_to_yard
    miles = yards * yard_to_mile
    return inches, feet, yards, miles

# Define the lengths in kilometers
length_km_1 = 10.1389
length_km_2 = 0.640

# Convert the lengths to imperial units
inches_1, feet_1, yards_1, miles_1 = convert_km_to_imperial(length_km_1)
inches_2, feet_2, yards_2, miles_2 = convert_km_to_imperial(length_km_2)

# Print the results
print(f"{length_km_1} kilometers is equivalent to {inches_1:.2f} inches, {feet_1:.2f} feet, {yards_1:.2f} yards, or {miles_1:.4f} miles.")
print(f"{length_km_2} kilometers is equivalent to {inches_2:.2f} inches, {feet_2:.2f} feet, {yards_2:.2f} yards, or {miles_2:.4f} miles.")

# Verification for length of 0.640 kilometers
print(f"Verification: {length_km_2} kilometers corresponds to {inches_2:.2f} inches, {feet_2:.2f} feet, {yards_2:.2f} yards, or {miles_2:.4f} miles.")

# I used copilot for help
