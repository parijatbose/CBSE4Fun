import math
from typing import Dict, Any

def solve_triangle_area(params: Dict[str, Any]) -> str:
    """
    Calculate area of triangle using various methods.
    """
    try:
        method = params.get("method", "auto")
        
        if method == "heron" or "sides" in params:
            return calculate_area_heron(params)
        elif method == "base_height" or ("base" in params and "height" in params):
            return calculate_area_base_height(params)
        elif method == "trigonometric" or "angle" in params:
            return calculate_area_trigonometric(params)
        else:
            return "❌ Need either: 3 sides (Heron's formula), base & height, or 2 sides & included angle"
            
    except Exception as e:
        return f"❌ Error calculating area: {str(e)}"

def calculate_area_heron(params: Dict[str, Any]) -> str:
    """
    Calculate area using Heron's formula.
    """
    sides = params.get("sides", [])
    
    if len(sides) != 3:
        return "❌ Need exactly 3 sides for Heron's formula"
    
    a, b, c = sides
    
    # Check triangle validity
    if not (a + b > c and b + c > a and c + a > b):
        return f"""
❌ **Invalid Triangle:**

Given sides: {a}, {b}, {c} cm

**Triangle Inequality Check:**
• {a} + {b} = {a + b} {'>' if a + b > c else '≤'} {c} {'✓' if a + b > c else '✗'}
• {b} + {c} = {b + c} {'>' if b + c > a else '≤'} {a} {'✓' if b + c > a else '✗'}
• {c} + {a} = {c + a} {'>' if c + a > b else '≤'} {b} {'✓' if c + a > b else '✗'}

**Result:** These sides cannot form a triangle!
"""
    
    # Calculate semi-perimeter
    s = (a + b + c) / 2
    
    # Calculate area using Heron's formula
    area_squared = s * (s - a) * (s - b) * (s - c)
    area = math.sqrt(area_squared)
    
    # Calculate angles for additional info
    angles = calculate_angles_from_sides(sides)
    
    result = f"""
✅ **Triangle Area (Heron's Formula):**

Given sides: a = {a} cm, b = {b} cm, c = {c} cm

📝 **Step-by-Step Solution:**

**1. Calculate semi-perimeter (s):**
   s = (a + b + c) / 2
   s = ({a} + {b} + {c}) / 2
   s = {a + b + c} / 2
   s = {s} cm

**2. Apply Heron's Formula:**
   Area = √[s(s-a)(s-b)(s-c)]
   Area = √[{s}({s}-{a})({s}-{b})({s}-{c})]
   Area = √[{s} × {s-a} × {s-b} × {s-c}]
   Area = √[{area_squared:.3f}]
   **Area = {area:.2f} cm²**

**3. Additional Information:**
   • Perimeter = {a + b + c} cm
   • Angles: {angles[0]:.1f}°, {angles[1]:.1f}°, {angles[2]:.1f}°
   • Type: {classify_triangle(sides, angles)}

💡 **Verification:** Sum of angles = {sum(angles):.1f}° ≈ 180° ✓
"""
    
    return result

def calculate_area_base_height(params: Dict[str, Any]) -> str:
    """
    Calculate area using base and height.
    """
    base = params.get("base", 0)
    height = params.get("height", 0)
    
    if base <= 0 or height <= 0:
        return "❌ Base and height must be positive values"
    
    area = 0.5 * base * height
    
    result = f"""
✅ **Triangle Area (Base × Height):**

Given:
• Base = {base} cm
• Height = {height} cm

📝 **Solution:**

**Formula:** Area = ½ × base × height
   Area = ½ × {base} × {height}
   Area = 0.5 × {base * height}
   **Area = {area:.2f} cm²**

💡 **Note:** Height must be perpendicular to the base.

**Quick Facts:**
• This is the simplest formula for triangle area
• Works for any triangle if you know base and perpendicular height
• For right triangles, the two legs can be base and height
"""
    
    return result

def calculate_area_trigonometric(params: Dict[str, Any]) -> str:
    """
    Calculate area using two sides and included angle.
    """
    side1 = params.get("side1", 0)
    side2 = params.get("side2", 0)
    angle = params.get("angle", 0)
    
    if side1 <= 0 or side2 <= 0:
        return "❌ Sides must be positive values"
    
    if angle <= 0 or angle >= 180:
        return "❌ Angle must be between 0° and 180°"
    
    # Convert angle to radians
    angle_rad = math.radians(angle)
    
    # Calculate area
    area = 0.5 * side1 * side2 * math.sin(angle_rad)
    
    result = f"""
✅ **Triangle Area (Trigonometric Formula):**

Given:
• Side 1 = {side1} cm
• Side 2 = {side2} cm
• Included angle = {angle}°

📝 **Solution:**

**Formula:** Area = ½ × a × b × sin(C)
   where C is the angle between sides a and b

   Area = ½ × {side1} × {side2} × sin({angle}°)
   Area = ½ × {side1} × {side2} × {math.sin(angle_rad):.4f}
   Area = 0.5 × {side1 * side2 * math.sin(angle_rad):.4f}
   **Area = {area:.2f} cm²**

💡 **Important:**
• The angle must be between the two given sides
• This formula is useful when you don't have the height
• sin({angle}°) = {math.sin(angle_rad):.4f}
"""
    
    return result

def calculate_angles_from_sides(sides: list) -> list:
    """
    Calculate angles using law of cosines.
    """
    a, b, c = sides
    
    # Law of cosines
    cos_A = (b**2 + c**2 - a**2) / (2 * b * c)
    cos_B = (a**2 + c**2 - b**2) / (2 * a * c)
    cos_C = (a**2 + b**2 - c**2) / (2 * a * b)
    
    # Ensure values are in valid range
    cos_A = max(-1, min(1, cos_A))
    cos_B = max(-1, min(1, cos_B))
    cos_C = max(-1, min(1, cos_C))
    
    # Calculate angles in degrees
    angle_A = math.degrees(math.acos(cos_A))
    angle_B = math.degrees(math.acos(cos_B))
    angle_C = math.degrees(math.acos(cos_C))
    
    return [angle_A, angle_B, angle_C]

def classify_triangle(sides: list, angles: list) -> str:
    """
    Classify triangle by sides and angles.
    """
    a, b, c = sorted(sides)
    
    # By sides
    if abs(a - b) < 0.001 and abs(b - c) < 0.001:
        side_type = "Equilateral"
    elif abs(a - b) < 0.001 or abs(b - c) < 0.001 or abs(a - c) < 0.001:
        side_type = "Isosceles"
    else:
        side_type = "Scalene"
    
    # By angles
    max_angle = max(angles)
    if abs(max_angle - 90) < 0.1:
        angle_type = "Right"
    elif max_angle > 90:
        angle_type = "Obtuse"
    else:
        angle_type = "Acute"
    
    return f"{angle_type} {side_type}"