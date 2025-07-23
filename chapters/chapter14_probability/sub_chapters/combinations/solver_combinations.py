# File: chapters/chapter14_probability/sub_chapters/combinations/solver_combinations.py

from math import comb, perm, factorial
from fractions import Fraction

def solve_combinations(params):
    """
    Smart router for all combination-related probability types:
    - Basic C(n, r)
    - Probability using combinations
    - Permutation-based probability
    - Birthday paradox
    """
    if "n" in params and "r" in params:
        return solve_basic_combination(params)
    if {"total_items", "desired_items", "selected_total", "selected_desired"}.issubset(params):
        return solve_combination_probability(params)
    if "total_items" in params and "selected_items" in params:
        return solve_permutation_probability(params)
    if "people" in params:
        return solve_birthday_paradox(params)
    return "❌ Unrecognized combination-related input."

def solve_basic_combination(params):
    n = params.get("n")
    r = params.get("r")
    if r > n or n < 0 or r < 0:
        return "❌ Invalid values. Ensure 0 ≤ r ≤ n."
    result = comb(n, r)
    return f"""
✅ **Combinations C(n, r)**

• n = {n}, r = {r}  
• Formula: C(n, r) = n! / [r!(n - r)!]  
• C({n}, {r}) = {result}

💡 **Answer:** {result} ways
"""

def solve_combination_probability(params):
    total = params.get("total_items")
    desired = params.get("desired_items")
    selected_total = params.get("selected_total")
    selected_desired = params.get("selected_desired")

    undesired = total - desired
    selected_undesired = selected_total - selected_desired

    numerator = comb(desired, selected_desired) * comb(undesired, selected_undesired)
    denominator = comb(total, selected_total)
    prob = Fraction(numerator, denominator)

    return f"""
✅ **Combination Probability**

• C({desired},{selected_desired}) × C({undesired},{selected_undesired}) = {numerator}  
• Total combinations = C({total},{selected_total}) = {denominator}  
• Probability = {numerator}/{denominator} = {prob} ≈ {float(prob):.3f}

💡 **Answer:** {prob} or {float(prob):.1%}
"""

def solve_permutation_probability(params):
    total = params.get("total_items")
    selected = params.get("selected_items")
    total_perms = perm(total, selected)
    all_possible = factorial(total)
    prob = Fraction(total_perms, all_possible)

    return f"""
✅ **Permutation Probability**

• P({total},{selected}) = {total_perms}  
• Total arrangements = {all_possible}  
• Probability = {total_perms}/{all_possible} = {prob} ≈ {float(prob):.3f}

💡 **Answer:** {prob} or {float(prob):.1%}
"""

def solve_birthday_paradox(params=None):
    n = params.get("people")
    if not n or n < 2:
        return "❌ Number of people must be ≥ 2."

    days = 365
    prob_unique = 1.0
    for i in range(n):
        prob_unique *= (days - i) / days

    prob_shared = 1 - prob_unique

    return f"""
🎂 **Birthday Paradox**

• People = {n}  
• Probability no shared birthday ≈ {prob_unique:.3f}  
• Probability at least one shared birthday ≈ {prob_shared:.3f}

💡 **Answer:** There is a **{prob_shared:.1%}** chance at least two people share a birthday.
"""
