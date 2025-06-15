import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import json
import os

class TrianglePlotter:
    def __init__(self):
        self.fig = None
        self.ax = None
        self.triangle_data = None
        self.load_triangle_data()
    
    def load_triangle_data(self):
        """Load triangle data from JSON file"""
        try:
            json_path = os.path.join(os.path.dirname(__file__), 'triangle.json')
            with open(json_path, 'r') as f:
                self.triangle_data = json.load(f)
        except FileNotFoundError:
            print("Warning: triangle.json not found. Using default values.")
            self.triangle_data = {
                "colors": {
                    "triangle": "#2E86C1",
                    "arc": "#E74C3C",
                    "text": "#2C3E50"
                },
                "styles": {
                    "line": "-",
                    "arc": "--"
                }
            }
    
    def plot_triangle(self, points, angles=None, show_angles=True, show_sides=True):
        """
        Plot a triangle with given points and angles
        
        Args:
            points: List of (x,y) coordinates for triangle vertices
            angles: List of angles in degrees (optional)
            show_angles: Whether to display angle values
            show_sides: Whether to display side lengths
        """
        self.fig, self.ax = plt.subplots(figsize=(10, 8))
        
        # Plot triangle
        x_coords = [p[0] for p in points]
        y_coords = [p[1] for p in points]
        x_coords.append(x_coords[0])  # Close the triangle
        y_coords.append(y_coords[0])
        
        # Plot triangle edges
        self.ax.plot(x_coords, y_coords, 
                    color=self.triangle_data['colors']['triangle'],
                    linestyle=self.triangle_data['styles']['line'],
                    linewidth=2)
        
        # Calculate and display angles if provided
        if angles and show_angles:
            self._plot_angles(points, angles)
        
        # Calculate and display side lengths if requested
        if show_sides:
            self._plot_side_lengths(points)
        
        # Set equal aspect ratio and remove axes
        self.ax.set_aspect('equal')
        self.ax.axis('off')
        
        # Add some padding around the triangle
        self._set_plot_limits(points)
        
        return self.fig
    
    def _plot_angles(self, points, angles):
        """Plot angle arcs and labels"""
        for i, (point, angle) in enumerate(zip(points, angles)):
            # Calculate angle arc parameters
            prev_point = points[i-1]
            next_point = points[(i+1) % 3]
            
            # Calculate vectors for angle
            v1 = np.array(prev_point) - np.array(point)
            v2 = np.array(next_point) - np.array(point)
            
            # Calculate angle arc radius (20% of shortest adjacent side)
            r1 = np.linalg.norm(v1)
            r2 = np.linalg.norm(v2)
            radius = min(r1, r2) * 0.2
            
            # Calculate start and end angles
            start_angle = np.degrees(np.arctan2(v1[1], v1[0]))
            end_angle = np.degrees(np.arctan2(v2[1], v2[0]))
            
            # Ensure proper angle direction
            if end_angle < start_angle:
                end_angle += 360
            
            # Create and add angle arc
            arc = Arc(point, 2*radius, 2*radius,
                     theta1=start_angle, theta2=end_angle,
                     color=self.triangle_data['colors']['arc'],
                     linestyle=self.triangle_data['styles']['arc'],
                     linewidth=1.5)
            self.ax.add_patch(arc)
            
            # Add angle label
            mid_angle = (start_angle + end_angle) / 2
            label_radius = radius * 1.3
            label_x = point[0] + label_radius * np.cos(np.radians(mid_angle))
            label_y = point[1] + label_radius * np.sin(np.radians(mid_angle))
            
            # Round angle to nearest integer
            angle_int = round(angle)
            self.ax.text(label_x, label_y, f'{angle_int}°',
                        color=self.triangle_data['colors']['text'],
                        ha='center', va='center',
                        fontsize=12, fontweight='bold')
    
    def _plot_side_lengths(self, points):
        """Plot side length labels"""
        for i in range(3):
            p1 = points[i]
            p2 = points[(i+1) % 3]
            
            # Calculate midpoint of side
            mid_x = (p1[0] + p2[0]) / 2
            mid_y = (p1[1] + p2[1]) / 2
            
            # Calculate side length
            length = np.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
            
            # Add side length label
            self.ax.text(mid_x, mid_y, f'{length:.1f}',
                        color=self.triangle_data['colors']['text'],
                        ha='center', va='center',
                        fontsize=10, fontweight='bold',
                        bbox=dict(facecolor='white', alpha=0.7, edgecolor='none'))
    
    def _set_plot_limits(self, points):
        """Set plot limits with padding"""
        x_coords = [p[0] for p in points]
        y_coords = [p[1] for p in points]
        
        x_min, x_max = min(x_coords), max(x_coords)
        y_min, y_max = min(y_coords), max(y_coords)
        
        # Add 20% padding
        x_padding = (x_max - x_min) * 0.2
        y_padding = (y_max - y_min) * 0.2
        
        self.ax.set_xlim(x_min - x_padding, x_max + x_padding)
        self.ax.set_ylim(y_min - y_padding, y_max + y_padding)
    
    def show(self):
        """Display the plot"""
        if self.fig:
            plt.show()
    
    def save(self, filename):
        """Save the plot to a file"""
        if self.fig:
            self.fig.savefig(filename, bbox_inches='tight', dpi=300)
            plt.close(self.fig) 