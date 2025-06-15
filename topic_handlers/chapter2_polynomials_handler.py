# File: cbse_math_solver/handlers/chapter2_polynomials_handler.py

import streamlit as st
from sympy import symbols, Poly, sympify

from utils.sanitizer import sanitize_expression, clean_query
from chapters.chapter2_polynomials.main_router import route_query
from chapters.chapter2_polynomials.sub_chapters.polynomial_factoring.plot_polynomial import plot_polynomial
from chapters.chapter2_polynomials.sub_chapters.polynomial_factoring.narrator_polynomial import narrate_polynomial_plot

def handle_chapter2_polynomials(topic: str):
    st.subheader(f'Selected: {topic}')

    if topic == 'Chapter 2: Polynomials > Polynomial Factoring':
        st.markdown('### 🧮 Polynomial Factoring (Quadratic & Cubic)')
        
        # Add example buttons for quick testing
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("Example: x² - 5x + 6"):
                st.session_state['poly_input'] = "x^2 - 5x + 6"
        with col2:
            if st.button("Example: x³ - 6x² + 11x - 6"):
                st.session_state['poly_input'] = "x^3 - 6x^2 + 11x - 6"
        with col3:
            if st.button("Example: x³ + x² - 4x - 4"):
                st.session_state['poly_input'] = "x^3 + x^2 - 4x - 4"
        
        # Input field
        default_value = st.session_state.get('poly_input', '')
        user_query = st.text_input(
            'Enter polynomial to factor (supports quadratic and cubic):',
            value=default_value,
            placeholder="e.g., x^2 + 5x + 6 or x^3 - 2x^2 - 5x + 6"
        )

        if user_query:
            with st.spinner('Factoring...'):
                # Clean input
                raw_expr = clean_query(user_query)

                # Route to factoring logic
                result = route_query(raw_expr)
                
                # Display result in a nice box
                st.markdown("---")
                st.markdown(result)

                # Try plotting
                try:
                    expr = sanitize_expression(raw_expr)
                    x = symbols('x')
                    poly = Poly(sympify(expr), x)
                    degree = poly.degree()
                    coeffs = poly.all_coeffs()

                    if degree == 2 and len(coeffs) == 3:
                        # Quadratic polynomial
                        a, b, c = map(float, coeffs)
                        plot_path = plot_polynomial([a, b, c], degree=2)
                        st.image(plot_path, caption="Quadratic Polynomial Curve")

                        st.markdown("### 🗣️ Visual Explanation")
                        narration = narrate_polynomial_plot([a, b, c], degree=2)
                        st.info(narration)
                        
                    elif degree == 3 and len(coeffs) == 4:
                        # Cubic polynomial
                        a, b, c, d = map(float, coeffs)
                        plot_path = plot_polynomial([a, b, c, d], degree=3)
                        st.image(plot_path, caption="Cubic Polynomial Curve")

                        st.markdown("### 🗣️ Visual Explanation")
                        narration = narrate_polynomial_plot([a, b, c, d], degree=3)
                        st.info(narration)
                        
                    else:
                        st.warning(f"Plotting is supported only for quadratic (degree 2) and cubic (degree 3) polynomials. Your polynomial has degree {degree}.")

                except Exception as e:
                    st.warning(f"⚠️ Could not extract coefficients for plotting: {e}")
                    
        # Add information box
        with st.expander("ℹ️ About Polynomial Factoring"):
            st.markdown("""
            **Supported polynomial types:**
            - **Quadratic**: ax² + bx + c
            - **Cubic**: ax³ + bx² + cx + d
            
            **How it works:**
            1. For quadratics, we check the discriminant (b² - 4ac)
            2. For cubics, we use the Rational Root Theorem and factor theorem
            3. The graph shows real roots as red dots where the curve crosses the x-axis
            4. Green triangles (for cubics) show critical points (local max/min)
            
            **Tips:**
            - Use ^ for exponents (x^2 means x²)
            - Coefficients can be positive or negative
            - Not all polynomials can be factored over real numbers!
            """)

    elif 'Question Bank' in topic:
        st.markdown(f'📚 Displaying questions for **{topic}** (static placeholder)')
        st.markdown('- Q1: Example question\n- Q2: Another question')