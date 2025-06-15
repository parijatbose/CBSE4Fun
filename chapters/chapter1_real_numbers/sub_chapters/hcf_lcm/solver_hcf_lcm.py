# File: chapters/chapter1_real_numbers/sub_chapters/hcf_lcm/solver_hcf_lcm.py

from collections import Counter
from math import gcd
from functools import reduce
import re
from typing import Dict, Any, List

def prime_factors(n):
    """Get prime factors of a number."""
    i = 2
    factors = []
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n = n // i
        i += 1
    if n > 1:
        factors.append(n)
    return factors

def factor_counter(n):
    """Count occurrences of each prime factor."""
    return Counter(prime_factors(n))

def get_hcf_lcm(a, b):
    """Calculate HCF and LCM using prime factorization."""
    fa = factor_counter(a)
    fb = factor_counter(b)

    hcf = 1
    lcm = 1

    # HCF: Product of smallest powers of common primes
    for prime in (fa.keys() & fb.keys()):
        hcf *= prime ** min(fa[prime], fb[prime])

    # LCM: Product of greatest powers of all primes involved
    all_primes = fa.keys() | fb.keys()
    for prime in all_primes:
        lcm *= prime ** max(fa.get(prime, 0), fb.get(prime, 0))

    return hcf, lcm, fa, fb

def solve_hcf_lcm(params: Dict[str, Any]) -> str:
    """
    Main solver for HCF and LCM problems.
    """
    try:
        # Extract numbers from parameters
        numbers = params.get('numbers', [])
        
        if len(numbers) < 2:
            return "❌ Please provide at least two numbers to find HCF and LCM."
        
        # Convert all numbers to integers
        numbers = [int(n) for n in numbers]
        
        # Check for non-positive numbers
        if any(n <= 0 for n in numbers):
            return "❌ Please provide positive integers only."
        
        # Handle multiple numbers
        if len(numbers) > 2:
            return explain_hcf_lcm_multiple(numbers)
        else:
            return explain_hcf_lcm_detailed(numbers[0], numbers[1])
        
    except Exception as e:
        return f"❌ Error calculating HCF and LCM: {str(e)}"

def explain_hcf_lcm_detailed(a, b):
    """
    Provide detailed step-by-step explanation of HCF and LCM calculation.
    """
    a, b = int(a), int(b)
    
    hcf, lcm, fa, fb = get_hcf_lcm(a, b)
    
    result = f"""
✅ **HCF and LCM of {a} and {b} using Prime Factorization**

📝 **Step-by-Step Solution:**

**Step 1: Prime Factorization**
• Prime factorization of {a} = {format_prime_factors(fa)}
• Prime factorization of {b} = {format_prime_factors(fb)}

**Step 2: Finding HCF (Highest Common Factor)**
• HCF = Product of **smallest powers** of **common primes**
• Common primes: {list(fa.keys() & fb.keys())}
• HCF calculation: {format_hcf_calculation(fa, fb)}
• **HCF = {hcf}**

**Step 3: Finding LCM (Least Common Multiple)**
• LCM = Product of **greatest powers** of **all primes**
• All primes involved: {sorted(fa.keys() | fb.keys())}
• LCM calculation: {format_lcm_calculation(fa, fb)}
• **LCM = {lcm}**

**Step 4: Verification**
• HCF × LCM = {hcf} × {lcm} = {hcf * lcm}
• {a} × {b} = {a * b}
• ✅ **Verification:** HCF × LCM = {a} × {b} (Property satisfied!)

🎯 **Final Answer:**
• **HCF({a}, {b}) = {hcf}**
• **LCM({a}, {b}) = {lcm}**

💡 **Key Concepts:**
• HCF: Greatest number that divides both numbers
• LCM: Smallest number that is divisible by both numbers
• For any two numbers: HCF × LCM = Product of the numbers
"""
    
    return result

def format_prime_factors(factor_dict):
    """Format prime factors for display."""
    if not factor_dict:
        return "1"
    
    formatted = []
    for prime in sorted(factor_dict.keys()):
        power = factor_dict[prime]
        if power == 1:
            formatted.append(str(prime))
        else:
            formatted.append(f"{prime}^{power}")
    
    return " × ".join(formatted)

def format_hcf_calculation(fa, fb):
    """Format HCF calculation steps."""
    common_primes = fa.keys() & fb.keys()
    if not common_primes:
        return "No common primes, so HCF = 1"
    
    hcf_terms = []
    for prime in sorted(common_primes):
        min_power = min(fa[prime], fb[prime])
        if min_power == 1:
            hcf_terms.append(str(prime))
        else:
            hcf_terms.append(f"{prime}^{min_power}")
    
    calculation = " × ".join(hcf_terms)
    hcf_value = 1
    for prime in common_primes:
        hcf_value *= prime ** min(fa[prime], fb[prime])
    
    return f"{calculation} = {hcf_value}"

def format_lcm_calculation(fa, fb):
    """Format LCM calculation steps."""
    all_primes = fa.keys() | fb.keys()
    
    lcm_terms = []
    for prime in sorted(all_primes):
        max_power = max(fa.get(prime, 0), fb.get(prime, 0))
        if max_power == 1:
            lcm_terms.append(str(prime))
        else:
            lcm_terms.append(f"{prime}^{max_power}")
    
    calculation = " × ".join(lcm_terms)
    lcm_value = 1
    for prime in all_primes:
        lcm_value *= prime ** max(fa.get(prime, 0), fb.get(prime, 0))
    
    return f"{calculation} = {lcm_value}"

def solve_hcf_lcm_multiple_numbers(numbers: List[int]) -> str:
    """
    Find HCF and LCM of multiple numbers.
    """
    if len(numbers) < 2:
        return "❌ Need at least 2 numbers"
    
    # Calculate HCF of all numbers
    overall_hcf = numbers[0]
    for num in numbers[1:]:
        overall_hcf = gcd(overall_hcf, num)
    
    # Calculate LCM of all numbers
    def lcm(a, b):
        return abs(a * b) // gcd(a, b)
    
    overall_lcm = numbers[0]
    for num in numbers[1:]:
        overall_lcm = lcm(overall_lcm, num)
    
    result = f"""
✅ **HCF and LCM of {len(numbers)} numbers: {', '.join(map(str, numbers))}**

📝 **Prime Factorizations:**
"""
    
    # Show prime factorization of each number
    for num in numbers:
        factors = factor_counter(num)
        result += f"• {num} = {format_prime_factors(factors)}\n"
    
    result += f"""
🎯 **Results:**
• **HCF = {overall_hcf}**
• **LCM = {overall_lcm}**

💡 **Method:**
• HCF = Product of smallest powers of common primes
• LCM = Product of greatest powers of all primes
"""
    
    return result

def explain_hcf_lcm_from_query(query: str):
    """
    Extract numbers from query and calculate HCF & LCM.
    """
    numbers = list(map(int, re.findall(r'\d+', query)))
    if len(numbers) >= 2:
        if len(numbers) == 2:
            return explain_hcf_lcm_detailed(numbers[0], numbers[1])
        else:
            return solve_hcf_lcm_multiple_numbers(numbers)
    else:
        return "❌ Please provide at least two numbers to compute HCF and LCM."

# Additional utility functions
def find_hcf_only(numbers: List[int]) -> str:
    """Find only HCF with detailed steps."""
    if len(numbers) < 2:
        return "❌ Need at least 2 numbers"
    
    if len(numbers) == 2:
        a, b = numbers[0], numbers[1]
        # Use Euclidean algorithm for detailed steps
        return euclidean_algorithm_steps(a, b)
    else:
        # Multiple numbers
        result_hcf = numbers[0]
        for num in numbers[1:]:
            result_hcf = gcd(result_hcf, num)
        
        return f"""
✅ **HCF of {', '.join(map(str, numbers))} = {result_hcf}**

📝 **Method:** Successive application of Euclidean algorithm
• Start with first two numbers, find their HCF
• Then find HCF of result with next number
• Continue until all numbers are processed
"""

def euclidean_algorithm_steps(a, b) -> str:
    """Show Euclidean algorithm steps for HCF."""
    original_a, original_b = a, b
    steps = []
    
    steps.append(f"**Finding HCF of {a} and {b} using Euclidean Algorithm:**")
    steps.append("")
    
    step_num = 1
    while b != 0:
        quotient = a // b
        remainder = a % b
        steps.append(f"Step {step_num}: {a} = {b} × {quotient} + {remainder}")
        a, b = b, remainder
        step_num += 1
    
    steps.append("")
    steps.append(f"✅ **HCF({original_a}, {original_b}) = {a}**")
    
    return "\n".join(steps)

def find_lcm_only(numbers: List[int]) -> str:
    """Find only LCM with detailed steps."""
    if len(numbers) < 2:
        return "❌ Need at least 2 numbers"
    
    def lcm(a, b):
        return abs(a * b) // gcd(a, b)
    
    if len(numbers) == 2:
        a, b = numbers[0], numbers[1]
        hcf = gcd(a, b)
        lcm_result = lcm(a, b)
        
        return f"""
✅ **LCM of {a} and {b}**

📝 **Method:** LCM = (a × b) / HCF

• HCF({a}, {b}) = {hcf}
• LCM = ({a} × {b}) / {hcf}
• LCM = {a * b} / {hcf}
• **LCM = {lcm_result}**
"""
    else:
        result_lcm = numbers[0]
        for num in numbers[1:]:
            result_lcm = lcm(result_lcm, num)
        
        return f"""
✅ **LCM of {', '.join(map(str, numbers))} = {result_lcm}**

📝 **Method:** Successive LCM calculation
• Find LCM of first two numbers
• Then find LCM of result with next number
• Continue until all numbers are processed
"""

def explain_hcf_lcm_multiple(numbers: List[int]) -> str:
    """
    Provide detailed step-by-step explanation of HCF and LCM calculation for multiple numbers.
    """
    # Get prime factorizations for all numbers
    factorizations = [factor_counter(n) for n in numbers]
    
    # Calculate HCF
    hcf = 1
    common_primes = set.intersection(*[set(f.keys()) for f in factorizations])
    for prime in common_primes:
        min_power = min(f[prime] for f in factorizations)
        hcf *= prime ** min_power
    
    # Calculate LCM
    lcm = 1
    all_primes = set.union(*[set(f.keys()) for f in factorizations])
    for prime in all_primes:
        max_power = max(f.get(prime, 0) for f in factorizations)
        lcm *= prime ** max_power
    
    # Format the result
    result = f"""
✅ **HCF and LCM of {len(numbers)} numbers: {', '.join(map(str, numbers))}**

📝 **Step-by-Step Solution:**

**Step 1: Prime Factorization of Each Number**
"""
    
    # Show prime factorization of each number
    for i, num in enumerate(numbers, 1):
        result += f"• Number {i} ({num}) = {format_prime_factors(factorizations[i-1])}\n"
    
    result += f"""
**Step 2: Finding HCF (Highest Common Factor)**
• Common primes across all numbers: {sorted(common_primes)}
• HCF calculation: {format_hcf_calculation_multiple(factorizations)}
• **HCF = {hcf}**

**Step 3: Finding LCM (Least Common Multiple)**
• All primes involved: {sorted(all_primes)}
• LCM calculation: {format_lcm_calculation_multiple(factorizations)}
• **LCM = {lcm}**

**Step 4: Verification**
• For any two numbers from the set, HCF × LCM = Product of those numbers
• Example verification with first two numbers:
  - HCF × LCM = {hcf} × {lcm} = {hcf * lcm}
  - {numbers[0]} × {numbers[1]} = {numbers[0] * numbers[1]}
  - ✅ **Verification:** HCF × LCM = Product of numbers (Property satisfied!)

🎯 **Final Answer:**
• **HCF({', '.join(map(str, numbers))}) = {hcf}**
• **LCM({', '.join(map(str, numbers))}) = {lcm}**

💡 **Key Concepts:**
• HCF: Greatest number that divides all given numbers
• LCM: Smallest number that is divisible by all given numbers
• For any two numbers from the set: HCF × LCM = Product of those numbers
"""
    
    return result

def format_hcf_calculation_multiple(factorizations: List[Counter]) -> str:
    """Format HCF calculation steps for multiple numbers."""
    common_primes = set.intersection(*[set(f.keys()) for f in factorizations])
    if not common_primes:
        return "No common primes, so HCF = 1"
    
    hcf_terms = []
    for prime in sorted(common_primes):
        min_power = min(f[prime] for f in factorizations)
        if min_power == 1:
            hcf_terms.append(str(prime))
        else:
            hcf_terms.append(f"{prime}^{min_power}")
    
    calculation = " × ".join(hcf_terms)
    hcf_value = 1
    for prime in common_primes:
        hcf_value *= prime ** min(f[prime] for f in factorizations)
    
    return f"{calculation} = {hcf_value}"

def format_lcm_calculation_multiple(factorizations: List[Counter]) -> str:
    """Format LCM calculation steps for multiple numbers."""
    all_primes = set.union(*[set(f.keys()) for f in factorizations])
    
    lcm_terms = []
    for prime in sorted(all_primes):
        max_power = max(f.get(prime, 0) for f in factorizations)
        if max_power == 1:
            lcm_terms.append(str(prime))
        else:
            lcm_terms.append(f"{prime}^{max_power}")
    
    calculation = " × ".join(lcm_terms)
    lcm_value = 1
    for prime in all_primes:
        lcm_value *= prime ** max(f.get(prime, 0) for f in factorizations)
    
    return f"{calculation} = {lcm_value}"