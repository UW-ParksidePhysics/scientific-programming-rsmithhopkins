# Define the maximum integer
maximum_integer = 10

# Compute the sum using a for loop
sum_for_loop = 0
for i in range(1, maximum_integer + 1):
    sum_for_loop += i

# Compute the sum using the formula
sum_formula = maximum_integer * (maximum_integer + 1) // 2

# Print the results
print(f"n = {maximum_integer}")
print(f"sum(1, n) = {sum_for_loop}")
print(f"n(n+1)/2 = {sum_formula}")