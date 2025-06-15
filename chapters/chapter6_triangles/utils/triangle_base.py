import json
import os
import numpy as np
from typing import List, Tuple, Dict, Optional, Union
from dataclasses import dataclass

@dataclass
class TriangleData:
    sides: List[float]
    angles: Optional[List[float]] = None
    points: Optional[List[Tuple[float, float]]] = None
    
    def is_valid(self) -> bool:
        """Check if the triangle is valid using triangle inequality theorem."""
        if len(self.sides) != 3:
            return False
        a, b, c = sorted(self.sides)
        return a + b > c
    
    def get_type(self) -> str:
        """Determine the type of triangle based on its sides."""
        if not self.is_valid():
            return 'invalid'
        
        a, b, c = sorted(self.sides)
        
        if abs(a - b) < 1e-10 and abs(b - c) < 1e-10:
            return 'equilateral'
        elif abs(a - b) < 1e-10 or abs(b - c) < 1e-10:
            return 'isosceles'
        else:
            return 'scalene'
    
    def is_right_triangle(self) -> bool:
        """Check if the triangle is a right triangle using Pythagorean theorem."""
        if not self.is_valid():
            return False
        
        a, b, c = sorted(self.sides)
        return abs(a**2 + b**2 - c**2) < 1e-10

class TriangleBase:
    def __init__(self):
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        """Load configuration from JSON file."""
        config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'triangle_config.json')
        with open(config_path, 'r') as f:
            return json.load(f)
    
    def validate_sides(self, sides: List[float]) -> bool:
        """Validate triangle sides."""
        if len(sides) != 3:
            return False
        
        min_length = self.config['validation']['min_side_length']
        max_length = self.config['validation']['max_side_length']
        
        return all(min_length <= side <= max_length for side in sides)
    
    def calculate_angles(self, sides: List[float]) -> List[float]:
        """Calculate angles using cosine law."""
        if not self.validate_sides(sides):
            return []
        
        a, b, c = sides
        angles = []
        
        # Calculate angles using cosine law
        cos_A = (b**2 + c**2 - a**2) / (2 * b * c)
        cos_B = (a**2 + c**2 - b**2) / (2 * a * c)
        cos_C = (a**2 + b**2 - c**2) / (2 * a * b)
        
        # Convert to degrees and round
        angles = [
            round(np.degrees(np.arccos(np.clip(cos_A, -1.0, 1.0))), 1),
            round(np.degrees(np.arccos(np.clip(cos_B, -1.0, 1.0))), 1),
            round(np.degrees(np.arccos(np.clip(cos_C, -1.0, 1.0))), 1)
        ]
        
        return angles
    
    def calculate_area(self, sides: List[float], method: str = 'heron') -> float:
        """Calculate triangle area using specified method."""
        if not self.validate_sides(sides):
            return 0.0
        
        if method == 'heron':
            # Heron's formula
            s = sum(sides) / 2
            return np.sqrt(s * (s - sides[0]) * (s - sides[1]) * (s - sides[2]))
        elif method == 'base_height':
            # Base-height formula (requires height)
            if len(sides) != 2:
                return 0.0
            return 0.5 * sides[0] * sides[1]
        else:
            return 0.0
    
    def are_similar(self, triangle1: TriangleData, triangle2: TriangleData) -> Tuple[bool, Optional[float]]:
        """Check if two triangles are similar and return scale factor if they are."""
        if not (triangle1.is_valid() and triangle2.is_valid()):
            return False, None
        
        # Sort sides for consistent comparison
        sides1 = sorted(triangle1.sides)
        sides2 = sorted(triangle2.sides)
        
        # Calculate ratios of corresponding sides
        ratios = [sides2[i] / sides1[i] for i in range(3)]
        
        # Check if all ratios are equal (within tolerance)
        if all(abs(ratio - ratios[0]) < 1e-10 for ratio in ratios):
            return True, ratios[0]
        
        return False, None
    
    def get_formula_explanation(self, formula_type: str) -> str:
        """Get explanation for a specific formula."""
        formulas = self.config['formulas']
        if formula_type in formulas:
            return self._format_formula_explanation(formulas[formula_type])
        return "Formula not found."
    
    def _format_formula_explanation(self, formula_data: Dict) -> str:
        """Format formula explanation in a readable way."""
        explanation = f"📐 **{formula_data['name']}:**\n\n"
        
        if 'formula' in formula_data:
            explanation += f"**Formula:** {formula_data['formula']}\n\n"
        
        if 'description' in formula_data:
            explanation += f"**Description:** {formula_data['description']}\n\n"
        
        if 'variables' in formula_data:
            explanation += "**Variables:**\n"
            for var, desc in formula_data['variables'].items():
                explanation += f"• {var}: {desc}\n"
            explanation += "\n"
        
        if 'example' in formula_data:
            explanation += f"**Example:** {formula_data['example']}\n"
        
        return explanation 