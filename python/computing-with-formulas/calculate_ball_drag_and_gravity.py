import math

# Constants
drag_coefficient = 0.2  # dimensionless
air_density = 1.2  # kg/m^3
ball_radius = 0.11  # meters (11 cm)
ball_mass = 0.43  # kg
gravitational_acceleration = 9.81  # m/s^2

# Cross-sectional area of the ball
cross_area = math.pi * ball_radius**2  # m^2

# Function to calculate drag force
def calculate_drag_force(velocity):
    return 0.5 * drag_coefficient * air_density * cross_area * velocity**2

# Function to calculate gravitational force
def calculate_gravitational_force(mass):
    return mass * gravitational_acceleration

# Velocities in m/s (converted from km/h)
hard_kick_velocity = 120 * (1000 / 3600)  # m/s
soft_kick_velocity = 10 * (1000 / 3600)  # m/s

# Calculate forces for hard kick
hard_kick_drag_force = calculate_drag_force(hard_kick_velocity)
hard_kick_gravitational_force = calculate_gravitational_force(ball_mass)

# Calculate forces for soft kick
soft_kick_drag_force = calculate_drag_force(soft_kick_velocity)
soft_kick_gravitational_force = calculate_gravitational_force(ball_mass)

# Print results for hard kick
print(f"Hard kick (v = 120 km/h):")
print(f"Drag force: {hard_kick_drag_force:.1f} N")
print(f"Gravitational force: {hard_kick_gravitational_force:.1f} N")
print(f"Ratio of drag force to gravitational force: {hard_kick_drag_force / hard_kick_gravitational_force:.2f}")

# Print results for soft kick
print(f"\nSoft kick (v = 10 km/h):")
print(f"Drag force: {soft_kick_drag_force:.1f} N")
print(f"Gravitational force: {soft_kick_gravitational_force:.1f} N")
print(f"Ratio of drag force to gravitational force: {soft_kick_drag_force / soft_kick_gravitational_force:.2f}")

#Used copilot a lot for help on this one
