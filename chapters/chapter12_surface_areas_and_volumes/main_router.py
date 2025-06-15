import os
import json
from utils.sanitizer import sanitize_expression
from chapters.chapter12_surface_areas_and_volumes.interpret_query_solids import interpret_query_solids
from chapters.chapter12_surface_areas_and_volumes.sub_chapters.cylinder.solver_cylinder import solve_cylinder
from chapters.chapter12_surface_areas_and_volumes.sub_chapters.cone.solver_cone import solve_cone
from chapters.chapter12_surface_areas_and_volumes.sub_chapters.sphere.solver_sphere import solve_sphere
from chapters.chapter12_surface_areas_and_volumes.sub_chapters.cuboid.solver_cuboid import solve_cuboid
from chapters.chapter12_surface_areas_and_volumes.sub_chapters.combined_solids.solver_combined import solve_combined_solid

def load_logic_template(intent: str):
    path = os.path.join(os.path.dirname(__file__), 'logic_templates', f'{intent}.json')
    if os.path.exists(path):
        with open(path, 'r') as f:
            return json.load(f)
    return None

def route_query(query: str) -> str:
    query = query.strip()
    query_lower = query.lower()
    
    # First, try LLM interpretation if available
    try:
        llm_result = interpret_query_solids(query)
        intent = llm_result.get("intent")
        params = llm_result.get("parameters", {})
        
        if intent == "solve_cylinder":
            return solve_cylinder(params)
        elif intent == "solve_cone":
            return solve_cone(params)
        elif intent == "solve_sphere":
            return solve_sphere(params)
        elif intent == "solve_cuboid":
            return solve_cuboid(params)
        elif intent == "solve_combined":
            return solve_combined_solid(params)
        elif intent == "formula_request":
            return get_formula_explanation(params.get("solid_type"))
            
    except Exception as e:
        # If LLM fails, continue with rule-based approach
        pass
    
    # Rule-based approach for common queries
    if any(word in query_lower for word in ["cylinder", "cylindrical"]):
        if any(word in query_lower for word in ["volume", "find", "calculate"]):
            return extract_and_solve_cylinder(query)
        elif any(word in query_lower for word in ["formula", "surface area", "csa", "tsa"]):
            return get_formula_explanation("cylinder")
            
    elif any(word in query_lower for word in ["cone", "conical"]):
        if any(word in query_lower for word in ["volume", "find", "calculate"]):
            return extract_and_solve_cone(query)
        elif any(word in query_lower for word in ["formula", "surface area", "csa", "tsa"]):
            return get_formula_explanation("cone")
            
    elif any(word in query_lower for word in ["sphere", "spherical", "hemisphere"]):
        if any(word in query_lower for word in ["volume", "find", "calculate"]):
            return extract_and_solve_sphere(query)
        elif any(word in query_lower for word in ["formula", "surface area"]):
            return get_formula_explanation("sphere")
            
    elif any(word in query_lower for word in ["cube", "cuboid", "box"]):
        if any(word in query_lower for word in ["volume", "find", "calculate"]):
            return extract_and_solve_cuboid(query)
        elif any(word in query_lower for word in ["formula", "surface area"]):
            return get_formula_explanation("cuboid")
    
    # No match found → show available options
    return show_available_options()

def extract_and_solve_cylinder(query: str):
    """Extract parameters and solve cylinder problem."""
    import re
    # Try to extract radius and height
    radius_match = re.search(r'radius[:\s]+(\d+(?:\.\d+)?)', query, re.IGNORECASE)
    height_match = re.search(r'height[:\s]+(\d+(?:\.\d+)?)', query, re.IGNORECASE)
    
    if radius_match and height_match:
        params = {
            "radius": float(radius_match.group(1)),
            "height": float(height_match.group(1)),
            "find": "all"  # Find volume, CSA, and TSA
        }
        return solve_cylinder(params)
    else:
        return "❌ Could not extract radius and height from the query. Please specify both values."

def extract_and_solve_cone(query: str):
    """Extract parameters and solve cone problem."""
    import re
    radius_match = re.search(r'radius[:\s]+(\d+(?:\.\d+)?)', query, re.IGNORECASE)
    height_match = re.search(r'height[:\s]+(\d+(?:\.\d+)?)', query, re.IGNORECASE)
    slant_match = re.search(r'slant\s*height[:\s]+(\d+(?:\.\d+)?)', query, re.IGNORECASE)
    
    params = {}
    if radius_match:
        params["radius"] = float(radius_match.group(1))
    if height_match:
        params["height"] = float(height_match.group(1))
    if slant_match:
        params["slant_height"] = float(slant_match.group(1))
        
    if len(params) >= 2:  # Need at least 2 parameters
        params["find"] = "all"
        return solve_cone(params)
    else:
        return "❌ Need at least 2 parameters (radius, height, or slant height) to solve cone problems."

def extract_and_solve_sphere(query: str):
    """Extract parameters and solve sphere problem."""
    import re
    radius_match = re.search(r'radius[:\s]+(\d+(?:\.\d+)?)', query, re.IGNORECASE)
    diameter_match = re.search(r'diameter[:\s]+(\d+(?:\.\d+)?)', query, re.IGNORECASE)
    
    params = {}
    if radius_match:
        params["radius"] = float(radius_match.group(1))
    elif diameter_match:
        params["radius"] = float(diameter_match.group(1)) / 2
        
    if "hemisphere" in query.lower():
        params["type"] = "hemisphere"
    else:
        params["type"] = "sphere"
        
    if "radius" in params:
        params["find"] = "all"
        return solve_sphere(params)
    else:
        return "❌ Could not extract radius or diameter from the query."

def extract_and_solve_cuboid(query: str):
    """Extract parameters and solve cuboid/cube problem."""
    import re
    
    if "cube" in query.lower() and "cuboid" not in query.lower():
        # It's a cube - only need side
        side_match = re.search(r'side[:\s]+(\d+(?:\.\d+)?)', query, re.IGNORECASE)
        edge_match = re.search(r'edge[:\s]+(\d+(?:\.\d+)?)', query, re.IGNORECASE)
        
        if side_match or edge_match:
            side = float(side_match.group(1) if side_match else edge_match.group(1))
            params = {
                "length": side,
                "breadth": side,
                "height": side,
                "type": "cube",
                "find": "all"
            }
            return solve_cuboid(params)
    else:
        # It's a cuboid - need length, breadth, height
        length_match = re.search(r'length[:\s]+(\d+(?:\.\d+)?)', query, re.IGNORECASE)
        breadth_match = re.search(r'breadth[:\s]+(\d+(?:\.\d+)?)', query, re.IGNORECASE)
        width_match = re.search(r'width[:\s]+(\d+(?:\.\d+)?)', query, re.IGNORECASE)
        height_match = re.search(r'height[:\s]+(\d+(?:\.\d+)?)', query, re.IGNORECASE)
        
        params = {}
        if length_match:
            params["length"] = float(length_match.group(1))
        if breadth_match:
            params["breadth"] = float(breadth_match.group(1))
        elif width_match:
            params["breadth"] = float(width_match.group(1))
        if height_match:
            params["height"] = float(height_match.group(1))
            
        if len(params) == 3:
            params["type"] = "cuboid"
            params["find"] = "all"
            return solve_cuboid(params)
            
    return "❌ Could not extract dimensions. For cube: specify side/edge. For cuboid: specify length, breadth, and height."

def get_formula_explanation(solid_type: str) -> str:
    """Return formula explanation for a solid type."""
    formulas = {
        "cylinder": """
📐 **Cylinder Formulas:**

• **Volume** = πr²h
• **Curved Surface Area (CSA)** = 2πrh
• **Total Surface Area (TSA)** = 2πr(r + h)

Where:
- r = radius of base
- h = height of cylinder
- π ≈ 3.14159 or 22/7
""",
        "cone": """
📐 **Cone Formulas:**

• **Volume** = ⅓πr²h
• **Curved Surface Area (CSA)** = πrl
• **Total Surface Area (TSA)** = πr(r + l)
• **Slant Height** l = √(r² + h²)

Where:
- r = radius of base
- h = height of cone
- l = slant height
- π ≈ 3.14159 or 22/7
""",
        "sphere": """
📐 **Sphere & Hemisphere Formulas:**

**Sphere:**
• **Volume** = ⁴⁄₃πr³
• **Surface Area** = 4πr²

**Hemisphere:**
• **Volume** = ⅔πr³
• **Curved Surface Area** = 2πr²
• **Total Surface Area** = 3πr²

Where:
- r = radius
- π ≈ 3.14159 or 22/7
""",
        "cuboid": """
📐 **Cuboid & Cube Formulas:**

**Cuboid:**
• **Volume** = l × b × h
• **Total Surface Area** = 2(lb + bh + hl)
• **Lateral Surface Area** = 2h(l + b)

**Cube:**
• **Volume** = a³
• **Total Surface Area** = 6a²
• **Lateral Surface Area** = 4a²

Where:
- l = length, b = breadth, h = height (cuboid)
- a = side/edge (cube)
"""
    }
    
    return formulas.get(solid_type, "❌ Unknown solid type. Available: cylinder, cone, sphere, cuboid")

def show_available_options():
    """Show available options when no specific query matches."""
    return """
📚 **Surface Areas and Volumes - Available Options:**

**1. Solve Problems:**
• "Find volume of cylinder with radius 7 cm and height 10 cm"
• "Calculate surface area of cone with radius 5 cm and height 12 cm"
• "Find volume of sphere with radius 14 cm"
• "Calculate TSA of cube with side 8 cm"

**2. Get Formulas:**
• "Show cylinder formulas"
• "What is the formula for volume of cone?"
• "Surface area of sphere formula"
• "Cuboid volume and surface area formulas"

**3. Combined Solids:**
• "Find volume of ice cream cone (cone + hemisphere)"
• "Calculate surface area of capsule (cylinder + 2 hemispheres)"

**Tips:**
- Specify the solid type and dimensions
- Use units consistently (cm, m, etc.)
- For combined solids, describe the shape clearly
"""