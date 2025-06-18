import streamlit as st
import sys, os

# Must be first Streamlit command
st.set_page_config(page_title='CBSE Math Solver', layout='wide')

# Add root for local imports
sys.path.append(os.path.abspath('.'))

# Imports
from chapter_sidebar import render_chapter_sidebar
from topic_handlers.chapter1_real_numbers_handler import handle_chapter1_real_numbers
from topic_handlers.chapter2_polynomials_handler import handle_chapter2_polynomials
from topic_handlers.chapter6_triangles_handler import handle_chapter6_triangles
from topic_handlers.chapter10_circles_handler import handle_chapter10_circles
from topic_handlers.chapter11_areas_circles_handler import handle_chapter11_areas_circles
from topic_handlers.chapter12_surface_areas_handler import handle_chapter12_surface_areas

# Sidebar
render_chapter_sidebar()

# Title
st.title('📘 CBSE Class X – Math Query Solver')

# Selected Topic
topic = st.session_state.get('selected_topic', '')

if topic:
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
    elif 'Question Bank' in topic:
        st.markdown(f'📚 Displaying questions for **{topic}** (static placeholder)')
        st.markdown('- Q1: Example question\n- Q2: Another question')
    else:
        st.info('⚠️ This topic is not yet implemented.')

else:
    st.info('Please select a topic from the sidebar.')
    
    # Show welcome message
    st.markdown("""
    ### Welcome to CBSE Math Solver! 🎯
    
    This interactive tool helps you:
    - 🧮 Solve mathematical problems step-by-step
    - 📊 Visualize concepts with graphs and calculations
    - 📚 Access formulas and explanations
    - 🎯 Practice with guided examples
    
    **Currently Available Chapters:**
    - ✅ **Chapter 1: Real Numbers** (HCF/LCM, Prime Factorization, Irrationality Proofs)
    - ✅ **Chapter 2: Polynomials** (Factoring, Graphing)
    - ✅ **Chapter 6: Triangles** (Right Triangles, Similarity, BPT)
    - ✅ **Chapter 10: Circles** (Tangent Properties, Circle Theorems)
    - ✅ **Chapter 11: Areas Related to Circles**
    - ✅ **Chapter 12: Surface Areas and Volumes** (3D Visualization, Calculations)
    - 🔄 More chapters coming soon...
    
    👈 **Select a topic from the sidebar to begin!**
    """)
    
    # Add sample problems
    with st.expander("📝 Sample Problems You Can Try"):
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
        
        **Chapter 10 - Circles:**
        - `Find tangent length from point (3,4) to circle with radius 5`
        - `Prove tangent is perpendicular to radius`
        - `Find angle between two tangents from external point`
        
        **Chapter 12 - Surface Areas and Volumes:**
        - `Find volume of cylinder with radius 7 cm and height 10 cm`
        - `Calculate surface area of cone with radius 5 cm and height 12 cm`
        - `Find TSA of sphere with radius 14 cm`
        """)

# Footer
st.markdown("---")
st.markdown("📚 *CBSE Class X Mathematics Solver - Making Math Visual and Interactive*")
