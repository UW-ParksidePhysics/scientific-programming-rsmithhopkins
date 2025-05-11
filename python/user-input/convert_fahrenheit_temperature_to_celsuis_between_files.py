def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def read_temperatures(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    temperatures = []
    for line in lines[2:]:  # Skip the first two lines
        temp = float(line.split()[2])
        temperatures.append(temp)
    return temperatures

def write_converted_temperatures(input_file, output_file):
    fahrenheit_temps = read_temperatures(input_file)
    with open(output_file, 'w') as file:
        file.write("Fahrenheit\tCelsius\n")
        for f in fahrenheit_temps:
            c = fahrenheit_to_celsius(f)
            file.write(f"{f:.2f}\t{c:.2f}\n")

if __name__ == '__main__':
    input_file = 'temperature_data.txt'
    output_file = 'converted_temperatures.txt'
    write_converted_temperatures(input_file, output_file)
    print(f"Converted temperatures have been written to {output_file}.")
