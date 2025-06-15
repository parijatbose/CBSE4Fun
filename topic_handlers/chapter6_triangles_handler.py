# File: topic_handlers/chapter6_triangles_handler.py

import streamlit as st
import math
import os
from chapters.chapter6_triangles.utils.triangle_plotter import TrianglePlotter
from chapters.chapter6_triangles.main_router import route_query
from chapters.chapter6_triangles.educational_intent_handler import EducationalIntentHandler

def handle_chapter6_triangles(topic: str):
    st.subheader(f'Selected: {topic}')
    
    if 'Triangles' in topic and 'Question Bank' not in topic:
        st.markdown('### 📐 Triangles Calculator')
        
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["🔢 Calculate", "📊 Visualize", "📚 Formulas", "🎯 Practice", "🎓 Learn"])

        with tab1:
            st.markdown("#### Enter your query or select a calculation type:")
            trigger_calculation = False
            
            col1, col2, col3 = st.columns(3)
            with col1:
                if st.button("📐 Right Triangle"):
                    st.session_state['triangle_input'] = "Find hypotenuse of right triangle with base 3 cm and height 4 cm"
                    trigger_calculation = True
            with col2:
                if st.button("🔄 Similar Triangles"):
                    st.session_state['triangle_input'] = "Check if triangles with sides (3,4,5) and (6,8,10) are similar"
                    trigger_calculation = True
            with col3:
                if st.button("📏 Area"):
                    st.session_state['triangle_input'] = "Find area of triangle with sides 5 cm, 6 cm, and 7 cm"
                    trigger_calculation = True
            
            default_value = st.session_state.get('triangle_input', '')
            user_query = st.text_area(
                'Enter your query:',
                value=default_value,
                placeholder="Examples:\n• Find hypotenuse of right triangle with base 3 cm and height 4 cm\n• Check if triangles with sides (3,4,5) and (6,8,10) are similar\n• Find area of triangle with sides 5 cm, 6 cm, and 7 cm",
                height=100
            )
            
            if user_query and (trigger_calculation or st.button("✅ Solve")):
                with st.spinner('Calculating...'):
                    try:
                        result = route_query(user_query)
                        st.markdown("---")
                        st.markdown(result)
                    except Exception as e:
                        st.error(f"❌ Error processing query: {str(e)}")
                        st.info("💡 Please try one of the example queries or check your input format.")
        
        with tab2:
            st.markdown("#### 📊 Visualize Triangles")
            plotter = TrianglePlotter()
            
            shape_type = st.selectbox(
                "Select type of triangle:",
                ["Right Triangle", "Similar Triangles", "General Triangle"]
            )

            if shape_type == "Right Triangle":
                col1, col2 = st.columns(2)
                with col1:
                    base = st.number_input("Base (cm):", min_value=0.1, max_value=20.0, value=3.0, step=0.5, key="rt_base")
                with col2:
                    height = st.number_input("Height (cm):", min_value=0.1, max_value=20.0, value=4.0, step=0.5, key="rt_height")
                
                if st.button("Generate Right Triangle"):
                    with st.spinner('Generating visualization...'):
                        try:
                            fig = plotter.plot_right_triangle(base, height)
                            st.pyplot(fig)
                            hypotenuse = math.sqrt(base**2 + height**2)
                            area = 0.5 * base * height
                            st.success(f"✅ **Calculations:**\n- Hypotenuse: {hypotenuse:.2f} cm\n- Area: {area:.2f} cm²")
                        except Exception as e:
                            st.error(f"❌ Error generating plot: {str(e)}")

            elif shape_type == "Similar Triangles":
                st.markdown("**First Triangle:**")
                col1, col2, col3 = st.columns(3)
                with col1:
                    a1 = st.number_input("Side a₁ (cm):", min_value=0.1, max_value=20.0, value=3.0, step=0.5, key="st_a1")
                with col2:
                    b1 = st.number_input("Side b₁ (cm):", min_value=0.1, max_value=20.0, value=4.0, step=0.5, key="st_b1")
                with col3:
                    c1 = st.number_input("Side c₁ (cm):", min_value=0.1, max_value=20.0, value=5.0, step=0.5, key="st_c1")
                
                st.markdown("**Second Triangle:**")
                col1, col2, col3 = st.columns(3)
                with col1:
                    a2 = st.number_input("Side a₂ (cm):", min_value=0.1, max_value=20.0, value=6.0, step=0.5, key="st_a2")
                with col2:
                    b2 = st.number_input("Side b₂ (cm):", min_value=0.1, max_value=20.0, value=8.0, step=0.5, key="st_b2")
                with col3:
                    c2 = st.number_input("Side c₂ (cm):", min_value=0.1, max_value=20.0, value=10.0, step=0.5, key="st_c2")
                
                if st.button("Generate Similar Triangles"):
                    with st.spinner('Generating visualization...'):
                        try:
                            sides1 = [a1, b1, c1]
                            sides2 = [a2, b2, c2]
                            
                            if not is_valid_triangle(sides1):
                                st.error("❌ First triangle is invalid (triangle inequality violated)")
                                return
                            if not is_valid_triangle(sides2):
                                st.error("❌ Second triangle is invalid (triangle inequality violated)")
                                return
                            
                            sorted1 = sorted(sides1)
                            sorted2 = sorted(sides2)
                            scale_factor = sorted2[0] / sorted1[0]
                            
                            fig = plotter.plot_similar_triangles(sides1, sides2, scale_factor)
                            st.pyplot(fig)
                            
                            ratios = [sorted2[i] / sorted1[i] for i in range(3)]
                            is_similar = all(abs(ratios[0] - ratio) < 0.001 for ratio in ratios)
                            
                            if is_similar:
                                st.success(f"✅ **These triangles are similar!**\n- Scale factor: {scale_factor:.3f}")
                            else:
                                st.warning(f"⚠️ **These triangles are NOT similar.**\n- Ratios: {ratios[0]:.3f}, {ratios[1]:.3f}, {ratios[2]:.3f}")
                        except Exception as e:
                            st.error(f"❌ Error generating plot: {str(e)}")

            else:
                col1, col2, col3 = st.columns(3)
                with col1:
                    a = st.number_input("Side a (cm):", min_value=0.1, max_value=20.0, value=5.0, step=0.5, key="gt_a")
                with col2:
                    b = st.number_input("Side b (cm):", min_value=0.1, max_value=20.0, value=6.0, step=0.5, key="gt_b")
                with col3:
                    c = st.number_input("Side c (cm):", min_value=0.1, max_value=20.0, value=7.0, step=0.5, key="gt_c")
                
                if st.button("Generate Triangle"):
                    with st.spinner('Generating visualization...'):
                        try:
                            sides = [a, b, c]
                            if not is_valid_triangle(sides):
                                st.error("❌ Invalid triangle! The sum of any two sides must be greater than the third side.")
                                return
                            
                            fig = plotter.plot_triangle(sides, "General Triangle")
                            st.pyplot(fig)
                            
                            angles = calculate_angles(sides)
                            area = calculate_area_heron(sides)
                            triangle_type = get_triangle_type(sides)
                            
                            st.success(f"✅ **Triangle Info:**\n- Type: {triangle_type}\n- Area: {area:.2f} cm²\n- Angles: {angles[0]:.1f}°, {angles[1]:.1f}°, {angles[2]:.1f}°")
                        except Exception as e:
                            st.error(f"❌ Error generating plot: {str(e)}")
        
        with tab3:
            st.markdown("#### 📐 Quick Formula Reference")
            formula_type = st.selectbox(
                "Select formula type:",
                ["All Formulas", "Right Triangle", "Similar Triangles", "Area", "Law of Cosines"]
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

        with tab5:
            st.markdown("#### 🎓 Learn Triangle Theorems")
            theorem = st.selectbox(
                "Choose a theorem to explore:",
                ["Basic Proportionality Theorem (BPT)", "Pythagorean Theorem", "Similar Triangles"]
            )
            if theorem == "Basic Proportionality Theorem (BPT)":
                AD = st.slider("AD", 1, 10, 4)
                DB = st.slider("DB", 1, 10, 6) 
                AE = st.slider("AE", 1, 10, 6)
                EC = st.slider("EC", 1, 10, 9)
                ratio1 = AD / DB
                ratio2 = AE / EC
                difference = abs(ratio1 - ratio2)
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("AD/DB", f"{ratio1:.3f}")
                with col2:
                    st.metric("AE/EC", f"{ratio2:.3f}")
                with col3:
                    if difference < 0.001:
                        st.success("✅ Equal Ratios!")
                    else:
                        st.warning(f"⚠️ Diff: {difference:.3f}")
            elif theorem == "Pythagorean Theorem":
                a = st.number_input("Side a:", value=3.0, min_value=0.1)
                b = st.number_input("Side b:", value=4.0, min_value=0.1)
                c = math.sqrt(a**2 + b**2)
                st.success(f"🎯 **Hypotenuse c = {c:.2f}**")
            else:
                st.markdown("## 📐 Similar Triangles Criteria: AA, SSS, SAS")

    elif 'Question Bank' in topic:
        display_question_bank()


# Utility Functions

def is_valid_triangle(sides):
    a, b, c = sides
    return (a + b > c) and (b + c > a) and (a + c > b)

def calculate_angles(sides):
    a, b, c = sides
    try:
        A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
        B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
        C = math.degrees(math.acos((a**2 + b**2 - c**2) / (2 * a * b)))
        return [round(A, 1), round(B, 1), round(C, 1)]
    except:
        return [0, 0, 0]

def calculate_area_heron(sides):
    a, b, c = sides
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def get_triangle_type(sides):
    a, b, c = sorted(sides)
    if abs(a**2 + b**2 - c**2) < 0.001:
        return "Right"
    elif a**2 + b**2 < c**2:
        return "Obtuse"
    else:
        return "Acute"

# The display_all_formulas, display_specific_formula, display_practice_problems, display_question_bank
# functions remain unchanged, as they're already correctly indented and structured.

def display_all_formulas():
    st.markdown("""
    ### 📊 Complete Formula Sheet - Triangles
    
    #### 1️⃣ Right Triangle
    - **Pythagorean Theorem:** c² = a² + b² (where c is hypotenuse)
    - **Area:** Area = ½ × base × height
    - **Trigonometric Ratios:**
      - sin θ = opposite / hypotenuse
      - cos θ = adjacent / hypotenuse  
      - tan θ = opposite / adjacent
    
    #### 2️⃣ Similar Triangles
    - **AA Criterion:** Two angles equal → triangles similar
    - **SSS Criterion:** All sides proportional → triangles similar
    - **SAS Criterion:** Two sides proportional + included angle equal → triangles similar
    - **Scale Factor:** ratio of corresponding sides
    - **Area Ratio:** (scale factor)²
    
    #### 3️⃣ Triangle Area
    - **Heron's Formula:** Area = √[s(s-a)(s-b)(s-c)], where s = (a+b+c)/2
    - **Base-Height:** Area = ½ × base × height
    - **Using sine:** Area = ½ab sin C
    
    #### 4️⃣ Law of Cosines
    - **Formula:** c² = a² + b² - 2ab cos C
    - **To find angle:** cos A = (b² + c² - a²) / (2bc)
    
    #### 5️⃣ Law of Sines
    - **Formula:** a/sin A = b/sin B = c/sin C
    """)

def display_specific_formula(formula_type: str):
    formulas = {
        "Right Triangle": """
### 📐 Right Triangle Formulas

**Pythagorean Theorem:**
- c² = a² + b² (where c is hypotenuse)
- c = √(a² + b²)

**Area:**
- Area = ½ × base × height

**Trigonometric Ratios:**
- sin θ = opposite / hypotenuse
- cos θ = adjacent / hypotenuse  
- tan θ = opposite / adjacent

**Special Right Triangles:**
- 30-60-90: sides in ratio 1 : √3 : 2
- 45-45-90: sides in ratio 1 : 1 : √2
        """,
        "Similar Triangles": """
### 🔄 Similar Triangles

**Similarity Criteria:**
- **AA:** Two angles equal
- **SSS:** All sides proportional  
- **SAS:** Two sides proportional + included angle equal

**Properties:**
- Corresponding angles are equal
- Corresponding sides are proportional
- Area ratio = (scale factor)²
- Perimeter ratio = scale factor
        """,
        "Area": """
### 📏 Triangle Area Formulas

**Heron's Formula:**
- Area = √[s(s-a)(s-b)(s-c)]
- where s = (a+b+c)/2 (semi-perimeter)

**Base-Height:**
- Area = ½ × base × height

**Using Sine:**
- Area = ½ab sin C
- Area = ½bc sin A  
- Area = ½ac sin B
        """,
        "Law of Cosines": """
### ⚖️ Law of Cosines

**To find a side:**
- c² = a² + b² - 2ab cos C
- a² = b² + c² - 2bc cos A
- b² = a² + c² - 2ac cos B

**To find an angle:**
- cos A = (b² + c² - a²) / (2bc)
- cos B = (a² + c² - b²) / (2ac)  
- cos C = (a² + b² - c²) / (2ab)
        """
    }
    st.markdown(formulas.get(formula_type, "❌ Unknown formula type"))

def display_practice_problems(difficulty: str):
    problems = {
        "Easy": [
            "Find the hypotenuse of a right triangle with base 3 cm and height 4 cm.",
            "Calculate the area of a triangle with sides 5 cm, 6 cm, and 7 cm.",
            "In a right triangle, if one leg is 5 cm and hypotenuse is 13 cm, find the other leg.",
            "Check if triangles with sides (6,8,10) and (3,4,5) are similar."
        ],
        "Medium": [
            "In a right triangle, if one angle is 30°, and the hypotenuse is 10 cm, find all sides.",
            "Two triangles have sides (5,12,13) and (10,24,26). Find their similarity ratio and area ratio.",
            "Find all angles of a triangle with sides 7 cm, 8 cm, and 9 cm.",
            "If triangles are similar with ratio 2:3 and smaller triangle area is 20 cm², find larger triangle area."
        ],
        "Hard": [
            "In triangle ABC, if AB = 7 cm, BC = 8 cm, and ∠B = 60°, find AC using law of cosines.",
            "If sides are in ratio 3:4:5 and the triangle area is 54 cm², find the actual side lengths.",
            "Prove that triangles with sides (a,b,c) and (ka,kb,kc) are similar for any positive k.",
            "In similar triangles, if perimeters are 30 cm and 45 cm, and area of smaller is 100 cm², find area of larger."
        ]
    }
    st.markdown(f"### 📝 {difficulty} Problems")
    for i, q in enumerate(problems[difficulty], 1):
        st.markdown(f"{i}. {q}")

def display_question_bank():
    st.markdown("""
### 📚 Question Bank - Triangles

#### 🔢 Multiple Choice Questions
1. In a right triangle, if one angle is 45°, the other acute angle is:
   - a) 45°  ✅
   - b) 30°  
   - c) 60°  
   - d) 90°

2. Triangles are similar if:
   - a) Corresponding angles are equal  ✅
   - b) All sides are equal  
   - c) Areas are equal  
   - d) Perimeters are equal

3. The hypotenuse of a right triangle with legs 5 and 12 is:
   - a) 17
   - b) 13  ✅
   - c) 15
   - d) 7

#### ✏️ Short Answer Questions
1. Find the hypotenuse of a right triangle with base 9 cm and height 12 cm.
2. Calculate the area of triangle with sides 8 cm, 15 cm, and 17 cm.
3. If triangles have sides (4,5,6) and (8,10,12), find the similarity ratio.

#### 📝 Long Answer Questions
1. **Triangle Analysis:**
   In triangle ABC, AB = 8 cm, BC = 10 cm, ∠B = 60°  
   a) Find AC using the law of cosines  
   b) Calculate the area using Heron's formula  
   c) Find all angles using law of cosines
   d) Verify angle sum = 180°

2. **Similar Triangles Problem:**
   Two similar triangles have perimeters 24 cm and 36 cm.
   a) Find the similarity ratio
   b) If area of smaller triangle is 32 cm², find area of larger triangle
   c) If one side of smaller triangle is 6 cm, find corresponding side of larger triangle
""")