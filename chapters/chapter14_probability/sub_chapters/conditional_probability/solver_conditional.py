# File: chapters/chapter14_probability/sub_chapters/conditional_probability/solver_conditional.py

from fractions import Fraction

def solve_conditional_probability(params):
    """
    Dispatcher for conditional probability, Bayes theorem, and independence test.
    """
    # Bayes Theorem
    if all(k in params for k in ["p_b_given_a", "p_a", "p_b"]):
        return apply_bayes_theorem(params)

    # Independence check
    if all(k in params for k in ["p_a", "p_b", "p_a_and_b"]):
        return test_independence(
            p_a=params.get("p_a"),
            p_b=params.get("p_b"),
            p_a_and_b=params.get("p_a_and_b")
        )

    # Contextual examples
    if params.get("type") == "card_conditional":
        return solve_card_conditional(params)
    if params.get("type") == "dice_conditional":
        return solve_dice_conditional(params)

    # Default: P(A|B) = P(A ∩ B) / P(B)
    if "p_a_and_b" in params and "p_b" in params:
        return _basic_conditional(params)

    return "❌ Insufficient information to solve conditional probability."

def _basic_conditional(params):
    p_a_and_b = params.get("p_a_and_b")
    p_b = params.get("p_b")
    if p_b == 0:
        return "❌ Division by zero."
    result = p_a_and_b / p_b
    return f"""
✅ **Conditional Probability**

• P(A ∩ B) = {p_a_and_b}  
• P(B) = {p_b}  
• P(A|B) = {p_a_and_b}/{p_b} = {result:.3f}

💡 **Answer:** {Fraction(p_a_and_b, p_b)} or {result:.1%}
"""

def apply_bayes_theorem(params):
    p_b_given_a = params.get("p_b_given_a")
    p_a = params.get("p_a")
    p_b = params.get("p_b")
    if p_b == 0:
        return "❌ Division by zero."
    result = (p_b_given_a * p_a) / p_b
    return f"""
📘 **Bayes' Theorem**

• P(B|A) = {p_b_given_a}, P(A) = {p_a}, P(B) = {p_b}  
• P(A|B) = ({p_b_given_a} × {p_a}) / {p_b} = {result:.3f}

💡 **Answer:** {result:.3f} or {result:.1%}
"""

def test_independence(p_a, p_b, p_a_and_b):
    expected = p_a * p_b
    is_independent = abs(expected - p_a_and_b) < 1e-6
    return f"""
🔍 **Independence Check**

• P(A) = {p_a}, P(B) = {p_b}, P(A ∩ B) = {p_a_and_b}  
• Expected P(A)×P(B) = {expected:.3f}  
• Independent? {'✅ Yes' if is_independent else '❌ No'}

💡 **Conclusion:** {'Independent' if is_independent else 'Not Independent'}
"""

def solve_card_conditional(params):
    red_faces = 6
    total_faces = 12
    probability = red_faces / total_faces
    return f"""
🃏 **Card Conditional Probability**

• P(Red | Face) = 6/12 = {probability:.2f}

💡 **Answer:** 1/2 or 50%
"""

def solve_dice_conditional(params):
    even = {2, 4, 6}
    gt3 = {4, 5, 6}
    intersection = even & gt3
    p = len(intersection) / len(even)
    return f"""
🎲 **Dice Conditional Probability**

• P(>3 | Even) = {len(intersection)}/{len(even)} = {p:.2f}

💡 **Answer:** {Fraction(len(intersection), len(even))} or {p:.1%}
"""
