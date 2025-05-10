import numpy as np

def calculate_quadratic_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant >= 0:
        root1 = (-b + np.sqrt(discriminant)) / (2*a)
        root2 = (-b - np.sqrt(discriminant)) / (2*a)
        return root1, root2 if discriminant > 0 else (root1,)
    else:
        real_part = -b / (2*a)
        imaginary_part = np.sqrt(-discriminant) / (2*a)
        return complex(real_part, imaginary_part), complex(real_part, -imaginary_part)

def test_single_root():
    result = calculate_quadratic_roots(1, 2, 1)
    print(f"x^2 + 2x + 1 = 0: x = -1     ; calculate_quadratic_roots(1,  2,  1) = {result}")

def test_roots_float():
    result = calculate_quadratic_roots(1, -2, -3)
    print(f"x^2 - 2x - 3 = 0: x = 3, -1.; calculate_quadratic_roots(1, -2, -3) = {result}")

def test_roots_complex():
    result = calculate_quadratic_roots(1, 0, 1)
    print(f"x^2 + 0x + 1 = 0: x = i, -i ; calculate_quadratic_roots(1,  0,  1) = {result}")

if __name__ == "__main__":
    test_single_root()
    test_roots_float()
    test_roots_complex()


