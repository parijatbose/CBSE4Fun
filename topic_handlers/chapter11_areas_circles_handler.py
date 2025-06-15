# File: topic_handlers/chapter11_areas_circles_handler.py

import streamlit as st
import math
from chapters.chapter11_areas_circles.plot_circles import plot_sector, plot_segment

def handle_chapter11_areas_circles(topic: str):
    st.subheader(f'Selected: {topic}')
    
    if 'Areas Related to Circles' in topic and 'Question Bank' not in topic:
        st.markdown('### 📐 Areas Related to Circles Calculator')
        
        # Add tabs for different sections
        tab1, tab2, tab3, tab4 = st.tabs(["🔢 Calculate", "📊 Visualize", "📚 Formulas", "🎯 Practice"])
        
        with tab1:
            st.markdown("#### Enter your query or select a calculation type:")
            
            # Quick selection buttons
            col1, col2 = st.columns(2)
            with col1:
                if st.button("🍕 Sector Area"):
                    st.session_state['circle_input'] = "Find area of sector with radius 7 cm and angle 60°"
            with col2:
                if st.button("🌙 Segment Area"):
                    st.session_state['circle_input'] = "Calculate area of segment with radius 5 cm and angle 45°"
            
            # Input field
            default_value = st.session_state.get('circle_input', '')
            user_query = st.text_area(
                'Enter your query:',
                value=default_value,
                placeholder="Examples:\n• Find area of sector with radius 7 cm and angle 60°\n• Calculate area of segment with radius 5 cm and angle 45°",
                height=100
            )
            
            if user_query:
                with st.spinner('Calculating...'):
                    result = calculate_area(user_query)
                    st.markdown("---")
                    st.markdown(result)
        
        with tab2:
            st.markdown("#### 📊 Visualize Circle Areas")
            
            # Shape selection
            shape_type = st.selectbox(
                "Select shape to visualize:",
                ["Sector", "Segment"]
            )
            
            # Input fields
            col1, col2 = st.columns(2)
            with col1:
                radius = st.number_input("Radius (cm):", min_value=1.0, max_value=20.0, value=7.0, step=0.5)
            with col2:
                angle = st.number_input("Angle (degrees):", min_value=1.0, max_value=360.0, value=60.0, step=1.0)
            
            if st.button("Generate Visualization"):
                with st.spinner('Generating visualization...'):
                    if shape_type == "Sector":
                        plot_path = plot_sector(radius, angle)
                        st.image(plot_path, caption="Sector Visualization", use_container_width=True)
                    else:  # Segment
                        plot_path = plot_segment(radius, angle)
                        st.image(plot_path, caption="Segment Visualization", use_container_width=True)
        
        with tab3:
            st.markdown("#### 📐 Quick Formula Reference")
            
            formula_type = st.selectbox(
                "Select calculation type:",
                ["All Formulas", "Sector Area", "Segment Area"]
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

def calculate_area(query: str) -> str:
    """Calculate area based on the query."""
    import re
    
    # Extract radius and angle
    radius_match = re.search(r'radius[:\s]+(\d+(?:\.\d+)?)', query, re.IGNORECASE)
    angle_match = re.search(r'angle[:\s]+(\d+(?:\.\d+)?)', query, re.IGNORECASE)
    
    if not (radius_match and angle_match):
        return "❌ Could not extract radius and angle from the query. Please specify both values."
    
    radius = float(radius_match.group(1))
    angle = float(angle_match.group(1))
    
    if radius <= 0 or angle <= 0 or angle > 360:
        return "❌ Invalid values. Radius must be positive and angle must be between 0° and 360°."
    
    # Use π = 22/7 for calculations
    pi = 22/7
    
    if "sector" in query.lower():
        # Sector area = (θ/360°) × πr²
        area = (angle/360) * pi * radius**2
        
        result = f"""
✅ **Sector Area Solution:**

Given:
• Radius (r) = {radius} cm
• Angle (θ) = {angle}°

📝 **Step-by-Step Solution:**

**Area of Sector = (θ/360°) × πr²**
   = ({angle}/360) × {pi:.3f} × {radius}²
   = {angle/360:.3f} × {pi:.3f} × {radius**2:.2f}
   = **{area:.2f} cm²**

💡 **Summary:**
• Area of Sector = {area:.2f} cm²
"""
    else:  # segment area
        # Segment area = (θ/360°) × πr² - ½r²sin(θ)
        sector_area = (angle/360) * pi * radius**2
        triangle_area = 0.5 * radius**2 * math.sin(math.radians(angle))
        area = sector_area - triangle_area
        
        result = f"""
✅ **Segment Area Solution:**

Given:
• Radius (r) = {radius} cm
• Angle (θ) = {angle}°

📝 **Step-by-Step Solution:**

**1. Area of Sector = (θ/360°) × πr²**
   = ({angle}/360) × {pi:.3f} × {radius}²
   = {angle/360:.3f} × {pi:.3f} × {radius**2:.2f}
   = {sector_area:.2f} cm²

**2. Area of Triangle = ½r²sin(θ)**
   = 0.5 × {radius}² × sin({angle}°)
   = 0.5 × {radius**2:.2f} × {math.sin(math.radians(angle)):.3f}
   = {triangle_area:.2f} cm²

**3. Area of Segment = Sector Area - Triangle Area**
   = {sector_area:.2f} - {triangle_area:.2f}
   = **{area:.2f} cm²**

💡 **Summary:**
• Area of Segment = {area:.2f} cm²
"""
    
    return result

def display_all_formulas():
    """Display all formulas in a structured format."""
    st.markdown("""
    ### 📊 Complete Formula Sheet - Areas Related to Circles
    
    #### 1️⃣ **Sector Area**
    - **Area** = (θ/360°) × πr²
    Where:
    - θ = angle in degrees
    - r = radius
    - π ≈ 22/7
    
    #### 2️⃣ **Segment Area**
    - **Area** = (θ/360°) × πr² - ½r²sin(θ)
    Where:
    - θ = angle in degrees
    - r = radius
    - π ≈ 22/7
    
    #### 📌 **Important Notes:**
    - Angle must be in degrees
    - Radius must be positive
    - For segment area, angle must be less than 180°
    """)

def display_specific_formula(formula_type: str):
    """Display specific formula with examples."""
    formulas = {
        "Sector Area": """
        ### 🍕 Sector Area Formula
        
        **Given:** radius (r) and angle (θ)
        
        - **Area** = (θ/360°) × πr²
        
        **Example:** r = 7 cm, θ = 60°
        - Area = (60/360) × 22/7 × 7²
        - Area = 1/6 × 22/7 × 49
        - Area = 25.67 cm²
        """,
        
        "Segment Area": """
        ### 🌙 Segment Area Formula
        
        **Given:** radius (r) and angle (θ)
        
        - **Area** = (θ/360°) × πr² - ½r²sin(θ)
        
        **Example:** r = 5 cm, θ = 45°
        - Sector Area = (45/360) × 22/7 × 5² = 9.82 cm²
        - Triangle Area = 0.5 × 5² × sin(45°) = 8.84 cm²
        - Segment Area = 9.82 - 8.84 = 0.98 cm²
        """
    }
    
    st.markdown(formulas.get(formula_type, "❌ Unknown formula type"))

def display_practice_problems(difficulty: str):
    """Display practice problems based on difficulty."""
    problems = {
        "Easy": [
            "Find area of sector with radius 7 cm and angle 60°",
            "Calculate area of segment with radius 5 cm and angle 45°"
        ],
        "Medium": [
            "A sector has radius 10 cm and area 78.5 cm². Find its angle.",
            "A segment has radius 8 cm and angle 120°. Find its area."
        ],
        "Hard": [
            "A sector has area 154 cm² and angle 90°. Find its radius.",
            "A segment has area 25.67 cm² and radius 7 cm. Find its angle."
        ]
    }
    
    st.markdown(f"### 📝 {difficulty} Problems")
    for i, problem in enumerate(problems[difficulty], 1):
        st.markdown(f"{i}. {problem}")

def display_question_bank():
    """Display question bank for the chapter."""
    st.markdown("""
    ### 📚 Question Bank - Areas Related to Circles
    
    #### Multiple Choice Questions
    1. The area of a sector of angle θ° of a circle with radius r is:
       a) (θ/360°) × πr²
       b) (θ/180°) × πr²
       c) (θ/90°) × πr²
       d) θ × πr²
    
    2. The area of a segment of a circle is:
       a) Always less than the area of the corresponding sector
       b) Always equal to the area of the corresponding sector
       c) Always greater than the area of the corresponding sector
       d) None of these
    
    #### Short Answer Questions
    1. Find the area of a sector of a circle with radius 6 cm and angle 60°.
    2. Calculate the area of a segment of a circle with radius 8 cm and angle 45°.
    
    #### Long Answer Questions
    1. A sector of a circle has radius 10 cm and angle 120°. Find:
       a) The area of the sector
       b) The area of the corresponding segment
       c) The length of the arc
    """)
