# File: chapters/chapter2_polynomials/sub_chapters/polynomial_factoring/test_polynomial_factoring.py

import sys
import os

# Automatically add the project root ('cbse_math_solver') to sys.path
CURRENT_FILE = os.path.abspath(__file__)
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_FILE, "../../../../.."))
sys.path.insert(0, PROJECT_ROOT)

from chapters.chapter2_polynomials.sub_chapters.polynomial_factoring.query_router_factoring import route_factoring

def run_tests():
    test_queries = [
        "Factor the polynomial 2x^2 + 3x + 1",
        "Factor 3x^2 + 5x + 2",
        "Factor x^2 - 4x + 4",
        "Factor x^2 + 1",
        "Factor x^3 + x^2 + x + 1"
    ]

    for query in test_queries:
        print(f"\nQuery: {query}")
        print("Result:", route_factoring(query))

if __name__ == "__main__":
    run_tests()
