import math

def solve_real_world_problem(problem_type: str, params: dict) -> str:
    """
    Solve real-world circle applications based on problem type.
    
    Args:
        problem_type: Type of real-world problem
        params: Dictionary containing problem parameters
    
    Returns:
        str: Formatted solution
    """
    if problem_type == "area_coverage":
        return solve_area_coverage(params)
    elif problem_type == "wheel_rotation":
        return solve_wheel_rotation(params)
    elif problem_type == "satellite_coverage":
        return solve_satellite_coverage(params)
    elif problem_type == "circular_track":
        return solve_circular_track(params)
    elif problem_type == "sprinkler_coverage":
        return solve_sprinkler_coverage(params)
    else:
        return show_general_applications()

def solve_area_coverage(params: dict) -> str:
    """
    Solve area coverage problems (general circular coverage)
    """
    radius = params.get("radius", params.get("value", 10))
    area = math.pi * radius * radius
    circumference = 2 * math.pi * radius
    
    return f"""
🎯 **Real World Application: Circular Area Coverage**

📝 **Problem:** Calculate coverage area for circular region with radius {radius} units

**Solution:**

**Step 1: Calculate Area**
- Area of circle = πr²
- Area = π × {radius}²
- Area = π × {radius**2}
- Area = 3.14159 × {radius**2}
- **Area = {area:.2f} square units**

**Step 2: Calculate Perimeter (Circumference)**
- Circumference = 2πr
- Circumference = 2 × π × {radius}
- Circumference = 2 × 3.14159 × {radius}
- **Circumference = {circumference:.2f} units**

**Step 3: Coverage Efficiency**
- Area per unit perimeter = Area ÷ Circumference
- Efficiency = {area:.2f} ÷ {circumference:.2f}
- **Efficiency = {area/circumference:.2f} units**

✅ **Answer:** 
- Total coverage area = **{area:.2f} square units**
- Perimeter length = **{circumference:.2f} units**
- Coverage efficiency = **{area/circumference:.2f} units**

**Real-world Examples:**
- Sprinkler systems covering {area:.2f} sq units
- Security camera coverage area
- WiFi router signal coverage
- Sound speaker coverage in auditorium
"""

def solve_wheel_rotation(params: dict) -> str:
    """
    Solve wheel rotation and distance problems
    """
    radius = params.get("radius", 0.5)  # in meters
    rotations = params.get("rotations", params.get("angle", 1))
    
    # Convert to reasonable units if needed
    if radius > 100:  # Likely in cm, convert to m
        radius = radius / 100
        unit = "m"
    elif radius < 1:  # Already in meters
        unit = "m"
    else:
        unit = "units"
    
    circumference = 2 * math.pi * radius
    distance = circumference * rotations
    area_covered = math.pi * radius * radius
    
    # Calculate time if speed is given
    speed_info = ""
    if "speed" in params:
        speed = params["speed"]  # in m/s
        time = distance / speed
        speed_info = f"""
**Step 4: Time Calculation**
- Speed = {speed} {unit}/s
- Time = Distance ÷ Speed
- Time = {distance:.2f} ÷ {speed}
- **Time = {time:.2f} seconds**
"""
    
    return f"""
🚴 **Wheel Rotation Problem**

📝 **Given:**
- Wheel radius: {radius} {unit}
- Number of rotations: {rotations}

**Solution:**

**Step 1: Calculate wheel circumference**
- Circumference = 2πr
- Circumference = 2 × π × {radius}
- Circumference = {circumference:.2f} {unit}

**Step 2: Calculate total distance traveled**
- Distance = Circumference × Number of rotations
- Distance = {circumference:.2f} × {rotations}
- **Distance = {distance:.2f} {unit}**

**Step 3: Ground area contacted**
- Contact area per rotation = πr²
- Total area = {area_covered:.2f} square {unit}
{speed_info}

✅ **Answer:** 
- Distance traveled = **{distance:.2f} {unit}**
- Each rotation covers = **{circumference:.2f} {unit}**

**Practical Applications:**
- Bicycle computer calculations
- Car odometer readings
- Conveyor belt measurements
- Industrial roller applications
"""

def solve_satellite_coverage(params: dict) -> str:
    """
    Solve satellite coverage problems using tangent properties
    """
    height = params.get("height", 500)  # km above earth
    earth_radius = 6371  # km
    
    # Calculate coverage using tangent properties
    # From satellite, tangent to Earth gives horizon distance
    horizon_distance = math.sqrt(height * (height + 2 * earth_radius))
    
    # Coverage area on Earth's surface (spherical cap)
    coverage_angle = math.asin(horizon_distance / (earth_radius + height))
    coverage_area = 2 * math.pi * earth_radius * earth_radius * (1 - math.cos(coverage_angle))
    
    # Convert to million sq km for readability
    coverage_area_millions = coverage_area / 1_000_000
    
    # Percentage of Earth covered
    earth_total_area = 4 * math.pi * earth_radius * earth_radius
    coverage_percentage = (coverage_area / earth_total_area) * 100
    
    return f"""
🛰️ **Satellite Coverage Problem**

📝 **Given:**
- Satellite altitude: {height} km above Earth
- Earth radius: {earth_radius} km

**Solution using Circle Tangent Properties:**

**Step 1: Calculate horizon distance**
- Using tangent from satellite to Earth's horizon
- Horizon distance = √[h(h + 2R)]
- Where h = altitude, R = Earth radius
- Horizon = √[{height}({height} + 2×{earth_radius})]
- Horizon = √[{height} × {height + 2*earth_radius}]
- **Horizon distance = {horizon_distance:.2f} km**

**Step 2: Calculate coverage angle**
- Coverage angle = arcsin(horizon distance / orbital radius)
- Coverage angle = arcsin({horizon_distance:.2f} / {earth_radius + height})
- **Coverage angle = {math.degrees(coverage_angle):.2f}°**

**Step 3: Calculate coverage area**
- Coverage area = 2πR²(1 - cos θ)
- Coverage area = 2π × {earth_radius}² × (1 - cos({math.degrees(coverage_angle):.2f}°))
- **Coverage area = {coverage_area_millions:.2f} million km²**

**Step 4: Coverage percentage**
- Earth's total area = {earth_total_area/1_000_000:.2f} million km²
- Coverage percentage = {coverage_percentage:.2f}%

✅ **Answer:** 
- Satellite covers **{coverage_area_millions:.2f} million km²**
- This is **{coverage_percentage:.2f}%** of Earth's surface
- Horizon distance: **{horizon_distance:.2f} km**

**Applications:**
- Communication satellite planning
- Earth observation coverage
- GPS satellite visibility
- Weather monitoring systems
"""

def solve_circular_track(params: dict) -> str:
    """
    Solve circular track problems
    """
    radius = params.get("radius", 100)  # meters
    lanes = params.get("lanes", 1)
    lane_width = params.get("lane_width", 1.22)  # standard lane width
    
    results = []
    total_extra = 0
    base_circumference = 2 * math.pi * radius  # Initialize base_circumference
    
    for lane in range(1, lanes + 1):
        lane_radius = radius + (lane - 1) * lane_width
        lane_circumference = 2 * math.pi * lane_radius
        if lane == 1:
            base_circumference = lane_circumference
            extra = 0
        else:
            extra = lane_circumference - base_circumference
            total_extra += extra
        
        results.append(f"Lane {lane}: radius = {lane_radius:.2f}m, distance = {lane_circumference:.2f}m" + 
                      (f", extra = {extra:.2f}m" if lane > 1 else ""))
    
    return f"""
🏃 **Circular Track Problem**

📝 **Given:**
- Inner radius: {radius} m
- Number of lanes: {lanes}
- Lane width: {lane_width} m

**Solution:**

**Lane Calculations:**
{chr(10).join(results)}

**Summary:**
- Inner lane distance: {base_circumference:.2f} m
- Each lane adds: {2 * math.pi * lane_width:.2f} m
- Total extra distance for outer lanes: {total_extra:.2f} m

**Staggered Start Calculation:**
For a fair race, runners in outer lanes must start ahead:
- Lane 2 starts {2 * math.pi * lane_width:.2f} m ahead
- Lane 3 starts {2 * math.pi * lane_width * 2:.2f} m ahead
- And so on...

✅ **Key Formula:** 
Extra distance per lane = 2π × (lane width) = {2 * math.pi * lane_width:.2f} m

**Applications:**
- Athletic track design
- Racing circuit planning
- Velodrome construction
"""

def solve_sprinkler_coverage(params: dict) -> str:
    """
    Solve irrigation sprinkler coverage problems
    """
    radius = params.get("radius", 10)  # meters
    angle = params.get("angle", 360)  # degrees
    overlap = params.get("overlap", 0)  # percentage
    
    # Full circle area
    full_area = math.pi * radius * radius
    
    # Actual coverage based on angle
    coverage_area = (angle / 360) * full_area
    
    # Effective area after overlap
    effective_area = coverage_area * (1 - overlap/100)
    
    # Water calculation if flow rate given
    water_info = ""
    if "flow_rate" in params:
        flow = params["flow_rate"]  # liters per minute
        time = params.get("time", 60)  # minutes
        total_water = flow * time
        water_per_sqm = total_water / effective_area
        water_info = f"""
**Water Distribution:**
- Flow rate: {flow} L/min
- Time: {time} minutes
- Total water: {total_water} L
- Water per m²: {water_per_sqm:.2f} L/m²
"""
    
    return f"""
💧 **Sprinkler Coverage Problem**

📝 **Given:**
- Sprinkler radius: {radius} m
- Spray angle: {angle}°
- Overlap: {overlap}%

**Solution:**

**Step 1: Calculate maximum coverage area**
- Full circle area = πr²
- Area = π × {radius}²
- Area = {full_area:.2f} m²

**Step 2: Calculate actual coverage**
- Coverage = (angle/360) × full area
- Coverage = ({angle}/360) × {full_area:.2f}
- **Coverage area = {coverage_area:.2f} m²**

**Step 3: Calculate effective coverage**
- Effective area = coverage × (1 - overlap)
- Effective area = {coverage_area:.2f} × {1 - overlap/100}
- **Effective area = {effective_area:.2f} m²**

{water_info}

✅ **Answer:** 
- Total coverage: **{coverage_area:.2f} m²**
- Effective coverage: **{effective_area:.2f} m²**

**Optimization Tips:**
- Triangular spacing: 86.6% efficiency
- Square spacing: 78.5% efficiency
- Hexagonal spacing: 90.7% efficiency
"""

def show_general_applications() -> str:
    """
    Show general real-world applications of circles
    """
    return """
🌍 **Real World Circle Applications**

## **1. Transportation & Motion**
🚗 **Wheels and Rotation**
- Distance = 2πr × rotations
- Applications: bicycles, cars, conveyor belts

🚁 **Turning Radius**
- Minimum space needed for vehicles to turn
- Critical for parking lots, road design

## **2. Communication & Coverage**
📡 **Signal Propagation**
- Radio/WiFi coverage = πr²
- Cell tower planning using overlapping circles

🛰️ **Satellite Coverage**
- Uses tangent properties for horizon calculation
- Coverage area depends on altitude

## **3. Engineering & Design**
⚙️ **Gears and Pulleys**
- Gear ratio = r₁/r₂
- Belt length calculations

🏗️ **Circular Structures**
- Domes, arches, tanks
- Stress distribution in circular designs

## **4. Agriculture & Irrigation**
💧 **Sprinkler Systems**
- Coverage area optimization
- Overlap calculations for efficiency

🌾 **Circular Fields**
- Center pivot irrigation
- Efficient water distribution

## **5. Sports & Recreation**
🏃 **Running Tracks**
- Lane distance = 2π(r + lane × width)
- Staggered starts calculation

⚽ **Sports Fields**
- Center circle, penalty arc
- Shot clock range in basketball

## **Common Formulas:**
- **Area**: A = πr²
- **Circumference**: C = 2πr
- **Arc Length**: L = rθ (θ in radians)
- **Sector Area**: A = (θ/360) × πr²
- **Tangent Length**: T = √(d² - r²)

## **Try These Problems:**
1. "Calculate wheel rotation distance for radius 30cm, 50 rotations"
2. "Find sprinkler coverage area with 15m radius"
3. "Satellite at 400km altitude coverage area"
4. "Running track with 100m radius, 8 lanes"
"""