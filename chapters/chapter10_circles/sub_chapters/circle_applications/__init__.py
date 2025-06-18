"""
Circle Applications for CBSE Class 10 Chapter 10 - Circles
Real-world problem solvers for circle-related applications
"""

# Try to import the solver function
try:
    from .solver_real_world import solve_real_world_problem
except ImportError:
    solve_real_world_problem = None

# Available application types
APPLICATION_TYPES = {
    'area_coverage': 'Calculate area covered by circular regions',
    'wheel_rotation': 'Solve wheel rotation and distance problems',
    'satellite_coverage': 'Calculate satellite coverage area',
    'circular_track': 'Problems related to circular tracks and paths',
    'sprinkler_coverage': 'Irrigation and sprinkler system coverage',
    'general': 'General circle applications overview'
}

def get_application_types():
    """
    Get available application problem types
    
    Returns:
        dict: Dictionary of application types and descriptions
    """
    return APPLICATION_TYPES

def solve_application(problem_type: str, parameters: dict):
    """
    Main function to solve circle application problems
    
    Args:
        problem_type (str): Type of application problem
        parameters (dict): Problem parameters
    
    Returns:
        str: Formatted solution
    """
    if solve_real_world_problem:
        return solve_real_world_problem(problem_type, parameters)
    else:
        return "❌ Real world solver module is not available."

# Export the functions
__all__ = ['solve_application', 'get_application_types']

if solve_real_world_problem:
    __all__.append('solve_real_world_problem')

