import math
from typing import Dict, Any

def solve_pythagoras(params: Dict[str, Any]) -> str:
    """
    Apply Pythagoras theorem to find missing side or verify right triangle.
    """
    try:
        find = params.get("find", "hypotenuse")
        
        if find == "verify":
            return verify_pythagoras(params)
        elif find == "hypotenuse":
            return find_hypotenuse(params)
        elif find == "side":
            return find_other_side(params)
        else:
            # Auto-detect what to find
            return auto_solve_pythagoras(params)
            
    except Exception as e:
        return f"❌ Error applying Pythagoras theorem: {str(e)}"

def find_hypotenuse(params: Dict[str, Any]) -> str:
    """
    Find hypotenuse given two other sides.
    """
    side1 = params.get("side1", 0)
    side2 = params.get("side2", 0)
    
    if side1 <= 0 or side2 <= 0:
        return "❌ Both sides must be positive values"
    
    hypotenuse = math.sqrt(side1**2 + side2**2)
    
    result = f"""
✅ **Pythagoras Theorem - Finding Hypotenuse:**

Given:
• Side 1 (a) = {side1} cm
• Side 2 (b) = {side2} cm

📝 **Step-by-Step Solution:**

**Pythagoras Theorem:** c² = a² + b²

**1. Square the given sides:**
   • a² = {side1}² = {side1**2}
   • b² = {side2}² = {side2**2}

**2. Add the squares:**
   • c² = a² + b²
   • c² = {side1**2} + {side2**2}
   • c² = {side1**2 + side2**2}

**3. Take square root:**
   • c = √{side1**2 + side2**2}
   • **c = {hypotenuse:.2f} cm**

💡 **Answer:** Hypotenuse = {hypotenuse:.2f} cm

**Verification:** {side1}² + {side2}² = {side1**2} + {side2**2} = {side1**2 + side2**2} = {hypotenuse:.2f}² ✓

**Practical Note:** This is the length of the longest side in the right triangle.
"""
    
    return result

def find_other_side(params: Dict[str, Any]) -> str:
    """
    Find one side given hypotenuse and another side.
    """
    hypotenuse = params.get("hypotenuse", 0)
    known_side = params.get("known_side", 0)
    
    if hypotenuse <= 0 or known_side <= 0:
        return "❌ Hypotenuse and known side must be positive"
    
    if known_side >= hypotenuse:
        return "❌ In a right triangle, hypotenuse must be longer than any other side"
    
    other_side = math.sqrt(hypotenuse**2 - known_side**2)
    
    result = f"""
✅ **Pythagoras Theorem - Finding Other Side:**

Given:
• Hypotenuse (c) = {hypotenuse} cm
• Known side (a) = {known_side} cm

📝 **Step-by-Step Solution:**

**From Pythagoras Theorem:** c² = a² + b²
**Rearranging:** b² = c² - a²

**1. Square the given values:**
   • c² = {hypotenuse}² = {hypotenuse**2}
   • a² = {known_side}² = {known_side**2}

**2. Subtract to find b²:**
   • b² = c² - a²
   • b² = {hypotenuse**2} - {known_side**2}
   • b² = {hypotenuse**2 - known_side**2}

**3. Take square root:**
   • b = √{hypotenuse**2 - known_side**2}
   • **b = {other_side:.2f} cm**

💡 **Answer:** Other side = {other_side:.2f} cm

**Verification:** {known_side}² + {other_side:.2f}² = {known_side**2} + {other_side**2:.2f} ≈ {hypotenuse**2} = {hypotenuse}² ✓
"""
    
    return result

def verify_pythagoras(params: Dict[str, Any]) -> str:
    """
    Verify if given sides form a right triangle.
    """
    sides = params.get("sides", [])
    
    if len(sides) != 3:
        return "❌ Need exactly 3 sides to verify"
    
    # Sort to identify potential hypotenuse
    a, b, c = sorted(sides)
    
    # Check Pythagoras theorem
    left_side = a**2 + b**2
    right_side = c**2
    difference = abs(left_side - right_side)
    is_right = difference < 0.001
    
    result = f"""
✅ **Pythagoras Theorem - Verification:**

Given sides: {sides[0]}, {sides[1]}, {sides[2]} cm
Sorted: {a}, {b}, {c} cm (smallest to largest)

📝 **Checking if it's a right triangle:**

**Pythagoras Theorem:** In a right triangle, a² + b² = c²

**1. Calculate squares:**
   • a² = {a}² = {a**2}
   • b² = {b}² = {b**2}
   • c² = {c}² = {c**2}

**2. Check the equation:**
   • a² + b² = {a**2} + {b**2} = {left_side}
   • c² = {right_side}
   • Difference = |{left_side} - {right_side}| = {difference:.6f}

💡 **Conclusion:**
{'✅ YES, this IS a right triangle!' if is_right else '❌ NO, this is NOT a right triangle'}
{f'The hypotenuse is {c} cm (the longest side)' if is_right else f'For a right triangle, we would need: c = √{left_side} = {math.sqrt(left_side):.2f} cm'}

**Triangle Type:** {classify_by_pythagoras(a, b, c)}
"""
    
    return result

def auto_solve_pythagoras(params: Dict[str, Any]) -> str:
    """
    Automatically determine what to solve based on given parameters.
    """
    # Check what's given
    if "sides" in params and len(params["sides"]) == 3:
        return verify_pythagoras(params)
    elif "side1" in params and "side2" in params:
        return find_hypotenuse(params)
    elif "hypotenuse" in params and "known_side" in params:
        return find_other_side(params)
    else:
        # Extract any numbers and try to make sense
        numbers = []
        for key, value in params.items():
            if isinstance(value, (int, float)) and value > 0:
                numbers.append(value)
        
        if len(numbers) == 2:
            params["side1"] = numbers[0]
            params["side2"] = numbers[1]
            return find_hypotenuse(params)
        elif len(numbers) == 3:
            params["sides"] = numbers
            return verify_pythagoras(params)
        else:
            return "❌ Unable to determine what to calculate. Please provide either:\n• Two sides to find hypotenuse\n• Hypotenuse and one side to find the other side\n• Three sides to verify if it's a right triangle"

def classify_by_pythagoras(a: float, b: float, c: float) -> str:
    """
    Classify triangle using Pythagoras theorem.
    """
    left = a**2 + b**2
    right = c**2
    
    if abs(left - right) < 0.001:
        return "Right Triangle (90° angle)"
    elif left > right:
        return "Acute Triangle (all angles < 90°)"
    else:
        return "Obtuse Triangle (one angle > 90°)"