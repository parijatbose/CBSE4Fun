from .interpret_query_factoring import interpret_query
from .solver_factoring import factor_polynomial

def route_factoring(query: str) -> str:
    try:
        expr = interpret_query(query)
        return factor_polynomial(expr)
    except Exception as e:
        return f"Error processing polynomial: {str(e)}"
