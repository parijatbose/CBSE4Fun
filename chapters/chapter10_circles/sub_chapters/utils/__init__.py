"""
Utility functions for CBSE Class 10 Chapter 9 - Circles
Helper functions for calculations, validations, and formatting
"""

import math
import re

def validate_point_outside_circle(point, center, radius):
    """
    Check if a point is outside a circle
    
    Args:
        point (list): Point coordinates [x, y]
        center (list): Circle center [h, k]
        radius (float): Circle radius
    
    Returns:
        bool: True if point is outside circle
    """
    distance = calculate_distance(point, center)
    return distance > radius

def calculate_distance(point1, point2):
    """
    Calculate distance between two points
    
    Args:
        point1 (list): First point [x1, y1]
        point2 (list): Second point [x2, y2]
    
    Returns:
        float: Distance between points
    """
    x1, y1 = point1[0], point1[1]
    x2, y2 = point2[0], point2[1]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def format_circle_equation(center, radius):
    """
    Format circle equation in standard form
    
    Args:
        center (list): Circle center [h, k]
        radius (float): Circle radius
    
    Returns:
        str: Formatted circle equation
    """
    h, k = center[0], center[1]
    if h == 0 and k == 0:
        return f"x² + y² = {radius**2}"
    elif h == 0:
        return f"x² + (y - {k})² = {radius**2}"
    elif k == 0:
        return f"(x - {h})² + y² = {radius**2}"
    else:
        return f"(x - {h})² + (y - {k})² = {radius**2}"

def extract_numbers_from_query(query):
    """
    Extract numeric values from text query
    
    Args:
        query (str): Input query string
    
    Returns:
        list: List of extracted numbers
    """
    return [float(x) for x in re.findall(r'-?\d+\.?\d*', query)]

def format_solution_header(problem_type):
    """
    Create formatted header for solutions
    
    Args:
        problem_type (str): Type of problem being solved
    
    Returns:
        str: Formatted header
    """
    icons = {
        'tangent_length': '📐',
        'theorem_proof': '📚',
        'construction': '🔧',
        'application': '🌍'
    }
    
    icon = icons.get(problem_type, '📝')
    title = problem_type.replace('_', ' ').title()
    
    return f"## {icon} {title}\n"

# Mathematical constants
PI = math.pi
DEGREES_TO_RADIANS = PI / 180
RADIANS_TO_DEGREES = 180 / PI

# Common validation patterns
COORDINATE_PATTERN = r'\(\s*(-?\d+\.?\d*)\s*,\s*(-?\d+\.?\d*)\s*\)'
NUMBER_PATTERN = r'-?\d+\.?\d*'
