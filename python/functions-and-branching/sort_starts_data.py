nearby_star_data = [
    ("Sol", 0.0000158, -26.72, 1),
    ("Alpha Centauri", 4.4, -0.01, 1.519),
    ("Barnard's Star", 6.0, 9.54e-29, 0.0004),
    ("Wolf 359", 7.7, 16, 0.0017),
    ("BD +36 degrees2147", 8.2, 9.81e-15, 0.0035),
    ("Luyten 726-8A", 8.4, 10.33e-16, 0.0033),
    ("Sirius A", 8.6, -1.46, 23),
]

def sort_by_parameter(data, parameter_index):
    return sorted(data, key=lambda star: star[parameter_index])

def print_sorted_data(data, parameter_name):
    print(f"Sorted by {parameter_name}:")
    for star in data:
        print(star)
    print()

if __name__ == "__main__":
    sorted_by_name = sort_by_parameter(nearby_star_data, 0)
    print_sorted_data(sorted_by_name, "name")

    sorted_by_distance = sort_by_parameter(nearby_star_data, 1)
    print_sorted_data(sorted_by_distance, "distance from the sun")

    sorted_by_brightness = sort_by_parameter(nearby_star_data, 2)
    print_sorted_data(sorted_by_brightness, "apparent brightness")

    sorted_by_luminosity = sort_by_parameter(nearby_star_data, 3)
    print_sorted_data(sorted_by_luminosity, "luminosity")
