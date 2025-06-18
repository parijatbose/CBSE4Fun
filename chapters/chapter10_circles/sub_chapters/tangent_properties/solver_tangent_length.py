import math
from typing import Dict, Any

def calculate_tangent_length(params: Dict[str, Any]) -> str:
    """
    Calculate the length of tangent from an external point to a circle.
    
    Args:
        params: Dictionary containing:
            - x, y: Coordinates of external point
            - h, k: Coordinates of circle center (default 0, 0)
            - radius: Radius of the circle
    
    Returns:
        str: Formatted solution with step-by-step calculation
    """
    # Extract parameters
    x = params.get('x', 0)
    y = params.get('y', 0)
    h = params.get('h', 0)
    k = params.get('k', 0)
    radius = params.get('radius', 1)
    
    # Calculate distance from point to center
    distance_squared = (x - h)**2 + (y - k)**2
    distance = math.sqrt(distance_squared)
    
    # Check if point is external
    if distance <= radius:
        return f"""
❌ **Error: Invalid Point Location**

The point ({x}, {y}) is {'on' if distance == radius else 'inside'} the circle.
- Distance from center to point: {distance:.2f}
- Circle radius: {radius}

**Note:** Tangents can only be drawn from points outside the circle (distance > radius).
"""
    
    # Calculate tangent length
    tangent_length_squared = distance_squared - radius**2
    tangent_length = math.sqrt(tangent_length_squared)
    
    # Format the solution
    return f"""
### 🔵 Tangent Length Calculation

**Given:**
- External point P: ({x}, {y})
- Circle center O: ({h}, {k})
- Circle radius: {radius}

**Solution:**

**Step 1: Calculate distance from point to center**
- Distance OP = √[(x-h)² + (y-k)²]
- Distance OP = √[({x}-{h})² + ({y}-{k})²]
- Distance OP = √[{(x-h)**2} + {(y-k)**2}]
- Distance OP = √{distance_squared} = {distance:.2f}

**Step 2: Verify point is external**
- Distance ({distance:.2f}) > Radius ({radius}) ✓
- Point is external, tangent can be drawn

**Step 3: Apply tangent length formula**
- For external point P and circle with center O and radius r:
- Tangent length = √[OP² - r²]
- Tangent length = √[{distance_squared} - {radius**2}]
- Tangent length = √{tangent_length_squared}
- **Tangent length = {tangent_length:.2f} units**

**Verification:**
- By Pythagorean theorem in right triangle OPT (where T is point of tangency):
- OP² = OT² + PT²
- {distance_squared:.2f} = {radius**2} + {tangent_length_squared:.2f} ✓

✅ **Answer:** The length of the tangent from point ({x}, {y}) to the circle is **{tangent_length:.2f} units**.

**Note:** From any external point, exactly two tangents of equal length can be drawn to a circle.
"""

def calculate_multiple_tangents(points: list, circle_params: Dict[str, Any]) -> str:
    """
    Calculate tangent lengths from multiple points to a circle.
    
    Args:
        points: List of (x, y) tuples
        circle_params: Dictionary with h, k, radius
    
    Returns:
        str: Formatted comparison of tangent lengths
    """
    h = circle_params.get('h', 0)
    k = circle_params.get('k', 0)
    radius = circle_params.get('radius', 1)
    
    results = []
    for x, y in points:
        distance_squared = (x - h)**2 + (y - k)**2
        if distance_squared > radius**2:
            tangent_length = math.sqrt(distance_squared - radius**2)
            results.append(f"- Point ({x}, {y}): Tangent length = {tangent_length:.2f} units")
        else:
            results.append(f"- Point ({x}, {y}): Inside/on circle - no tangent possible")
    
    return f"""
### 🔵 Multiple Tangent Lengths

**Circle:** Center ({h}, {k}), Radius {radius}

**Tangent lengths from different points:**
{chr(10).join(results)}

**Key Property:** All tangents from the same external point have equal length (Theorem 10.2).
"""