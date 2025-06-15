import numpy as np
from typing import List, Tuple, Optional

class TriangleSolver:
    @staticmethod
    def is_valid_triangle(sides: List[float]) -> bool:
        """
        Check if three sides can form a valid triangle using triangle inequality theorem.
        
        Args:
            sides: List of three side lengths
            
        Returns:
            bool: True if sides can form a valid triangle, False otherwise
        """
        if len(sides) != 3:
            return False
        
        a, b, c = sorted(sides)
        return a + b > c
    
    @staticmethod
    def are_similar_triangles(sides1: List[float], sides2: List[float]) -> Tuple[bool, Optional[float]]:
        """
        Check if two triangles are similar by comparing their side ratios.
        
        Args:
            sides1: List of three side lengths for first triangle
            sides2: List of three side lengths for second triangle
            
        Returns:
            Tuple[bool, float]: (True if similar, scale factor) or (False, None)
        """
        # Check if both sets of sides form valid triangles
        if not (TriangleSolver.is_valid_triangle(sides1) and TriangleSolver.is_valid_triangle(sides2)):
            return False, None
        
        # Sort sides to ensure consistent comparison
        sides1_sorted = sorted(sides1)
        sides2_sorted = sorted(sides2)
        
        # Calculate ratios of corresponding sides
        ratios = [sides2_sorted[i] / sides1_sorted[i] for i in range(3)]
        
        # Check if all ratios are equal (within a small tolerance for floating point comparison)
        if all(abs(ratio - ratios[0]) < 1e-10 for ratio in ratios):
            return True, ratios[0]
        
        return False, None
    
    @staticmethod
    def get_triangle_type(sides: List[float]) -> str:
        """
        Determine the type of triangle based on its sides.
        
        Args:
            sides: List of three side lengths
            
        Returns:
            str: Type of triangle ('equilateral', 'isosceles', 'scalene', or 'invalid')
        """
        if not TriangleSolver.is_valid_triangle(sides):
            return 'invalid'
        
        a, b, c = sorted(sides)
        
        if abs(a - b) < 1e-10 and abs(b - c) < 1e-10:
            return 'equilateral'
        elif abs(a - b) < 1e-10 or abs(b - c) < 1e-10:
            return 'isosceles'
        else:
            return 'scalene'
    
    @staticmethod
    def is_right_triangle(sides: List[float]) -> bool:
        """
        Check if a triangle is a right triangle using the Pythagorean theorem.
        
        Args:
            sides: List of three side lengths
            
        Returns:
            bool: True if the triangle is a right triangle, False otherwise
        """
        if not TriangleSolver.is_valid_triangle(sides):
            return False
        
        a, b, c = sorted(sides)
        return abs(a**2 + b**2 - c**2) < 1e-10 