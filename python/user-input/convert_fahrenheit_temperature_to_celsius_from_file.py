def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

if __name__ == '__main__':
    with open('temperature_data.txt', 'r') as file:
        lines = file.readlines()

    # Extracting the Fahrenheit temperature from the third line
    fahrenheit_line = lines[2]
    fahrenheit = float(fahrenheit_line.split()[2])

    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
