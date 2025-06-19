import re

def sanitize_expression(query: str) -> str:
    """
    Clean and normalize user query for consistent parsing.
    """
    query = query.lower().strip()

    # Remove trailing punctuation
    query = re.sub(r'[?\.!]+$', '', query)

    # Normalize spacing around parentheses
    query = re.sub(r'\s*,\s*', ',', query)
    query = re.sub(r'\(\s*', '(', query)
    query = re.sub(r'\s*\)', ')', query)

    # Handle cases where center is given: add 'center' tag if needed
    # e.g., from "...circle of radius 3 and center at (1,1)" to "...radius 3 center (1,1)"
    query = re.sub(r'circle of radius (\d+\.?\d*) and center at \(([^)]+)\)',
                   r'radius \1 center (\2)', query)

    # Normalize phrases like "length of the tangent from point"
    query = query.replace("length of the tangent", "tangent length")
    query = query.replace("from point", "from point")

    return query
