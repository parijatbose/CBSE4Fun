# File: chapters/chapter6_triangles/sub_chapters/area/solver.py

import math

def calculate_area_heron(sides: list) -> dict:
    """Calculate area of a triangle using Heron's formula."""
    if len(sides) != 3:
        raise ValueError("Triangle must have exactly 3 sides")
    
    a, b, c = sides
    
    # Check if triangle is valid
    if not (a + b > c and b + c > a and c + a > b):
        raise ValueError("Invalid triangle: sum of any two sides must be greater than the third side")
    
    # Calculate semi-perimeter
    s = (a + b + c) / 2
    
    # Calculate area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    return {
        'area': area,
        'semi_perimeter': s,
        'message': f"Area = {area:.2f} cm²"
    }

def calculate_area_base_height(base: float, height: float) -> dict:
    """Calculate area of a triangle using base and height."""
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive")
    
    area = 0.5 * base * height
    
    return {
        'area': area,
        'message': f"Area = {area:.2f} cm²"
    }

def calculate_area_sides_angle(side1: float, side2: float, angle: float) -> dict:
    """Calculate area of a triangle using two sides and included angle."""
    if side1 <= 0 or side2 <= 0:
        raise ValueError("Sides must be positive")
    
    if angle <= 0 or angle >= 180:
        raise ValueError("Angle must be between 0° and 180°")
    
    # Convert angle to radians
    angle_rad = math.radians(angle)
    
    # Calculate area using formula: Area = ½ × a × b × sin(C)
    area = 0.5 * side1 * side2 * math.sin(angle_rad)
    
    return {
        'area': area,
        'message': f"Area = {area:.2f} cm²"
    }

def find_height_given_area(area: float, base: float) -> dict:
    """Find height of a triangle given area and base."""
    if area <= 0 or base <= 0:
        raise ValueError("Area and base must be positive")
    
    height = (2 * area) / base
    
    return {
        'height': height,
        'message': f"Height = {height:.2f} cm"
    }

def find_base_given_area(area: float, height: float) -> dict:
    """Find base of a triangle given area and height."""
    if area <= 0 or height <= 0:
        raise ValueError("Area and height must be positive")
    
    base = (2 * area) / height
    
    return {
        'base': base,
        'message': f"Base = {base:.2f} cm"
    } 