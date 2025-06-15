import math
from typing import Dict, Any

def solve_cone(params: Dict[str, Any]) -> str:
    """
    Solve cone problems - volume, CSA, TSA.
    """
    try:
        radius = params.get("radius", 0)
        height = params.get("height", 0)
        slant_height = params.get("slant_height", 0)
        unit = params.get("unit", "cm")
        
        # Calculate missing parameter using Pythagoras theorem
        if radius > 0 and height > 0 and slant_height == 0:
            slant_height = math.sqrt(radius**2 + height**2)
        elif radius > 0 and slant_height > 0 and height == 0:
            height = math.sqrt(slant_height**2 - radius**2)
        elif height > 0 and slant_height > 0 and radius == 0:
            radius = math.sqrt(slant_height**2 - height**2)
        
        if radius <= 0 or height <= 0:
            return "❌ Need at least 2 parameters: radius, height, or slant height."
        
        # Use π = 22/7 for calculations
        pi = 22/7
        
        # Calculate all values
        volume = (1/3) * pi * radius**2 * height
        csa = pi * radius * slant_height
        tsa = pi * radius * (radius + slant_height)
        
        # Format result
        result = f"""
✅ **Cone Solution:**

Given/Calculated:
• Radius (r) = {radius:.2f} {unit}
• Height (h) = {height:.2f} {unit}
• Slant Height (l) = {slant_height:.2f} {unit}

📝 **Step-by-Step Solution:**

**1. Slant Height Verification:**
   l = √(r² + h²)
   l = √({radius}² + {height}²)
   l = √({radius**2:.2f} + {height**2:.2f})
   l = √{radius**2 + height**2:.2f}
   l = {slant_height:.2f} {unit} ✓

**2. Volume = ⅓πr²h**
   = ⅓ × {pi:.3f} × {radius}² × {height}
   = ⅓ × {pi:.3f} × {radius**2:.2f} × {height}
   = ⅓ × {pi * radius**2 * height:.2f}
   = **{volume:.2f} {unit}³**

**3. Curved Surface Area (CSA) = πrl**
   = {pi:.3f} × {radius} × {slant_height:.2f}
   = **{csa:.2f} {unit}²**

**4. Total Surface Area (TSA) = πr(r + l)**
   = {pi:.3f} × {radius} × ({radius} + {slant_height:.2f})
   = {pi:.3f} × {radius} × {radius + slant_height:.2f}
   = **{tsa:.2f} {unit}²**

💡 **Summary:**
• Volume = {volume:.2f} {unit}³
• CSA = {csa:.2f} {unit}²
• TSA = {tsa:.2f} {unit}²
• Slant Height = {slant_height:.2f} {unit}
"""
        
        return result
        
    except Exception as e:
        return f"❌ Error solving cone problem: {str(e)}"

def find_missing_cone_parameter(known_params: Dict[str, Any]) -> str:
    """
    Find missing parameter when volume or surface area is given.
    """
    try:
        pi = 22/7
        
        if "volume" in known_params and "radius" in known_params:
            # Find height
            volume = known_params["volume"]
            radius = known_params["radius"]
            height = (3 * volume) / (pi * radius**2)
            slant_height = math.sqrt(radius**2 + height**2)
            
            return f"""
✅ **Finding Height of Cone:**

Given:
• Volume = {volume} cm³
• Radius = {radius} cm

Using V = ⅓πr²h:
{volume} = ⅓ × {pi:.3f} × {radius}² × h
{volume} = ⅓ × {pi * radius**2:.2f} × h
h = {3 * volume} ÷ {pi * radius**2:.2f}
**h = {height:.2f} cm**

Slant height: l = √(r² + h²) = √({radius}² + {height:.2f}²) = **{slant_height:.2f} cm**
"""
        
        elif "csa" in known_params and "radius" in known_params:
            # Find slant height
            csa = known_params["csa"]
            radius = known_params["radius"]
            slant_height = csa / (pi * radius)
            
            return f"""
✅ **Finding Slant Height of Cone:**

Given:
• CSA = {csa} cm²
• Radius = {radius} cm

Using CSA = πrl:
{csa} = {pi:.3f} × {radius} × l
l = {csa} ÷ ({pi:.3f} × {radius})
**l = {slant_height:.2f} cm**
"""
        
        return "❌ Need appropriate parameters to find the missing value."
        
    except Exception as e:
        return f"❌ Error finding missing parameter: {str(e)}"