import sys

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

if __name__ == '__main__':
    try:
        fahrenheit = float(sys.argv[1])
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
    except IndexError:
        print("Error: Missing temperature argument. Usage: python script.py <temperature_in_fahrenheit>")
    except ValueError:
        print("Error: Invalid temperature value. Please enter a valid number.")
