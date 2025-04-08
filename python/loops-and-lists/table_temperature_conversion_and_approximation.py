# Print the table header
print(f"{'°F':>3} {'°C':>6} {'Approx °C':>10}")

# Initialize the Fahrenheit value
fahrenheit = 0

# Use a while loop to generate the table
while fahrenheit <= 100:
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    celsius_approx = round(celsius)
    print(f"{fahrenheit:>3} {celsius:>6.1f} {celsius_approx:>10}")
    fahrenheit += 10

    # In Copilot, Write a Python program that prints out a table with Fahrenheit degrees 0, 10, 20, …, 100 in the first column and the corresponding Celsius degrees in the second column using a while loop. Be sure to label the columns as °F and °C.
    # can you rewrite the code without def
    #Modify the program from the previous program so that it prints three columns: F,C, and approximate the value c
