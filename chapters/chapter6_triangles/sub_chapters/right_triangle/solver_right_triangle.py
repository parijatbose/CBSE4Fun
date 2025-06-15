import math
import os
from typing import Dict, Any
from chapters.chapter6_triangles.utils.triangle_plotter import TrianglePlotter

def solve_right_triangle(params: Dict[str, Any]) -> str:
    """
    Solve right triangle problems: hypotenuse, angles, area, perimeter + plot.
    """
    try:
        base = params.get("base", 0)
        height = params.get("height", 0)
        hypotenuse = params.get("hypotenuse", 0)
        angle = params.get("angle", 0)
        
        # Initialize plotter
        plotter = TrianglePlotter()
        plot_info = None

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
            
            # Generate plot
            try:
                fig = plotter.plot_right_triangle(base, height)
                plot_path = "static/plots/right_triangle_auto.png"
                os.makedirs("static/plots", exist_ok=True)
                fig.savefig(plot_path, dpi=300, bbox_inches='tight')
                plot_info = f"![Right Triangle]({plot_path})"
            except Exception as e:
                plot_info = f"⚠️ Plot generation failed: {str(e)}"
            
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
{plot_info}
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
            
            # Generate plot
            try:
                fig = plotter.plot_right_triangle(base, height)
                plot_path = "static/plots/right_triangle_auto.png"
                os.makedirs("static/plots", exist_ok=True)
                fig.savefig(plot_path, dpi=300, bbox_inches='tight')
                plot_info = f"![Right Triangle]({plot_path})"
            except Exception as e:
                plot_info = f"⚠️ Plot generation failed: {str(e)}"

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
{plot_info}
"""

        # Case 3: Given hypotenuse and one side
        elif hypotenuse > 0 and (base > 0 or height > 0):
            if base > 0:
                # Calculate height using Pythagorean theorem
                if hypotenuse**2 - base**2 < 0:
                    return "❌ Invalid input: base cannot be larger than hypotenuse in a right triangle."
                height = math.sqrt(hypotenuse**2 - base**2)
                known_side = "base"
                known_value = base
                other_side = height
                other_name = "height"
            else:
                # Calculate base using Pythagorean theorem
                if hypotenuse**2 - height**2 < 0:
                    return "❌ Invalid input: height cannot be larger than hypotenuse in a right triangle."
                base = math.sqrt(hypotenuse**2 - height**2)
                known_side = "height"
                known_value = height
                other_side = base
                other_name = "base"

            # Calculate angles using inverse tangent
            angle_B = math.degrees(math.atan(height / base))
            angle_A = 90 - angle_B
            area = 0.5 * base * height
            
            # Generate plot
            try:
                fig = plotter.plot_right_triangle(base, height)
                plot_path = "static/plots/right_triangle_auto.png"
                os.makedirs("static/plots", exist_ok=True)
                fig.savefig(plot_path, dpi=300, bbox_inches='tight')
                plot_info = f"![Right Triangle]({plot_path})"
            except Exception as e:
                plot_info = f"⚠️ Plot generation failed: {str(e)}"

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
{plot_info}
"""
        
        else:
            result = "❌ Insufficient data. Need at least:\n• Base and height, OR\n• Hypotenuse and one angle, OR\n• Hypotenuse and one other side."
        
        return result

    except Exception as e:
        return f"❌ Error solving right triangle: {str(e)}"