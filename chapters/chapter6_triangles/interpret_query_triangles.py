import os
import re
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def interpret_query_triangles(query: str) -> dict:
    """
    Uses LLM to interpret natural language queries related to triangles.
    Returns intent + parsed parameters.
    """
    prompt = f"""
You are a math query classifier for CBSE Class X Triangles topics.
Classify the user query into one of the following intents:
- solve_right_triangle (for right triangle problems)
- check_similarity (for checking if triangles are similar)
- calculate_area (for finding area of triangles)
- apply_pythagoras (for Pythagoras theorem problems)
- apply_bpt (for Basic Proportionality Theorem)
- formula_request (when asking for formulas/theorems)

Extract all numerical parameters and their context.

Return a JSON like:
{{
  "intent": "solve_right_triangle",
  "parameters": {{
    "base": 3,
    "height": 4,
    "find": "hypotenuse"
  }}
}}

Query: "{query}"
"""

    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )
        content = response.choices[0].message.content.strip()
        if content.startswith("{"):
            import json
            return json.loads(content)
        else:
            return {"intent": "unknown", "raw_response": content}
    except Exception as e:
        return {"intent": "error", "error": str(e)}

def extract_triangle_measurements(query: str) -> dict:
    """
    Extract triangle measurements from query using regex.
    """
    measurements = {}
    
    # Common patterns for sides
    # Pattern 1: "sides 3, 4, 5" or "sides are 3, 4, 5"
    sides_pattern = r'sides?\s*(?:are\s*)?(\d+(?:\.\d+)?)\s*,\s*(\d+(?:\.\d+)?)\s*,\s*(\d+(?:\.\d+)?)'
    sides_match = re.search(sides_pattern, query, re.IGNORECASE)
    if sides_match:
        measurements['sides'] = [float(sides_match.group(i)) for i in range(1, 4)]
    
    # Pattern 2: Triangle notation like (3,4,5)
    triangle_pattern = r'\((\d+(?:\.\d+)?)\s*,\s*(\d+(?:\.\d+)?)\s*,\s*(\d+(?:\.\d+)?)\)'
    triangles = re.findall(triangle_pattern, query)
    if triangles:
        measurements['triangles'] = [[float(x) for x in t] for t in triangles]
    
    # Pattern for base and height
    base_pattern = r'base[:\s=]+(\d+(?:\.\d+)?)'
    height_pattern = r'height[:\s=]+(\d+(?:\.\d+)?)'
    
    base_match = re.search(base_pattern, query, re.IGNORECASE)
    height_match = re.search(height_pattern, query, re.IGNORECASE)
    
    if base_match:
        measurements['base'] = float(base_match.group(1))
    if height_match:
        measurements['height'] = float(height_match.group(1))
    
    # Pattern for angles
    angle_pattern = r'(\d+(?:\.\d+)?)\s*(?:degree|deg|°)'
    angles = re.findall(angle_pattern, query, re.IGNORECASE)
    if angles:
        measurements['angles'] = [float(a) for a in angles]
    
    # Check for specific terms
    if 'hypotenuse' in query.lower():
        measurements['find'] = 'hypotenuse'
    elif 'area' in query.lower():
        measurements['find'] = 'area'
    elif 'similar' in query.lower():
        measurements['find'] = 'similarity'
    
    return measurements

def parse_triangle_notation(notation: str) -> list:
    """
    Parse triangle notation like ABC or PQR.
    """
    # Remove special characters and spaces
    notation = re.sub(r'[^\w]', '', notation)
    
    # Check if it's a valid triangle notation (3 letters)
    if len(notation) == 3 and notation.isalpha():
        return list(notation.upper())
    elif 'triangle' in notation.lower():
        # Extract letters after 'triangle'
        match = re.search(r'triangle\s*([A-Z]{3})', notation, re.IGNORECASE)
        if match:
            return list(match.group(1).upper())
    
    return None

# Example for testing
if __name__ == "__main__":
    test_queries = [
        "Find hypotenuse of right triangle with base 3 cm and height 4 cm",
        "Check if triangles with sides (3,4,5) and (6,8,10) are similar",
        "Find area of triangle with sides 5, 6, and 7",
        "What is Pythagoras theorem?"
    ]
    
    for q in test_queries:
        print(f"\nQuery: {q}")
        print(f"LLM Result: {interpret_query_triangles(q)}")
        print(f"Regex Extract: {extract_triangle_measurements(q)}")
        print("-" * 50)