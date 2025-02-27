# Function to generate n+1 equally spaced x coordinates in the interval [a,b]
def generate_coordinates(a, b, n):
    h = (b - a) / n
    coordinates = []
    for i in range(n + 1):
        x = a + i * h
        coordinates.append(x)
    return coordinates

# Function to generate n+1 equally spaced x coordinates using list comprehension
def generate_coordinates_comprehension(a, b, n):
    h = (b - a) / n
    return [a + i * h for i in range(n + 1)]

# Interval [a, b] and number of intervals n
a = 1
b = 2
n = 20

# Generate coordinates using for loop
coordinates_loop = generate_coordinates(a, b, n)

# Generate coordinates using list comprehension
coordinates_comprehension = generate_coordinates_comprehension(a, b, n)

# Print the results
print(f"For x in [{a}, {b}] with {n} intervals, the interval length is h = {(b - a) / n:.3f}, and")
print("Using a for loop:")
print(f"x = {coordinates_loop}")
print("Using list comprehension:")
print(f"x = {coordinates_comprehension}")