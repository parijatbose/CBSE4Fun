# File: topic_handlers/chapter12_surface_areas_handler.py

import streamlit as st
from chapters.chapter12_surface_areas_and_volumes.main_router import route_query
from chapters.chapter12_surface_areas_and_volumes.plot_solids import (
    plot_cylinder, plot_cone, plot_sphere, plot_cuboid, 
    plot_combined_solid, create_2d_net
)

def handle_chapter12_surface_areas(topic: str):
    st.subheader(f'Selected: {topic}')
    
    if 'Surface Areas and Volumes' in topic and 'Question Bank' not in topic:
        st.markdown('### 📐 Surface Areas and Volumes Calculator')
        
        # Add tabs for different sections
        tab1, tab2, tab3, tab4 = st.tabs(["🔢 Calculate", "📊 Visualize", "📚 Formulas", "🎯 Practice"])
        
        with tab1:
            st.markdown("#### Enter your query or select a solid type:")
            
            # Quick selection buttons
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                if st.button("🔵 Cylinder"):
                    st.session_state['solid_input'] = "Find volume and surface area of cylinder with radius 7 cm and height 10 cm"
            with col2:
                if st.button("🔺 Cone"):
                    st.session_state['solid_input'] = "Calculate surface area of cone with radius 5 cm and height 12 cm"
            with col3:
                if st.button("⚪ Sphere"):
                    st.session_state['solid_input'] = "Find volume of sphere with radius 14 cm"
            with col4:
                if st.button("📦 Cube"):
                    st.session_state['solid_input'] = "Calculate TSA of cube with side 8 cm"
            
            # Input field
            default_value = st.session_state.get('solid_input', '')
            user_query = st.text_area(
                'Enter your query:',
                value=default_value,
                placeholder="Examples:\n• Find volume of cylinder with radius 7 cm and height 10 cm\n• What is the formula for surface area of cone?\n• Calculate TSA of sphere with radius 21 cm",
                height=100
            )
            
            if user_query:
                with st.spinner('Calculating...'):
                    result = route_query(user_query)
                    st.markdown("---")
                    st.markdown(result)
        
        with tab2:
            st.markdown("""
            #### 📊 3D Visualization of Solids
            
            This tool helps you visualize different 3D shapes. Here's how to use it:
            1. Select a shape from the dropdown below
            2. Enter the required dimensions
            3. Click the "Generate Plot" button
            4. The 3D visualization will appear below
            
            You can also:
            - See the shape from different angles in the saved image
            - View net diagrams for some shapes (like cylinder and cube)
            - Compare different shapes by generating multiple plots
            """)
            
            # Create two columns for better layout
            col_left, col_right = st.columns([1, 2])
            
            with col_left:
                st.markdown("### 🎯 Select Shape")
                shape_type = st.selectbox(
                    "Select shape to visualize:",
                    ["Sphere", "Hemisphere", "Cube", "Cuboid", "Cylinder", "Cone", "Combined Solids"]
                )
                
                st.markdown("### 📏 Enter Dimensions")
                
                if shape_type == "Sphere":
                    radius = st.number_input("Radius (cm):", min_value=1.0, value=7.0, step=0.5)
                    if st.button("🎨 Generate Sphere Plot", use_container_width=True):
                        with st.spinner('Generating 3D visualization...'):
                            plot_path = plot_sphere(radius, is_hemisphere=False)
                            st.session_state['current_plot'] = plot_path
                            st.session_state['plot_caption'] = f"3D Sphere Visualization (r = {radius} cm)"
                
                elif shape_type == "Hemisphere":
                    radius = st.number_input("Radius (cm):", min_value=1.0, value=7.0, step=0.5)
                    if st.button("🎨 Generate Hemisphere Plot", use_container_width=True):
                        with st.spinner('Generating 3D visualization...'):
                            plot_path = plot_sphere(radius, is_hemisphere=True)
                            st.session_state['current_plot'] = plot_path
                            st.session_state['plot_caption'] = f"3D Hemisphere Visualization (r = {radius} cm)"
                
                elif shape_type == "Cube":
                    side = st.number_input("Side/Edge (cm):", min_value=1.0, value=5.0, step=0.5)
                    if st.button("🎨 Generate Cube Plot", use_container_width=True):
                        with st.spinner('Generating 3D visualization...'):
                            plot_path = plot_cuboid(side, side, side)
                            st.session_state['current_plot'] = plot_path
                            st.session_state['plot_caption'] = f"3D Cube Visualization (a = {side} cm)"
                            
                            # Generate net diagram
                            net_path = create_2d_net("cube", {"side": side})
                            st.session_state['current_net'] = net_path
                            st.session_state['net_caption'] = "Net Diagram of Cube"
                
                elif shape_type == "Cuboid":
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        length = st.number_input("Length (cm):", min_value=1.0, value=8.0, step=0.5)
                    with col2:
                        breadth = st.number_input("Breadth (cm):", min_value=1.0, value=6.0, step=0.5)
                    with col3:
                        height = st.number_input("Height (cm):", min_value=1.0, value=4.0, step=0.5)
                    
                    if st.button("🎨 Generate Cuboid Plot", use_container_width=True):
                        with st.spinner('Generating 3D visualization...'):
                            plot_path = plot_cuboid(length, breadth, height)
                            st.session_state['current_plot'] = plot_path
                            st.session_state['plot_caption'] = f"3D Cuboid Visualization (l = {length}, b = {breadth}, h = {height} cm)"
                
                elif shape_type == "Cylinder":
                    col1, col2 = st.columns(2)
                    with col1:
                        radius = st.number_input("Radius (cm):", min_value=1.0, value=5.0, step=0.5)
                    with col2:
                        height = st.number_input("Height (cm):", min_value=1.0, value=10.0, step=0.5)
                    
                    if st.button("🎨 Generate Cylinder Plot", use_container_width=True):
                        with st.spinner('Generating 3D visualization...'):
                            plot_path = plot_cylinder(radius, height)
                            st.session_state['current_plot'] = plot_path
                            st.session_state['plot_caption'] = f"3D Cylinder Visualization (r = {radius}, h = {height} cm)"
                            
                            # Generate net diagram
                            net_path = create_2d_net("cylinder", {"radius": radius, "height": height})
                            st.session_state['current_net'] = net_path
                            st.session_state['net_caption'] = "Net Diagram of Cylinder"
                
                elif shape_type == "Cone":
                    col1, col2 = st.columns(2)
                    with col1:
                        radius = st.number_input("Radius (cm):", min_value=1.0, value=5.0, step=0.5)
                    with col2:
                        height = st.number_input("Height (cm):", min_value=1.0, value=12.0, step=0.5)
                    
                    if st.button("🎨 Generate Cone Plot", use_container_width=True):
                        with st.spinner('Generating 3D visualization...'):
                            plot_path = plot_cone(radius, height)
                            st.session_state['current_plot'] = plot_path
                            st.session_state['plot_caption'] = f"3D Cone Visualization (r = {radius}, h = {height} cm)"
                
                elif shape_type == "Combined Solids":
                    combined_type = st.selectbox(
                        "Select combined solid:",
                        ["Cone on Hemisphere"]
                    )
                    
                    if combined_type == "Cone on Hemisphere":
                        radius = st.number_input("Radius (cm):", min_value=1.0, max_value=20.0, value=1.0, step=0.5)
                        height = st.number_input("Cone Height (cm):", min_value=1.0, max_value=20.0, value=1.0, step=0.5)
                        
                        if st.button("Generate Combined Solid Plot"):
                            with st.spinner('Generating visualization...'):
                                plot_path = plot_combined_solid(radius, height)
                                st.image(plot_path, caption="Combined Solid Visualization", use_container_width=True)
                                
                                # Display volume calculation
                                hemisphere_volume = (2/3) * (22/7) * radius**3
                                cone_volume = (1/3) * (22/7) * radius**2 * height
                                total_volume = hemisphere_volume + cone_volume
                                
                                st.markdown(f"""
                                ### 📊 Volume Calculation
                                
                                **Given:**
                                - Radius (r) = {radius} cm
                                - Cone Height (h) = {height} cm
                                
                                **Step-by-Step Solution:**
                                
                                1. Volume of Hemisphere = ⅔πr³
                                   = ⅔ × ²²⁄₇ × {radius}³
                                   = {hemisphere_volume:.2f} cm³
                                
                                2. Volume of Cone = ⅓πr²h
                                   = ⅓ × ²²⁄₇ × {radius}² × {height}
                                   = {cone_volume:.2f} cm³
                                
                                3. Total Volume = Hemisphere Volume + Cone Volume
                                   = {hemisphere_volume:.2f} + {cone_volume:.2f}
                                   = **{total_volume:.2f} cm³**
                                """)
            
            with col_right:
                st.markdown("### 🖼️ Visualization")
                if 'current_plot' in st.session_state:
                    st.image(st.session_state['current_plot'], 
                            caption=st.session_state['plot_caption'],
                            use_container_width=True)
                    
                    if 'current_net' in st.session_state:
                        st.markdown("### 📐 Net Diagram")
                        st.image(st.session_state['current_net'],
                                caption=st.session_state['net_caption'],
                                use_container_width=True)
                else:
                    st.info("👈 Select a shape and enter dimensions to generate a 3D visualization")
        
        with tab3:
            st.markdown("#### 📐 Quick Formula Reference")
            
            formula_type = st.selectbox(
                "Select solid:",
                ["All Formulas", "Cylinder", "Cone", "Sphere & Hemisphere", "Cube & Cuboid"]
            )
            
            if formula_type == "All Formulas":
                display_all_formulas()
            else:
                display_specific_formula(formula_type)
        
        with tab4:
            st.markdown("#### 🎯 Practice Problems")
            
            difficulty = st.select_slider(
                "Select difficulty:",
                options=["Easy", "Medium", "Hard"],
                value="Medium"
            )
            
            display_practice_problems(difficulty)
    
    elif 'Question Bank' in topic:
        display_question_bank()

def display_all_formulas():
    """Display all formulas in a structured format."""
    st.markdown("""
    ### 📊 Complete Formula Sheet - Surface Areas and Volumes
    
    #### 1️⃣ **Cylinder**
    - **Volume** = πr²h
    - **Curved Surface Area (CSA)** = 2πrh
    - **Total Surface Area (TSA)** = 2πr(r + h)
    
    #### 2️⃣ **Cone**
    - **Volume** = ⅓πr²h
    - **Curved Surface Area (CSA)** = πrl
    - **Total Surface Area (TSA)** = πr(r + l)
    - **Slant Height**: l = √(r² + h²)
    
    #### 3️⃣ **Sphere**
    - **Volume** = ⁴⁄₃πr³
    - **Surface Area** = 4πr²
    
    #### 4️⃣ **Hemisphere**
    - **Volume** = ⅔πr³
    - **Curved Surface Area** = 2πr²
    - **Total Surface Area** = 3πr²
    
    #### 5️⃣ **Cube**
    - **Volume** = a³
    - **Total Surface Area** = 6a²
    - **Lateral Surface Area** = 4a²
    - **Diagonal** = a√3
    
    #### 6️⃣ **Cuboid**
    - **Volume** = l × b × h
    - **Total Surface Area** = 2(lb + bh + hl)
    - **Lateral Surface Area** = 2h(l + b)
    - **Diagonal** = √(l² + b² + h²)
    
    #### 📌 **Important Notes:**
    - Use π = 22/7 for calculations unless specified
    - 1 cm³ = 1 ml
    - 1 m³ = 1000 litres
    """)

def display_specific_formula(formula_type):
    """Display specific formula with examples."""
    formulas = {
        "Cylinder": """
        ### 🔵 Cylinder Formulas
        
        **Given:** radius (r) and height (h)
        
        - **Volume** = πr²h
        - **CSA** = 2πrh
        - **TSA** = 2πr(r + h)
        
        **Example:** r = 7 cm, h = 10 cm
        - Volume = 22/7 × 7² × 10 = 1540 cm³
        - CSA = 2 × 22/7 × 7 × 10 = 440 cm²
        - TSA = 2 × 22/7 × 7 × (7 + 10) = 748 cm²
        """,
        
        "Cone": """
        ### 🔺 Cone Formulas
        
        **Given:** radius (r), height (h), slant height (l)
        
        - **Volume** = ⅓πr²h
        - **CSA** = πrl
        - **TSA** = πr(r + l)
        - **Relation:** l² = r² + h²
        
        **Example:** r = 3 cm, h = 4 cm
        - l = √(3² + 4²) = 5 cm
        - Volume = ⅓ × 22/7 × 3² × 4 = 37.71 cm³
        - CSA = 22/7 × 3 × 5 = 47.14 cm²
        """,
        
        "Sphere & Hemisphere": """
        ### ⚪ Sphere & Hemisphere Formulas
        
        **Sphere (radius r):**
        - Volume = ⁴⁄₃πr³
        - Surface Area = 4πr²
        
        **Hemisphere (radius r):**
        - Volume = ⅔πr³
        - CSA = 2πr²
        - TSA = 3πr² (includes base)
        
        **Example:** r = 7 cm
        - Sphere Volume = ⁴⁄₃ × 22/7 × 7³ = 1437.33 cm³
        - Hemisphere Volume = ⅔ × 22/7 × 7³ = 718.67 cm³
        """,
        
        "Cube & Cuboid": """
        ### 📦 Cube & Cuboid Formulas
        
        **Cube (side a):**
        - Volume = a³
        - TSA = 6a²
        - Diagonal = a√3
        
        **Cuboid (l, b, h):**
        - Volume = l × b × h
        - TSA = 2(lb + bh + hl)
        - Diagonal = √(l² + b² + h²)
        
        **Example:** Cube with a = 5 cm
        - Volume = 5³ = 125 cm³
        - TSA = 6 × 5² = 150 cm²
        - Diagonal = 5√3 = 8.66 cm
        """
    }
    
    st.markdown(formulas.get(formula_type, ""))

def display_practice_problems(difficulty):
    """Display practice problems based on difficulty."""
    problems = {
        "Easy": [
            "1. Find the volume of a cylinder with radius 7 cm and height 10 cm.",
            "2. Calculate the TSA of a cube with side 6 cm.",
            "3. Find the volume of a sphere with radius 3 cm.",
        ],
        "Medium": [
            "1. A cone has radius 5 cm and slant height 13 cm. Find its volume and TSA.",
            "2. A cylindrical tank has radius 14 cm and height 20 cm. Find its capacity in litres.",
            "3. Find the surface area of a hemisphere with radius 10.5 cm.",
        ],
        "Hard": [
            "1. An ice cream cone consists of a hemisphere surmounted by a cone. If radius is 3.5 cm and height of cone is 12 cm, find the total volume.",
            "2. A capsule is formed by a cylinder with hemispheres on both ends. If radius is 5 cm and cylinder length is 14 cm, find TSA.",
            "3. A cuboid has volume 480 cm³. If its length and breadth are 8 cm and 6 cm respectively, find its TSA.",
        ]
    }
    
    st.markdown(f"### {difficulty} Problems:")
    for problem in problems[difficulty]:
        st.markdown(problem)
    
    if st.button("Show Solutions"):
        st.info("Solutions will be displayed here. Try solving them first!")

def display_question_bank():
    """Display question bank for the chapter."""
    st.markdown("""
    ### 📚 Question Bank - Surface Areas and Volumes
    
    #### Section A: Very Short Answer (1 mark each)
    1. State the formula for volume of a cone.
    2. What is the CSA of a sphere with radius r?
    3. How many faces does a cuboid have?
    
    #### Section B: Short Answer (2 marks each)
    1. Find the volume of a cylinder with radius 14 cm and height 15 cm.
    2. Calculate the slant height of a cone with radius 5 cm and height 12 cm.
    
    #### Section C: Long Answer (3-4 marks each)
    1. A tent is in the shape of a cylinder surmounted by a cone. The radius is 7 m and heights of cylindrical and conical parts are 8 m and 3 m respectively. Find the total surface area of the tent.
    
    #### Section D: Case Study (5 marks)
    1. A company manufactures spherical balls of radius 7 cm. These are packed in cubical boxes of side 14 cm. Find:
       (a) Volume of the ball
       (b) Volume of the box
       (c) Empty space in the box
    """)

# Add information box
def add_info_box():
    with st.expander("ℹ️ About Surface Areas and Volumes"):
        st.markdown("""
        **Key Concepts:**
        - Surface area measures the total area of all faces
        - Volume measures the space occupied by a solid
        - CSA (Curved Surface Area) excludes flat surfaces
        - TSA (Total Surface Area) includes all surfaces
        
        **Tips for Problem Solving:**
        1. Identify the solid shape correctly
        2. List given values and what to find
        3. Choose appropriate formula
        4. Substitute values carefully with units
        5. Use π = 22/7 unless specified otherwise
        6. Convert units if needed (cm³ to litres, etc.)
        
        **Common Mistakes to Avoid:**
        - Confusing radius with diameter
        - Mixing up CSA and TSA
        - Forgetting to square or cube values
        - Using wrong value of π
        """)

# Call this function at the end of handle_chapter12_surface_areas
handle_chapter12_surface_areas.__doc__ = """
Handler for Chapter 12: Surface Areas and Volumes.
Includes calculator, 3D visualizations, formulas, and practice problems.
"""