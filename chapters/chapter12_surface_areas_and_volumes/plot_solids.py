import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
import os

# Use π = 22/7 for all calculations
PI = 22/7

def format_calculation(expression, value):
    """Format calculation with π = 22/7."""
    return f"{expression} = {value:.2f}"

def calculate_areas(shape_type, params):
    """Calculate areas and volumes for different shapes."""
    if shape_type == "sphere":
        radius = params["radius"]
        volume = (4/3) * PI * radius**3
        surface_area = 4 * PI * radius**2
        return {
            "Volume": f"⁴⁄₃πr³ = ⁴⁄₃ × ²²⁄₇ × {radius}³ = {volume:.2f} cm³",
            "Surface Area": f"4πr² = 4 × ²²⁄₇ × {radius}² = {surface_area:.2f} cm²"
        }
    
    elif shape_type == "hemisphere":
        radius = params["radius"]
        volume = (2/3) * PI * radius**3
        csa = 2 * PI * radius**2
        tsa = 3 * PI * radius**2
        return {
            "Volume": f"⅔πr³ = ⅔ × ²²⁄₇ × {radius}³ = {volume:.2f} cm³",
            "Curved Surface Area": f"2πr² = 2 × ²²⁄₇ × {radius}² = {csa:.2f} cm²",
            "Total Surface Area": f"3πr² = 3 × ²²⁄₇ × {radius}² = {tsa:.2f} cm²"
        }
    
    elif shape_type == "cube":
        side = params["side"]
        volume = side**3
        tsa = 6 * side**2
        lsa = 4 * side**2
        return {
            "Volume": f"a³ = {side}³ = {volume:.2f} cm³",
            "Total Surface Area": f"6a² = 6 × {side}² = {tsa:.2f} cm²",
            "Lateral Surface Area": f"4a² = 4 × {side}² = {lsa:.2f} cm²"
        }
    
    elif shape_type == "cuboid":
        l, b, h = params["length"], params["breadth"], params["height"]
        volume = l * b * h
        tsa = 2 * (l*b + b*h + h*l)
        lsa = 2 * h * (l + b)
        return {
            "Volume": f"l × b × h = {l} × {b} × {h} = {volume:.2f} cm³",
            "Total Surface Area": f"2(lb + bh + hl) = 2({l}×{b} + {b}×{h} + {h}×{l}) = {tsa:.2f} cm²",
            "Lateral Surface Area": f"2h(l + b) = 2×{h}({l} + {b}) = {lsa:.2f} cm²"
        }
    
    elif shape_type == "cylinder":
        r, h = params["radius"], params["height"]
        volume = PI * r**2 * h
        csa = 2 * PI * r * h
        tsa = 2 * PI * r * (r + h)
        return {
            "Volume": f"πr²h = ²²⁄₇ × {r}² × {h} = {volume:.2f} cm³",
            "Curved Surface Area": f"2πrh = 2 × ²²⁄₇ × {r} × {h} = {csa:.2f} cm²",
            "Total Surface Area": f"2πr(r + h) = 2 × ²²⁄₇ × {r} × ({r} + {h}) = {tsa:.2f} cm²"
        }
    
    elif shape_type == "cone":
        r, h = params["radius"], params["height"]
        l = (r**2 + h**2)**0.5  # slant height
        volume = (1/3) * PI * r**2 * h
        csa = PI * r * l
        tsa = PI * r * (r + l)
        return {
            "Volume": f"⅓πr²h = ⅓ × ²²⁄₇ × {r}² × {h} = {volume:.2f} cm³",
            "Curved Surface Area": f"πrl = ²²⁄₇ × {r} × {l:.2f} = {csa:.2f} cm²",
            "Total Surface Area": f"πr(r + l) = ²²⁄₇ × {r} × ({r} + {l:.2f}) = {tsa:.2f} cm²",
            "Slant Height": f"l = √(r² + h²) = √({r}² + {h}²) = {l:.2f} cm"
        }
    
    return {}

def plot_cylinder(radius, height, save_name="cylinder_plot.png"):
    """
    Creates a 3D plot of a cylinder.
    """
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Create cylinder
    z = np.linspace(0, height, 50)
    theta = np.linspace(0, 2 * np.pi, 50)
    theta_grid, z_grid = np.meshgrid(theta, z)
    x_grid = radius * np.cos(theta_grid)
    y_grid = radius * np.sin(theta_grid)
    
    # Plot surface
    ax.plot_surface(x_grid, y_grid, z_grid, alpha=0.7, color='lightblue', edgecolor='none')
    
    # Plot top and bottom circles
    circle_theta = np.linspace(0, 2 * np.pi, 50)
    circle_x = radius * np.cos(circle_theta)
    circle_y = radius * np.sin(circle_theta)
    
    # Bottom circle
    ax.plot(circle_x, circle_y, 0, 'b-', linewidth=2)
    ax.plot_surface(circle_x.reshape(1, -1), circle_y.reshape(1, -1), 
                    np.zeros_like(circle_x).reshape(1, -1), alpha=0.7, color='lightblue')
    
    # Top circle
    ax.plot(circle_x, circle_y, height, 'b-', linewidth=2)
    ax.plot_surface(circle_x.reshape(1, -1), circle_y.reshape(1, -1), 
                    np.full_like(circle_x, height).reshape(1, -1), alpha=0.7, color='lightblue')
    
    # Labels and formatting
    ax.set_xlabel('X', fontsize=12)
    ax.set_ylabel('Y', fontsize=12)
    ax.set_zlabel('Z', fontsize=12)
    ax.set_title(f'Cylinder\nRadius = {radius}, Height = {height} cm', fontsize=16, fontweight='bold')
    
    # Add dimension annotations
    ax.text(0, 0, height/2, f'h = {height}', fontsize=12, color='red')
    ax.text(radius, 0, 0, f'r = {radius}', fontsize=12, color='red')
    
    # Calculate and display areas
    areas = calculate_areas("cylinder", {"radius": radius, "height": height})
    area_text = "\n".join([f"{k}:\n{v}" for k, v in areas.items()])
    ax.text2D(0.02, 0.98, area_text, transform=ax.transAxes, fontsize=10,
              bbox=dict(facecolor='white', alpha=0.8))
    
    ax.set_box_aspect([1,1,height/radius])
    
    save_dir = os.path.join(os.path.dirname(__file__), "plots")
    os.makedirs(save_dir, exist_ok=True)
    save_path = os.path.join(save_dir, save_name)
    plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.close()
    return save_path

def plot_cone(radius, height, save_name="cone_plot.png"):
    """
    Creates a 3D plot of a cone.
    """
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Create cone
    z = np.linspace(0, height, 50)
    theta = np.linspace(0, 2 * np.pi, 50)
    
    R = radius * (1 - z/height)  # Radius decreases linearly with height
    Z, Theta = np.meshgrid(z, theta)
    X = R * np.cos(Theta)
    Y = R * np.sin(Theta)
    
    # Plot surface
    ax.plot_surface(X.T, Y.T, Z.T, alpha=0.7, color='lightcoral', edgecolor='none')
    
    # Plot base circle
    circle_theta = np.linspace(0, 2 * np.pi, 50)
    circle_x = radius * np.cos(circle_theta)
    circle_y = radius * np.sin(circle_theta)
    ax.plot(circle_x, circle_y, 0, 'r-', linewidth=2)
    
    # Fill base
    ax.plot_surface(circle_x.reshape(1, -1), circle_y.reshape(1, -1), 
                    np.zeros_like(circle_x).reshape(1, -1), alpha=0.7, color='lightcoral')
    
    # Plot apex
    ax.scatter([0], [0], [height], color='red', s=50)
    
    # Calculate slant height
    slant_height = np.sqrt(radius**2 + height**2)
    
    # Labels
    ax.set_xlabel('X', fontsize=12)
    ax.set_ylabel('Y', fontsize=12)
    ax.set_zlabel('Z', fontsize=12)
    ax.set_title(f'Cone\nRadius = {radius}, Height = {height} cm\nSlant Height = {slant_height:.2f} cm', 
                 fontsize=16, fontweight='bold')
    
    # Add dimension annotations
    ax.text(0, 0, height/2, f'h = {height}', fontsize=12, color='red')
    ax.text(radius/2, 0, 0, f'r = {radius}', fontsize=12, color='red')
    
    # Draw slant height line
    ax.plot([radius, 0], [0, 0], [0, height], 'r--', linewidth=2)
    ax.text(radius/2, 0, height/2, f'l = {slant_height:.1f}', fontsize=12, color='red')
    
    # Calculate and display areas
    areas = calculate_areas("cone", {"radius": radius, "height": height})
    area_text = "\n".join([f"{k}:\n{v}" for k, v in areas.items()])
    ax.text2D(0.02, 0.98, area_text, transform=ax.transAxes, fontsize=10,
              bbox=dict(facecolor='white', alpha=0.8))
    
    ax.set_box_aspect([1,1,height/radius])
    
    save_dir = os.path.join(os.path.dirname(__file__), "plots")
    os.makedirs(save_dir, exist_ok=True)
    save_path = os.path.join(save_dir, save_name)
    plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.close()
    return save_path

def plot_sphere(radius, is_hemisphere=False, save_name="sphere_plot.png"):
    """
    Creates a 3D plot of a sphere or hemisphere.
    """
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Create sphere
    u = np.linspace(0, 2 * np.pi, 50)
    if is_hemisphere:
        v = np.linspace(0, np.pi/2, 25)  # Only upper hemisphere
    else:
        v = np.linspace(0, np.pi, 50)  # Full sphere
    
    x = radius * np.outer(np.cos(u), np.sin(v))
    y = radius * np.outer(np.sin(u), np.sin(v))
    z = radius * np.outer(np.ones(np.size(u)), np.cos(v))
    
    # Plot surface
    ax.plot_surface(x, y, z, alpha=0.7, color='lightgreen', edgecolor='none')
    
    if is_hemisphere:
        # Add base circle for hemisphere
        circle_theta = np.linspace(0, 2 * np.pi, 50)
        circle_x = radius * np.cos(circle_theta)
        circle_y = radius * np.sin(circle_theta)
        ax.plot(circle_x, circle_y, 0, 'g-', linewidth=2)
        
        # Fill base
        ax.plot_surface(circle_x.reshape(1, -1), circle_y.reshape(1, -1), 
                        np.zeros_like(circle_x).reshape(1, -1), alpha=0.7, color='lightgreen')
    
    # Labels
    ax.set_xlabel('X', fontsize=12)
    ax.set_ylabel('Y', fontsize=12)
    ax.set_zlabel('Z', fontsize=12)
    
    shape_name = "Hemisphere" if is_hemisphere else "Sphere"
    ax.set_title(f'{shape_name}\nRadius = {radius} cm', fontsize=16, fontweight='bold')
    
    # Add radius annotation
    ax.plot([0, radius], [0, 0], [0, 0], 'r-', linewidth=2)
    ax.text(radius/2, 0, 0, f'r = {radius}', fontsize=12, color='red')
    
    # Calculate and display areas
    areas = calculate_areas("hemisphere" if is_hemisphere else "sphere", {"radius": radius})
    area_text = "\n".join([f"{k}:\n{v}" for k, v in areas.items()])
    ax.text2D(0.02, 0.98, area_text, transform=ax.transAxes, fontsize=10,
              bbox=dict(facecolor='white', alpha=0.8))
    
    ax.set_box_aspect([1,1,1])
    
    save_dir = os.path.join(os.path.dirname(__file__), "plots")
    os.makedirs(save_dir, exist_ok=True)
    save_path = os.path.join(save_dir, save_name)
    plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.close()
    return save_path

def plot_cuboid(length, breadth, height, save_name="cuboid_plot.png"):
    """
    Creates a 3D plot of a cuboid or cube.
    """
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Define vertices
    vertices = [
        [0, 0, 0], [length, 0, 0], [length, breadth, 0], [0, breadth, 0],  # bottom
        [0, 0, height], [length, 0, height], [length, breadth, height], [0, breadth, height]  # top
    ]
    vertices = np.array(vertices)
    
    # Define faces
    faces = [
        [vertices[0], vertices[1], vertices[5], vertices[4]],  # front
        [vertices[1], vertices[2], vertices[6], vertices[5]],  # right
        [vertices[2], vertices[3], vertices[7], vertices[6]],  # back
        [vertices[3], vertices[0], vertices[4], vertices[7]],  # left
        [vertices[0], vertices[1], vertices[2], vertices[3]],  # bottom
        [vertices[4], vertices[5], vertices[6], vertices[7]]   # top
    ]
    
    # Create collection of faces
    face_collection = Poly3DCollection(faces, alpha=0.7, facecolor='lightblue', edgecolor='darkblue')
    ax.add_collection3d(face_collection)
    
    # Plot edges
    edges = [
        [0, 1], [1, 2], [2, 3], [3, 0],  # bottom edges
        [4, 5], [5, 6], [6, 7], [7, 4],  # top edges
        [0, 4], [1, 5], [2, 6], [3, 7]   # vertical edges
    ]
    
    for edge in edges:
        points = vertices[edge]
        ax.plot3D(*points.T, 'b-', linewidth=2)
    
    # Labels
    ax.set_xlabel('X', fontsize=12)
    ax.set_ylabel('Y', fontsize=12)
    ax.set_zlabel('Z', fontsize=12)
    
    # Check if it's a cube
    if length == breadth == height:
        ax.set_title(f'Cube\nSide = {length} cm', fontsize=16, fontweight='bold')
        # Add dimension annotation
        ax.text(length/2, 0, -0.5, f'a = {length}', fontsize=12, color='red', ha='center')
        # Calculate and display areas
        areas = calculate_areas("cube", {"side": length})
    else:
        ax.set_title(f'Cuboid\nLength = {length}, Breadth = {breadth}, Height = {height} cm', 
                     fontsize=16, fontweight='bold')
        # Add dimension annotations
        ax.text(length/2, 0, -0.5, f'l = {length}', fontsize=12, color='red', ha='center')
        ax.text(length+0.5, breadth/2, 0, f'b = {breadth}', fontsize=12, color='red', ha='center')
        ax.text(0, -0.5, height/2, f'h = {height}', fontsize=12, color='red', ha='center')
        # Calculate and display areas
        areas = calculate_areas("cuboid", {"length": length, "breadth": breadth, "height": height})
    
    # Display areas
    area_text = "\n".join([f"{k}:\n{v}" for k, v in areas.items()])
    ax.text2D(0.02, 0.98, area_text, transform=ax.transAxes, fontsize=10,
              bbox=dict(facecolor='white', alpha=0.8))
    
    # Set limits
    ax.set_xlim([-1, length+1])
    ax.set_ylim([-1, breadth+1])
    ax.set_zlim([-1, height+1])
    
    ax.set_box_aspect([length, breadth, height])
    
    save_dir = os.path.join(os.path.dirname(__file__), "plots")
    os.makedirs(save_dir, exist_ok=True)
    save_path = os.path.join(save_dir, save_name)
    plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.close()
    return save_path

def plot_combined_solid(radius, height=None, save_name="combined_solid_plot.png"):
    """Creates a 3D plot of a cone standing on a hemisphere."""
    if height is None:
        height = radius  # If height not provided, use radius as height
    
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Create hemisphere
    u = np.linspace(0, 2 * np.pi, 50)
    v = np.linspace(0, np.pi/2, 25)  # Only lower hemisphere
    x_hemi = radius * np.outer(np.cos(u), np.sin(v))
    y_hemi = radius * np.outer(np.sin(u), np.sin(v))
    z_hemi = radius * np.outer(np.ones(np.size(u)), np.cos(v))
    
    # Plot hemisphere surface
    ax.plot_surface(x_hemi, y_hemi, -z_hemi, alpha=0.7, color='lightgreen', edgecolor='none')
    
    # Create cone
    z = np.linspace(0, height, 50)
    theta = np.linspace(0, 2 * np.pi, 50)
    
    R = radius * (1 - z/height)  # Radius decreases linearly with height
    Z, Theta = np.meshgrid(z, theta)
    X = R * np.cos(Theta)
    Y = R * np.sin(Theta)
    
    # Plot cone surface
    ax.plot_surface(X.T, Y.T, Z.T, alpha=0.7, color='lightcoral', edgecolor='none')
    
    # Plot base circle
    circle_theta = np.linspace(0, 2 * np.pi, 50)
    circle_x = radius * np.cos(circle_theta)
    circle_y = radius * np.sin(circle_theta)
    ax.plot(circle_x, circle_y, 0, 'b-', linewidth=2)
    
    # Fill base
    ax.plot_surface(circle_x.reshape(1, -1), circle_y.reshape(1, -1), 
                    np.zeros_like(circle_x).reshape(1, -1), alpha=0.7, color='lightcoral')
    
    # Plot apex
    ax.scatter([0], [0], [height], color='red', s=50)
    
    # Calculate slant height
    slant_height = np.sqrt(radius**2 + height**2)
    
    # Labels
    ax.set_xlabel('X', fontsize=12)
    ax.set_ylabel('Y', fontsize=12)
    ax.set_zlabel('Z', fontsize=12)
    ax.set_title(f'Cone on Hemisphere\nRadius = {radius}, Height = {height} cm\nSlant Height = {slant_height:.2f} cm', 
                 fontsize=16, fontweight='bold')
    
    # Add dimension annotations
    ax.text(0, 0, height/2, f'h = {height}', fontsize=12, color='red')
    ax.text(radius/2, 0, 0, f'r = {radius}', fontsize=12, color='red')
    
    # Calculate volumes
    hemisphere_volume = (2/3) * PI * radius**3
    cone_volume = (1/3) * PI * radius**2 * height
    total_volume = hemisphere_volume + cone_volume
    
    # Add volume calculations
    volume_text = (f"Total Volume = Hemisphere Volume + Cone Volume\n"
                  f"= ⅔πr³ + ⅓πr²h\n"
                  f"= ⅔ × ²²⁄₇ × {radius}³ + ⅓ × ²²⁄₇ × {radius}² × {height}\n"
                  f"= {hemisphere_volume:.2f} + {cone_volume:.2f}\n"
                  f"= {total_volume:.2f} cm³")
    ax.text2D(0.02, 0.98, volume_text, transform=ax.transAxes, fontsize=10,
              bbox=dict(facecolor='white', alpha=0.8))
    
    ax.set_box_aspect([1,1,height/radius])
    
    save_dir = os.path.join(os.path.dirname(__file__), "plots")
    os.makedirs(save_dir, exist_ok=True)
    save_path = os.path.join(save_dir, save_name)
    plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.close()
    return save_path

def create_2d_net(solid_type, params, save_name="net_diagram.png"):
    """
    Creates 2D net diagrams for solids.
    """
    fig, ax = plt.subplots(figsize=(10, 8))
    
    if solid_type == "cube":
        side = params.get("side", 5)
        
        # Draw cube net (cross pattern)
        # Central square
        central = plt.Rectangle((side, side), side, side, fill=False, edgecolor='black', linewidth=2)
        ax.add_patch(central)
        ax.text(side + side/2, side + side/2, 'Base', ha='center', va='center', fontsize=12)
        
        # Top square
        top = plt.Rectangle((side, 2*side), side, side, fill=False, edgecolor='black', linewidth=2)
        ax.add_patch(top)
        ax.text(side + side/2, 2*side + side/2, 'Top', ha='center', va='center', fontsize=12)
        
        # Bottom square
        bottom = plt.Rectangle((side, 0), side, side, fill=False, edgecolor='black', linewidth=2)
        ax.add_patch(bottom)
        ax.text(side + side/2, side/2, 'Bottom', ha='center', va='center', fontsize=12)
        
        # Left square
        left = plt.Rectangle((0, side), side, side, fill=False, edgecolor='black', linewidth=2)
        ax.add_patch(left)
        ax.text(side/2, side + side/2, 'Left', ha='center', va='center', fontsize=12)
        
        # Right square
        right = plt.Rectangle((2*side, side), side, side, fill=False, edgecolor='black', linewidth=2)
        ax.add_patch(right)
        ax.text(2*side + side/2, side + side/2, 'Right', ha='center', va='center', fontsize=12)
        
        # Far right square (back)
        back = plt.Rectangle((3*side, side), side, side, fill=False, edgecolor='black', linewidth=2)
        ax.add_patch(back)
        ax.text(3*side + side/2, side + side/2, 'Back', ha='center', va='center', fontsize=12)
        
        ax.set_xlim(-0.5, 4*side + 0.5)
        ax.set_ylim(-0.5, 3*side + 0.5)
        ax.set_title(f'Net Diagram of Cube (side = {side})', fontsize=16, fontweight='bold')
        
    elif solid_type == "cylinder":
        radius = params.get("radius", 3)
        height = params.get("height", 8)
        
        # Draw rectangle for curved surface
        rect_width = 2 * np.pi * radius
        rect = plt.Rectangle((0, radius), rect_width, height, fill=False, edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        ax.text(rect_width/2, radius + height/2, f'Curved Surface\n(2πr × h)', ha='center', va='center', fontsize=12)
        
        # Draw two circles
        circle1 = plt.Circle((rect_width/4, 0), radius, fill=False, edgecolor='black', linewidth=2)
        circle2 = plt.Circle((3*rect_width/4, 0), radius, fill=False, edgecolor='black', linewidth=2)
        ax.add_patch(circle1)
        ax.add_patch(circle2)
        ax.text(rect_width/4, 0, 'Base', ha='center', va='center', fontsize=10)
        ax.text(3*rect_width/4, 0, 'Top', ha='center', va='center', fontsize=10)
        
        ax.set_xlim(-radius-1, rect_width+radius+1)
        ax.set_ylim(-radius-1, radius+height+1)
        ax.set_title(f'Net Diagram of Cylinder (r = {radius}, h = {height})', fontsize=16, fontweight='bold')
    
    ax.set_aspect('equal')
    ax.axis('off')
    
    save_dir = os.path.join(os.path.dirname(__file__), "plots")
    os.makedirs(save_dir, exist_ok=True)
    save_path = os.path.join(save_dir, save_name)
    plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.close()
    return save_path