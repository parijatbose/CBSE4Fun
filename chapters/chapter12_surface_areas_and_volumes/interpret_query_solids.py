import os
import re
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def interpret_query_solids(query: str) -> dict:
    """
    Uses LLM to interpret natural language queries related to surface areas and volumes.
    Returns intent + parsed parameters.
    """
    prompt = f"""
You are a math query classifier for CBSE Class X Surface Areas and Volumes topics.
Classify the user query into one of the following intents:
- solve_cylinder (for cylinder volume/surface area problems)
- solve_cone (for cone volume/surface area problems)
- solve_sphere (for sphere/hemisphere problems)
- solve_cuboid (for cuboid/cube problems)
- solve_combined (for combined solids like cone on hemisphere)
- formula_request (when asking for formulas)
- conversion (for unit conversions)

Extract all numerical parameters with their units.

Return a JSON like:
{{
  "intent": "solve_cylinder",
  "parameters": {{
    "radius": 7,
    "height": 10,
    "unit": "cm",
    "find": "volume"
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

def extract_measurements(query: str) -> dict:
    """
    Extract numerical measurements from query using regex.
    """
    measurements = {}
    
    # Common patterns
    patterns = {
        'radius': r'radius[:\s]+(\d+(?:\.\d+)?)\s*(\w+)?',
        'height': r'height[:\s]+(\d+(?:\.\d+)?)\s*(\w+)?',
        'length': r'length[:\s]+(\d+(?:\.\d+)?)\s*(\w+)?',
        'breadth': r'breadth[:\s]+(\d+(?:\.\d+)?)\s*(\w+)?',
        'width': r'width[:\s]+(\d+(?:\.\d+)?)\s*(\w+)?',
        'side': r'side[:\s]+(\d+(?:\.\d+)?)\s*(\w+)?',
        'edge': r'edge[:\s]+(\d+(?:\.\d+)?)\s*(\w+)?',
        'diameter': r'diameter[:\s]+(\d+(?:\.\d+)?)\s*(\w+)?',
        'slant_height': r'slant\s*height[:\s]+(\d+(?:\.\d+)?)\s*(\w+)?'
    }
    
    for key, pattern in patterns.items():
        match = re.search(pattern, query, re.IGNORECASE)
        if match:
            measurements[key] = {
                'value': float(match.group(1)),
                'unit': match.group(2) if match.group(2) else 'cm'
            }
    
    return measurements

# Example for testing
if __name__ == "__main__":
    queries = [
        "Find volume of cylinder with radius 7 cm and height 10 cm",
        "Calculate surface area of cone with radius 5 and height 12",
        "What is the formula for volume of sphere?"
    ]
    
    for q in queries:
        print(f"Query: {q}")
        print(f"LLM Result: {interpret_query_solids(q)}")
        print(f"Regex Extract: {extract_measurements(q)}")
        print("-" * 50)