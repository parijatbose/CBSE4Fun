# File: chapters/chapter2_polynomials/sub_chapters/polynomial_factoring/solver_factoring.py

from sympy import factor, sympify, symbols, solve, I, expand, nsimplify, Rational
import re

x = symbols('x')

def format_root(root):
    """Format a root value nicely."""
    try:
        # Try to simplify to a nice form
        simplified = nsimplify(root, rational=True)
        if simplified.is_Integer:
            return str(simplified)
        elif simplified.is_Rational:
            return str(simplified)
        else:
            # For irrational roots, show decimal approximation
            return f"{float(root):.3f}"
    except:
        return f"{float(root):.3f}"

def explain_factoring_steps(expr, degree):
    """Generate step-by-step explanation for factoring."""
    poly = expr.as_poly(x)
    coeffs = poly.all_coeffs()
    
    if degree == 2:
        a, b, c = coeffs
        steps = f"\n📝 **Steps for factoring {expr}:**\n"
        steps += f"1. Identify coefficients: a={a}, b={b}, c={c}\n"
        steps += f"2. Calculate discriminant: b²-4ac = {b}²-4({a})({c}) = {b**2 - 4*a*c}\n"
        
        if b**2 - 4*a*c >= 0:
            steps += f"3. Find two numbers that multiply to {a*c} and add to {b}\n"
            # Try to find integer factors
            for i in range(1, abs(a*c) + 1):
                if (a*c) % i == 0:
                    j = (a*c) // i
                    if i + j == b or -i - j == b:
                        steps += f"   Found: {i} and {j}\n"
                        break
        return steps
    
    elif degree == 3:
        a, b, c, d = coeffs
        steps = f"\n📝 **Steps for factoring the cubic {expr}:**\n"
        steps += f"1. Coefficients: a={a}, b={b}, c={c}, d={d}\n"
        steps += f"2. Try to find rational roots using Rational Root Theorem\n"
        steps += f"   Possible rational roots: ±(factors of {abs(d)})/(factors of {abs(a)})\n"
        
        # Find actual roots
        roots = solve(expr, x)
        real_roots = [r for r in roots if not r.has(I)]
        if real_roots:
            steps += f"3. Found roots: {', '.join([format_root(r) for r in real_roots])}\n"
        
        return steps
    
    return ""

def factor_polynomial(expression: str) -> str:
    """
    Factors polynomials (quadratic and cubic) with detailed explanations.
    """
    try:
        expr = sympify(expression)
        
        # Expand first to ensure standard form
        expr = expand(expr)

        # Degree of the polynomial
        if not expr.is_polynomial(x):
            return "Only polynomial expressions are supported."

        degree = expr.as_poly(x).degree()
        
        if degree > 3:
            return f"Currently supporting polynomials up to degree 3. Your polynomial has degree {degree}."

        # Get factoring steps explanation
        steps = explain_factoring_steps(expr, degree)

        # ✅ Quadratic check: discriminant
        if degree == 2:
            a, b, c = expr.as_poly(x).all_coeffs()
            discriminant = b**2 - 4*a*c
            if discriminant < 0:
                return f"The polynomial {expr} cannot be factorized over real numbers.\n{steps}❌ Since discriminant < 0, this has complex roots only."

        # ✅ Cubic check: real roots
        if degree == 3:
            roots = solve(expr, x)
            real_roots = [r for r in roots if not r.has(I)]
            complex_roots = [r for r in roots if r.has(I)]
            
            if len(real_roots) == 0:
                return f"The cubic polynomial {expr} has no real roots and cannot be factorized over real numbers.\n{steps}❌ All roots are complex."
            elif len(real_roots) == 1:
                # One real root, two complex roots
                real_root = real_roots[0]
                steps += f"\n✅ This cubic has 1 real root and 2 complex roots.\n"

        # Perform factoring
        factored = factor(expr)

        # If unchanged, it's irreducible
        if factored == expr:
            return f"The polynomial {expr} cannot be factorized further over rational numbers.\n{steps}"
        
        # Format the output nicely with roots information
        result = f"✅ **Factored form of {expr}:**\n\n**{factored}**"
        
        # Add roots information
        roots = solve(expr, x)
        if roots:
            result += f"\n\n🎯 **Roots/Zeros:**\n"
            for i, root in enumerate(roots, 1):
                if root.is_real:
                    result += f"   x_{i} = {format_root(root)}\n"
                else:
                    result += f"   x_{i} = {root} (complex)\n"
        
        result += steps
        
        return result

    except Exception as e:
        return f"Failed to factor the expression: {expression}\nError: {str(e)}"