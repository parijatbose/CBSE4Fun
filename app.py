import streamlit as st
import sys, os

# Must be first Streamlit command
st.set_page_config(
    page_title='CBSE Math Solver', 
    layout='wide',
    initial_sidebar_state='expanded',
    menu_items={
        'About': "CBSE Class X Mathematics Solver with Interactive Plotting"
    }
)

# Add root for local imports
sys.path.append(os.path.abspath('.'))

# Imports with error handling
try:
    from chapter_sidebar import render_chapter_sidebar
    from topic_handlers.chapter1_real_numbers_handler import handle_chapter1_real_numbers
    from topic_handlers.chapter2_polynomials_handler import handle_chapter2_polynomials
    from topic_handlers.chapter6_triangles_handler import handle_chapter6_triangles
    from topic_handlers.chapter10_circles_handler import handle_chapter10_circles
    from topic_handlers.chapter11_areas_circles_handler import handle_chapter11_areas_circles
    from topic_handlers.chapter12_surface_areas_handler import handle_chapter12_surface_areas
    from topic_handlers.chapter14_probability_handler import handle_chapter14_probability
except ImportError as e:
    st.error(f"❌ Import Error: {e}")
    st.info("Please ensure all handler files are present in the topic_handlers directory.")
    st.stop()

# Initialize session state for better performance
if 'app_initialized' not in st.session_state:
    st.session_state.app_initialized = True
    # Add any initialization logic here

# Sidebar
try:
    render_chapter_sidebar()
except Exception as e:
    st.error(f"❌ Sidebar Error: {e}")

# Title with enhanced styling
st.title('📘 CBSE Class X – Math Query Solver')
st.caption("🎨 Now with Interactive Plotting and Visualizations!")

# Selected Topic
topic = st.session_state.get('selected_topic', '')

if topic:
    # Add progress indicator for better UX
    with st.spinner(f"Loading {topic}..."):
        try:
            # Route to appropriate chapter handler
            if topic.startswith('Chapter 1: Real Numbers'):
                handle_chapter1_real_numbers(topic)
            elif topic.startswith('Chapter 2: Polynomials'):
                handle_chapter2_polynomials(topic)
            elif topic.startswith('Chapter 6: Triangles'):
                handle_chapter6_triangles(topic)
            elif topic.startswith('Chapter 10: Circles'):
                handle_chapter10_circles(topic)
            elif topic.startswith('Chapter 11: Areas Related to Circles'):
                handle_chapter11_areas_circles(topic)
            elif topic.startswith('Chapter 12: Surface Areas and Volumes'):
                handle_chapter12_surface_areas(topic)
            elif topic.startswith('Chapter 14: Probability'):
                handle_chapter14_probability(topic)

            elif 'Question Bank' in topic:
                st.markdown(f'📚 Displaying questions for **{topic}** (static placeholder)')
                st.markdown('- Q1: Example question\n- Q2: Another question')
            else:
                st.info('⚠️ This topic is not yet implemented.')
        except Exception as e:
            st.error(f"❌ Error loading {topic}: {str(e)}")
            st.info("Please try refreshing the page or selecting a different topic.")
            with st.expander("🔧 Debug Information"):
                st.exception(e)

else:
    st.info('Please select a topic from the sidebar.')
    
    # Show welcome message with enhanced formatting
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### Welcome to CBSE Math Solver! 🎯
        
        This interactive tool helps you:
        - 🧮 Solve mathematical problems step-by-step
        - 📊 **NEW!** Visualize concepts with interactive plots and diagrams
        - 📚 Access formulas and explanations
        - 🎯 Practice with guided examples
        - 🎨 **NEW!** Generate NCERT-style constructions and proofs
        
        **Currently Available Chapters:**
        - ✅ **Chapter 1: Real Numbers** (HCF/LCM, Prime Factorization, Irrationality Proofs)
        - ✅ **Chapter 2: Polynomials** (Factoring, Graphing)
        - ✅ **Chapter 6: Triangles** (Right Triangles, Similarity, BPT)
        - ✅ **Chapter 10: Circles** 🎨 **(Tangent Properties, Interactive Plotting, Visual Proofs)**
        - ✅ **Chapter 11: Areas Related to Circles**
        - ✅ **Chapter 12: Surface Areas and Volumes** (3D Visualization, Calculations)
        - 🔄 More chapters coming soon...
        
        👈 **Select a topic from the sidebar to begin!**
        """)
    
    with col2:
        st.markdown("""
        ### 🎨 New Plotting Features!
        
        **Chapter 10 - Circles:**
        - Interactive tangent construction
        - Step-by-step NCERT methods
        - Theorem visual proofs
        - Custom variable support
        - Real-time calculations
        
        **Try these plot commands:**
        - "Draw circle with radius=5"
        - "Show tangent construction"
        - "Visualize theorem 10.1"
        """)
    
    # Add sample problems with plot examples
    with st.expander("📝 Sample Problems You Can Try"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **Chapter 1 - Real Numbers:**
            - `Find HCF and LCM of 24 and 36`
            - `Prime factorization of 144`
            - `Prove √2 is irrational`
            - `HCF of 48 and 18 using Euclidean algorithm`
            
            **Chapter 6 - Triangles:**
            - `Find hypotenuse of right triangle with base 3 and height 4`
            - `Check if triangles with sides (3,4,5) and (6,8,10) are similar`
            - `Find area of triangle with sides 5, 6, 7`
            
            **Chapter 2 - Polynomials:**
            - `factor x^2 - 5x + 6`
            - `y = x^3 - 4x`
            - `factorize x^2 + 7x + 12`
            """)
        
        with col2:
            st.markdown("""
            **Chapter 10 - Circles (🎨 WITH PLOTS!):**
            - `Draw tangent from point (5,3) to circle radius=2`
            - `Show theorem 10.1 proof with diagram`
            - `Visualize construction from external point`
            - `Plot circle center=(1,2) radius=3 with variables a=5, b=4`
            - `Create step-by-step tangent construction`
            
            **Chapter 12 - Surface Areas and Volumes:**
            - `Find volume of cylinder with radius 7 cm and height 10 cm`
            - `Calculate surface area of cone with radius 5 cm and height 12 cm`
            - `Find TSA of sphere with radius 14 cm`
            """)

    # Add quick start guide
    with st.expander("🚀 Quick Start Guide"):
        st.markdown("""
        ### How to Use the Plotting Features:
        
        1. **Select Chapter 10: Circles** from the sidebar
        2. **Check "Generate Diagram"** checkbox for visual plots
        3. **Type your query** with specific variables like:
           - `radius=5` for circle radius
           - `center=(2,3)` for circle center
           - `point=(7,4)` for external point
        4. **Use plot keywords** like "draw", "show", "visualize", "construct"
        5. **Click "Solve Problem"** and see interactive diagrams!
        
        ### Example Workflow:
        ```
        Input: "Draw tangent from point (6,4) to circle center=(1,1) radius=3"
        ↓
        Output: Step-by-step construction + Interactive matplotlib plot
        ```
        """)

# Footer with version info
st.markdown("---")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("📚 *CBSE Class X Mathematics Solver v2.0 - Now with Interactive Plotting!*")
    st.markdown("🎨 *Making Math Visual and Interactive*")