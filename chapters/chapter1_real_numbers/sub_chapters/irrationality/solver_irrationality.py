# File: chapters/chapter1_real_numbers/sub_chapters/irrationality/solver_irrationality.py

import re
from typing import Dict, Any

def solve_irrationality_proof(params: Dict[str, Any]) -> str:
    """
    Main solver for irrationality proofs.
    """
    try:
        expression = params.get('expression', '')
        if not expression:
            return "❌ Please provide an expression to prove irrationality."
        
        return prove_irrationality_detailed(expression)
        
    except Exception as e:
        return f"❌ Error proving irrationality: {str(e)}"

def prove_irrationality_detailed(value) -> str:
    """
    Prove irrationality of various expressions involving square roots.
    Enhanced version with better formatting and explanations.
    """
    
    # Clean and normalize the input
    query = str(value).lower().replace("root", "√")
    query = re.sub(r"[√\u221a]\s+(\d+)", r"√\1", query)  # remove space between √ and number
    query = re.sub(r"[^√0-9+\-*/^=()./ ]", " ", query)
    query = re.sub(r"\s+", " ", query).strip()
    
    # Remove irrelevant words
    query = re.sub(r"\b(prove|is|irrational|rational|that|the|of|number|an|a|whether|show|check|test|if|then)\b", "", query)
    query = re.sub(r"\s+", " ", query).strip()
    
    # Pattern matching for different types of expressions
    
    # √n ± k patterns
    match_root_n_offset = re.search(r"√(\d+)\s*([\-+])\s*(\d+)", query)
    match_root_offset_alt = re.search(r"(\d+)\s*([\-+])\s*√(\d+)", query)
    
    # a + b√n patterns
    match_a_brootn = re.search(r"(\d+)\s*\+\s*(\d+)\s*√(\d+)", query)
    
    # r√n patterns
    match_r_root_n = re.search(r"(\d+)\s*\*?\s*√(\d+)", query)
    
    # √n only
    match_root_only = re.search(r"[√\u221a](\d+)", query)
    
    # √n ± √m patterns
    match_root_diff = re.search(r"√(\d+)\s*([+-])\s*√(\d+)", query)
    
    # 1/√n patterns
    match_one_by_root = re.search(r"1\s*/\s*√(\d+)", query)
    
    # k ± √n patterns
    match_k_rootn = re.search(r"(\d+)\s*([+-])\s*√(\d+)", query)
    
    # 1/(k ± √n) patterns
    match_one_by_k_rootn = re.search(r"1\s*/\s*\(\s*(\d+)\s*([+-])\s*√(\d+)\s*\)", query)
    
    # Process patterns (most specific first)
    if match_root_n_offset:
        return prove_root_plus_minus_constant(match_root_n_offset)
    elif match_a_brootn:
        return prove_linear_combination(match_a_brootn)
    elif match_r_root_n:
        return prove_coefficient_times_root(match_r_root_n)
    elif match_root_offset_alt:
        return prove_constant_plus_root(match_root_offset_alt)
    elif match_root_diff:
        return prove_root_sum_difference(match_root_diff)
    elif match_one_by_root:
        return prove_reciprocal_root(match_one_by_root)
    elif match_k_rootn:
        return prove_constant_plus_minus_root(match_k_rootn)
    elif match_one_by_k_rootn:
        return prove_reciprocal_linear_combination(match_one_by_k_rootn)
    elif match_root_only:
        return prove_simple_root(match_root_only)
    else:
        return """
❌ **Could not parse the expression.**

💡 **Supported formats:**
• √n (e.g., √2, √3)
• √n ± k (e.g., √2 + 3, √5 - 1)
• k ± √n (e.g., 3 + √2, 5 - √3)
• a + b√n (e.g., 2 + 3√5)
• r√n (e.g., 2√3, 5√7)
• √a ± √b (e.g., √2 + √3)
• 1/√n (e.g., 1/√2)
• 1/(k ± √n) (e.g., 1/(2 + √3))

**Example queries:**
"Prove √2 is irrational"
"Show that 3 + √5 is irrational"
"Prove 2√3 is irrational"
"""

def prove_simple_root(match) -> str:
    """Prove √n is irrational."""
    n = match.group(1)
    n_val = int(n)
    sqrt_n = n_val ** 0.5

    # Check if √n is a perfect square
    if sqrt_n.is_integer():
        return f"""
🔍 **Analysis of √{n}:**

⚠️ **√{n} = {int(sqrt_n)}** is actually a **rational number** because {n} is a perfect square.

✅ **Conclusion:** √{n} is **NOT irrational** - it's rational!

💡 **Remember:** Only square roots of non-perfect squares are irrational.
"""

    return f"""
✅ **Proving that √{n} is irrational using Proof by Contradiction**

📝 **Theorem:** √{n} is an irrational number.

**Proof:**

**Step 1: Assumption**
• Assume, for the sake of contradiction, that √{n} is rational
• Then √{n} = a/b, where a and b are integers with b ≠ 0
• We can assume gcd(a,b) = 1 (a and b are coprime)

**Step 2: Algebraic Manipulation**
• Squaring both sides: (√{n})² = (a/b)²
• This gives us: {n} = a²/b²
• Rearranging: a² = {n} × b²

**Step 3: Divisibility Analysis**
• Since a² = {n} × b², we see that {n} divides a²
• Therefore, {n} must divide a (since {n} is prime or has prime factors)
• Let a = {n}k for some integer k

**Step 4: Substitution**
• Substituting a = {n}k into a² = {n} × b²:
• ({n}k)² = {n} × b²
• {n}²k² = {n} × b²
• {n}k² = b²

**Step 5: Contradiction**
• From {n}k² = b², we see that {n} divides b²
• Therefore, {n} must also divide b
• But this means both a and b are divisible by {n}
• This contradicts our assumption that gcd(a,b) = 1

**Step 6: Conclusion**
• Since our assumption leads to a contradiction, it must be false
• **Therefore, √{n} is irrational** ✅

💡 **Key Insight:** The proof works because {n} is not a perfect square, so its square root cannot be expressed as a simple fraction.
"""

def prove_root_plus_minus_constant(match) -> str:
    """Prove √n ± k is irrational."""
    n = match.group(1)
    sign = match.group(2)
    k = int(match.group(3))
    expr = f"√{n} {sign} {k}"
    opposite = "-" if sign == "+" else "+"
    
    return f"""
✅ **Proving that {expr} is irrational using Proof by Contradiction**

📝 **Theorem:** {expr} is an irrational number.

**Proof:**

**Step 1: Assumption**
• Assume {expr} is rational
• Then {expr} = p/q, where p and q are integers with q ≠ 0

**Step 2: Isolate the Square Root**
• From {expr} = p/q, we get:
• √{n} = p/q {opposite} {k}
• √{n} = (p {opposite} {k}q)/q

**Step 3: Analyze the Result**
• The right side (p {opposite} {k}q)/q is a ratio of integers
• This would mean √{n} is rational

**Step 4: Contradiction**
• But we know that √{n} is irrational (since {n} is not a perfect square)
• This contradicts our conclusion from Step 3

**Step 5: Final Conclusion**
• Since our assumption leads to a contradiction, it must be false
• **Therefore, {expr} is irrational** ✅

💡 **Key Principle:** The sum/difference of a rational and irrational number is always irrational.
"""

def prove_linear_combination(match) -> str:
    """Prove a + b√n is irrational."""
    a = int(match.group(1))
    b = int(match.group(2))
    n = match.group(3)
    expr = f"{a} + {b}√{n}"

    return f"""
✅ **Proving that {expr} is irrational using Proof by Contradiction**

📝 **Theorem:** {expr} is an irrational number.

**Proof:**

**Step 1: Assumption**
• Assume {expr} is rational
• Then {expr} = p/q, where p and q are integers with q ≠ 0, gcd(p,q) = 1

**Step 2: Isolate the Irrational Part**
• From {a} + {b}√{n} = p/q, we get:
• {b}√{n} = p/q - {a}
• {b}√{n} = (p - {a}q)/q

**Step 3: Solve for √{n}**
• Dividing both sides by {b}:
• √{n} = (p - {a}q)/({b}q)

**Step 4: Analyze the Result**
• The right side is a ratio of integers: (p - {a}q) and ({b}q)
• Since p, q, a, and b are all integers, this fraction represents a rational number
• This would mean √{n} is rational

**Step 5: Contradiction**
• But √{n} is irrational (assuming {n} is not a perfect square)
• This contradicts our conclusion from Step 4

**Step 6: Final Conclusion**
• Since our assumption leads to a contradiction, it must be false
• **Therefore, {expr} is irrational** ✅

💡 **General Principle:** If a and b are rational numbers and √n is irrational, then a + b√n is irrational (provided b ≠ 0).
"""

def prove_coefficient_times_root(match) -> str:
    """Prove r√n is irrational."""
    r = int(match.group(1))
    n = match.group(2)
    expr = f"{r}√{n}"
    
    return f"""
✅ **Proving that {expr} is irrational using Proof by Contradiction**

📝 **Theorem:** {expr} is an irrational number.

**Proof:**

**Step 1: Assumption**
• Assume {expr} is rational
• Then {expr} = a/b, where a and b are integers with b ≠ 0

**Step 2: Isolate √{n}**
• From {r}√{n} = a/b, we get:
• √{n} = a/({r}b)

**Step 3: Analyze the Result**
• The right side a/({r}b) is a ratio of integers
• Since a, r, and b are integers, and {r}b ≠ 0, this represents a rational number
• This would mean √{n} is rational

**Step 4: Contradiction**
• But √{n} is irrational (assuming {n} is not a perfect square)
• This contradicts our conclusion from Step 3

**Step 5: Final Conclusion**
• Since our assumption leads to a contradiction, it must be false
• **Therefore, {expr} is irrational** ✅

💡 **Key Insight:** A non-zero rational number times an irrational number is always irrational.
"""

def prove_constant_plus_root(match) -> str:
    """Prove a ± √n is irrational."""
    a = int(match.group(1))
    sign = match.group(2)
    n = match.group(3)
    expr = f"{a} {sign} √{n}"
    opposite_sign = "-" if sign == "+" else "+"
    
    return f"""
✅ **Proving that {expr} is irrational using Proof by Contradiction**

📝 **Theorem:** {expr} is an irrational number.

**Proof:**

**Step 1: Assumption**
• Assume {expr} is rational
• Then {expr} = p/q, where p and q are integers with q ≠ 0

**Step 2: Isolate the Square Root**
• From {a} {sign} √{n} = p/q, we get:
• √{n} = p/q {opposite_sign} {a}
• √{n} = (p {opposite_sign} {a}q)/q

**Step 3: Analyze the Result**
• The right side is a ratio of integers
• This would mean √{n} is rational

**Step 4: Contradiction**
• But √{n} is irrational (since {n} is not a perfect square)
• This contradicts our conclusion from Step 3

**Step 5: Final Conclusion**
• Since our assumption leads to a contradiction, it must be false
• **Therefore, {expr} is irrational** ✅

💡 **Key Principle:** The sum or difference of a rational and irrational number is always irrational.
"""

def prove_root_sum_difference(match) -> str:
    """Prove √a ± √b is irrational."""
    n1 = match.group(1)
    op = match.group(2)
    n2 = match.group(3)
    expr = f"√{n1} {op} √{n2}"
    opposite_op = "-" if op == "+" else "+"

    return f"""
✅ **Proving that {expr} is irrational using Proof by Contradiction**

📝 **Theorem:** {expr} is an irrational number.

**Proof:**

**Step 1: Assumption**
• Assume {expr} is rational
• Then {expr} = p/q, where p and q are integers with q ≠ 0

**Step 2: Isolate One Square Root**
• From √{n1} {op} √{n2} = p/q, we get:
• √{n1} = p/q {opposite_op} √{n2}

**Step 3: Analyze the Components**
• The term p/q is rational (by definition)
• The term √{n2} is irrational (assuming {n2} is not a perfect square)
• The {op.replace('+', 'sum').replace('-', 'difference')} of a rational and irrational number is irrational

**Step 4: Contradiction**
• From Step 2, √{n1} would equal an irrational number
• But if both √{n1} and √{n2} are irrational, their {op.replace('+', 'sum').replace('-', 'difference')} cannot be rational
• This contradicts our assumption from Step 1

**Step 5: Final Conclusion**
• Since our assumption leads to a contradiction, it must be false
• **Therefore, {expr} is irrational** ✅

💡 **General Rule:** The sum or difference of two irrational square roots is typically irrational (with rare exceptions like √8 - √2 = √2).
"""

def prove_reciprocal_root(match) -> str:
    """Prove 1/√n is irrational."""
    n = match.group(1)
    
    return f"""
✅ **Proving that 1/√{n} is irrational using Proof by Contradiction**

📝 **Theorem:** 1/√{n} is an irrational number.

**Proof:**

**Step 1: Assumption**
• Assume 1/√{n} is rational
• Then 1/√{n} = a/b, where a and b are integers with a ≠ 0, b ≠ 0

**Step 2: Take the Reciprocal**
• Taking reciprocals of both sides:
• √{n} = b/a

**Step 3: Analyze the Result**
• The right side b/a is a ratio of integers
• This would mean √{n} is rational

**Step 4: Contradiction**
• But √{n} is irrational (since {n} is not a perfect square)
• This contradicts our conclusion from Step 3

**Step 5: Final Conclusion**
• Since our assumption leads to a contradiction, it must be false
• **Therefore, 1/√{n} is irrational** ✅

💡 **Key Insight:** The reciprocal of an irrational number is also irrational.
"""

def prove_constant_plus_minus_root(match) -> str:
    """Prove k ± √n is irrational."""
    k = int(match.group(1))
    sign = match.group(2)
    n = match.group(3)
    expr = f"{k} {sign} √{n}"
    opposite_sign = "-" if sign == "+" else "+"
    
    return f"""
✅ **Proving that {expr} is irrational using Proof by Contradiction**

📝 **Theorem:** {expr} is an irrational number.

**Proof:**

**Step 1: Assumption**
• Assume {expr} is rational
• Then {expr} = p/q, where p and q are integers with q ≠ 0

**Step 2: Isolate the Square Root**
• From {k} {sign} √{n} = p/q, we get:
• √{n} = p/q {opposite_sign} {k}
• √{n} = (p {opposite_sign} {k}q)/q

**Step 3: Analyze the Result**
• The right side is a ratio of integers
• This would mean √{n} is rational

**Step 4: Contradiction**
• But √{n} is irrational (since {n} is not a perfect square)
• This contradicts our conclusion from Step 3

**Step 5: Final Conclusion**
• Since our assumption leads to a contradiction, it must be false
• **Therefore, {expr} is irrational** ✅
"""

def prove_reciprocal_linear_combination(match) -> str:
    """Prove 1/(k ± √n) is irrational."""
    k = int(match.group(1))
    sign = match.group(2)
    n = match.group(3)
    expr = f"1/({k} {sign} √{n})"
    
    return f"""
✅ **Proving that {expr} is irrational using Proof by Contradiction**

📝 **Theorem:** {expr} is an irrational number.

**Proof:**

**Step 1: Assumption**
• Assume {expr} is rational
• Then {expr} = p/q, where p and q are integers with p ≠ 0, q ≠ 0

**Step 2: Take the Reciprocal**
• Taking reciprocals: {k} {sign} √{n} = q/p

**Step 3: Isolate the Square Root**
• From {k} {sign} √{n} = q/p:
• √{n} = q/p {"-" if sign == "+" else "+"} {k}
• √{n} = (q {"-" if sign == "+" else "+"} {k}p)/p

**Step 4: Analyze the Result**
• The right side is a ratio of integers
• This would mean √{n} is rational

**Step 5: Contradiction**
• But √{n} is irrational (since {n} is not a perfect square)
• This contradicts our conclusion from Step 4

**Step 6: Final Conclusion**
• Since our assumption leads to a contradiction, it must be false
• **Therefore, {expr} is irrational** ✅

💡 **Key Insight:** The reciprocal of an irrational expression is also irrational.
"""

def prove_irrationality_from_query(query: str) -> str:
    """
    Extract expression from query and prove its irrationality.
    """
    return prove_irrationality_detailed(query)