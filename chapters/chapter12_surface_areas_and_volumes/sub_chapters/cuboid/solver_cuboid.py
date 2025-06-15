import math
from typing import Dict, Any

def solve_cuboid(params: Dict[str, Any]) -> str:
    """
    Solve cuboid/cube problems - volume and surface areas.
    """
    try:
        shape_type = params.get("type", "cuboid").lower()
        unit = params.get("unit", "cm")
        
        if shape_type == "cube":
            # For cube, all sides are equal
            side = params.get("length", params.get("side", params.get("edge", 0)))
            
            if side <= 0:
                return "❌ Side/edge must be a positive value."
            
            volume = side**3
            tsa = 6 * side**2
            lsa = 4 * side**2
            diagonal = side * math.sqrt(3)
            
            result = f"""
✅ **Cube Solution:**

Given:
• Side/Edge (a) = {side} {unit}

📝 **Step-by-Step Solution:**

**1. Volume = a³**
   = {side}³
   = **{volume:.2f} {unit}³**

**2. Total Surface Area (TSA) = 6a²**
   = 6 × {side}²
   = 6 × {side**2:.2f}
   = **{tsa:.2f} {unit}²**

**3. Lateral Surface Area (LSA) = 4a²**
   = 4 × {side}²
   = 4 × {side**2:.2f}
   = **{lsa:.2f} {unit}²**

**4. Diagonal = a√3**
   = {side} × √3
   = {side} × {math.sqrt(3):.3f}
   = **{diagonal:.2f} {unit}**

💡 **Summary:**
• Volume = {volume:.2f} {unit}³
• TSA = {tsa:.2f} {unit}²
• LSA = {lsa:.2f} {unit}²
• Diagonal = {diagonal:.2f} {unit}
"""
            
        else:  # cuboid
            length = params.get("length", 0)
            breadth = params.get("breadth", 0)
            height = params.get("height", 0)
            
            if length <= 0 or breadth <= 0 or height <= 0:
                return "❌ Length, breadth, and height must be positive values."
            
            volume = length * breadth * height
            tsa = 2 * (length*breadth + breadth*height + height*length)
            lsa = 2 * height * (length + breadth)
            diagonal = math.sqrt(length**2 + breadth**2 + height**2)
            
            result = f"""
✅ **Cuboid Solution:**

Given:
• Length (l) = {length} {unit}
• Breadth (b) = {breadth} {unit}
• Height (h) = {height} {unit}

📝 **Step-by-Step Solution:**

**1. Volume = l × b × h**
   = {length} × {breadth} × {height}
   = **{volume:.2f} {unit}³**

**2. Total Surface Area (TSA) = 2(lb + bh + hl)**
   = 2 × ({length}×{breadth} + {breadth}×{height} + {height}×{length})
   = 2 × ({length*breadth:.2f} + {breadth*height:.2f} + {height*length:.2f})
   = 2 × {length*breadth + breadth*height + height*length:.2f}
   = **{tsa:.2f} {unit}²**

**3. Lateral Surface Area (LSA) = 2h(l + b)**
   = 2 × {height} × ({length} + {breadth})
   = 2 × {height} × {length + breadth}
   = **{lsa:.2f} {unit}²**

**4. Diagonal = √(l² + b² + h²)**
   = √({length}² + {breadth}² + {height}²)
   = √({length**2:.2f} + {breadth**2:.2f} + {height**2:.2f})
   = √{length**2 + breadth**2 + height**2:.2f}
   = **{diagonal:.2f} {unit}**

💡 **Summary:**
• Volume = {volume:.2f} {unit}³
• TSA = {tsa:.2f} {unit}²
• LSA = {lsa:.2f} {unit}²
• Diagonal = {diagonal:.2f} {unit}
"""
        
        return result
        
    except Exception as e:
        return f"❌ Error solving {shape_type} problem: {str(e)}"

def find_missing_dimension(known_params: Dict[str, Any]) -> str:
    """
    Find missing dimension when volume or surface area is given.
    """
    try:
        if "volume" in known_params and "length" in known_params and "breadth" in known_params:
            # Find height
            volume = known_params["volume"]
            length = known_params["length"]
            breadth = known_params["breadth"]
            height = volume / (length * breadth)
            
            return f"""
✅ **Finding Height of Cuboid:**

Given:
• Volume = {volume} cm³
• Length = {length} cm
• Breadth = {breadth} cm

Using V = l × b × h:
{volume} = {length} × {breadth} × h
{volume} = {length * breadth} × h
h = {volume} ÷ {length * breadth}
**h = {height:.2f} cm**
"""
        
        elif "tsa" in known_params and known_params.get("type") == "cube":
            # Find side of cube
            tsa = known_params["tsa"]
            side = math.sqrt(tsa / 6)
            
            return f"""
✅ **Finding Side of Cube from TSA:**

Given:
• Total Surface Area = {tsa} cm²

Using TSA = 6a²:
{tsa} = 6 × a²
a² = {tsa} ÷ 6
a² = {tsa / 6:.2f}
**a = {side:.2f} cm**
"""
        
        return "❌ Need appropriate parameters to find the missing dimension."
        
    except Exception as e:
        return f"❌ Error finding missing dimension: {str(e)}"