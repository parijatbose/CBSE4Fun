import math
from typing import Dict, Any
import matplotlib.pyplot as plt
import numpy as np
import os

def test_right_triangle_calc():
    """Test right triangle calculations with different input cases."""
    
    # Test Case 1: Base and Height
    params1 = {
        "base": 3,
        "height": 4
    }
    
    # Test Case 2: Hypotenuse and Angle
    params2 = {
        "hypotenuse": 5,
        "angle": 36.87
    }
    
    # Test Case 3: Hypotenuse and Base
    params3 = {
        "hypotenuse": 5,
        "base": 3
    }
    
    print("\n=== Test Case 1: Base and Height ===")
    result1 = solve_right_triangle(params1)
    print(result1)
    
    print("\n=== Test Case 2: Hypotenuse and Angle ===")
    result2 = solve_right_triangle(params2)
    print(result2)
    
    print("\n=== Test Case 3: Hypotenuse and Base ===")
    result3 = solve_right_triangle(params3)
    print(result3)

def solve_right_triangle(params: Dict[str, Any]) -> str:
    """
    Solve right triangle problems: hypotenuse, angles, area, perimeter + plot.
    """
    try:
        base = params.get("base", 0)
        height = params.get("height", 0)
        hypotenuse = params.get("hypotenuse", 0)
        angle = params.get("angle", 0)
        
        plot_path = None

        # Case 1: Given base and height
        if base > 0 and height > 0:
            # Calculate hypotenuse using Pythagorean theorem
            hypotenuse = math.sqrt(base**2 + height**2)
            # Calculate angles using inverse tangent
            angle_B = math.degrees(math.atan(height / base))
            angle_A = 90 - angle_B
            # Calculate area and perimeter
            area = 0.5 * base * height
            perimeter = base + height + hypotenuse
            # Order sides: [base, height, hypotenuse]
            sides = [base, height, hypotenuse]
            # Order angles: [angle_A, angle_B, 90]
            angles = [round(angle_A, 1), round(angle_B, 1), 90]
            plot_path = plot_triangle(sides, angles, "test_right_triangle1.png")
            
            result = f"""
✅ **Right Triangle Solution:**

Given:
• Base = {base} cm  
• Height = {height} cm  

📝 **Step-by-Step Calculations:**

1. **Hypotenuse (c):**
   • Using Pythagorean theorem: c = √(a² + b²)
   • c = √({base}² + {height}²)
   • c = √({base**2} + {height**2})
   • c = √{base**2 + height**2}
   • c = **{hypotenuse:.2f} cm**

2. **Angles:**
   • Angle B = tan⁻¹(height/base)
   • Angle B = tan⁻¹({height}/{base})
   • Angle B = tan⁻¹({height/base:.2f})
   • Angle B = **{angle_B:.1f}°**
   
   • Angle A = 90° - Angle B
   • Angle A = 90° - {angle_B:.1f}°
   • Angle A = **{angle_A:.1f}°**

3. **Area:**
   • Area = ½ × base × height
   • Area = ½ × {base} × {height}
   • Area = **{area:.2f} cm²**

4. **Perimeter:**
   • Perimeter = base + height + hypotenuse
   • Perimeter = {base} + {height} + {hypotenuse:.2f}
   • Perimeter = **{perimeter:.2f} cm**

📊 **Visualization:**

![Right Triangle]({plot_path})
"""
        
        # Case 2: Given hypotenuse and one angle
        elif hypotenuse > 0 and angle > 0 and angle < 90:
            # Convert angle to radians for calculations
            angle_rad = math.radians(angle)
            # Calculate base and height using trigonometric ratios
            base = hypotenuse * math.cos(angle_rad)
            height = hypotenuse * math.sin(angle_rad)
            other_angle = 90 - angle
            area = 0.5 * base * height
            # Order sides: [base, height, hypotenuse]
            sides = [base, height, hypotenuse]
            # Order angles: [angle, other_angle, 90]
            angles = [round(angle, 1), round(other_angle, 1), 90]
            plot_path = plot_triangle(sides, angles, "test_right_triangle2.png")

            result = f"""
✅ **Right Triangle Solution:**

Given:
• Hypotenuse = {hypotenuse} cm  
• Angle = {angle}°

📝 **Step-by-Step Calculations:**

1. **Base (a):**
   • Using cosine: a = hypotenuse × cos(angle)
   • a = {hypotenuse} × cos({angle}°)
   • a = {hypotenuse} × {math.cos(angle_rad):.4f}
   • a = **{base:.2f} cm**

2. **Height (b):**
   • Using sine: b = hypotenuse × sin(angle)
   • b = {hypotenuse} × sin({angle}°)
   • b = {hypotenuse} × {math.sin(angle_rad):.4f}
   • b = **{height:.2f} cm**

3. **Other Angle:**
   • Other Angle = 90° - {angle}°
   • Other Angle = **{other_angle:.1f}°**

4. **Area:**
   • Area = ½ × base × height
   • Area = ½ × {base:.2f} × {height:.2f}
   • Area = **{area:.2f} cm²**

📊 **Visualization:**

![Right Triangle]({plot_path})
"""

        # Case 3: Given hypotenuse and one side
        elif hypotenuse > 0 and (base > 0 or height > 0):
            if base > 0:
                # Calculate height using Pythagorean theorem
                height = math.sqrt(hypotenuse**2 - base**2)
                known_side = "base"
                known_value = base
                other_side = height
                other_name = "height"
            else:
                # Calculate base using Pythagorean theorem
                base = math.sqrt(hypotenuse**2 - height**2)
                known_side = "height"
                known_value = height
                other_side = base
                other_name = "base"

            # Calculate angles using inverse tangent
            angle_B = math.degrees(math.atan(height / base))
            angle_A = 90 - angle_B
            area = 0.5 * base * height
            # Order sides: [base, height, hypotenuse]
            sides = [base, height, hypotenuse]
            # Order angles: [angle_A, angle_B, 90]
            angles = [round(angle_A, 1), round(angle_B, 1), 90]
            plot_path = plot_triangle(sides, angles, "test_right_triangle3.png")

            result = f"""
✅ **Right Triangle Solution:**

Given:
• Hypotenuse = {hypotenuse} cm  
• {known_side.capitalize()} = {known_value} cm

📝 **Step-by-Step Calculations:**

1. **{other_name.capitalize()}:**
   • Using Pythagorean theorem: {other_name} = √(hypotenuse² - {known_side}²)
   • {other_name} = √({hypotenuse}² - {known_value}²)
   • {other_name} = √({hypotenuse**2} - {known_value**2})
   • {other_name} = √{hypotenuse**2 - known_value**2}
   • {other_name} = **{other_side:.2f} cm**

2. **Angles:**
   • Angle B = tan⁻¹({other_name}/{known_side})
   • Angle B = tan⁻¹({other_side:.2f}/{known_value})
   • Angle B = tan⁻¹({other_side/known_value:.2f})
   • Angle B = **{angle_B:.1f}°**
   
   • Angle A = 90° - Angle B
   • Angle A = 90° - {angle_B:.1f}°
   • Angle A = **{angle_A:.1f}°**

3. **Area:**
   • Area = ½ × base × height
   • Area = ½ × {base:.2f} × {height:.2f}
   • Area = **{area:.2f} cm²**

📊 **Visualization:**

![Right Triangle]({plot_path})
"""
        
        else:
            result = "❌ Insufficient data. Need at least:\n• Base and height, OR\n• Hypotenuse and one angle, OR\n• Hypotenuse and one other side."
        
        return result

    except Exception as e:
        return f"❌ Error solving right triangle: {str(e)}"

def plot_triangle(sides, angles, save_name="triangle_plot.png"):
    """Plot a triangle with given sides and angles."""
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(10, 10))
    
    # Calculate coordinates using law of cosines
    a, b, c = sides
    A, B, C = angles
    
    # For right triangles, place the right angle at the origin
    if C == 90:  # Right angle is C
        x1, y1 = 0, 0  # Right angle vertex
        x2, y2 = a, 0  # Base vertex
        x3, y3 = 0, b  # Height vertex
    elif B == 90:  # Right angle is B
        x1, y1 = 0, 0  # Right angle vertex
        x2, y2 = c, 0  # Base vertex
        x3, y3 = c, a  # Height vertex
    else:  # Right angle is A
        x1, y1 = 0, 0  # Right angle vertex
        x2, y2 = b, 0  # Base vertex
        x3, y3 = 0, c  # Height vertex
    
    # Plot triangle
    ax.plot([x1, x2], [y1, y2], 'b-', linewidth=2)  # Base
    ax.plot([x1, x3], [y1, y3], 'b-', linewidth=2)  # Height
    ax.plot([x2, x3], [y2, y3], 'b-', linewidth=2)  # Hypotenuse
    
    # Add angle arcs
    def plot_angle_arc(x, y, angle, radius, start_angle=0):
        arc_theta = np.linspace(start_angle, start_angle + np.radians(angle), 100)
        arc_x = x + radius * np.cos(arc_theta)
        arc_y = y + radius * np.sin(arc_theta)
        ax.plot(arc_x, arc_y, 'r-')
        # Adjust text position to be inside the triangle
        text_x = x + radius*0.5*np.cos(np.radians(start_angle + angle/2))
        text_y = y + radius*0.5*np.sin(np.radians(start_angle + angle/2))
        ax.text(text_x, text_y, f'{angle}°', ha='center', va='center')
    
    # Plot angle arcs with smaller radius
    arc_radius = min(a, b, c) * 0.15
    plot_angle_arc(x1, y1, A, arc_radius)
    plot_angle_arc(x2, y2, B, arc_radius, start_angle=180)
    plot_angle_arc(x3, y3, C, arc_radius, start_angle=-B)
    
    # Add side labels with correct positions
    ax.text((x1 + x2)/2, -0.5, f'Base = {a:.1f} cm', ha='center')
    ax.text(-0.5, (y1 + y3)/2, f'Hypotenuse = {b:.1f} cm', va='center')
    ax.text((x2 + x3)/2, (y2 + y3)/2, f'Height = {c:.1f} cm', ha='center')
    
    # Calculate and display area
    area = 0.5 * a * c  # For right triangle
    ax.text(-max(sides), max(sides), f'Area = {area:.2f} cm²',
            bbox=dict(facecolor='white', alpha=0.8))
    
    # Set equal aspect ratio and limits
    ax.set_aspect('equal')
    margin = max(sides) * 0.2
    ax.set_xlim(-margin, max(sides) + margin)
    ax.set_ylim(-margin, max(sides) + margin)
    
    # Remove axes
    ax.axis('off')
    
    # Create plots directory if it doesn't exist
    os.makedirs('chapters/chapter6_triangles/plots', exist_ok=True)
    
    # Save the plot
    plt.savefig(f'chapters/chapter6_triangles/plots/{save_name}',
                bbox_inches='tight', dpi=300)
    plt.close()
    
    return f'chapters/chapter6_triangles/plots/{save_name}'

if __name__ == "__main__":
    test_right_triangle_calc() 