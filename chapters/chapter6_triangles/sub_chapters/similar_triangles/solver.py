# File: chapters/chapter6_triangles/sub_chapters/similar_triangles/solver.py

import math

def check_similar_triangles(sides1: list, sides2: list) -> dict:
    """Check if two triangles are similar using SSS criterion."""
    if len(sides1) != 3 or len(sides2) != 3:
        raise ValueError("Both triangles must have exactly 3 sides")
    
    # Calculate ratios of corresponding sides
    ratios = [sides2[i]/sides1[i] for i in range(3)]
    
    # Check if all ratios are equal (within a small tolerance)
    is_similar = all(abs(r - ratios[0]) < 1e-10 for r in ratios)
    
    return {
        'is_similar': is_similar,
        'ratio': ratios[0] if is_similar else None,
        'message': f"Triangles are {'similar' if is_similar else 'not similar'} by SSS criterion"
    }

def check_similar_triangles_angles(angles1: list, angles2: list) -> dict:
    """Check if two triangles are similar using AA criterion."""
    if len(angles1) != 3 or len(angles2) != 3:
        raise ValueError("Both triangles must have exactly 3 angles")
    
    # Check if two angles are equal (within a small tolerance)
    angles1.sort()
    angles2.sort()
    is_similar = (abs(angles1[0] - angles2[0]) < 1e-10 and 
                 abs(angles1[1] - angles2[1]) < 1e-10)
    
    return {
        'is_similar': is_similar,
        'message': f"Triangles are {'similar' if is_similar else 'not similar'} by AA criterion"
    }

def find_missing_side(sides1: list, sides2: list, missing_index: int) -> dict:
    """Find the missing side in a similar triangle."""
    if len(sides1) != 3 or len(sides2) != 3:
        raise ValueError("Both triangles must have exactly 3 sides")
    
    # Find the ratio using the known sides
    known_ratios = [sides2[i]/sides1[i] for i in range(3) if i != missing_index]
    if not known_ratios or not all(abs(r - known_ratios[0]) < 1e-10 for r in known_ratios):
        raise ValueError("Triangles are not similar")
    
    ratio = known_ratios[0]
    missing_side = sides1[missing_index] * ratio
    
    return {
        'missing_side': missing_side,
        'ratio': ratio,
        'message': f"Missing side = {missing_side:.2f} cm"
    }

def find_missing_angle(angles1: list, angles2: list, missing_index: int) -> dict:
    """Find the missing angle in a similar triangle."""
    if len(angles1) != 3 or len(angles2) != 3:
        raise ValueError("Both triangles must have exactly 3 angles")
    
    # In similar triangles, corresponding angles are equal
    missing_angle = angles1[missing_index]
    
    return {
        'missing_angle': missing_angle,
        'message': f"Missing angle = {missing_angle}°"
    } 