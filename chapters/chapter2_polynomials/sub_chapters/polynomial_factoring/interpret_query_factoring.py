# File: chapters/chapter2_polynomials/sub_chapters/polynomial_factoring/interpret_query_factoring.py

import re
from utils.sanitizer import sanitize_expression

def interpret_query(query: str) -> str:
    """
    Extracts and sanitizes the polynomial expression from the user query.
    Example: 'Factor x^2 - 15x + 60' → 'x**2 - 15*x + 60'
    """
    # Use regex to capture expression after 'factor' or 'factor the polynomial'
    match = re.search(r'factor(?: the)?(?: polynomial)?\s+([-\d\w\s\^\+\*/xX]+)', query, re.IGNORECASE)
    if match:
        raw_expr = match.group(1).strip()
        return sanitize_expression(raw_expr)

    raise ValueError("Could not extract a valid polynomial expression from the query.")
