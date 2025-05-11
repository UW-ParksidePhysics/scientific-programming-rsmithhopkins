import sys

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <temperature_in_fahrenheit>")
    else:
        try:
            fahrenheit = float(sys.argv[1])
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
        except ValueError:
            print("Please enter a valid number for the temperature.")
