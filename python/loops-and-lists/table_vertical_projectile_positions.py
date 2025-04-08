# Constants for the first table
v1 = 12  # m/s
g1 = 25.93  # m/s^2

# Constants for the second table
v2 = 12  # m/s
g2 = 3.728  # m/s^2

# Calculate the upper limit of t for both tables
t_max1 = 2 * v1 / g1
t_max2 = 2 * v2 / g2

# Number of intervals
n = 20

# Calculate the interval length for both tables
h1 = t_max1 / n
h2 = t_max2 / n

# Function to calculate y(t)
def y(t, v, g):
    return v * t - 0.5 * g * t**2

# Generate table using for loop
print("Using for loop:")
print(f"{'t':>10} {'y(t) (g=25.93)':>20} {'t':>10} {'y(t) (g=3.728)':>20}")
for i in range(n + 1):
    t1 = i * h1
    t2 = i * h2
    print(f"{t1:>10.3f} {y(t1, v1, g1):>20.3f} {t2:>10.3f} {y(t2, v2, g2):>20.3f}")

# Generate table using while loop
print("\nUsing while loop:")
print(f"{'t':>10} {'y(t) (g=25.93)':>20} {'t':>10} {'y(t) (g=3.728)':>20}")
t1 = 0
t2 = 0
while t1 <= t_max1 or t2 <= t_max2:
    if t1 <= t_max1:
        y_t1 = y(t1, v1, g1)
    else:
        y_t1 = ""
    if t2 <= t_max2:
        y_t2 = y(t2, v2, g2)
    else:
        y_t2 = ""
    print(f"{t1:>10.3f} {y_t1:>20} {t2:>10.3f} {y_t2:>20}")
    t1 += h1
    t2 += h2

# Ensure the last point (t=2v/g, y=0) is included for both tables
if t1 - h1 < t_max1:
    print(f"{t_max1:>10.3f} {y(t_max1, v1, g1):>20.3f}")
if t2 - h2 < t_max2:
    print(f"{t_max2:>10.3f} {y(t_max2, v2, g2):>20.3f}")

# Jupiter is g=25.95 and Mars is 3.728