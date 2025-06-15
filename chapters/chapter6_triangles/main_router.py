# File: chapters/chapter6_triangles/main_router.py

import re
import math
from typing import Dict, Any, List, Tuple, Optional

# Import your solvers with CORRECT paths and error handling
try:
    from chapters.chapter6_triangles.sub_chapters.right_triangle.solver_right_triangle import solve_right_triangle
except ImportError:
    def solve_right_triangle(params):
        return "❌ Right triangle solver not available. Check solver_right_triangle.py file."

try:
    from chapters.chapter6_triangles.sub_chapters.similar_triangles.solver_similar import solve_similar_triangles
    # Try to also import the similarity check function
    try:
        from chapters.chapter6_triangles.sub_chapters.similar_triangles.solver_similar import check_similarity_sss
    except ImportError:
        def check_similarity_sss(triangle1, triangle2):
            return check_similarity_sss_inline(triangle1, triangle2)
except ImportError:
    def solve_similar_triangles(params):
        return "❌ Similar triangles solver not available. Check solver_similar.py file."
    def check_similarity_sss(triangle1, triangle2):
        return check_similarity_sss_inline(triangle1, triangle2)

try:
    from chapters.chapter6_triangles.sub_chapters.basic_proportionality.solver_bpt import solve_bpt
except ImportError:
    def solve_bpt(params):
        return "❌ BPT solver not available. Check solver_bpt.py file."

try:
    from chapters.chapter6_triangles.interpret_query_triangles import interpret_query_triangles, extract_triangle_measurements
except ImportError:
    def interpret_query_triangles(query):
        return {"intent": "error", "error": "LLM interpreter not available"}
    def extract_triangle_measurements(query):
        return {}

def route_query(query: str) -> str:
    """
    Main router function that parses natural language queries 
    and routes them to appropriate triangle solvers.
    """
    try:
        if not query or not query.strip():
            return "❌ Please enter a query about triangles."
        
        query = query.lower().strip()
        
        # First try using your existing LLM interpreter
        try:
            llm_result = interpret_query_triangles(query)
            if llm_result.get("intent") != "error" and llm_result.get("intent") != "unknown":
                return route_by_intent(llm_result)
        except:
            # Fall back to regex parsing if LLM fails
            pass
        
        # Fallback: Parse the query and determine the type using regex
        query_type, params = parse_triangle_query(query)
        
        # Route to appropriate solver
        if query_type == "right_triangle":
            return solve_right_triangle(params)
        elif query_type == "similar_triangles":
            return solve_similar_triangles(params)
        elif query_type == "similarity_check":
            # Try to use the similarity check function if available
            try:
                return check_similarity_sss(params.get('triangle1', []), params.get('triangle2', []))
            except:
                # Fallback to inline similarity check
                return check_similarity_sss_inline(params.get('triangle1', []), params.get('triangle2', []))
        elif query_type == "bpt":
            return solve_bpt(params)
        elif query_type == "area":
            return calculate_triangle_area(params)
        elif query_type == "angles":
            return calculate_triangle_angles_from_sides(params)
        else:
            return generate_help_message(query)
            
    except Exception as e:
        return f"❌ Error processing query: {str(e)}\n\n" + generate_help_message(query)

def route_by_intent(llm_result: dict) -> str:
    """Route based on LLM interpretation."""
    intent = llm_result.get("intent")
    params = llm_result.get("parameters", {})
    
    if intent == "solve_right_triangle":
        return solve_right_triangle(params)
    elif intent == "check_similarity":
        # Convert parameters to expected format
        if "triangle1" in params and "triangle2" in params:
            try:
                return check_similarity_sss(params["triangle1"], params["triangle2"])
            except:
                return check_similarity_sss_inline(params["triangle1"], params["triangle2"])
        else:
            return "❌ Need two triangles to check similarity"
    elif intent == "calculate_area":
        return calculate_triangle_area(params)
    elif intent == "apply_bpt":
        return solve_bpt(params)
    else:
        return generate_help_message(str(llm_result))

def parse_triangle_query(query: str) -> Tuple[str, Dict[str, Any]]:
    """
    Parse natural language query and extract parameters using regex.
    """
    query = query.lower().strip()
    
    # Use your existing extraction function
    measurements = extract_triangle_measurements(query)
    
    # Extract numbers from the query
    numbers = extract_numbers(query)
    
    # Right triangle patterns
    right_triangle_keywords = [
        "right triangle", "hypotenuse", "pythagorean", 
        "base and height", "90 degree", "right angle"
    ]
    
    # Similar triangles patterns
    similar_keywords = [
        "similar", "similarity", "check if", "are triangles similar",
        "similar triangles", "proportional"
    ]
    
    # BPT patterns
    bpt_keywords = [
        "bpt", "basic proportionality", "thales", "parallel", 
        "proportional segments", "divides proportionally"
    ]
    
    # Area patterns
    area_keywords = [
        "area", "heron", "heron's formula", "find area"
    ]
    
    # Angle patterns
    angle_keywords = [
        "angles", "find angles", "calculate angles", "angle"
    ]
    
    # Determine query type and extract parameters
    if any(keyword in query for keyword in right_triangle_keywords):
        return "right_triangle", parse_right_triangle_params(query, numbers, measurements)
    
    elif any(keyword in query for keyword in similar_keywords):
        if "check" in query or "are" in query:
            return "similarity_check", parse_similarity_check_params(query, numbers, measurements)
        else:
            return "similar_triangles", parse_similarity_check_params(query, numbers, measurements)
    
    elif any(keyword in query for keyword in bpt_keywords):
        return "bpt", parse_bpt_params(query, numbers)
    
    elif any(keyword in query for keyword in area_keywords):
        return "area", parse_area_params(query, numbers, measurements)
    
    elif any(keyword in query for keyword in angle_keywords):
        return "angles", parse_angle_params(query, numbers, measurements)
    
    # Auto-detect based on numbers provided
    elif len(numbers) >= 2:
        return auto_detect_query_type(query, numbers)
    
    else:
        return "unknown", {}

def extract_numbers(text: str) -> List[float]:
    """Extract all numbers from text."""
    # Pattern to match integers and decimals
    pattern = r'\b\d+\.?\d*\b'
    matches = re.findall(pattern, text)
    return [float(match) for match in matches]

def parse_right_triangle_params(query: str, numbers: List[float], measurements: dict) -> Dict[str, Any]:
    """Parse parameters for right triangle problems."""
    params = {}
    
    # Use measurements from your existing function first
    if "base" in measurements:
        params["base"] = measurements["base"]
    if "height" in measurements:
        params["height"] = measurements["height"]
    
    # Fallback to positional parsing
    if "base" in query and "height" in query and len(numbers) >= 2:
        if "base" not in params:
            params["base"] = numbers[0]
        if "height" not in params:
            params["height"] = numbers[1]
    elif "hypotenuse" in query and len(numbers) >= 2:
        if "base" in query:
            params["hypotenuse"] = numbers[0]
            params["base"] = numbers[1]
        elif "height" in query:
            params["hypotenuse"] = numbers[0]
            params["height"] = numbers[1]
        else:
            params["hypotenuse"] = numbers[0]
            params["angle"] = numbers[1]
    elif len(numbers) == 2:
        # Default: assume base and height
        params["base"] = numbers[0]
        params["height"] = numbers[1]
    
    return params

def parse_similarity_check_params(query: str, numbers: List[float], measurements: dict) -> Dict[str, Any]:
    """Parse parameters for similarity check."""
    
    # Use your existing measurements extraction
    if "triangles" in measurements and len(measurements["triangles"]) >= 2:
        return {
            "triangle1": measurements["triangles"][0],
            "triangle2": measurements["triangles"][1]
        }
    
    if len(numbers) >= 6:
        return {
            "triangle1": numbers[:3],
            "triangle2": numbers[3:6]
        }
    else:
        # Look for patterns like (3,4,5) and (6,8,10)
        pattern = r'\(([^)]+)\)'
        matches = re.findall(pattern, query)
        if len(matches) >= 2:
            try:
                triangle1 = [float(x.strip()) for x in matches[0].split(',')]
                triangle2 = [float(x.strip()) for x in matches[1].split(',')]
                return {"triangle1": triangle1, "triangle2": triangle2}
            except:
                pass
        
        return {"triangle1": [], "triangle2": []}

def parse_bpt_params(query: str, numbers: List[float]) -> Dict[str, Any]:
    """Parse parameters for BPT problems."""
    return {
        "type": "verify_parallel",
        "segments": numbers[:4] if len(numbers) >= 4 else numbers
    }

def parse_area_params(query: str, numbers: List[float], measurements: dict) -> Dict[str, Any]:
    """Parse parameters for area calculations."""
    
    # Use existing measurements first
    if "sides" in measurements:
        return {"sides": measurements["sides"]}
    elif "base" in measurements and "height" in measurements:
        return {"base": measurements["base"], "height": measurements["height"]}
    
    # Fallback to positional
    if len(numbers) >= 3:
        return {"sides": numbers[:3]}
    elif len(numbers) == 2:
        return {"base": numbers[0], "height": numbers[1]}
    else:
        return {"sides": numbers}

def parse_angle_params(query: str, numbers: List[float], measurements: dict) -> Dict[str, Any]:
    """Parse parameters for angle calculations."""
    
    # Use existing measurements first
    if "sides" in measurements:
        return {"sides": measurements["sides"]}
    
    if len(numbers) >= 3:
        return {"sides": numbers[:3]}
    else:
        return {"sides": numbers}

def auto_detect_query_type(query: str, numbers: List[float]) -> Tuple[str, Dict[str, Any]]:
    """Auto-detect query type based on context and numbers."""
    if len(numbers) == 2:
        return "right_triangle", {"base": numbers[0], "height": numbers[1]}
    elif len(numbers) == 3:
        return "area", {"sides": numbers}
    elif len(numbers) == 6:
        return "similarity_check", {
            "triangle1": numbers[:3], 
            "triangle2": numbers[3:]
        }
    else:
        return "unknown", {}

def calculate_triangle_area(params: Dict[str, Any]) -> str:
    """Calculate triangle area using different methods."""
    try:
        if "sides" in params and len(params["sides"]) >= 3:
            # Use Heron's formula
            a, b, c = params["sides"][:3]
            
            # Check if triangle is valid
            if not (a + b > c and b + c > a and a + c > b):
                return "❌ Invalid triangle! The sum of any two sides must be greater than the third side."
            
            # Calculate semi-perimeter
            s = (a + b + c) / 2
            
            # Heron's formula
            area = math.sqrt(s * (s - a) * (s - b) * (s - c))
            
            return f"""
✅ **Triangle Area Calculation (Heron's Formula):**

Given sides:
• a = {a} cm
• b = {b} cm  
• c = {c} cm

📝 **Step-by-Step Calculation:**

1. **Semi-perimeter (s):**
   • s = (a + b + c) / 2
   • s = ({a} + {b} + {c}) / 2
   • s = {a + b + c} / 2
   • s = {s} cm

2. **Heron's Formula:**
   • Area = √[s(s-a)(s-b)(s-c)]
   • Area = √[{s} × ({s}-{a}) × ({s}-{b}) × ({s}-{c})]
   • Area = √[{s} × {s-a} × {s-b} × {s-c}]
   • Area = √{s * (s-a) * (s-b) * (s-c)}
   • Area = **{area:.2f} cm²**

💡 **Additional Information:**
• Perimeter = {a + b + c} cm
• This triangle is {'right-angled' if abs(a**2 + b**2 - c**2) < 0.001 or abs(b**2 + c**2 - a**2) < 0.001 or abs(a**2 + c**2 - b**2) < 0.001 else 'not right-angled'}
"""
        
        elif "base" in params and "height" in params:
            # Use base × height / 2
            base = params["base"]
            height = params["height"]
            area = 0.5 * base * height
            
            return f"""
✅ **Triangle Area Calculation (Base × Height):**

Given:
• Base = {base} cm
• Height = {height} cm

📝 **Calculation:**
• Area = ½ × base × height
• Area = ½ × {base} × {height}
• Area = **{area:.2f} cm²**
"""
        
        else:
            return "❌ Insufficient data for area calculation. Need either 3 sides or base and height."
            
    except Exception as e:
        return f"❌ Error calculating area: {str(e)}"

def calculate_triangle_angles_from_sides(params: Dict[str, Any]) -> str:
    """Calculate all angles of a triangle from its sides."""
    try:
        if "sides" not in params or len(params["sides"]) < 3:
            return "❌ Need all three sides to calculate angles."
        
        a, b, c = params["sides"][:3]
        
        # Check if triangle is valid
        if not (a + b > c and b + c > a and a + c > b):
            return "❌ Invalid triangle! The sum of any two sides must be greater than the third side."
        
        # Use law of cosines to find angles
        # cos(A) = (b² + c² - a²) / (2bc)
        cos_A = (b**2 + c**2 - a**2) / (2 * b * c)
        cos_B = (a**2 + c**2 - b**2) / (2 * a * c)
        cos_C = (a**2 + b**2 - c**2) / (2 * a * b)
        
        # Convert to degrees
        angle_A = math.degrees(math.acos(max(-1, min(1, cos_A))))
        angle_B = math.degrees(math.acos(max(-1, min(1, cos_B))))
        angle_C = math.degrees(math.acos(max(-1, min(1, cos_C))))
        
        return f"""
✅ **Triangle Angles Calculation (Law of Cosines):**

Given sides:
• a = {a} cm (opposite to angle A)
• b = {b} cm (opposite to angle B)
• c = {c} cm (opposite to angle C)

📝 **Step-by-Step Calculation:**

1. **Angle A:**
   • cos(A) = (b² + c² - a²) / (2bc)
   • cos(A) = ({b}² + {c}² - {a}²) / (2 × {b} × {c})
   • cos(A) = ({b**2} + {c**2} - {a**2}) / {2*b*c}
   • cos(A) = {b**2 + c**2 - a**2} / {2*b*c}
   • cos(A) = {cos_A:.4f}
   • A = **{angle_A:.1f}°**

2. **Angle B:**
   • cos(B) = (a² + c² - b²) / (2ac)
   • B = **{angle_B:.1f}°**

3. **Angle C:**
   • cos(C) = (a² + b² - c²) / (2ab)
   • C = **{angle_C:.1f}°**

✅ **Verification:**
• Sum of angles = {angle_A:.1f}° + {angle_B:.1f}° + {angle_C:.1f}° = {angle_A + angle_B + angle_C:.1f}°
• Should equal 180° ✓

💡 **Triangle Type:**
• This is a {'right-angled' if abs(max(angle_A, angle_B, angle_C) - 90) < 0.1 else 'acute' if max(angle_A, angle_B, angle_C) < 90 else 'obtuse'} triangle
"""
        
    except Exception as e:
        return f"❌ Error calculating angles: {str(e)}"

def check_similarity_sss_inline(triangle1: List[float], triangle2: List[float]) -> str:
    """
    Check if two triangles are similar using SSS criterion.
    """
    if len(triangle1) != 3 or len(triangle2) != 3:
        return "❌ Each triangle must have exactly 3 sides"
    
    if not triangle1 or not triangle2:
        return "❌ Please provide valid triangle sides"
    
    # Sort sides to match corresponding sides
    a1, b1, c1 = sorted(triangle1)
    a2, b2, c2 = sorted(triangle2)
    
    # Calculate ratios
    ratio_a = a2 / a1
    ratio_b = b2 / b1
    ratio_c = c2 / c1
    
    # Check if all ratios are equal (within tolerance)
    tolerance = 0.001
    is_similar = (abs(ratio_a - ratio_b) < tolerance and 
                  abs(ratio_b - ratio_c) < tolerance and 
                  abs(ratio_a - ratio_c) < tolerance)
    
    result = f"""
✅ **Similar Triangles Check (SSS Criterion):**

**Triangle 1:** Sides = {triangle1[0]}, {triangle1[1]}, {triangle1[2]} cm
**Triangle 2:** Sides = {triangle2[0]}, {triangle2[1]}, {triangle2[2]} cm

📝 **Step-by-Step Analysis:**

**1. Sorting sides (smallest to largest):**
   • Triangle 1: {a1}, {b1}, {c1}
   • Triangle 2: {a2}, {b2}, {c2}

**2. Calculating ratios of corresponding sides:**
   • Ratio 1: {a2}/{a1} = {ratio_a:.3f}
   • Ratio 2: {b2}/{b1} = {ratio_b:.3f}
   • Ratio 3: {c2}/{c1} = {ratio_c:.3f}

**3. Checking if all ratios are equal:**
   • Difference between ratios: {abs(ratio_a - ratio_b):.6f}, {abs(ratio_b - ratio_c):.6f}, {abs(ratio_a - ratio_c):.6f}
   • All differences < 0.001? {'YES ✓' if is_similar else 'NO ✗'}

💡 **Conclusion:**
{'✅ The triangles ARE SIMILAR by SSS criterion!' if is_similar else '❌ The triangles are NOT SIMILAR'}
{f'• Scale factor (ratio) = {ratio_a:.3f}' if is_similar else '• Ratios are not equal'}
{f'• Corresponding angles are equal' if is_similar else '• Corresponding angles may differ'}
"""
    
    return result

def generate_help_message(original_query: str) -> str:
    """Generate helpful message with examples."""
    return f"""
❓ **I couldn't understand your query: "{original_query}"**

Here are some examples of what you can ask:

🔹 **Right Triangles:**
• "Find hypotenuse of right triangle with base 3 cm and height 4 cm"
• "Right triangle with hypotenuse 10 cm and angle 30 degrees"

🔹 **Similar Triangles:**
• "Check if triangles with sides (3,4,5) and (6,8,10) are similar"
• "Are triangles with sides 5,6,7 and 10,12,14 similar?"

🔹 **Triangle Area:**
• "Find area of triangle with sides 5 cm, 6 cm, and 7 cm"
• "Calculate area with base 8 cm and height 6 cm"

🔹 **Triangle Angles:**
• "Find angles of triangle with sides 3, 4, 5"
• "Calculate all angles for sides 7, 8, 9"

🔹 **BPT (Basic Proportionality Theorem):**
• "BPT with segments 4, 6, 8, 12"
• "Check if line is parallel using segments 3, 6, 4, 8"

💡 **Tips:**
• Use specific numbers (e.g., "3 cm", "5.5", "10")
• Include units when possible
• Be specific about what you want to find
"""