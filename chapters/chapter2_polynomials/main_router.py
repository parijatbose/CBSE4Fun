import os
import json
from utils.sanitizer import sanitize_expression
from chapters.chapter2_polynomials.sub_chapters.polynomial_factoring.solver_factoring import factor_polynomial
from chapters.chapter2_polynomials.interpret_query_polynomial import interpret_query_polynomial

def load_logic_template(intent: str):
    path = os.path.join(os.path.dirname(__file__), 'logic_templates', f'{intent}.json')
    if os.path.exists(path):
        with open(path, 'r') as f:
            return json.load(f)
    return None

def route_query(query: str) -> str:
    query = query.strip()
    query_lower = query.lower()
    
    # First, try LLM interpretation if available
    try:
        llm_result = interpret_query_polynomial(query)
        if llm_result.get("intent") == "factor_polynomial" and llm_result.get("expression"):
            expr = sanitize_expression(llm_result["expression"])
            return factor_polynomial(expr)
    except Exception as e:
        # If LLM fails, continue with rule-based approach
        pass
    
    # Rule-based approach
    if any(kw in query_lower for kw in ["factor", "factorise", "expand"]):
        # Extract expression more flexibly
        import re
        # Look for polynomial patterns
        pattern = r'[x\d\s\+\-\*\^]+'
        matches = re.findall(pattern, query)
        if matches:
            # Take the longest match (likely the expression)
            expr = max(matches, key=len)
            expr = sanitize_expression(expr)
            return factor_polynomial(expr)
    
    # Direct polynomial check (already sanitized)
    expr = sanitize_expression(query)
    try:
        # Check if it's a valid polynomial expression
        if "x" in expr and any(op in expr for op in ["+", "-", "*", "**"]):
            return factor_polynomial(expr)
    except Exception:
        pass

    # No match found → fallback to logic_template examples
    fallback = load_logic_template("factor_polynomial")
    if fallback:
        examples = fallback.get("examples", [])
        response_template = fallback.get("response_template", "")
        message = "**⚠️ Could not understand the query. Try these examples:**\n"
        for e in examples:
            message += f"- {e}\n"
        if response_template:
            message += f"\n**📘 Note:** {response_template}"
        return message
    else:
        return "❌ Unrecognized polynomial query."