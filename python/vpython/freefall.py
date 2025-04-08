"""
This module calculates quantinties for one dimensional freefall motion
"""

import numpy as np


def velocity_in_time(time, initial_velocity=0, gravitiational_acceleration=9.8):
    return initial_velocity - gravitiational_acceleration * time


def height_in_time(time, initial_height=0, initial_velocity=0, gravitational_acceleration=9.8):
    return initial_height + initial_velocity * time - 0.5 * gravitaional_acceleration * time**2

def velocity_in_height(height, initial_velocity=0, initial_velocity=0, gravitiational_acceleration=9.8):
    height_change = height - initial_height
    return np.sign(initial_velocity) * np. sqrt(initial_velocity**2 - 2 *gravitaional_acceleration * (height_change))