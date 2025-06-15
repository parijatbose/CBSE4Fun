import matplotlib.pyplot as plt
import numpy as np
import os

# Define π = 22/7 for calculations
PI = 22/7

def plot_sector(radius, angle, save_name="sector_plot.png"):
    """Plot a sector of a circle with given radius and angle."""
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(10, 10))
    
    # Plot the circle
    circle = plt.Circle((0, 0), radius, fill=False, color='blue')
    ax.add_artist(circle)
    
    # Calculate sector points
    theta = np.linspace(0, np.radians(angle), 100)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    
    # Plot the sector
    ax.fill_between(x, 0, y, color='lightblue', alpha=0.3)
    ax.plot(x, y, 'b-')
    
    # Plot radius lines
    ax.plot([0, radius], [0, 0], 'b-')
    ax.plot([0, radius*np.cos(np.radians(angle))], 
            [0, radius*np.sin(np.radians(angle))], 'b-')
    
    # Add angle arc
    arc_radius = radius * 0.3
    arc_theta = np.linspace(0, np.radians(angle), 100)
    arc_x = arc_radius * np.cos(arc_theta)
    arc_y = arc_radius * np.sin(arc_theta)
    ax.plot(arc_x, arc_y, 'r-')
    
    # Add labels
    ax.text(radius/2, -radius/10, f'r = {radius} cm', ha='center')
    ax.text(arc_radius/2, arc_radius/2, f'θ = {angle}°', ha='center')
    
    # Calculate and display area
    area = (angle/360) * PI * radius**2
    ax.text(-radius, radius, f'Area = {area:.2f} cm²', 
            bbox=dict(facecolor='white', alpha=0.8))
    
    # Set equal aspect ratio and limits
    ax.set_aspect('equal')
    ax.set_xlim(-radius*1.2, radius*1.2)
    ax.set_ylim(-radius*1.2, radius*1.2)
    
    # Remove axes
    ax.axis('off')
    
    # Create plots directory if it doesn't exist
    os.makedirs('chapters/chapter11_areas_circles/plots', exist_ok=True)
    
    # Save the plot
    plt.savefig(f'chapters/chapter11_areas_circles/plots/{save_name}', 
                bbox_inches='tight', dpi=300)
    plt.close()
    
    return f'chapters/chapter11_areas_circles/plots/{save_name}'

def plot_segment(radius, angle, save_name="segment_plot.png"):
    """Plot a segment of a circle with given radius and angle."""
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(10, 10))
    
    # Plot the circle
    circle = plt.Circle((0, 0), radius, fill=False, color='blue')
    ax.add_artist(circle)
    
    # Calculate segment points
    theta = np.linspace(0, np.radians(angle), 100)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    
    # Plot the segment
    ax.fill_between(x, 0, y, color='lightgreen', alpha=0.3)
    ax.plot(x, y, 'b-')
    
    # Plot chord
    chord_x = [radius, radius*np.cos(np.radians(angle))]
    chord_y = [0, radius*np.sin(np.radians(angle))]
    ax.plot(chord_x, chord_y, 'b-')
    
    # Add angle arc
    arc_radius = radius * 0.3
    arc_theta = np.linspace(0, np.radians(angle), 100)
    arc_x = arc_radius * np.cos(arc_theta)
    arc_y = arc_radius * np.sin(arc_theta)
    ax.plot(arc_x, arc_y, 'r-')
    
    # Add labels
    ax.text(radius/2, -radius/10, f'r = {radius} cm', ha='center')
    ax.text(arc_radius/2, arc_radius/2, f'θ = {angle}°', ha='center')
    
    # Calculate and display area
    sector_area = (angle/360) * PI * radius**2
    triangle_area = 0.5 * radius**2 * np.sin(np.radians(angle))
    segment_area = sector_area - triangle_area
    ax.text(-radius, radius, f'Area = {segment_area:.2f} cm²', 
            bbox=dict(facecolor='white', alpha=0.8))
    
    # Set equal aspect ratio and limits
    ax.set_aspect('equal')
    ax.set_xlim(-radius*1.2, radius*1.2)
    ax.set_ylim(-radius*1.2, radius*1.2)
    
    # Remove axes
    ax.axis('off')
    
    # Create plots directory if it doesn't exist
    os.makedirs('chapters/chapter11_areas_circles/plots', exist_ok=True)
    
    # Save the plot
    plt.savefig(f'chapters/chapter11_areas_circles/plots/{save_name}', 
                bbox_inches='tight', dpi=300)
    plt.close()
    
    return f'chapters/chapter11_areas_circles/plots/{save_name}'
