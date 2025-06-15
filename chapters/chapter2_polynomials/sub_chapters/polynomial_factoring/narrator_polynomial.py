def narrate_polynomial_plot(coefficients, degree=2):
    from sympy import symbols, solve, nsimplify, I
    x = symbols('x')
    
    if degree == 2:
        a, b, c = coefficients
        expr = a * x**2 + b * x + c
        vertex_x = -b / (2*a)
        vertex_y = a * vertex_x**2 + b * vertex_x + c
        
        if a > 0:
            direction = "opens upward (U-shaped)"
            vertex_type = "minimum"
        else:
            direction = "opens downward (inverted U-shaped)"
            vertex_type = "maximum"
            
        narration = f"This quadratic curve {direction} since the coefficient of x² is {a}. "
        narration += f"The vertex ({vertex_type} point) is at ({vertex_x:.2f}, {vertex_y:.2f}). "
        
    elif degree == 3:
        a, b, c, d = coefficients
        expr = a * x**3 + b * x**2 + c * x + d
        
        if a > 0:
            behavior = "rises to +∞ as x→+∞ and falls to -∞ as x→-∞"
        else:
            behavior = "falls to -∞ as x→+∞ and rises to +∞ as x→-∞"
            
        narration = f"This cubic curve {behavior} since the coefficient of x³ is {a}. "
        
        # Check for critical points
        discriminant = 4*b**2 - 12*a*c
        if discriminant > 0:
            narration += "The curve has two critical points (local maximum and minimum). "
        elif discriminant == 0:
            narration += "The curve has one critical point (inflection point). "
        else:
            narration += "The curve has no critical points (monotonic). "
    
    # Find and describe roots
    roots = solve(expr, x)
    real_roots = [r for r in roots if not r.has(I)]
    complex_roots = [r for r in roots if r.has(I)]
    
    # Format roots nicely
    if real_roots:
        root_texts = []
        for r in real_roots:
            try:
                simplified = nsimplify(r, rational=True)
                if simplified.is_Integer or simplified.is_Rational:
                    root_texts.append(f"x = {simplified}")
                else:
                    root_texts.append(f"x = {float(r):.2f}")
            except:
                root_texts.append(f"x = {float(r):.2f}")
        
        root_text = ', '.join(root_texts)
        narration += f"It intersects the x-axis at: {root_text}. "
        
        if len(real_roots) == 1 and degree == 3:
            narration += "This cubic has one real root and two complex roots. "
    else:
        narration += "The curve does not intersect the x-axis (no real roots). "
    
    if complex_roots:
        narration += f"It has {len(complex_roots)} complex root(s). "
    
    narration += "These are the zeros of the polynomial."
    
    return narration