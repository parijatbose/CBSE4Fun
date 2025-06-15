# File: chapters/chapter1_real_numbers/main_router.py

import re
import math
from typing import Dict, Any, List, Tuple, Optional

# Import solvers with error handling
try:
    from chapters.chapter1_real_numbers.sub_chapters.hcf_lcm.solver_hcf_lcm import solve_hcf_lcm, explain_hcf_lcm_from_query
except ImportError:
    def solve_hcf_lcm(params):
        return "❌ HCF/LCM solver not available. Check solver_hcf_lcm.py file."
    def explain_hcf_lcm_from_query(query):
        return "❌ HCF/LCM solver not available."

try:
    from chapters.chapter1_real_numbers.sub_chapters.irrationality.solver_irrationality import solve_irrationality_proof, prove_irrationality_from_query
except ImportError:
    def solve_irrationality_proof(params):
        return "❌ Irrationality proof solver not available. Check solver_irrationality.py file."
    def prove_irrationality_from_query(query):
        return "❌ Irrationality proof solver not available."

def route_query(query: str) -> str:
    """
    Main router function for Real Numbers chapter.
    Routes queries to appropriate solvers based on content analysis.
    """
    try:
        if not query or not query.strip():
            return "❌ Please enter a query about real numbers."
        
        query = query.lower().strip()
        
        # Parse the query and determine the type
        query_type, params = parse_real_numbers_query(query)
        
        # Route to appropriate solver
        if query_type == "hcf_lcm":
            return solve_hcf_lcm(params)
        elif query_type == "hcf_only":
            return handle_hcf_only(params)
        elif query_type == "lcm_only":
            return handle_lcm_only(params)
        elif query_type == "irrationality_proof":
            return solve_irrationality_proof(params)
        elif query_type == "prime_factorization":
            return handle_prime_factorization(params)
        elif query_type == "euclidean_algorithm":
            return handle_euclidean_algorithm(params)
        else:
            return generate_help_message(query)
            
    except Exception as e:
        return f"❌ Error processing query: {str(e)}\n\n" + generate_help_message(query)

def parse_real_numbers_query(query: str) -> Tuple[str, Dict[str, Any]]:
    """
    Parse natural language query for real numbers topics.
    """
    query = query.lower().strip()
    
    # Extract numbers from the query
    numbers = extract_numbers(query)
    
    # HCF/LCM patterns
    hcf_lcm_keywords = [
        "hcf and lcm", "lcm and hcf", "highest common factor and least common multiple",
        "gcd and lcm", "both hcf lcm", "find hcf lcm"
    ]
    
    # HCF only patterns
    hcf_keywords = [
        "hcf", "highest common factor", "gcd", "greatest common divisor",
        "common factor", "euclidean algorithm"
    ]
    
    # LCM only patterns
    lcm_keywords = [
        "lcm", "least common multiple", "lowest common multiple", "common multiple"
    ]
    
    # Irrationality patterns
    irrationality_keywords = [
        "irrational", "prove irrational", "show irrational", "is irrational",
        "irrationality proof", "rational or irrational", "√", "root", "square root"
    ]
    
    # Prime factorization patterns
    prime_factorization_keywords = [
        "prime factorization", "prime factors", "factorize", "factor",
        "prime decomposition", "fundamental theorem"
    ]
    
    # Euclidean algorithm patterns
    euclidean_keywords = [
        "euclidean algorithm", "euclidean method", "division algorithm"
    ]
    
    # Determine query type based on keywords
    if any(keyword in query for keyword in hcf_lcm_keywords):
        return "hcf_lcm", {"numbers": numbers}
    
    elif any(keyword in query for keyword in irrationality_keywords):
        # Extract expression for irrationality proof
        expression = extract_irrationality_expression(query)
        return "irrationality_proof", {"expression": expression}
    
    elif any(keyword in query for keyword in euclidean_keywords):
        return "euclidean_algorithm", {"numbers": numbers}
    
    elif any(keyword in query for keyword in hcf_keywords):
        return "hcf_only", {"numbers": numbers}
    
    elif any(keyword in query for keyword in lcm_keywords):
        return "lcm_only", {"numbers": numbers}
    
    elif any(keyword in query for keyword in prime_factorization_keywords):
        return "prime_factorization", {"numbers": numbers}
    
    # Auto-detect based on numbers and context
    elif len(numbers) >= 2:
        if "√" in query or "root" in query:
            return "irrationality_proof", {"expression": query}
        else:
            return "hcf_lcm", {"numbers": numbers}
    elif len(numbers) == 1:
        if "√" in query or "root" in query:
            return "irrationality_proof", {"expression": query}
        else:
            return "prime_factorization", {"numbers": numbers}
    else:
        return "unknown", {}

def extract_numbers(text: str) -> List[float]:
    """Extract all numbers from text."""
    pattern = r'\b\d+\.?\d*\b'
    matches = re.findall(pattern, text)
    return [float(match) for match in matches]

def extract_irrationality_expression(query: str) -> str:
    """Extract the mathematical expression for irrationality proof."""
    # Remove common words but keep mathematical symbols
    expression = re.sub(r'\b(prove|show|that|is|irrational|rational|whether|check|test)\b', '', query)
    expression = expression.strip()
    
    # If empty after cleaning, return original query
    if not expression:
        return query
    
    return expression

def handle_hcf_only(params: Dict[str, Any]) -> str:
    """Handle HCF-only queries."""
    numbers = params.get("numbers", [])
    
    if len(numbers) < 2:
        return "❌ Please provide at least two numbers to find HCF."
    
    # Convert to integers
    int_numbers = [int(num) for num in numbers]
    
    from chapters.chapter1_real_numbers.sub_chapters.hcf_lcm.solver_hcf_lcm import find_hcf_only
    return find_hcf_only(int_numbers)

def handle_lcm_only(params: Dict[str, Any]) -> str:
    """Handle LCM-only queries."""
    numbers = params.get("numbers", [])
    
    if len(numbers) < 2:
        return "❌ Please provide at least two numbers to find LCM."
    
    # Convert to integers
    int_numbers = [int(num) for num in numbers]
    
    from chapters.chapter1_real_numbers.sub_chapters.hcf_lcm.solver_hcf_lcm import find_lcm_only
    return find_lcm_only(int_numbers)

def handle_prime_factorization(params: Dict[str, Any]) -> str:
    """Handle prime factorization queries."""
    numbers = params.get("numbers", [])
    
    if not numbers:
        return "❌ Please provide a number for prime factorization."
    
    num = int(numbers[0])
    
    if num <= 1:
        return "❌ Please provide a number greater than 1 for prime factorization."
    
    from chapters.chapter1_real_numbers.sub_chapters.hcf_lcm.solver_hcf_lcm import prime_factors, format_prime_factors, factor_counter
    
    factors = prime_factors(num)
    factor_count = factor_counter(num)
    
    result = f"""
✅ **Prime Factorization of {num}**

📝 **Step-by-Step Process:**

**Method: Division by Prime Numbers**

• Start with the smallest prime (2) and divide repeatedly
• Move to next prime when current prime no longer divides
• Continue until quotient becomes 1

**Prime Factors:** {factors}

**Standard Form:** {num} = {format_prime_factors(factor_count)}

**Verification:** {' × '.join(map(str, factors))} = {num} ✓

💡 **Fundamental Theorem of Arithmetic:** Every integer greater than 1 has a unique prime factorization.
"""
    
    return result

def handle_euclidean_algorithm(params: Dict[str, Any]) -> str:
    """Handle Euclidean algorithm queries."""
    numbers = params.get("numbers", [])
    
    if len(numbers) < 2:
        return "❌ Please provide two numbers for Euclidean algorithm."
    
    a, b = int(numbers[0]), int(numbers[1])
    
    from chapters.chapter1_real_numbers.sub_chapters.hcf_lcm.solver_hcf_lcm import euclidean_algorithm_steps
    
    return euclidean_algorithm_steps(a, b)

def generate_help_message(original_query: str) -> str:
    """Generate helpful message with examples."""
    return f"""
❓ **I couldn't understand your query: "{original_query}"**

Here are some examples of what you can ask:

🔹 **HCF and LCM:**
• "Find HCF and LCM of 12 and 18"
• "Calculate HCF LCM of 24, 36, 48"
• "What is the HCF of 15 and 25?"
• "Find LCM of 6 and 8"

🔹 **Prime Factorization:**
• "Prime factorization of 60"
• "Find prime factors of 144"
• "Factorize 210"

🔹 **Irrationality Proofs:**
• "Prove √2 is irrational"
• "Show that √3 + 2 is irrational"
• "Is 2√5 rational or irrational?"
• "Prove 1/√3 is irrational"

🔹 **Euclidean Algorithm:**
• "Find HCF of 48 and 18 using Euclidean algorithm"
• "Use division algorithm to find GCD of 56 and 42"

💡 **Tips:**
• Use specific numbers (e.g., "12 and 18", "√2 + 3")
• Be clear about what you want to find
• For irrationality, include the expression clearly

📚 **Chapter 1 Topics Covered:**
• Real Numbers and their classification
• HCF and LCM using prime factorization
• Fundamental Theorem of Arithmetic
• Euclidean Algorithm
• Irrationality proofs using contradiction
"""

# Quick calculation functions for simple queries
def quick_hcf_lcm_calculation(query: str) -> str:
    """Quick calculation for simple HCF/LCM queries."""
    numbers = extract_numbers(query)
    
    if len(numbers) >= 2:
        return explain_hcf_lcm_from_query(query)
    else:
        return "❌ Please provide at least two numbers."

def quick_irrationality_proof(query: str) -> str:
    """Quick irrationality proof for simple expressions."""
    return prove_irrationality_from_query(query)

# Additional utility functions
def classify_number_type(query: str) -> str:
    """Classify if a number is rational or irrational."""
    
    # Extract potential mathematical expressions
    if "√" in query or "root" in query:
        return quick_irrationality_proof(query)
    
    numbers = extract_numbers(query)
    if numbers:
        num = numbers[0]
        if num.is_integer():
            return f"✅ {int(num)} is a **rational number** (it's an integer)."
        else:
            return f"✅ {num} is a **rational number** (it's a terminating decimal)."
    
    return "❌ Could not determine the type of number from your query."

def explain_fundamental_theorem() -> str:
    """Explain the Fundamental Theorem of Arithmetic."""
    return """
📚 **Fundamental Theorem of Arithmetic**

🎯 **Statement:** Every integer greater than 1 either is prime itself or is the product of prime numbers, and this product is unique, up to the order of the factors.

📝 **Key Points:**
• Every composite number can be expressed as a product of primes
• This factorization is unique (except for the order of factors)
• This theorem is the foundation for finding HCF and LCM

💡 **Applications:**
• Finding HCF using smallest powers of common primes
• Finding LCM using greatest powers of all primes
• Proving irrationality of certain square roots
• Number theory and cryptography

**Example:**
60 = 2² × 3 × 5 (unique prime factorization)
"""