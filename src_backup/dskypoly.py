#!/usr/bin/env python3

import sys
import cmath
import re
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore", message=".*QSocketNotifier.*")

def parse_coeffs(args):
    if len(args) != 3:
        print("Usage: dskypoly.py a b c")
        sys.exit(1)
    try:
        return map(float, args)
    except ValueError:
        print("Coefficients must be numbers.")
        sys.exit(1)

def parse_symbolic(expr):
    expr = expr.replace("−", "-").replace(" ", "")
    pattern = r'([+-]?\d*\.?\d*)x²([+-]?\d*\.?\d*)x([+-]?\d*\.?\d*)'
    match = re.match(pattern, expr)
    if not match:
        print("Invalid symbolic input. Use format like: x² - 3x + 2")
        sys.exit(1)
    a, b, c = match.groups()
    def clean(x): return float(x) if x not in ("", "+", "-") else float(x + "1")
    return clean(a), clean(b), float(c)

def solve_quadratic(a, b, c):
    Δ = b**2 - 4*a*c
    root1 = (-b + cmath.sqrt(Δ)) / (2*a)
    root2 = (-b - cmath.sqrt(Δ)) / (2*a)
    return Δ, root1, root2

def format_factorization(a, r1, r2, Δ):
    if Δ == 0:
        return f"Factorization over ℝ: ({a})(x - {r1.real})²"
    elif Δ > 0:
        return f"Factorization over ℝ: ({a})(x - {r1.real})(x - {r2.real})"
    else:
        real = round(r1.real, 5)
        imag = round(abs(r1.imag), 5)
        return (
            f"Factorization over ℝ: ({a})(x² - {2 * real}x + {real**2 + imag**2})\n"
            f"Factorization over ℂ: ({a})(x - ({r1}))(x - ({r2}))"
        )

def plot_roots(r1, r2):
    plt.axhline(0, color='gray', lw=0.5)
    plt.axvline(0, color='gray', lw=0.5)
    plt.plot([r1.real, r2.real], [r1.imag, r2.imag], 'ro')
    plt.title("Roots on the Complex Plane")
    plt.xlabel("Re")
    plt.ylabel("Im")
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

def main():
    if len(sys.argv) == 2:
        a, b, c = parse_symbolic(sys.argv[1])
    else:
        a, b, c = parse_coeffs(sys.argv[1:])

    Δ, r1, r2 = solve_quadratic(a, b, c)

    print(f"Input: {a}x² + {b}x + {c}")
    print(f"Discriminant (Δ): {Δ}")
    print(f"Roots: {r1}, {r2}")
    print(format_factorization(a, r1, r2, Δ))

    plot_roots(r1, r2)

if __name__ == "__main__":
    main()
	

