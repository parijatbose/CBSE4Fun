import sys
import os
from typing import Dict, Any
import numpy as np
import math
from sympy import symbols, solve, Eq

# Add the current directory to the path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

# Import interpret_query for better query parsing
try:
    from interpret_query_circle import interpret_query
except ImportError:
    print("Warning: Could not import interpret_query_circle")
    interpret_query = None

# Import solvers from sub_chapters
try:
    from sub_chapters.tangent_properties.solver_tangent_length import calculate_tangent_length
except ImportError as e:
    print(f"Warning: Could not import tangent length solver: {e}")
    calculate_tangent_length = None

try:
    from sub_chapters.tangent_properties.solver_tangent_theorems import prove_tangent_theorem
except ImportError as e:
    print(f"Warning: Could not import tangent theorems solver: {e}")
    prove_tangent_theorem = None

try:
    from sub_chapters.tangent_properties.solver_tangent_constructions import construct_tangent
except ImportError as e:
    print(f"Warning: Could not import tangent constructions solver: {e}")
    construct_tangent = None

try:
    from sub_chapters.circle_applications.solver_real_world import solve_real_world_problem
except ImportError as e:
    print(f"Warning: Could not import real world solver: {e}")
    solve_real_world_problem = None

def route_query(query: str) -> str:
    """
    Route the query to appropriate circle problem solver.
    """
    query_lower = query.lower().strip()
    
    # Use interpret_query if available
    if interpret_query:
        result = interpret_query(query)
        if result['type'] and not result['error']:
            return route_by_type(result['type'], result['parameters'], query)
    
    # Fall back to keyword-based routing
    # Tangent length problems
    if any(keyword in query_lower for keyword in ['tangent length', 'length of tangent']):
        return solve_tangent_length(query)
    
    # Tangent theorem proofs
    elif any(keyword in query_lower for keyword in ['prove', 'theorem', 'proof']):
        return solve_theorem_proof(query)
    
    # Construction problems
    elif any(keyword in query_lower for keyword in ['construct', 'draw', 'construction']):
        return solve_construction(query)
    
    # Real world applications
    elif any(keyword in query_lower for keyword in ['area', 'rotation', 'wheel', 'distance', 'coverage', 'satellite']):
        return solve_real_world(query)
    
    else:
        return """
I can help you with various circle problems! Try asking about:

**📐 Tangent Problems:**
- Find the length of tangent from point (3,4) to circle with radius 5
- Calculate tangent length from external point to circle

**📖 Theorem Proofs:**
- Prove that tangent is perpendicular to radius (Theorem 10.1)
- Show that tangents from external point are equal (Theorem 10.2)

**✏️ Construction:**
- Construct tangent from external point
- Draw tangent to circle at given point

**🌍 Real World Applications:**
- Find area covered by wheel rotation
- Calculate satellite coverage area
- Wheel rotation and distance problems
"""

def route_by_type(problem_type: str, parameters: Dict[str, Any], original_query: str) -> str:
    """Route based on problem type from interpret_query."""
    if problem_type == 'tangent_length':
        return solve_tangent_length_with_params(parameters)
    elif problem_type == 'theorem_proof':
        return solve_theorem_proof_with_params(parameters)
    elif problem_type == 'construction':
        return solve_construction_with_params(parameters)
    elif problem_type == 'real_world':
        return solve_real_world_with_params(parameters)
    else:
        return "Unknown problem type. Please try rephrasing your question."

def solve_tangent_length(query: str) -> str:
    """Solve tangent length problems."""
    try:
        # Extract numbers from query
        import re
        numbers = re.findall(r'-?\d+\.?\d*', query)
        numbers = [float(n) for n in numbers]
        
        if len(numbers) >= 3:  # Point coordinates and radius
            x, y = numbers[0], numbers[1]
            r = numbers[2]
            
            # Check if center is specified
            h, k = 0, 0  # Default center at origin
            if len(numbers) >= 5:
                h, k = numbers[3], numbers[4]
            
            # Use imported solver if available
            if calculate_tangent_length:
                params = {'x': x, 'y': y, 'radius': r, 'h': h, 'k': k}
                return calculate_tangent_length(params)
            
            # Fallback calculation
            # Calculate tangent length using formula: √((x-h)² + (y-k)² - r²)
            distance_squared = (x-h)**2 + (y-k)**2
            if distance_squared <= r**2:
                return "❌ Error: The point is inside or on the circle. Tangent can only be drawn from external points."
            
            tangent_length = math.sqrt(distance_squared - r**2)
            
            return f"""
### 🔵 Tangent Length Solution

**Given:**
- Point: ({x}, {y})
- Circle center: ({h}, {k})
- Circle radius: {r}

**Using the tangent length formula:**
Length = √[(x-h)² + (y-k)² - r²]

**Calculation:**
- Distance from point to center² = ({x}-{h})² + ({y}-{k})²
- Distance² = {(x-h)**2} + {(y-k)**2} = {distance_squared}
- Tangent length² = {distance_squared} - {r**2} = {distance_squared - r**2}
- Tangent length = √{distance_squared - r**2} = **{tangent_length:.2f} units**

✅ **Answer:** The length of the tangent is **{tangent_length:.2f} units**.
"""
        else:
            return "❌ Please provide the point coordinates and circle radius. Example: 'Find tangent length from point (3,4) to circle with radius 5'"
            
    except Exception as e:
        return f"❌ Error solving tangent length problem: {str(e)}"

def solve_tangent_length_with_params(params: Dict[str, Any]) -> str:
    """Solve tangent length with extracted parameters."""
    if calculate_tangent_length:
        return calculate_tangent_length(params)
    else:
        # Fallback implementation
        x = params.get('x', 0)
        y = params.get('y', 0)
        r = params.get('radius', 1)
        h = params.get('h', 0)
        k = params.get('k', 0)
        
        distance_squared = (x-h)**2 + (y-k)**2
        if distance_squared <= r**2:
            return "❌ Error: The point is inside or on the circle. Tangent can only be drawn from external points."
        
        tangent_length = math.sqrt(distance_squared - r**2)
        return f"""
### 🔵 Tangent Length Solution

**Given:**
- Point: ({x}, {y})
- Circle center: ({h}, {k})
- Circle radius: {r}

**Solution:**
- Tangent length = √[(x-h)² + (y-k)² - r²]
- Tangent length = √[{distance_squared} - {r**2}]
- Tangent length = **{tangent_length:.2f} units**

✅ **Answer:** The length of the tangent is **{tangent_length:.2f} units**.
"""

def solve_theorem_proof(query: str) -> str:
    """Solve theorem proof problems."""
    query_lower = query.lower()
    
    if prove_tangent_theorem:
        if 'theorem 10.1' in query_lower or 'perpendicular' in query_lower:
            return prove_tangent_theorem({'theorem_type': 'perpendicular'})
        elif 'theorem 10.2' in query_lower or 'equal' in query_lower:
            return prove_tangent_theorem({'theorem_type': 'equal_tangents'})
        else:
            return prove_tangent_theorem({'theorem_type': 'general'})
    
    # Fallback proofs
    if 'theorem 10.1' in query_lower or 'perpendicular' in query_lower:
        return """
### 📖 Theorem 10.1: The tangent at any point of a circle is perpendicular to the radius through the point of contact.

**Proof by Contradiction:**

1. **Assume** the tangent line l at point P is NOT perpendicular to radius OP.

2. **Then** there exists another line through P that is perpendicular to OP.

3. **Consider** any point Q on tangent line l (Q ≠ P).
   - Since l is tangent, Q lies outside the circle
   - Therefore: OQ > OP (radius)

4. **But** if l is not perpendicular to OP, we can find a point R on l such that OR < OQ.

5. **This means** R would be inside the circle, contradicting that l is a tangent (which touches the circle at only one point).

6. **Therefore**, our assumption is wrong, and the tangent must be perpendicular to the radius.

✅ **Conclusion:** The tangent at any point of a circle is perpendicular to the radius through the point of contact.
"""
    
    elif 'theorem 10.2' in query_lower or 'equal' in query_lower:
        return """
### 📖 Theorem 10.2: The lengths of tangents drawn from an external point to a circle are equal.

**Proof:**

1. **Given:** Circle with center O, external point P, and tangents PA and PB.

2. **In triangles OAP and OBP:**
   - OA = OB (radii of the same circle)
   - OP is common
   - ∠OAP = ∠OBP = 90° (tangent ⊥ radius by Theorem 10.1)

3. **By RHS congruence:** △OAP ≅ △OBP

4. **Therefore:** PA = PB (corresponding parts of congruent triangles)

✅ **Conclusion:** The lengths of tangents drawn from an external point to a circle are equal.
"""
    
    else:
        return "Please specify which theorem you want to prove (Theorem 10.1 or 10.2)."

def solve_theorem_proof_with_params(params: Dict[str, Any]) -> str:
    """Solve theorem proof with parameters."""
    theorem = params.get('theorem', '10.1')
    if prove_tangent_theorem:
        theorem_type = 'perpendicular' if theorem == '10.1' else 'equal_tangents'
        return prove_tangent_theorem({'theorem_type': theorem_type})
    else:
        return solve_theorem_proof(f"Prove theorem {theorem}")

def solve_construction(query: str) -> str:
    """Solve construction problems."""
    if construct_tangent:
        if 'external' in query.lower() or 'outside' in query.lower():
            return construct_tangent({'construction_type': 'external_point'})
        elif 'given point' in query.lower() or 'at point' in query.lower():
            return construct_tangent({'construction_type': 'given_point'})
        else:
            return construct_tangent({'construction_type': 'external_point'})
    
    # Fallback construction
    return """
### ✏️ Construction of Tangent from External Point

**Steps:**

1. **Draw** the given circle with center O and mark external point P.

2. **Join** O and P with a straight line.

3. **Find** the midpoint M of OP.

4. **Draw** a circle with M as center and MO as radius.

5. **Mark** the intersection points A and B where this new circle meets the original circle.

6. **Join** PA and PB. These are the required tangents.

**Verification:**
- ∠OAP = ∠OBP = 90° (angle in semicircle)
- Therefore, PA ⊥ OA and PB ⊥ OB
- By definition, PA and PB are tangents to the circle

✅ **Result:** Two tangents PA and PB from external point P to the circle.
"""

def solve_construction_with_params(params: Dict[str, Any]) -> str:
    """Solve construction with parameters."""
    if construct_tangent:
        return construct_tangent(params)
    else:
        return solve_construction("construct tangent")

def solve_real_world(query: str) -> str:
    """Solve real-world application problems."""
    query_lower = query.lower()
    
    # Determine problem type
    if 'wheel' in query_lower or 'rotation' in query_lower:
        problem_type = 'wheel_rotation'
    elif 'satellite' in query_lower or 'coverage' in query_lower:
        problem_type = 'satellite_coverage'
    elif 'area' in query_lower:
        problem_type = 'area_coverage'
    else:
        problem_type = 'general'
    
    # Extract numbers
    import re
    numbers = re.findall(r'-?\d+\.?\d*', query)
    numbers = [float(n) for n in numbers]
    
    params = {}
    if numbers:
        params['radius'] = numbers[0] if len(numbers) > 0 else 5
        params['value'] = numbers[0] if len(numbers) > 0 else 5
        if len(numbers) > 1:
            params['angle'] = numbers[1]
            params['rotations'] = numbers[1]
        if len(numbers) > 2:
            params['height'] = numbers[2]
    
    # Use imported solver if available
    if solve_real_world_problem:
        return solve_real_world_problem(problem_type, params)
    
    # Fallback implementation
    if problem_type == 'wheel_rotation' and len(numbers) >= 2:
        r = numbers[0]
        rotations = numbers[1] if len(numbers) > 1 else 1
        
        circumference = 2 * math.pi * r
        distance = circumference * rotations
        area_per_rotation = math.pi * r * r
        
        return f"""
### 🎯 Wheel Rotation Problem

**Given:**
- Wheel radius: {r} units
- Number of rotations: {rotations}

**Solution:**

**Step 1: Calculate circumference**
- Circumference = 2πr = 2π × {r} = {circumference:.2f} units

**Step 2: Calculate total distance**
- Distance = Circumference × Rotations
- Distance = {circumference:.2f} × {rotations} = {distance:.2f} units

**Step 3: Area covered per rotation**
- Area = πr² = π × {r}² = {area_per_rotation:.2f} square units

✅ **Answer:** 
- Distance traveled: **{distance:.2f} units**
- Area covered per rotation: **{area_per_rotation:.2f} square units**
"""
    
    elif problem_type == 'satellite_coverage':
        height = params.get('height', 500)
        earth_radius = 6371
        
        coverage_radius = math.sqrt(height * (height + 2 * earth_radius))
        coverage_area = math.pi * coverage_radius * coverage_radius
        
        return f"""
### 🛰️ Satellite Coverage Problem

**Given:**
- Satellite height: {height} km above Earth
- Earth radius: {earth_radius} km

**Solution using Circle Tangent Properties:**

**Step 1: Calculate coverage radius**
- Using tangent length formula from satellite to Earth's horizon
- Coverage radius = √[h(h + 2R)] where h = height, R = Earth radius
- Coverage radius = √[{height}({height} + 2×{earth_radius})]
- Coverage radius = **{coverage_radius:.2f} km**

**Step 2: Calculate coverage area**
- Coverage area = π × (coverage radius)²
- Coverage area = π × {coverage_radius:.2f}²
- Coverage area = **{coverage_area:.2f} km²**

✅ **Answer:** Satellite covers **{coverage_area:.2f} km²** of Earth's surface.
"""
    
    else:
        return """
### 🌍 Real World Circle Applications

Circle concepts are used in many real-world scenarios:

**1. Transportation**
- Wheel rotation and distance calculation
- Turning radius of vehicles
- Circular tracks and roundabouts

**2. Communication**
- Satellite coverage areas
- Radio transmission ranges
- Antenna radiation patterns

**3. Engineering**
- Gear systems and pulleys
- Circular motion in machinery
- Pipeline bends and curves

**Try asking specific questions like:**
- "Find area covered by wheel with radius 10 rotating 5 times"
- "Calculate satellite coverage from height 500 km"
- "Distance traveled by bicycle wheel radius 30 cm in 100 rotations"
"""

def solve_real_world_with_params(params: Dict[str, Any]) -> str:
    """Solve real world problems with parameters."""
    if solve_real_world_problem:
        problem_type = params.get('type', 'general')
        return solve_real_world_problem(problem_type, params)
    else:
        return solve_real_world("real world application")
