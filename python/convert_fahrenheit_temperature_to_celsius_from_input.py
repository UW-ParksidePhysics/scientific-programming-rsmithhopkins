print(f"{'°F':>3} {'°C':>6}")
    fahrenheit = 0

    while fahrenheit <= 100:
        celsius = (fahrenheit - 32) * 5.0 / 9.0
        print(f"{fahrenheit:>3} {celsius:>6.1f}")
        fahrenheit += 10
if __