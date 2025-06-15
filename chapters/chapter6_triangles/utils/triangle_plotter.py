import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple, Dict, Any
from .triangle_base import TriangleBase

class TrianglePlotter:
    def __init__(self):
        self.base = TriangleBase()
        self.config = self.base.config["plotting"]
    
    def plot_triangle(self, sides: List[float], title: str = "Triangle", 
                     color: str = "blue", alpha: float = 0.3) -> plt.Figure:
        """Plot a single triangle given its sides."""
        # Calculate coordinates using law of cosines
        a, b, c = sides
        cos_A = (b**2 + c**2 - a**2) / (2 * b * c)
        sin_A = np.sqrt(1 - cos_A**2)
        
        # Set up coordinates
        x = [0, c, b * cos_A, 0]
        y = [0, 0, b * sin_A, 0]
        
        # Create figure
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.plot(x, y, color=color, linewidth=2)
        ax.fill(x, y, color=color, alpha=alpha)
        
        # Add labels
        ax.text(-0.2, -0.2, 'A', fontsize=12)
        ax.text(c + 0.1, -0.2, 'B', fontsize=12)
        ax.text(b * cos_A - 0.2, b * sin_A + 0.1, 'C', fontsize=12)
        
        # Add side lengths
        ax.text(c/2, -0.3, f'a={a:.1f}', fontsize=10)
        ax.text(b * cos_A/2, b * sin_A/2, f'b={b:.1f}', fontsize=10)
        ax.text((c + b * cos_A)/2, b * sin_A/2, f'c={c:.1f}', fontsize=10)
        
        # Set equal aspect ratio and remove axes
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_title(title)
        
        return fig
    
    def plot_similar_triangles(self, triangle1: List[float], triangle2: List[float], 
                             scale_factor: float = 1.0) -> plt.Figure:
        """Plot two similar triangles with their corresponding sides."""
        # Create figure with two subplots
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        
        # Plot first triangle directly on ax1
        self._plot_triangle_on_axis(ax1, triangle1, "Triangle 1", "blue", 0.3)
        
        # Plot second triangle directly on ax2  
        self._plot_triangle_on_axis(ax2, triangle2, "Triangle 2", "red", 0.3)
        
        # Add scale factor information
        fig.suptitle(f"Similar Triangles (Scale Factor: {scale_factor:.3f})", fontsize=16, fontweight='bold')
        
        # Add similarity information
        area1 = self._calculate_area_heron(triangle1)
        area2 = self._calculate_area_heron(triangle2)
        area_ratio = area2 / area1
        
        info_text = f'Triangle 1 Area: {area1:.2f} units²\n'
        info_text += f'Triangle 2 Area: {area2:.2f} units²\n'
        info_text += f'Area Ratio: {area_ratio:.3f}\n'
        info_text += f'Expected Area Ratio: {scale_factor**2:.3f}'
        
        fig.text(0.5, 0.02, info_text, ha='center', fontsize=11,
                bbox=dict(boxstyle='round,pad=0.5', facecolor='lightyellow', alpha=0.9))
        
        plt.tight_layout()
        return fig
    
    def _plot_triangle_on_axis(self, ax, sides: List[float], title: str, color: str, alpha: float):
        """Helper method to plot a triangle directly on a given axis."""
        # Calculate coordinates using law of cosines
        a, b, c = sides
        
        # Ensure valid triangle
        if not (a + b > c and b + c > a and a + c > b):
            ax.text(0.5, 0.5, f'Invalid Triangle\n{sides}', 
                   ha='center', va='center', transform=ax.transAxes,
                   fontsize=12, color='red')
            ax.set_title(title)
            ax.axis('off')
            return
        
        cos_A = (b**2 + c**2 - a**2) / (2 * b * c)
        cos_A = max(-1, min(1, cos_A))  # Clamp to valid range
        sin_A = np.sqrt(1 - cos_A**2)
        
        # Set up coordinates
        x = [0, c, b * cos_A, 0]
        y = [0, 0, b * sin_A, 0]
        
        # Plot triangle
        ax.plot(x, y, color=color, linewidth=2)
        ax.fill(x, y, color=color, alpha=alpha)
        
        # Add vertex labels
        ax.text(-0.15, -0.15, 'A', fontsize=12, fontweight='bold')
        ax.text(c + 0.05, -0.15, 'B', fontsize=12, fontweight='bold')
        ax.text(b * cos_A - 0.15, b * sin_A + 0.05, 'C', fontsize=12, fontweight='bold')
        
        # Add side lengths with better positioning
        ax.text(c/2, -0.25, f'{a:.1f}', fontsize=10, ha='center', 
               bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.8))
        ax.text(b * cos_A/2 - 0.2, b * sin_A/2, f'{b:.1f}', fontsize=10, ha='center',
               bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.8))
        ax.text((c + b * cos_A)/2 + 0.1, b * sin_A/2, f'{c:.1f}', fontsize=10, ha='center',
               bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.8))
        
        # Set equal aspect ratio and clean up axes
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_title(title, fontsize=14, fontweight='bold')
        
        # Set reasonable axis limits with padding
        max_coord = max(max(x), max(y))
        padding = max_coord * 0.2
        ax.set_xlim(-padding, max_coord + padding)
        ax.set_ylim(-padding, max_coord + padding)
    
    def plot_right_triangle(self, base: float, height: float) -> plt.Figure:
        """Plot a right triangle given base and height."""
        # Calculate hypotenuse
        hypotenuse = np.sqrt(base**2 + height**2)
        
        # Set up coordinates
        x = [0, base, 0, 0]
        y = [0, 0, height, 0]
        
        # Create figure
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.plot(x, y, color='blue', linewidth=2)
        ax.fill(x, y, color='blue', alpha=0.3)
        
        # Add labels
        ax.text(-0.2, -0.2, 'A', fontsize=12, fontweight='bold')
        ax.text(base + 0.1, -0.2, 'B', fontsize=12, fontweight='bold')
        ax.text(-0.2, height + 0.1, 'C', fontsize=12, fontweight='bold')
        
        # Add side lengths
        ax.text(base/2, -0.3, f'Base = {base:.1f} cm', fontsize=11, ha='center',
               bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.7))
        ax.text(-0.4, height/2, f'Height = {height:.1f} cm', fontsize=11, ha='center', rotation=90,
               bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.7))
        ax.text(base/2, height/2, f'Hypotenuse = {hypotenuse:.1f} cm', fontsize=11, ha='center',
               bbox=dict(boxstyle='round,pad=0.3', facecolor='orange', alpha=0.7))
        
        # Add right angle marker
        right_angle_size = min(base, height) * 0.1
        ax.plot([0, right_angle_size], [0, 0], 'k-', linewidth=1)
        ax.plot([0, 0], [0, right_angle_size], 'k-', linewidth=1)
        ax.plot([right_angle_size, right_angle_size], [0, right_angle_size], 'k-', linewidth=1)
        ax.plot([0, right_angle_size], [right_angle_size, right_angle_size], 'k-', linewidth=1)
        
        # Add 90° label
        ax.text(right_angle_size/2, right_angle_size/2, '90°', fontsize=10, ha='center', va='center',
               color='red', fontweight='bold')
        
        # Calculate and display angles
        angle_B = np.degrees(np.arctan(height / base))
        angle_C = 90 - angle_B
        
        ax.text(base * 0.8, height * 0.1, f'{angle_B:.1f}°', fontsize=10, color='red', fontweight='bold')
        ax.text(base * 0.1, height * 0.8, f'{angle_C:.1f}°', fontsize=10, color='red', fontweight='bold')
        
        # Set equal aspect ratio and remove axes
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_title("Right Triangle", fontsize=16, fontweight='bold', pad=20)
        
        # Set axis limits with padding
        margin = max(base, height) * 0.2
        ax.set_xlim(-margin, base + margin)
        ax.set_ylim(-margin, height + margin)
        
        # Add grid for better visualization
        ax.grid(True, alpha=0.3)
        
        return fig
    
    def plot_bpt_theorem(self, segments: List[float]) -> plt.Figure:
        """Plot Basic Proportionality Theorem scenario."""
        if len(segments) < 4:
            raise ValueError("Need at least 4 segments for BPT plot")
            
        AD, DB, AE, EC = segments[:4]
        
        # Create figure
        fig, ax = plt.subplots(figsize=(10, 7))
        
        # Calculate proportional coordinates
        total_base = AD + DB
        total_height = AE + EC
        
        # Scale for better visualization
        scale = 8
        base_scale = scale
        height_scale = scale * (total_height / total_base)
        
        # Main triangle vertices
        A = [0, 0]
        B = [base_scale, 0]
        C = [base_scale * 0.4, height_scale]
        
        # Points D and E based on ratios
        D_ratio = AD / total_base
        E_ratio = AE / total_height
        
        D = [base_scale * D_ratio, 0]
        E = [C[0] * E_ratio, C[1] * E_ratio]
        
        # Plot main triangle ABC
        triangle_x = [A[0], B[0], C[0], A[0]]
        triangle_y = [A[1], B[1], C[1], A[1]]
        ax.plot(triangle_x, triangle_y, 'b-', linewidth=3, label='Triangle ABC')
        
        # Plot parallel line DE
        ax.plot([D[0], E[0]], [D[1], E[1]], 'r-', linewidth=3, label='Line DE')
        
        # Plot segments AD, DB, AE, EC with different colors for clarity
        ax.plot([A[0], D[0]], [A[1], D[1]], 'g-', linewidth=4, alpha=0.7, label=f'AD = {AD:.1f}')
        ax.plot([D[0], B[0]], [D[1], B[1]], 'm-', linewidth=4, alpha=0.7, label=f'DB = {DB:.1f}')
        ax.plot([A[0], E[0]], [A[1], E[1]], 'orange', linewidth=4, alpha=0.7, label=f'AE = {AE:.1f}')
        ax.plot([E[0], C[0]], [E[1], C[1]], 'purple', linewidth=4, alpha=0.7, label=f'EC = {EC:.1f}')
        
        # Add point labels
        offset = 0.2
        ax.text(A[0] - offset, A[1] - offset, 'A', fontsize=14, fontweight='bold')
        ax.text(B[0] + offset, B[1] - offset, 'B', fontsize=14, fontweight='bold')
        ax.text(C[0] - offset, C[1] + offset, 'C', fontsize=14, fontweight='bold')
        ax.text(D[0], D[1] - offset, 'D', fontsize=14, fontweight='bold', color='red')
        ax.text(E[0] - offset, E[1], 'E', fontsize=14, fontweight='bold', color='red')
        
        # Add ratios
        ratio1 = AD / DB
        ratio2 = AE / EC
        is_parallel = abs(ratio1 - ratio2) < 0.001
        
        # Add BPT verification text
        verification_text = f'AD/DB = {AD:.1f}/{DB:.1f} = {ratio1:.3f}\n'
        verification_text += f'AE/EC = {AE:.1f}/{EC:.1f} = {ratio2:.3f}\n'
        verification_text += f'Ratios equal? {"YES" if is_parallel else "NO"}\n'
        verification_text += f'Therefore: DE {"||" if is_parallel else "∦"} BC'
        
        ax.text(0.02, 0.98, verification_text, transform=ax.transAxes, fontsize=12,
               verticalalignment='top', 
               bbox=dict(boxstyle='round,pad=0.5', facecolor='lightyellow', alpha=0.9))
        
        # Set equal aspect ratio and clean up
        ax.set_aspect('equal')
        ax.legend(loc='upper right')
        ax.grid(True, alpha=0.3)
        ax.set_title("Basic Proportionality Theorem (Thales' Theorem)", fontsize=16, fontweight='bold')
        
        # Remove axis ticks for cleaner look
        ax.set_xticks([])
        ax.set_yticks([])
        
        return fig
    
    def _calculate_area_heron(self, sides: List[float]) -> float:
        """Calculate triangle area using Heron's formula."""
        a, b, c = sides
        s = (a + b + c) / 2  # semi-perimeter
        try:
            area = np.sqrt(s * (s - a) * (s - b) * (s - c))
            return area
        except:
            return 0.0