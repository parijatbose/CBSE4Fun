
"""
Tangent Properties for CBSE Class 10 Chapter 10 - Circles
Solvers for tangent-related calculations, theorems, and constructions
"""

# Try to import the solver functions
try:
    from .solver_tangent_length import calculate_tangent_length
except ImportError:
    calculate_tangent_length = None

try:
    from .solver_tangent_theorems import prove_tangent_theorem
except ImportError:
    prove_tangent_theorem = None

try:
    from .solver_tangent_constructions import construct_tangent
except ImportError:
    construct_tangent = None

# Available tangent operations
TANGENT_OPERATIONS = {
    'length_calculation': 'Calculate tangent length from external point',
    'theorem_proof': 'Prove tangent-related theorems',
    'construction': 'Step-by-step tangent constructions',
    'properties': 'Tangent properties and relationships'
}

def solve_tangent_problem(operation_type: str, parameters: dict):
    """
    Main function to solve tangent-related problems
    
    Args:
        operation_type (str): Type of tangent operation
        parameters (dict): Problem parameters
    
    Returns:
        str: Formatted solution
    """
    if operation_type == 'length_calculation' and calculate_tangent_length:
        return calculate_tangent_length(parameters)
    elif operation_type == 'theorem_proof' and prove_tangent_theorem:
        return prove_tangent_theorem(parameters)
    elif operation_type == 'construction' and construct_tangent:
        return construct_tangent(parameters)
    elif operation_type == 'properties':
        # Return general tangent properties
        return """
## 📚 Tangent Properties

**1. Perpendicular Property:**
- The tangent at any point on a circle is perpendicular to the radius through that point.

**2. Equal Tangents Property:**
- Tangents drawn from an external point to a circle are equal in length.

**3. Angle Properties:**
- The angle between a tangent and a chord through the point of contact equals the angle in the alternate segment.
- If two tangents are drawn from an external point, the angle between them is supplementary to the angle subtended by the line joining the points of contact at the center.

**4. Power of a Point:**
- If a line through point P intersects a circle at points A and B, then PA × PB is constant for all such lines.
- If P is external and PT is a tangent, then PT² = PA × PB.

**5. Common Tangents:**
- Two circles can have at most 4 common tangents.
- Number of common tangents depends on the relative positions of the circles.

**6. Tangent-Secant Theorem:**
- If from an external point P, a tangent PT and a secant PAB are drawn to a circle, then PT² = PA × PB.
"""
    else:
        return "❌ The requested operation is not available or the solver module is missing."

def get_tangent_operations():
    """
    Get available tangent operation types
    
    Returns:
        dict: Dictionary of operation types and descriptions
    """
    return TANGENT_OPERATIONS

# Export the functions if they're available
__all__ = ['solve_tangent_problem', 'get_tangent_operations']

if calculate_tangent_length:
    __all__.append('calculate_tangent_length')
if prove_tangent_theorem:
    __all__.append('prove_tangent_theorem')
if construct_tangent:
    __all__.append('construct_tangent')
