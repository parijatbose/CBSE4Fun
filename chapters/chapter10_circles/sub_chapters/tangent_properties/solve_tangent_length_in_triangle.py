import math

def solve_tangent_length_in_triangle(params: dict) -> str:
    r = params.get('radius')
    oq = params.get('oq')

    if r is None or oq is None:
        return "❌ Missing required values (radius and OQ distance)."

    if oq <= r:
        return "❌ Invalid input: OQ must be greater than radius to form a tangent triangle."

    pq = math.sqrt(oq**2 - r**2)

    return f"""
### 📐 Triangle-Based Tangent Length

**Given:**
- Radius (OP) = {r} cm
- OQ = {oq} cm

**Using Pythagoras theorem in △OPQ:**

\\[
PQ = \\sqrt{{OQ^2 - OP^2}} = \\sqrt{{{oq}^2 - {r}^2}} = \\sqrt{{{oq**2 - r**2}}} = {pq:.2f} \\text{{ cm}}
\\]

✅ **Answer:** Length of PQ = **{pq:.2f} cm**
"""
