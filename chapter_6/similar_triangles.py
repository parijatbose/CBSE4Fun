import streamlit as st
import numpy as np
from .utils.triangle_solver import TriangleSolver
from .utils.triangle_plotter import TrianglePlotter

def check_similar_triangles():
    st.title("Similar Triangles Checker")
    
    # Input for first triangle
    st.subheader("First Triangle")
    col1, col2, col3 = st.columns(3)
    with col1:
        a1 = st.number_input("Side a", min_value=0.1, value=3.0, step=0.1, key="a1")
    with col2:
        b1 = st.number_input("Side b", min_value=0.1, value=4.0, step=0.1, key="b1")
    with col3:
        c1 = st.number_input("Side c", min_value=0.1, value=5.0, step=0.1, key="c1")
    
    # Input for second triangle
    st.subheader("Second Triangle")
    col1, col2, col3 = st.columns(3)
    with col1:
        a2 = st.number_input("Side a", min_value=0.1, value=6.0, step=0.1, key="a2")
    with col2:
        b2 = st.number_input("Side b", min_value=0.1, value=8.0, step=0.1, key="b2")
    with col3:
        c2 = st.number_input("Side c", min_value=0.1, value=10.0, step=0.1, key="c2")
    
    # Check if triangles are similar
    sides1 = [a1, b1, c1]
    sides2 = [a2, b2, c2]
    
    # Validate triangles
    if not TriangleSolver.is_valid_triangle(sides1):
        st.error("First triangle is not valid! The sum of any two sides must be greater than the third side.")
        return
    
    if not TriangleSolver.is_valid_triangle(sides2):
        st.error("Second triangle is not valid! The sum of any two sides must be greater than the third side.")
        return
    
    # Check similarity
    is_similar, scale_factor = TriangleSolver.are_similar_triangles(sides1, sides2)
    
    # Display results
    if is_similar:
        st.success(f"✅ The triangles are similar!")
        st.info(f"Scale factor: {scale_factor:.2f}")
        
        # Additional information
        st.subheader("Additional Information")
        
        # Triangle types
        type1 = TriangleSolver.get_triangle_type(sides1)
        type2 = TriangleSolver.get_triangle_type(sides2)
        st.write(f"First triangle is {type1}")
        st.write(f"Second triangle is {type2}")
        
        # Right triangle check
        if TriangleSolver.is_right_triangle(sides1):
            st.write("First triangle is a right triangle")
        if TriangleSolver.is_right_triangle(sides2):
            st.write("Second triangle is a right triangle")
        
        # Visualize triangles
        st.subheader("Triangle Visualization")
        plotter = TrianglePlotter()
        
        # Calculate points for first triangle (3-4-5)
        points1 = [(0, 0), (3, 0), (0, 4)]
        angles1 = [90, 53, 37]  # Approximate angles for 3-4-5 triangle
        
        # Calculate points for second triangle (6-8-10)
        points2 = [(0, 0), (6, 0), (0, 8)]
        angles2 = [90, 53, 37]  # Same angles as first triangle
        
        # Plot both triangles
        col1, col2 = st.columns(2)
        with col1:
            st.write("First Triangle")
            fig1 = plotter.plot_triangle(points1, angles1)
            st.pyplot(fig1)
        
        with col2:
            st.write("Second Triangle")
            fig2 = plotter.plot_triangle(points2, angles2)
            st.pyplot(fig2)
        
        # Explanation
        st.subheader("Explanation")
        st.write("""
        Two triangles are similar if their corresponding sides are proportional.
        In this case:
        - First triangle sides: 3, 4, 5
        - Second triangle sides: 6, 8, 10
        
        The ratio of corresponding sides is 2:1 (6/3 = 8/4 = 10/5 = 2)
        Therefore, the triangles are similar with a scale factor of 2.
        """)
    else:
        st.error("❌ The triangles are not similar!")
        
        # Show why they're not similar
        st.subheader("Analysis")
        sides1_sorted = sorted(sides1)
        sides2_sorted = sorted(sides2)
        ratios = [sides2_sorted[i] / sides1_sorted[i] for i in range(3)]
        
        st.write("Side ratios:")
        for i in range(3):
            st.write(f"Ratio {i+1}: {ratios[i]:.2f}")
        
        st.write("""
        For triangles to be similar, all side ratios must be equal.
        In this case, the ratios are different, which means the triangles are not similar.
        """) 