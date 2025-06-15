# File: cbse_math_solver/chapters/chapter12_surface_areas_and_volumes/sub_chapters/sphere/solver_sphere.py

import math
from typing import Dict, Any

def solve_sphere(params: Dict[str, Any]) -> str:
    """
    Solve sphere/hemisphere problems - volume and surface area.
    """
    try:
        radius = params.get("radius", 0)
        shape_type = params.get("type", "sphere").lower()
        unit = params.get("unit", "cm")
        
        if radius <= 0:
            return "❌ Radius must be a positive value."
        
        # Use π = 22/7 for calculations
        pi = 22/7
        
        if shape_type == "sphere":
            # Sphere calculations
            volume = (4/3) * pi * radius**3
            surface_area = 4 * pi * radius**2
            
            result = f"""
✅ **Sphere Solution:**

Given:
• Radius (r) = {radius} {unit}

📝 **Step-by-Step Solution:**

**1. Volume = ⁴⁄₃πr³**
   = ⁴⁄₃ × {pi:.3f} × {radius}³
   = ⁴⁄₃ × {pi:.3f} × {radius**3:.2f}
   = {4/3:.3f} × {pi * radius**3:.2f}
   = **{volume:.2f} {unit}³**

**2. Surface Area = 4πr²**
   = 4 × {pi:.3f} × {radius}²
   = 4 × {pi:.3f} × {radius**2:.2f}
   = **{surface_area:.2f} {unit}²**

💡 **Summary:**
• Volume = {volume:.2f} {unit}³
• Surface Area = {surface_area:.2f} {unit}²
"""
            
        else:  # hemisphere
            # Hemisphere calculations
            volume = (2/3) * pi * radius**3
            csa = 2 * pi * radius**2
            tsa = 3 * pi * radius**2
            
            result = f"""
✅ **Hemisphere Solution:**

Given:
• Radius (r) = {radius} {unit}

📝 **Step-by-Step Solution:**

**1. Volume = ⅔πr³**
   = ⅔ × {pi:.3f} × {radius}³
   = ⅔ × {pi:.3f} × {radius**3:.2f}
   = {2/3:.3f} × {pi * radius**3:.2f}
   = **{volume:.2f} {unit}³**

**2. Curved Surface Area (CSA) = 2πr²**
   = 2 × {pi:.3f} × {radius}²
   = 2 × {pi:.3f} × {radius**2:.2f}
   = **{csa:.2f} {unit}²**

**3. Total Surface Area (TSA) = 3πr²**
   (CSA + Base Area)
   = 3 × {pi:.3f} × {radius}²
   = 3 × {pi:.3f} × {radius**2:.2f}
   = **{tsa:.2f} {unit}²**

💡 **Summary:**
• Volume = {volume:.2f} {unit}³
• Curved Surface Area = {csa:.2f} {unit}²
• Total Surface Area = {tsa:.2f} {unit}²

📌 **Note:** TSA includes the flat circular base of the hemisphere.
"""

        return result

    except Exception as e:
        return f"❌ Error solving {shape_type} problem: {str(e)}"
