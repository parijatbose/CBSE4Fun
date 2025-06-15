import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def interpret_query_polynomial(query: str) -> dict:
    """
    Uses LLM to interpret natural language queries related to polynomials.
    Returns intent + parsed expression.
    """
    prompt = f"""
You are a math query classifier for CBSE Class X Polynomial topics.
Classify the user query into one of the following intents:
- factor_polynomial
- find_zeroes
- construct_quadratic

Return a JSON like:
{{
  "intent": "factor_polynomial",
  "expression": "x^2 + 5x + 6"
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

# Example for testing
if __name__ == "__main__":
    q = "Can you factor x^2 - 3x - 10?"
    print(interpret_query_polynomial(q))
