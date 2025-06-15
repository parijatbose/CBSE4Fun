import math
from typing import Dict, Any

def solve_cylinder(params: Dict[str, Any]) -> str:
    """
    Solve cylinder problems - volume, CSA, TSA.
    """
    try:
        radius = params.get("radius", 0)
        height = params.get("height", 0)
        find = params.get("find", "all")
        unit = params.get("unit", "cm")
        
        if radius <= 0 or height <= 0:
            return "❌ Radius and height must be positive values."
        
        # Use π = 22/7 for calculations (CBSE preference)
        pi = 22/7
        
        # Calculate all values
        volume = pi * radius**2 * height
        csa = 2 * pi * radius * height
        tsa = 2 * pi * radius * (radius + height)
        
        # Format result
        result = f"""
✅ **Cylinder Solution:**

Given:
• Radius (r) = {radius} {unit}
• Height (h) = {height} {unit}

📝 **Step-by-Step Solution:**

**1. Volume = πr²h**
   = {pi:.3f} × {radius}² × {height}
   = {pi:.3f} × {radius**2} × {height}
   = **{volume:.2f} {unit}³**

**2. Curved Surface Area (CSA) = 2πrh**
   = 2 × {pi:.3f} × {radius} × {height}
   = **{csa:.2f} {unit}²**

**3. Total Surface Area (TSA) = 2πr(r + h)**
   = 2 × {pi:.3f} × {radius} × ({radius} + {height})
   = 2 × {pi:.3f} × {radius} × {radius + height}
   = **{tsa:.2f} {unit}²**

💡 **Summary:**
• Volume = {volume:.2f} {unit}³
• CSA = {csa:.2f} {unit}²
• TSA = {tsa:.2f} {unit}²
"""
        
        # Add practical interpretation
        if unit == "cm":
            volume_ml = volume / 1  # 1 cm³ = 1 ml
            result += f"\n📊 **Capacity:** {volume_ml:.2f} ml or {volume_ml/1000:.3f} litres"
        
        return result
        
    except Exception as e:
        return f"❌ Error solving cylinder problem: {str(e)}"

def find_missing_cylinder_parameter(known_params: Dict[str, Any]) -> str:
    """
    Find missing parameter when volume or surface area is given.
    """
    try:
        pi = 22/7
        
        if "volume" in known_params and "radius" in known_params:
            # Find height
            volume = known_params["volume"]
            radius = known_params["radius"]
            height = volume / (pi * radius**2)
            
            return f"""
✅ **Finding Height of Cylinder:**

Given:
• Volume = {volume} cm³
• Radius = {radius} cm

Using V = πr²h:
{volume} = {pi:.3f} × {radius}² × h
{volume} = {pi * radius**2:.2f} × h
h = {volume} ÷ {pi * radius**2:.2f}
**h = {height:.2f} cm**
"""
        
        elif "volume" in known_params and "height" in known_params:
            # Find radius
            volume = known_params["volume"]
            height = known_params["height"]
            radius = math.sqrt(volume / (pi * height))
            
            return f"""
✅ **Finding Radius of Cylinder:**

Given:
• Volume = {volume} cm³
• Height = {height} cm

Using V = πr²h:
{volume} = {pi:.3f} × r² × {height}
r² = {volume} ÷ ({pi:.3f} × {height})
r² = {volume / (pi * height):.2f}
**r = {radius:.2f} cm**
"""
        
        return "❌ Need at least volume and one dimension to find the missing parameter."
        
    except Exception as e:
        return f"❌ Error finding missing parameter: {str(e)}"