import numpy as np

def sinusoidal_sum(time, number_of_functions, period):
    sum_value = 0.5
    for k in range(1, number_of_functions + 1):
        sum_value += np.sin((2 * k - 1) * np.pi * time / period) / ((2 * k - 1) * np.pi)
    return sum_value

def piecewise_function(time, period):
    if 0 < time < period / 2:
        return 0
    elif period / 2 <= time < period:
        return 1
    else:
        return None  # Handle edge cases if needed

def compare_functions(period, times, alphas, n_values):
    print("t\talpha\tn\tS(t;n)\tf(t)")
    print("-----------------------------------")
    for t in times:
        for alpha in alphas:
            for n in n_values:
                S_t_n = sinusoidal_sum(t, n, period)
                f_t = piecewise_function(t, period)
                print(f"{t:.2f}\t{alpha:.2f}\t{n}\t{S_t_n:.2f}\t{f_t}")

if __name__ == "__main__":
    period = 2 * np.pi
    times = [period / 4, period / 3, period / 10]
    alphas = [0.01, 0.25, 0.49]
    n_values = [3, 5, 10, 30, 100]

    compare_functions(period, times, alphas, n_values)
