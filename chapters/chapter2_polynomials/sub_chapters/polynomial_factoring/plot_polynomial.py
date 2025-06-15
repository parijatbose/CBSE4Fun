#cbse_math_solver/chpater/chapter2_polynomial_sub_chapters/polynomial_factoring/plot_polynomial.py
import matplotlib.pyplot as plt
import numpy as np
import os
from sympy import symbols, solve, I

def plot_polynomial(coefficients, degree=2, plot_name="polynomial_plot.png"):
    """
    Generates and saves the plot of polynomial to chapters/chapter2_polynomials/plots/
    Supports both quadratic (ax^2 + bx + c) and cubic (ax^3 + bx^2 + cx + d) polynomials
    """
    # First, find the roots to determine optimal viewing window
    x = symbols('x')
    if degree == 2:
        a, b, c = coefficients
        expr = a * x**2 + b * x + c
    else:
        a, b, c, d = coefficients
        expr = a * x**3 + b * x**2 + c * x + d
    
    roots = solve(expr, x)
    real_roots = [float(r.evalf()) for r in roots if not r.has(I)]
    
    # Determine x-range based on roots and critical points
    if real_roots:
        min_root = min(real_roots)
        max_root = max(real_roots)
        root_range = max_root - min_root
        
        # Add padding around roots for better visibility
        padding = max(root_range * 0.5, 2.0)  # At least 2 units padding
        x_min = min_root - padding
        x_max = max_root + padding
    else:
        # Default range if no real roots
        x_min, x_max = -10, 10
    
    # For cubic, also consider critical points
    if degree == 3 and real_roots:
        # Critical points where dy/dx = 0
        # For ax³ + bx² + cx + d, derivative is 3ax² + 2bx + c
        discriminant = (2*b)**2 - 4*(3*a)*c
        if discriminant >= 0:
            crit_x1 = (-2*b + np.sqrt(discriminant)) / (6*a)
            crit_x2 = (-2*b - np.sqrt(discriminant)) / (6*a)
            # Extend range if critical points are outside current range
            x_min = min(x_min, crit_x1 - 1, crit_x2 - 1)
            x_max = max(x_max, crit_x1 + 1, crit_x2 + 1)
    
    # Create more points for smoother curve
    x_vals = np.linspace(x_min, x_max, 1000)
    
    if degree == 2:
        y_vals = a * x_vals**2 + b * x_vals + c
        # Format polynomial equation nicely
        equation = ""
        if a == 1:
            equation += "x²"
        elif a == -1:
            equation += "-x²"
        else:
            equation += f"{a}x²"
        
        if b != 0:
            if b == 1:
                equation += " + x"
            elif b == -1:
                equation += " - x"
            elif b > 0:
                equation += f" + {b}x"
            else:
                equation += f" - {abs(b)}x"
        
        if c != 0:
            if c > 0:
                equation += f" + {c}"
            else:
                equation += f" - {abs(c)}"
                
    elif degree == 3:
        y_vals = a * x_vals**3 + b * x_vals**2 + c * x_vals + d
        # Format polynomial equation nicely
        equation = ""
        if a == 1:
            equation += "x³"
        elif a == -1:
            equation += "-x³"
        else:
            equation += f"{a}x³"
        
        if b != 0:
            if b == 1:
                equation += " + x²"
            elif b == -1:
                equation += " - x²"
            elif b > 0:
                equation += f" + {b}x²"
            else:
                equation += f" - {abs(b)}x²"
        
        if c != 0:
            if c == 1:
                equation += " + x"
            elif c == -1:
                equation += " - x"
            elif c > 0:
                equation += f" + {c}x"
            else:
                equation += f" - {abs(c)}x"
        
        if d != 0:
            if d > 0:
                equation += f" + {d}"
            else:
                equation += f" - {abs(d)}"
    else:
        raise ValueError(f"Unsupported degree: {degree}")

    save_dir = os.path.join(os.path.dirname(__file__), "plots")
    os.makedirs(save_dir, exist_ok=True)
    save_path = os.path.join(save_dir, plot_name)

    # Create figure with high DPI for clarity
    fig, ax = plt.subplots(figsize=(14, 10))
    
    # Plot the polynomial curve
    ax.plot(x_vals, y_vals, 'b-', linewidth=3, label=f'y = {equation}', zorder=5)
    
    # Set up the axes to pass through origin
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    
    # Add arrows to axes
    arrow_props = dict(arrowstyle='->', lw=2, color='black')
    ax.annotate('', xy=(x_max, 0), xytext=(x_min, 0), arrowprops=arrow_props)
    ax.annotate('', xy=(0, max(y_vals)), xytext=(0, min(y_vals)), arrowprops=arrow_props)
    
    # Add axis labels
    ax.text(x_max - 0.3, -0.5, 'x', fontsize=20, fontweight='bold', ha='center')
    ax.text(0.3, max(y_vals) - 0.5, 'y', fontsize=20, fontweight='bold', va='center')
    
    # Enhanced grid
    ax.grid(True, which='major', alpha=0.3, linestyle='-', color='gray')
    ax.minorticks_on()
    ax.grid(True, which='minor', alpha=0.1, linestyle=':', color='gray')

    # Mark real roots with enhanced visibility
    if real_roots:
        # Plot roots with larger markers
        ax.plot(real_roots, [0] * len(real_roots), 'o', color='red', markersize=14, 
                label='Zeros (x-intercepts)', markeredgecolor='darkred', markeredgewidth=3,
                markerfacecolor='red', zorder=10)
        
        # Add vertical lines at roots for emphasis
        for root in real_roots:
            ax.axvline(x=root, color='red', alpha=0.3, linestyle='--', linewidth=2, zorder=1)
        
        # Annotate roots with enhanced visibility
        for i, root in enumerate(real_roots):
            # Format root value nicely
            if abs(root - round(root)) < 0.001:
                root_str = f"{int(round(root))}"
            else:
                root_str = f"{root:.3f}"
            
            # Calculate annotation position
            y_range = max(y_vals) - min(y_vals)
            y_offset = y_range * 0.08
            
            # Alternate positions for close roots
            position_multiplier = 1
            for other_root in real_roots[:i]:
                if abs(other_root - root) < 1:
                    position_multiplier *= -1.2
            
            ax.annotate(f'({root_str}, 0)', 
                       xy=(root, 0), 
                       xytext=(root, y_offset * position_multiplier),
                       ha='center',
                       fontsize=14,
                       fontweight='bold',
                       color='darkred',
                       bbox=dict(boxstyle="round,pad=0.5", facecolor="yellow", 
                                edgecolor='darkred', linewidth=2, alpha=0.9),
                       arrowprops=dict(arrowstyle='->', color='darkred', lw=2))

    # Find and mark critical points for cubic
    if degree == 3:
        discriminant = (2*b)**2 - 4*(3*a)*c
        if discriminant >= 0:
            x1 = (-2*b + np.sqrt(discriminant)) / (6*a)
            x2 = (-2*b - np.sqrt(discriminant)) / (6*a)
            y1 = a*x1**3 + b*x1**2 + c*x1 + d
            y2 = a*x2**3 + b*x2**2 + c*x2 + d
            
            # Plot critical points
            ax.plot([x1, x2], [y1, y2], '^', markersize=14, color='green',
                   label='Critical Points', markeredgecolor='darkgreen', 
                   markeredgewidth=2, markerfacecolor='lightgreen', zorder=10)

    # Add shading to show positive/negative regions
    ax.fill_between(x_vals, 0, y_vals, where=(y_vals > 0), 
                    interpolate=True, alpha=0.15, color='blue')
    ax.fill_between(x_vals, 0, y_vals, where=(y_vals < 0), 
                    interpolate=True, alpha=0.15, color='red')

    # Set title
    ax.set_title(f"Graph of Polynomial Function", 
                 fontsize=22, fontweight='bold', pad=30)
    
    # Add equation in a very prominent box at the top
    equation_text = f"y = {equation}"
    props_eq = dict(boxstyle='round,pad=1', facecolor='lightblue', 
                   edgecolor='darkblue', linewidth=4, alpha=0.95)
    ax.text(0.5, 0.92, equation_text, transform=ax.transAxes, 
            fontsize=24, fontweight='bold', ha='center', va='center', 
            bbox=props_eq, color='darkblue')
    
    # Add text box with root information
    if real_roots:
        root_info = "Zeros (x-intercepts):\n"
        for root in sorted(real_roots):
            if abs(root - round(root)) < 0.001:
                root_info += f"x = {int(round(root))}\n"
            else:
                root_info += f"x = {root:.3f}\n"
        
        props = dict(boxstyle='round,pad=0.5', facecolor='lightyellow', 
                    edgecolor='darkgoldenrod', linewidth=2, alpha=0.9)
        ax.text(0.02, 0.98, root_info.strip(), transform=ax.transAxes, 
                fontsize=14, verticalalignment='top', bbox=props)
    
    # Set y-limits with padding
    y_min, y_max = min(y_vals), max(y_vals)
    y_range = y_max - y_min
    y_padding = y_range * 0.15
    ax.set_ylim(y_min - y_padding, y_max + y_padding)
    
    # Set x-limits
    ax.set_xlim(x_min, x_max)
    
    # Enhance legend
    ax.legend(loc='lower right', fontsize=14, framealpha=0.95, edgecolor='black')
    
    # Make tick labels larger and cleaner
    ax.tick_params(axis='both', which='major', labelsize=14)
    
    # Adjust tick label positions to avoid overlapping with axes
    ax.xaxis.set_tick_params(pad=10)
    ax.yaxis.set_tick_params(pad=10)
    
    # Remove tick labels at origin to avoid clutter
    xticks = ax.get_xticks()
    yticks = ax.get_yticks()
    
    # Filter out zero from tick labels
    xticks_filtered = [t for t in xticks if abs(t) > 0.1]
    yticks_filtered = [t for t in yticks if abs(t) > 0.1]
    
    ax.set_xticks(xticks_filtered)
    ax.set_yticks(yticks_filtered)
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    return save_path