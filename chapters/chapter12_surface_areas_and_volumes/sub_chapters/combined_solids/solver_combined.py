import math
from typing import Dict, Any

def solve_combined_solid(params: Dict[str, Any]) -> str:
    """
    Solve combined solid problems (e.g., cone on hemisphere, capsule).
    """
    try:
        solid_type = params.get("type", "").lower()
        
        if "cone" in solid_type and "hemisphere" in solid_type:
            return solve_cone_on_hemisphere(params)
        elif "capsule" in solid_type or ("cylinder" in solid_type and "hemisphere" in solid_type):
            return solve_capsule(params)
        elif "toy" in solid_type or "cone on cylinder" in solid_type:
            return solve_toy_shape(params)
        else:
            return "❌ Unknown combined solid type. Supported: cone on hemisphere, capsule, toy (cone on cylinder)"
            
    except Exception as e:
        return f"❌ Error solving combined solid: {str(e)}"

def solve_cone_on_hemisphere(params: Dict[str, Any]) -> str:
    """
    Solve problems for cone mounted on hemisphere (ice cream cone shape).
    """
    radius = params.get("radius", 0)
    cone_height = params.get("cone_height", params.get("height", 0))
    unit = params.get("unit", "cm")
    
    if radius <= 0 or cone_height <= 0:
        return "❌ Need radius and cone height for this combined solid."
    
    pi = 22/7
    
    # Calculate individual components
    # Hemisphere
    hemi_volume = (2/3) * pi * radius**3
    hemi_csa = 2 * pi * radius**2
    
    # Cone
    slant_height = math.sqrt(radius**2 + cone_height**2)
    cone_volume = (1/3) * pi * radius**2 * cone_height
    cone_csa = pi * radius * slant_height
    
    # Combined
    total_volume = hemi_volume + cone_volume
    total_surface_area = hemi_csa + cone_csa
    
    result = f"""
✅ **Cone on Hemisphere (Ice Cream Shape) Solution:**

Given:
• Common Radius (r) = {radius} {unit}
• Height of Cone (h) = {cone_height} {unit}
• Slant Height of Cone (l) = √(r² + h²) = {slant_height:.2f} {unit}

📝 **Step-by-Step Solution:**

**Part 1: Hemisphere**
• Volume = ⅔πr³ = ⅔ × {pi:.3f} × {radius}³ = {hemi_volume:.2f} {unit}³
• CSA = 2πr² = 2 × {pi:.3f} × {radius}² = {hemi_csa:.2f} {unit}²

**Part 2: Cone**
• Volume = ⅓πr²h = ⅓ × {pi:.3f} × {radius}² × {cone_height} = {cone_volume:.2f} {unit}³
• CSA = πrl = {pi:.3f} × {radius} × {slant_height:.2f} = {cone_csa:.2f} {unit}²

**Combined Solid:**
• **Total Volume** = {hemi_volume:.2f} + {cone_volume:.2f} = **{total_volume:.2f} {unit}³**
• **Total Surface Area** = {hemi_csa:.2f} + {cone_csa:.2f} = **{total_surface_area:.2f} {unit}²**

💡 **Summary:**
• Total Volume = {total_volume:.2f} {unit}³
• Total Surface Area = {total_surface_area:.2f} {unit}²
"""
    
    return result

def solve_capsule(params: Dict[str, Any]) -> str:
    """
    Solve capsule (cylinder with hemispheres on both ends).
    """
    radius = params.get("radius", 0)
    cylinder_height = params.get("cylinder_height", params.get("height", 0))
    unit = params.get("unit", "cm")
    
    if radius <= 0 or cylinder_height <= 0:
        return "❌ Need radius and cylinder height for capsule."
    
    pi = 22/7
    
    # Cylinder part
    cyl_volume = pi * radius**2 * cylinder_height
    cyl_csa = 2 * pi * radius * cylinder_height
    
    # Two hemispheres = 1 sphere
    sphere_volume = (4/3) * pi * radius**3
    sphere_sa = 4 * pi * radius**2
    
    # Total
    total_volume = cyl_volume + sphere_volume
    total_surface_area = cyl_csa + sphere_sa
    total_height = cylinder_height + 2 * radius
    
    result = f"""
✅ **Capsule Solution:**

Given:
• Radius (r) = {radius} {unit}
• Cylinder Height (h) = {cylinder_height} {unit}
• Total Height = h + 2r = {total_height} {unit}

📝 **Step-by-Step Solution:**

**Part 1: Cylinder**
• Volume = πr²h = {pi:.3f} × {radius}² × {cylinder_height} = {cyl_volume:.2f} {unit}³
• CSA = 2πrh = 2 × {pi:.3f} × {radius} × {cylinder_height} = {cyl_csa:.2f} {unit}²

**Part 2: Two Hemispheres (= 1 Sphere)**
• Volume = ⁴⁄₃πr³ = ⁴⁄₃ × {pi:.3f} × {radius}³ = {sphere_volume:.2f} {unit}³
• Surface Area = 4πr² = 4 × {pi:.3f} × {radius}² = {sphere_sa:.2f} {unit}²

**Combined Capsule:**
• **Total Volume** = {cyl_volume:.2f} + {sphere_volume:.2f} = **{total_volume:.2f} {unit}³**
• **Total Surface Area** = {cyl_csa:.2f} + {sphere_sa:.2f} = **{total_surface_area:.2f} {unit}²**

💡 **Summary:**
• Total Volume = {total_volume:.2f} {unit}³
• Total Surface Area = {total_surface_area:.2f} {unit}²
• Total Height = {total_height} {unit}
"""
    
    return result

def solve_toy_shape(params: Dict[str, Any]) -> str:
    """
    Solve toy shape (cone on cylinder).
    """
    radius = params.get("radius", 0)
    cylinder_height = params.get("cylinder_height", 0)
    cone_height = params.get("cone_height", 0)
    unit = params.get("unit", "cm")
    
    if radius <= 0 or cylinder_height <= 0 or cone_height <= 0:
        return "❌ Need radius, cylinder height, and cone height."
    
    pi = 22/7
    
    # Cylinder
    cyl_volume = pi * radius**2 * cylinder_height
    cyl_csa = 2 * pi * radius * cylinder_height
    cyl_base = pi * radius**2
    
    # Cone
    slant_height = math.sqrt(radius**2 + cone_height**2)
    cone_volume = (1/3) * pi * radius**2 * cone_height
    cone_csa = pi * radius * slant_height
    
    # Combined
    total_volume = cyl_volume + cone_volume
    total_surface_area = cyl_csa + cyl_base + cone_csa  # One base of cylinder
    total_height = cylinder_height + cone_height
    
    result = f"""
✅ **Toy Shape (Cone on Cylinder) Solution:**

Given:
• Radius (r) = {radius} {unit}
• Cylinder Height = {cylinder_height} {unit}
• Cone Height = {cone_height} {unit}
• Total Height = {total_height} {unit}

📝 **Step-by-Step Solution:**

**Part 1: Cylinder**
• Volume = πr²h = {cyl_volume:.2f} {unit}³
• CSA = 2πrh = {cyl_csa:.2f} {unit}²
• Base Area = πr² = {cyl_base:.2f} {unit}²

**Part 2: Cone**
• Slant Height = √(r² + h²) = {slant_height:.2f} {unit}
• Volume = ⅓πr²h = {cone_volume:.2f} {unit}³
• CSA = πrl = {cone_csa:.2f} {unit}²

**Combined Toy:**
• **Total Volume** = {total_volume:.2f} {unit}³
• **Total Surface Area** = {cyl_csa:.2f} + {cyl_base:.2f} + {cone_csa:.2f} = **{total_surface_area:.2f} {unit}²**

💡 **Summary:**
• Total Volume = {total_volume:.2f} {unit}³
• Total Surface Area = {total_surface_area:.2f} {unit}²
• Total Height = {total_height} {unit}
"""
    
    return result