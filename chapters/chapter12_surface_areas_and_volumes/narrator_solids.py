def narrate_cylinder(radius, height, volume, csa, tsa):
    """
    Generate educational narration for cylinder.
    """
    return f"""
🔵 **Understanding the Cylinder:**

Imagine a circular disc of radius {radius} cm. Now, if we move this disc vertically upward by {height} cm, 
it traces out a cylinder!

**Key Features:**
• The cylinder has two circular bases (top and bottom) each with radius {radius} cm
• The height is the perpendicular distance between these bases: {height} cm
• When we "unwrap" the curved surface, it forms a rectangle of dimensions 2πr × h

**Why these formulas work:**
• **Volume** = Area of base × Height = πr² × h = {volume:.2f} cm³
• **CSA** = Perimeter of base × Height = 2πr × h = {csa:.2f} cm²
• **TSA** = CSA + 2 × Base Area = {csa:.2f} + 2π({radius})² = {tsa:.2f} cm²

💡 **Real-world connection:** This cylinder can hold {volume:.2f} ml of water!
"""

def narrate_cone(radius, height, slant_height, volume, csa, tsa):
    """
    Generate educational narration for cone.
    """
    return f"""
🔺 **Understanding the Cone:**

Picture a circle with radius {radius} cm. Now imagine lifting its center point straight up by {height} cm 
while keeping the edge fixed. This creates a cone!

**Key Features:**
• The base is a circle with radius {radius} cm
• The apex (tip) is {height} cm directly above the center
• The slant height ({slant_height:.2f} cm) is the distance from apex to edge

**Pythagorean Connection:**
The radius, height, and slant height form a right triangle:
l² = r² + h² → {slant_height:.2f}² = {radius}² + {height}²

**Why these formulas work:**
• **Volume** = ⅓ × Base Area × Height = ⅓πr²h = {volume:.2f} cm³
  (It's exactly ⅓ of a cylinder with same base and height!)
• **CSA** = π × radius × slant height = {csa:.2f} cm²
• **TSA** = CSA + Base Area = {tsa:.2f} cm²

💡 **Fun fact:** Ice cream cones use this shape for structural strength!
"""

def narrate_sphere(radius, volume, surface_area):
    """
    Generate educational narration for sphere.
    """
    return f"""
⚪ **Understanding the Sphere:**

A sphere is the set of all points that are exactly {radius} cm from a center point. 
It's perfectly round in all directions - like a ball!

**Key Features:**
• Every point on the surface is {radius} cm from the center
• It has the maximum volume for its surface area
• Cross-section through center is always a circle

**Why these formulas work:**
• **Volume** = ⁴⁄₃πr³ = {volume:.2f} cm³
  (Related to the volume of the circumscribing cylinder)
• **Surface Area** = 4πr² = {surface_area:.2f} cm²
  (Exactly 4 times the area of its great circle!)

💡 **Amazing fact:** Bubbles form spheres because this shape minimizes surface area for a given volume!
"""

def narrate_hemisphere(radius, volume, csa, tsa):
    """
    Generate educational narration for hemisphere.
    """
    return f"""
⚪ **Understanding the Hemisphere:**

A hemisphere is exactly half of a sphere, cut along a plane through its center.
Think of it as a dome with radius {radius} cm!

**Key Features:**
• The curved surface is half of a sphere's surface
• The flat base is a circle with radius {radius} cm
• Common in architecture (domes) and cooking (bowls)

**Why these formulas work:**
• **Volume** = ½ × Sphere Volume = ⅔πr³ = {volume:.2f} cm³
• **CSA** = ½ × Sphere Surface = 2πr² = {csa:.2f} cm²
• **TSA** = CSA + Base Area = 2πr² + πr² = 3πr² = {tsa:.2f} cm²

💡 **Practical use:** Hemispheres are used in satellite dishes to focus signals!
"""

def narrate_cube(side, volume, tsa, diagonal):
    """
    Generate educational narration for cube.
    """
    return f"""
📦 **Understanding the Cube:**

A cube is a 3D shape where all edges are equal ({side} cm) and all faces are squares.
It's the 3D version of a square!

**Key Features:**
• 6 identical square faces, each with area {side}² = {side**2} cm²
• 12 equal edges, each {side} cm long
• 8 vertices (corners)
• All angles are 90°

**Why these formulas work:**
• **Volume** = side × side × side = {side}³ = {volume:.2f} cm³
• **TSA** = 6 × (area of one face) = 6 × {side}² = {tsa:.2f} cm²
• **Diagonal** = {side}√3 = {diagonal:.2f} cm
  (Using 3D Pythagorean theorem)

💡 **Fun fact:** Dice are cubes because each face has equal probability of landing up!
"""

def narrate_cuboid(length, breadth, height, volume, tsa, diagonal):
    """
    Generate educational narration for cuboid.
    """
    return f"""
📦 **Understanding the Cuboid:**

A cuboid is like a stretched cube - a box shape with length {length} cm, breadth {breadth} cm, 
and height {height} cm.

**Key Features:**
• 6 rectangular faces in 3 pairs of identical opposites
• Face areas: {length}×{breadth} = {length*breadth} cm² (top/bottom)
            {breadth}×{height} = {breadth*height} cm² (front/back)
            {height}×{length} = {height*length} cm² (left/right)

**Why these formulas work:**
• **Volume** = length × breadth × height = {volume:.2f} cm³
  (How many 1×1×1 cubes fit inside)
• **TSA** = 2(lb + bh + hl) = {tsa:.2f} cm²
  (Sum of all 6 face areas)
• **Diagonal** = √(l² + b² + h²) = {diagonal:.2f} cm
  (3D distance formula)

💡 **Real example:** Most rooms, boxes, and buildings are cuboid-shaped!
"""

def narrate_combined_solid(solid_type, params, total_volume, total_surface_area):
    """
    Generate narration for combined solids.
    """
    if "cone" in solid_type and "hemisphere" in solid_type:
        radius = params.get("radius")
        cone_height = params.get("cone_height")
        
        return f"""
🍦 **Understanding the Ice Cream Shape (Cone on Hemisphere):**

This combined solid looks exactly like an ice cream cone with a scoop on top!

**Structure:**
• Bottom part: Hemisphere (the ice cream scoop) with radius {radius} cm
• Top part: Cone (the wafer) with same radius {radius} cm and height {cone_height} cm
• They share a common circular boundary

**How volumes combine:**
• Hemisphere volume = ⅔πr³ 
• Cone volume = ⅓πr²h
• Total = Hemisphere + Cone = {total_volume:.2f} cm³

**Surface area calculation:**
• We count the curved surface of hemisphere (2πr²)
• Plus the curved surface of cone (πrl)
• The circular junction is internal, so not counted!
• Total Surface Area = {total_surface_area:.2f} cm²

💡 **Design wisdom:** The cone shape provides stability while maximizing ice cream volume!
"""
    
    elif "capsule" in solid_type:
        radius = params.get("radius")
        cylinder_height = params.get("cylinder_height")
        
        return f"""
💊 **Understanding the Capsule Shape:**

A capsule is formed by placing hemispheres on both ends of a cylinder - like a medicine capsule!

**Structure:**
• Middle part: Cylinder with radius {radius} cm and height {cylinder_height} cm
• End parts: Two hemispheres (= 1 complete sphere) with radius {radius} cm
• Total length = {cylinder_height + 2*radius} cm

**Volume calculation:**
• Cylinder volume = πr²h
• Two hemispheres = One sphere = ⁴⁄₃πr³
• Total = {total_volume:.2f} cm³

**Surface area:**
• Curved surface of cylinder = 2πrh
• Surface of complete sphere = 4πr²
• Total = {total_surface_area:.2f} cm²

💡 **Why this shape?** Capsules are aerodynamic and have no sharp edges - perfect for medicine!
"""
    
    return "Combined solid narration not available."

def explain_real_world_applications():
    """
    Explain real-world applications of different solids.
    """
    return """
🌍 **Real-World Applications of 3D Solids:**

**🔵 Cylinders:**
• Water tanks and oil drums (maximum volume, easy to manufacture)
• Pillars in buildings (distribute weight evenly)
• Cans and containers (efficient packing)

**🔺 Cones:**
• Ice cream cones (easy to hold, no spillage)
• Funnels (direct flow of liquids)
• Traffic cones (stable base, visible shape)
• Rocket nose cones (aerodynamic)

**⚪ Spheres:**
• Balls in sports (roll in any direction)
• Planets and stars (gravity pulls equally in all directions)
• Water droplets (minimum surface tension)
• Ball bearings (reduce friction)

**📦 Cubes & Cuboids:**
• Buildings and rooms (efficient use of space)
• Shipping boxes (easy stacking)
• Dice and game pieces (equal probabilities)
• Storage containers (no wasted space)

**🍦 Combined Shapes:**
• Lighthouses (cylinder + cone for stability and visibility)
• Silos (cylinder + hemisphere for grain storage)
• Pencils (cylinder + cone for writing)
• Architecture domes (hemisphere on cylinder/cuboid)

Understanding these shapes helps in:
- Engineering and construction
- Product design and packaging
- Architecture and planning
- Scientific calculations
"""