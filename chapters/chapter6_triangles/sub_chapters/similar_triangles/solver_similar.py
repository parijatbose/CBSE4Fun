import math
import streamlit as st
import numpy as np
from typing import Dict, Any, List, Tuple
from ...utils.triangle_base import TriangleBase, TriangleData
from ...utils.triangle_plotter import TrianglePlotter

def solve_similar_triangles(params: Dict) -> str:
    """Entry point for similar triangles solver."""
    solver = SimilarTriangleSolver()
    return solver.solve(params)

class SimilarTriangleSolver(TriangleBase):
    def __init__(self):
        super().__init__()
        self.plotter = TrianglePlotter()
    
    def solve(self, params: Dict) -> str:
        """Solve similar triangles problem."""
        try:
            # Extract parameters
            triangle1_sides = params.get('triangle1', [])
            triangle2_sides = params.get('triangle2', [])
            
            # Validate input
            if not (triangle1_sides and triangle2_sides):
                return "❌ Please provide sides for both triangles."
            
            # Create triangle data objects
            triangle1 = TriangleData(sides=triangle1_sides)
            triangle2 = TriangleData(sides=triangle2_sides)
            
            # Check if triangles are valid
            if not triangle1.is_valid():
                return "❌ First triangle is not valid! The sum of any two sides must be greater than the third side."
            if not triangle2.is_valid():
                return "❌ Second triangle is not valid! The sum of any two sides must be greater than the third side."
            
            # Check similarity
            is_similar, scale_factor = self.are_similar(triangle1, triangle2)
            
            # Prepare response
            response = []
            
            if is_similar:
                response.append("✅ The triangles are similar!")
                response.append(f"Scale factor: {scale_factor:.2f}")
                
                # Additional information
                response.append("\n📐 **Additional Information:**")
                response.append(f"First triangle is {triangle1.get_type()}")
                response.append(f"Second triangle is {triangle2.get_type()}")
                
                if triangle1.is_right_triangle():
                    response.append("First triangle is a right triangle")
                if triangle2.is_right_triangle():
                    response.append("Second triangle is a right triangle")
                
                # Calculate and display angles
                angles1 = self.calculate_angles(triangle1.sides)
                angles2 = self.calculate_angles(triangle2.sides)
                
                response.append("\n📐 **Angles:**")
                response.append(f"First triangle: {', '.join(f'{angle}°' for angle in angles1)}")
                response.append(f"Second triangle: {', '.join(f'{angle}°' for angle in angles2)}")
                
                # Calculate and display areas
                area1 = self.calculate_area(triangle1.sides)
                area2 = self.calculate_area(triangle2.sides)
                
                response.append("\n📐 **Areas:**")
                response.append(f"First triangle: {area1:.2f} square units")
                response.append(f"Second triangle: {area2:.2f} square units")
                response.append(f"Area ratio: {(area2/area1):.2f} (should be square of scale factor)")
                
                # Visualize triangles
                response.append("\n📐 **Visualization:**")
                
                # Calculate points for visualization
                points1 = self._calculate_triangle_points(triangle1.sides)
                points2 = self._calculate_triangle_points(triangle2.sides)
                
                # Plot triangles
                col1, col2 = st.columns(2)
                with col1:
                    st.write("First Triangle")
                    fig1 = self.plotter.plot_triangle(points1, angles1)
                    st.pyplot(fig1)
                
                with col2:
                    st.write("Second Triangle")
                    fig2 = self.plotter.plot_triangle(points2, angles2)
                    st.pyplot(fig2)
                
                # Explanation
                response.append("\n📐 **Explanation:**")
                response.append("Two triangles are similar if their corresponding sides are proportional.")
                response.append(f"In this case, the ratio of corresponding sides is {scale_factor:.2f}:1")
                response.append("Therefore, the triangles are similar.")
                
            else:
                response.append("❌ The triangles are not similar!")
                
                # Show why they're not similar
                response.append("\n📐 **Analysis:**")
                sides1_sorted = sorted(triangle1.sides)
                sides2_sorted = sorted(triangle2.sides)
                ratios = [sides2_sorted[i] / sides1_sorted[i] for i in range(3)]
                
                response.append("Side ratios:")
                for i, ratio in enumerate(ratios):
                    response.append(f"Ratio {i+1}: {ratio:.2f}")
                
                response.append("\nFor triangles to be similar, all side ratios must be equal.")
                response.append("In this case, the ratios are different, which means the triangles are not similar.")
            
            return "\n".join(response)
            
        except Exception as e:
            return f"❌ Error: {str(e)}"
    
    def _calculate_triangle_points(self, sides: List[float]) -> List[Tuple[float, float]]:
        """Calculate points for triangle visualization."""
        # Place first point at origin
        points = [(0, 0)]
        
        # Place second point on x-axis
        points.append((sides[0], 0))
        
        # Calculate third point using cosine law
        a, b, c = sides
        cos_C = (a**2 + b**2 - c**2) / (2 * a * b)
        sin_C = np.sqrt(1 - cos_C**2)
        
        x = a * cos_C
        y = a * sin_C
        points.append((x, y))
        
        return points

def check_similarity_sss(sides1: List[float], sides2: List[float]) -> str:
    """
    Check if two triangles are similar using SSS criterion.
    """
    if len(sides1) != 3 or len(sides2) != 3:
        return "❌ Each triangle must have exactly 3 sides"
    
    # Sort sides to match corresponding sides
    a1, b1, c1 = sorted(sides1)
    a2, b2, c2 = sorted(sides2)
    
    # Calculate ratios
    ratio_a = a2 / a1
    ratio_b = b2 / b1
    ratio_c = c2 / c1
    
    # Check if all ratios are equal (within tolerance)
    tolerance = 0.001
    is_similar = (abs(ratio_a - ratio_b) < tolerance and 
                  abs(ratio_b - ratio_c) < tolerance and 
                  abs(ratio_a - ratio_c) < tolerance)
    
    # Calculate angles for both triangles
    angles1 = calculate_triangle_angles(sides1)
    angles2 = calculate_triangle_angles(sides2)
    
    result = f"""
✅ **Similar Triangles Check (SSS Criterion):**

**Triangle 1:** Sides = {sides1[0]}, {sides1[1]}, {sides1[2]} cm
**Triangle 2:** Sides = {sides2[0]}, {sides2[1]}, {sides2[2]} cm

📝 **Step-by-Step Analysis:**

**1. Sorting sides (smallest to largest):**
   • Triangle 1: {a1}, {b1}, {c1}
   • Triangle 2: {a2}, {b2}, {c2}

**2. Calculating ratios of corresponding sides:**
   • Ratio 1: {a2}/{a1} = {ratio_a:.3f}
   • Ratio 2: {b2}/{b1} = {ratio_b:.3f}
   • Ratio 3: {c2}/{c1} = {ratio_c:.3f}

**3. Checking if all ratios are equal:**
   • Difference between ratios: {abs(ratio_a - ratio_b):.6f}, {abs(ratio_b - ratio_c):.6f}, {abs(ratio_a - ratio_c):.6f}
   • All differences < 0.001? {'YES ✓' if is_similar else 'NO ✗'}

**4. Angles of triangles:**
   • Triangle 1: {angles1[0]:.1f}°, {angles1[1]:.1f}°, {angles1[2]:.1f}°
   • Triangle 2: {angles2[0]:.1f}°, {angles2[1]:.1f}°, {angles2[2]:.1f}°

💡 **Conclusion:**
{'✅ The triangles ARE SIMILAR by SSS criterion!' if is_similar else '❌ The triangles are NOT SIMILAR'}
{f'• Scale factor (ratio) = {ratio_a:.3f}' if is_similar else '• Ratios are not equal'}
{f'• Corresponding angles are equal' if is_similar else '• Corresponding angles may differ'}

**Properties of similar triangles:**
• Corresponding angles are equal
• Corresponding sides are proportional
• Ratio of areas = (ratio of sides)²
{f'• Area ratio = {ratio_a**2:.3f}' if is_similar else ''}
"""
    
    return result

def check_similarity_aa(params: Dict[str, Any]) -> str:
    """
    Check if two triangles are similar using AA criterion.
    """
    angles1 = params.get("angles1", [])
    angles2 = params.get("angles2", [])
    
    if len(angles1) < 2 or len(angles2) < 2:
        return "❌ Need at least 2 angles from each triangle"
    
    # Sort angles for comparison
    angles1_sorted = sorted(angles1[:2])
    angles2_sorted = sorted(angles2[:2])
    
    # Check if two angles are equal
    tolerance = 0.1
    is_similar = (abs(angles1_sorted[0] - angles2_sorted[0]) < tolerance and 
                  abs(angles1_sorted[1] - angles2_sorted[1]) < tolerance)
    
    # Calculate third angles
    third_angle1 = 180 - sum(angles1[:2])
    third_angle2 = 180 - sum(angles2[:2])
    
    result = f"""
✅ **Similar Triangles Check (AA Criterion):**

**Triangle 1 angles:** {angles1[0]}°, {angles1[1]}°, {third_angle1:.1f}°
**Triangle 2 angles:** {angles2[0]}°, {angles2[1]}°, {third_angle2:.1f}°

📝 **Analysis:**

**1. Comparing corresponding angles:**
   • Angle 1: {angles1_sorted[0]}° vs {angles2_sorted[0]}° (difference: {abs(angles1_sorted[0] - angles2_sorted[0]):.1f}°)
   • Angle 2: {angles1_sorted[1]}° vs {angles2_sorted[1]}° (difference: {abs(angles1_sorted[1] - angles2_sorted[1]):.1f}°)

**2. AA Criterion Check:**
   Two angles of one triangle equal to two angles of another? {'YES ✓' if is_similar else 'NO ✗'}

💡 **Conclusion:**
{'✅ The triangles ARE SIMILAR by AA criterion!' if is_similar else '❌ The triangles are NOT SIMILAR'}
"""
    
    return result

def find_missing_side_similar(params: Dict[str, Any]) -> str:
    """
    Find missing side in similar triangles.
    """
    known_triangle = params.get("known_triangle", [])
    partial_triangle = params.get("partial_triangle", [])
    ratio = params.get("ratio", 0)
    
    if not ratio and len(known_triangle) == 3 and len(partial_triangle) >= 2:
        # Calculate ratio from known sides
        for i in range(len(partial_triangle)):
            if partial_triangle[i] > 0 and known_triangle[i] > 0:
                ratio = partial_triangle[i] / known_triangle[i]
                break
    
    if not ratio:
        return "❌ Cannot determine scale factor. Need at least one corresponding pair of sides."
    
    # Find missing sides
    missing_sides = []
    for i in range(3):
        if i < len(partial_triangle) and partial_triangle[i] == 0:
            missing_sides.append((i, known_triangle[i] * ratio))
    
    result = f"""
✅ **Finding Missing Sides in Similar Triangles:**

**Known Triangle:** {known_triangle}
**Partial Triangle:** {partial_triangle}
**Scale Factor:** {ratio:.3f}

📝 **Solution:**
"""
    
    for idx, value in missing_sides:
        side_name = ['a', 'b', 'c'][idx]
        result += f"""
**Missing side {side_name}:**
• {side_name} = {known_triangle[idx]} × {ratio:.3f}
• {side_name} = {value:.2f} cm
"""
    
    return result

def calculate_triangle_angles(sides: List[float]) -> List[float]:
    """
    Calculate angles of a triangle using law of cosines.
    """
    a, b, c = sides
    
    # Law of cosines: cos(A) = (b² + c² - a²) / (2bc)
    cos_A = (b**2 + c**2 - a**2) / (2 * b * c)
    cos_B = (a**2 + c**2 - b**2) / (2 * a * c)
    cos_C = (a**2 + b**2 - c**2) / (2 * a * b)
    
    # Ensure values are in valid range for arccos
    cos_A = max(-1, min(1, cos_A))
    cos_B = max(-1, min(1, cos_B))
    cos_C = max(-1, min(1, cos_C))
    
    # Calculate angles in degrees
    angle_A = math.degrees(math.acos(cos_A))
    angle_B = math.degrees(math.acos(cos_B))
    angle_C = math.degrees(math.acos(cos_C))
    
    return [angle_A, angle_B, angle_C]

def area_ratio_similar_triangles(ratio: float) -> str:
    """
    Calculate area ratio of similar triangles.
    """
    area_ratio = ratio ** 2
    
    result = f"""
✅ **Area Ratio of Similar Triangles:**

Given:
• Linear scale factor (ratio of sides) = {ratio}

📝 **Formula:**
• Area ratio = (Linear ratio)²
• Area ratio = {ratio}²
• Area ratio = {area_ratio:.3f}

💡 **This means:**
• If sides are in ratio {ratio}:1
• Then areas are in ratio {area_ratio:.3f}:1

**Example:**
If smaller triangle has area 10 cm²,
then larger triangle has area = 10 × {area_ratio:.3f} = {10 * area_ratio:.2f} cm²
"""
    
    return result