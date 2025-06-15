# File: chapters/chapter6_triangles/plot_triangles.py

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import math
from typing import List, Tuple
import os

def plot_triangle(sides: List[float], angles: List[float], filename: str = "triangle_plot.png") -> str:
    """
    Plot a triangle given its sides and angles.
    Returns the path to the saved plot.
    """
    try:
        # Create figure and axis
        fig, ax = plt.subplots(1, 1, figsize=(10, 8))
        ax.set_aspect('equal')
        
        # Calculate triangle coordinates
        points = calculate_triangle_coordinates(sides, angles)
        
        # Extract coordinates
        x_coords = [p[0] for p in points] + [points[0][0]]  # Close the triangle
        y_coords = [p[1] for p in points] + [points[0][1]]
        
        # Plot triangle
        ax.plot(x_coords, y_coords, 'b-', linewidth=3, label='Triangle')
        ax.fill(x_coords, y_coords, alpha=0.3, color='lightblue')
        
        # Add vertices
        ax.scatter([p[0] for p in points], [p[1] for p in points], 
                  c='red', s=100, zorder=5)
        
        # Label vertices
        labels = ['A', 'B', 'C']
        for i, (point, label) in enumerate(zip(points, labels)):
            ax.annotate(label, (point[0], point[1]), 
                       xytext=(5, 5), textcoords='offset points',
                       fontsize=14, fontweight='bold')
        
        # Label sides
        for i in range(3):
            p1, p2 = points[i], points[(i + 1) % 3]
            mid_x, mid_y = (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2
            side_length = sides[i]
            ax.annotate(f'{side_length:.1f} cm', (mid_x, mid_y),
                       xytext=(0, -15), textcoords='offset points',
                       ha='center', fontsize=12, 
                       bbox=dict(boxstyle='round,pad=0.2', facecolor='yellow', alpha=0.7))
        
        # Label angles
        for i in range(3):
            angle_pos = points[i]
            angle_value = angles[i]
            ax.annotate(f'{angle_value:.1f}°', angle_pos,
                       xytext=(10, 10), textcoords='offset points',
                       fontsize=11, color='red', fontweight='bold',
                       bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.8))
        
        # Set title and labels
        triangle_type = determine_triangle_type(sides, angles)
        ax.set_title(f'{triangle_type} Triangle\nSides: {sides[0]:.1f}, {sides[1]:.1f}, {sides[2]:.1f} cm', 
                    fontsize=16, fontweight='bold', pad=20)
        
        # Calculate area and perimeter
        area = calculate_area_heron(sides)
        perimeter = sum(sides)
        
        # Add info box
        info_text = f'Area: {area:.2f} cm²\nPerimeter: {perimeter:.1f} cm'
        ax.text(0.02, 0.98, info_text, transform=ax.transAxes, 
               verticalalignment='top', fontsize=12,
               bbox=dict(boxstyle='round,pad=0.5', facecolor='lightgreen', alpha=0.8))
        
        # Set axis limits with padding
        all_x = [p[0] for p in points]
        all_y = [p[1] for p in points]
        margin = max(max(sides) * 0.2, 1)
        
        ax.set_xlim(min(all_x) - margin, max(all_x) + margin)
        ax.set_ylim(min(all_y) - margin, max(all_y) + margin)
        
        # Remove axis ticks and labels for cleaner look
        ax.set_xticks([])
        ax.set_yticks([])
        
        # Add grid
        ax.grid(True, alpha=0.3)
        
        # Save plot
        plot_path = f"static/plots/{filename}"
        os.makedirs("static/plots", exist_ok=True)
        plt.savefig(plot_path, dpi=300, bbox_inches='tight', facecolor='white')
        plt.close()
        
        return plot_path
        
    except Exception as e:
        print(f"Error plotting triangle: {e}")
        return "Error creating plot"

def plot_similar_triangles(triangle1_data: Tuple[List[float], List[float]], 
                          triangle2_data: Tuple[List[float], List[float]], 
                          filename: str = "similar_triangles.png") -> str:
    """
    Plot two triangles side by side to show similarity.
    """
    try:
        sides1, angles1 = triangle1_data
        sides2, angles2 = triangle2_data
        
        # Create figure with subplots
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
        
        # Plot first triangle
        points1 = calculate_triangle_coordinates(sides1, angles1)
        plot_single_triangle(ax1, points1, sides1, angles1, "Triangle 1", 'lightblue')
        
        # Plot second triangle
        points2 = calculate_triangle_coordinates(sides2, angles2)
        plot_single_triangle(ax2, points2, sides2, angles2, "Triangle 2", 'lightcoral')
        
        # Calculate similarity ratio
        ratio = sides2[0] / sides1[0]
        
        # Add similarity information
        fig.suptitle(f'Similar Triangles Comparison\nScale Factor: {ratio:.2f}', 
                    fontsize=18, fontweight='bold')
        
        # Add similarity details
        info_text = f'Triangle 1 Area: {calculate_area_heron(sides1):.2f} cm²\n'
        info_text += f'Triangle 2 Area: {calculate_area_heron(sides2):.2f} cm²\n'
        info_text += f'Area Ratio: {(calculate_area_heron(sides2)/calculate_area_heron(sides1)):.2f}\n'
        info_text += f'Expected Area Ratio: {ratio**2:.2f}'
        
        fig.text(0.5, 0.02, info_text, ha='center', fontsize=12,
                bbox=dict(boxstyle='round,pad=0.5', facecolor='lightyellow', alpha=0.9))
        
        # Save plot
        plot_path = f"static/plots/{filename}"
        os.makedirs("static/plots", exist_ok=True)
        plt.savefig(plot_path, dpi=300, bbox_inches='tight', facecolor='white')
        plt.close()
        
        return plot_path
        
    except Exception as e:
        print(f"Error plotting similar triangles: {e}")
        return "Error creating plot"

def plot_single_triangle(ax, points: List[Tuple[float, float]], sides: List[float], 
                        angles: List[float], title: str, color: str):
    """Helper function to plot a single triangle on given axis."""
    
    # Extract coordinates
    x_coords = [p[0] for p in points] + [points[0][0]]
    y_coords = [p[1] for p in points] + [points[0][1]]
    
    # Plot triangle
    ax.plot(x_coords, y_coords, 'b-', linewidth=3)
    ax.fill(x_coords, y_coords, alpha=0.4, color=color)
    
    # Add vertices
    ax.scatter([p[0] for p in points], [p[1] for p in points], 
              c='red', s=100, zorder=5)
    
    # Label vertices
    labels = ['A', 'B', 'C']
    for i, (point, label) in enumerate(zip(points, labels)):
        ax.annotate(label, (point[0], point[1]), 
                   xytext=(5, 5), textcoords='offset points',
                   fontsize=14, fontweight='bold')
    
    # Label sides
    for i in range(3):
        p1, p2 = points[i], points[(i + 1) % 3]
        mid_x, mid_y = (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2
        side_length = sides[i]
        ax.annotate(f'{side_length:.1f}', (mid_x, mid_y),
                   xytext=(0, -15), textcoords='offset points',
                   ha='center', fontsize=11, 
                   bbox=dict(boxstyle='round,pad=0.2', facecolor='yellow', alpha=0.7))
    
    # Set title
    ax.set_title(title, fontsize=14, fontweight='bold')
    
    # Set equal aspect and clean up
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_xticks([])
    ax.set_yticks([])
    
    # Set limits with padding
    all_x = [p[0] for p in points]
    all_y = [p[1] for p in points]
    margin = max(max(sides) * 0.2, 1)
    
    ax.set_xlim(min(all_x) - margin, max(all_x) + margin)
    ax.set_ylim(min(all_y) - margin, max(all_y) + margin)

def calculate_triangle_coordinates(sides: List[float], angles: List[float]) -> List[Tuple[float, float]]:
    """
    Calculate triangle coordinates for plotting.
    Places first vertex at origin, second on x-axis.
    """
    a, b, c = sides
    
    # Place first point at origin
    A = (0.0, 0.0)
    
    # Place second point on x-axis
    B = (c, 0.0)  # Side c is between A and B
    
    # Calculate third point using law of cosines
    # We need angle A (at vertex A)
    angle_A_rad = math.radians(angles[0])
    
    # Point C coordinates
    C_x = b * math.cos(angle_A_rad)
    C_y = b * math.sin(angle_A_rad)
    C = (C_x, C_y)
    
    return [A, B, C]

def determine_triangle_type(sides: List[float], angles: List[float]) -> str:
    """Determine the type of triangle."""
    max_angle = max(angles)
    
    if abs(max_angle - 90) < 0.1:
        return "Right"
    elif max_angle > 90:
        return "Obtuse"
    else:
        return "Acute"

def calculate_area_heron(sides: List[float]) -> float:
    """Calculate triangle area using Heron's formula."""
    a, b, c = sides
    s = (a + b + c) / 2  # semi-perimeter
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def plot_right_triangle_special(base: float, height: float, filename: str = "right_triangle.png") -> str:
    """
    Special plotting function for right triangles with base and height.
    """
    try:
        fig, ax = plt.subplots(1, 1, figsize=(10, 8))
        ax.set_aspect('equal')
        
        # Right triangle coordinates
        A = (0, 0)      # Origin
        B = (base, 0)   # Base point
        C = (0, height) # Height point
        
        points = [A, B, C]
        x_coords = [0, base, 0, 0]
        y_coords = [0, 0, height, 0]
        
        # Plot triangle
        ax.plot(x_coords, y_coords, 'b-', linewidth=3)
        ax.fill(x_coords, y_coords, alpha=0.3, color='lightblue')
        
        # Add vertices
        ax.scatter([0, base, 0], [0, 0, height], c='red', s=100, zorder=5)
        
        # Label vertices
        ax.annotate('A', (0, 0), xytext=(-10, -10), textcoords='offset points',
                   fontsize=14, fontweight='bold')
        ax.annotate('B', (base, 0), xytext=(5, -10), textcoords='offset points',
                   fontsize=14, fontweight='bold')
        ax.annotate('C', (0, height), xytext=(-10, 5), textcoords='offset points',
                   fontsize=14, fontweight='bold')
        
        # Label sides
        ax.annotate(f'Base = {base} cm', (base/2, -0.1*height), ha='center', 
                   fontsize=12, bbox=dict(boxstyle='round,pad=0.2', facecolor='yellow', alpha=0.7))
        ax.annotate(f'Height = {height} cm', (-0.1*base, height/2), ha='center', rotation=90,
                   fontsize=12, bbox=dict(boxstyle='round,pad=0.2', facecolor='yellow', alpha=0.7))
        
        # Calculate and label hypotenuse
        hypotenuse = math.sqrt(base**2 + height**2)
        ax.annotate(f'Hypotenuse = {hypotenuse:.2f} cm', (base/2, height/2), 
                   xytext=(10, 10), textcoords='offset points',
                   fontsize=12, bbox=dict(boxstyle='round,pad=0.2', facecolor='orange', alpha=0.7))
        
        # Add right angle indicator
        right_angle_size = min(base, height) * 0.1
        square = patches.Rectangle((0, 0), right_angle_size, right_angle_size, 
                                 linewidth=2, edgecolor='red', facecolor='none')
        ax.add_patch(square)
        
        # Calculate angles
        angle_B = math.degrees(math.atan(height / base))
        angle_C = 90 - angle_B
        
        # Label angles
        ax.annotate('90°', (right_angle_size/2, right_angle_size/2), ha='center', va='center',
                   fontsize=11, color='red', fontweight='bold')
        ax.annotate(f'{angle_B:.1f}°', (base*0.8, height*0.1), 
                   fontsize=11, color='red', fontweight='bold')
        ax.annotate(f'{angle_C:.1f}°', (base*0.1, height*0.8), 
                   fontsize=11, color='red', fontweight='bold')
        
        # Title and info
        ax.set_title(f'Right Triangle\nBase: {base} cm, Height: {height} cm, Hypotenuse: {hypotenuse:.2f} cm', 
                    fontsize=16, fontweight='bold', pad=20)
        
        # Area and perimeter
        area = 0.5 * base * height
        perimeter = base + height + hypotenuse
        info_text = f'Area: {area:.2f} cm²\nPerimeter: {perimeter:.2f} cm'
        ax.text(0.98, 0.98, info_text, transform=ax.transAxes, 
               verticalalignment='top', horizontalalignment='right', fontsize=12,
               bbox=dict(boxstyle='round,pad=0.5', facecolor='lightgreen', alpha=0.8))
        
        # Set limits
        margin = max(base, height) * 0.2
        ax.set_xlim(-margin, base + margin)
        ax.set_ylim(-margin, height + margin)
        
        # Clean up axes
        ax.set_xticks([])
        ax.set_yticks([])
        ax.grid(True, alpha=0.3)
        
        # Save plot
        plot_path = f"static/plots/{filename}"
        os.makedirs("static/plots", exist_ok=True)
        plt.savefig(plot_path, dpi=300, bbox_inches='tight', facecolor='white')
        plt.close()
        
        return plot_path
        
    except Exception as e:
        print(f"Error plotting right triangle: {e}")
        return "Error creating plot"