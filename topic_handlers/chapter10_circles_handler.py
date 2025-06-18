# File: topic_handlers/chapter10_circles_handler.py

import streamlit as st
import sys
import os

# Add the chapters directory to the path
chapters_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'chapters')
if chapters_path not in sys.path:
    sys.path.append(chapters_path)

# Add chapter9_circles to the path (using chapter 9, not 10)
chapter9_path = os.path.join(chapters_path, 'chapter9_circles')
if chapter9_path not in sys.path:
    sys.path.append(chapter9_path)

def handle_chapter10_circles(topic: str):
    """
    Handle Chapter 10: Circles queries and route them appropriately.
    """
    st.markdown("## 🔵 Chapter 10: Circles")
    
    # Import the main router from chapter9_circles
    try:
        from chapters.chapter10_circles.main_router import route_query
        
        # Create input section
        st.markdown("### 📝 Enter Your Circle Problem")
        
        # Text input for the query
        query = st.text_area(
            "Type your circle-related question:",
            placeholder="Example: Find the length of tangent from point (3,4) to circle with radius 5",
            height=100
        )
        
        # Submit button
        if st.button("🔍 Solve Problem", type="primary"):
            if query.strip():
                with st.spinner("Solving your circle problem..."):
                    try:
                        result = route_query(query)
                        st.markdown("### 📊 Solution")
                        st.markdown(result)
                    except Exception as e:
                        st.error(f"❌ Error solving problem: {str(e)}")
                        st.info("Please check your input and try again.")
            else:
                st.warning("⚠️ Please enter a question to solve.")
        
        # Show example problems
        with st.expander("📚 Example Problems You Can Try"):
            st.markdown("""
            **Tangent Length Problems:**
            - `Find the length of tangent from point (3,4) to circle with radius 5`
            - `Calculate tangent length from (6,8) to circle centered at origin with radius 4`
            - `Length of tangent from external point (5,12) to circle with radius 3`
            
            **Tangent Theorems:**
            - `Prove that tangent is perpendicular to radius`
            - `Show that tangents from external point are equal`
            - `Theorem 10.1 proof`
            - `Theorem 10.2 proof`
            
            **Construction Problems:**
            - `Construct tangent from external point`
            - `Draw tangent to circle from given point`
            - `Construction of tangent lines`
            
            **Real World Applications:**
            - `Find area covered by wheel rotation`
            - `Calculate coverage area of circular motion`
            - `Wheel rotation and distance problems`
            """)
        
        # Show key concepts
        with st.expander("🎯 Key Concepts - Chapter 10: Circles"):
            st.markdown("""
            **Important Theorems:**
            
            **Theorem 10.1:** The tangent at any point of a circle is perpendicular to the radius through the point of contact.
            
            **Theorem 10.2:** The lengths of tangents drawn from an external point to a circle are equal.
            
            **Key Formulas:**
            
            1. **Tangent Length Formula:**
               - If tangent is drawn from external point P(x₁, y₁) to circle with center O(h, k) and radius r
               - Length of tangent = √[(x₁-h)² + (y₁-k)² - r²]
            
            2. **For circle centered at origin:**
               - Length of tangent from P(x, y) = √[x² + y² - r²]
            
            3. **Angle between two tangents:**
               - If tangents are drawn from external point, angle between them can be calculated using trigonometry
            
            **Properties:**
            - Tangent touches circle at exactly one point
            - Tangent is perpendicular to radius at point of contact
            - Two tangents from external point are equal in length
            - Tangent segments from external point make equal angles with line joining external point to center
            """)
            
    except ImportError as e:
        st.error("❌ Could not import circle solver modules.")
        st.info("Please ensure all required files are in place:")
        st.code("""
        Required files:
        - chapters/chapter9_circles/main_router.py
        - chapters/chapter9_circles/interpret_query_circle.py
        - chapters/chapter9_circles/sub_chapters/ (with solver modules)
        """)
        st.exception(e)
    
    except Exception as e:
        st.error(f"❌ An error occurred: {str(e)}")
        st.info("Please check the console for more details.")