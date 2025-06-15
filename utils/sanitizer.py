# File: utils/sanitizer.py
import re

def sanitize_expression(expr: str) -> str:
    expr = expr.replace("^", "**")
    expr = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', expr)  # 5x → 5*x
    expr = re.sub(r'([a-zA-Z])(\d)', r'\1*\2', expr)  # x5 → x*5 (if any)
    return expr

def clean_query(text: str) -> str:
    """
    Removes common LLM-style prefixes like 'factor', 'please factor', etc.
    to isolate the pure mathematical expression.
    """
    text = text.lower().strip()
    trigger_phrases = ["factor", "can you factor", "please factor", "find the factors of"]
    for phrase in trigger_phrases:
        if text.startswith(phrase):
            return text.replace(phrase, "").strip()
    return text

