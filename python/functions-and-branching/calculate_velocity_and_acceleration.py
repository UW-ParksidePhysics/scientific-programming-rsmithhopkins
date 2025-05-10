def calculate_velocity_and_acceleration(positions, index, time_step=0.6):
    velocity = (positions[index + 1] - positions[index - 1]) / (2 * time_step)
    acceleration = 2 * ((positions[index + 1] - positions[index]) / time_step - (positions[index] - positions[index - 1]) / time_step) / (time_step ** 2)
    return velocity, acceleration

def test_kinematics():
    positions = [0, 0.6, 1.2, 1.8, 2.4, 3.0, 3.6, 4.2, 4.8, 5.4, 6.0]  # Examples of positions
    time_step = 0.6
    for i in range(1, len(positions) - 1):
        velocity, acceleration = calculate_velocity_and_acceleration(positions, i, time_step)
        print(f"t = {i * time_step:.1f}s: velocity = {velocity:.2f}, acceleration = {acceleration:.2f}")

if __name__ == "__main__":
    test_kinematics()
