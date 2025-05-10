def convert_fahrenheit_temperature_to_celsius(fahrenheit_temperature):
    return (5/9) * (fahrenheit_temperature - 32)

def convert_celsius_temperature_to_fahrenheit(celsius_temperature):
    return (9/5) * celsius_temperature + 32

def test_temperature_conversion():
    test_temperatures_celsius = [0, 21, 100]  # Freezing point, room temperature, boiling point
    print("Celsius | Fahrenheit | Converted Back to Celsius")
    print("---------------------------------------------")
    for temp_c in test_temperatures_celsius:
        temp_f = convert_celsius_temperature_to_fahrenheit(temp_c)
        converted_back_c = convert_fahrenheit_temperature_to_celsius(temp_f)
        print(f"{temp_c:7} | {temp_f:11.2f} | {converted_back_c:23.2f}")

if __name__ == "__main__":
    test_temperature_conversion()



