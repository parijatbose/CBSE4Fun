# File: topic_handlers/chapter1_real_numbers_handler.py

import streamlit as st
import math
from chapters.chapter1_real_numbers.main_router import route_query

def handle_chapter1_real_numbers(topic: str):
    st.subheader(f'Selected: {topic}')
    
    if 'Real Numbers' in topic and 'Question Bank' not in topic:
        st.markdown('### 🔢 Real Numbers Calculator')
        
        # Add tabs for different sections
        tab1, tab2, tab3, tab4 = st.tabs(["🔢 Calculate", "📊 Examples", "📚 Formulas", "🎯 Practice"])
        
        with tab1:
            st.markdown("#### Enter your query or select a calculation type:")
            trigger_calculation = False
            
            # Quick selection buttons
            col1, col2, col3 = st.columns(3)
            with col1:
                if st.button("🔢 HCF & LCM"):
                    st.session_state['real_numbers_input'] = "Find HCF and LCM of 12 and 18"
                    trigger_calculation = True
            with col2:
                if st.button("🧮 Prime Factorization"):
                    st.session_state['real_numbers_input'] = "Prime factorization of 60"
                    trigger_calculation = True
            with col3:
                if st.button("🔍 Irrationality Proof"):
                    st.session_state['real_numbers_input'] = "Prove √2 is irrational"
                    trigger_calculation = True
            
            # Input field
            default_value = st.session_state.get('real_numbers_input', '')
            user_query = st.text_area(
                'Enter your query:',
                value=default_value,
                placeholder="Examples:\n• Find HCF and LCM of 24 and 36\n• Prime factorization of 144\n• Prove √3 + 2 is irrational\n• HCF of 48 and 72 using Euclidean algorithm",
                height=120
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
            st.markdown("#### 📊 Interactive Examples")
            
            example_type = st.selectbox(
                "Select example type:",
                ["HCF and LCM Calculator", "Prime Factorization", "Irrationality Checker", "Euclidean Algorithm"]
            )

            if example_type == "HCF and LCM Calculator":
                st.markdown("**📊 HCF and LCM Calculator**")
                
                col1, col2 = st.columns(2)
                with col1:
                    num1 = st.number_input("First Number:", min_value=1, max_value=10000, value=12, step=1, key="hcf_num1")
                with col2:
                    num2 = st.number_input("Second Number:", min_value=1, max_value=10000, value=18, step=1, key="hcf_num2")
                
                if st.button("Calculate HCF and LCM"):
                    with st.spinner('Calculating...'):
                        try:
                            result = route_query(f"Find HCF and LCM of {int(num1)} and {int(num2)}")
                            st.markdown(result)
                        except Exception as e:
                            st.error(f"Error: {str(e)}")

            elif example_type == "Prime Factorization":
                st.markdown("**🧮 Prime Factorization**")
                
                number = st.number_input("Enter a number:", min_value=2, max_value=10000, value=60, step=1, key="prime_num")
                
                if st.button("Find Prime Factorization"):
                    with st.spinner('Calculating...'):
                        try:
                            result = route_query(f"Prime factorization of {int(number)}")
                            st.markdown(result)
                        except Exception as e:
                            st.error(f"Error: {str(e)}")

            elif example_type == "Irrationality Checker":
                st.markdown("**🔍 Irrationality Proof Generator**")
                
                expression_type = st.selectbox(
                    "Choose expression type:",
                    ["√n", "√n ± k", "a + b√n", "r√n", "1/√n"]
                )
                
                if expression_type == "√n":
                    n = st.number_input("Enter n:", min_value=2, max_value=100, value=2, step=1, key="sqrt_n")
                    expression = f"√{int(n)}"
                elif expression_type == "√n ± k":
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        n = st.number_input("n:", min_value=2, max_value=100, value=2, step=1, key="sqrt_n_k")
                    with col2:
                        operation = st.selectbox("Operation:", ["+", "-"], key="op_n_k")
                    with col3:
                        k = st.number_input("k:", min_value=1, max_value=100, value=3, step=1, key="k_n")
                    expression = f"√{int(n)} {operation} {int(k)}"
                elif expression_type == "a + b√n":
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        a = st.number_input("a:", min_value=1, max_value=100, value=2, step=1, key="a_val")
                    with col2:
                        b = st.number_input("b:", min_value=1, max_value=100, value=3, step=1, key="b_val")
                    with col3:
                        n = st.number_input("n:", min_value=2, max_value=100, value=5, step=1, key="n_val")
                    expression = f"{int(a)} + {int(b)}√{int(n)}"
                elif expression_type == "r√n":
                    col1, col2 = st.columns(2)
                    with col1:
                        r = st.number_input("r:", min_value=1, max_value=100, value=2, step=1, key="r_val")
                    with col2:
                        n = st.number_input("n:", min_value=2, max_value=100, value=3, step=1, key="rn_val")
                    expression = f"{int(r)}√{int(n)}"
                else:  # 1/√n
                    n = st.number_input("Enter n:", min_value=2, max_value=100, value=3, step=1, key="inv_sqrt_n")
                    expression = f"1/√{int(n)}"
                
                st.write(f"**Expression:** {expression}")
                
                if st.button("Generate Irrationality Proof"):
                    with st.spinner('Generating proof...'):
                        try:
                            result = route_query(f"Prove {expression} is irrational")
                            st.markdown(result)
                        except Exception as e:
                            st.error(f"Error: {str(e)}")

            else:  # Euclidean Algorithm
                st.markdown("**🔄 Euclidean Algorithm**")
                
                col1, col2 = st.columns(2)
                with col1:
                    a = st.number_input("First Number (a):", min_value=1, max_value=10000, value=48, step=1, key="euc_a")
                with col2:
                    b = st.number_input("Second Number (b):", min_value=1, max_value=10000, value=18, step=1, key="euc_b")
                
                if st.button("Apply Euclidean Algorithm"):
                    with st.spinner('Calculating...'):
                        try:
                            result = route_query(f"Find HCF of {int(a)} and {int(b)} using Euclidean algorithm")
                            st.markdown(result)
                        except Exception as e:
                            st.error(f"Error: {str(e)}")
        
        with tab3:
            st.markdown("#### 📚 Quick Formula Reference")
            formula_type = st.selectbox(
                "Select formula type:",
                ["All Formulas", "HCF and LCM", "Prime Factorization", "Irrationality Proofs", "Euclidean Algorithm"]
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
    st.markdown("""
    ### 📊 Complete Formula Sheet - Real Numbers
    
    #### 1️⃣ HCF and LCM
    - **HCF:** Product of smallest powers of common prime factors
    - **LCM:** Product of greatest powers of all prime factors
    - **Relationship:** HCF(a,b) × LCM(a,b) = a × b
    
    #### 2️⃣ Prime Factorization
    - **Fundamental Theorem:** Every integer > 1 has unique prime factorization
    - **Method:** Divide by smallest primes successively
    - **Standard Form:** n = p₁^a₁ × p₂^a₂ × ... × pₖ^aₖ
    
    #### 3️⃣ Euclidean Algorithm
    - **For HCF(a,b):** a = bq + r, then HCF(a,b) = HCF(b,r)
    - **Continue until remainder = 0**
    - **Last non-zero remainder is the HCF**
    
    #### 4️⃣ Irrationality Proofs
    - **Method:** Proof by contradiction
    - **Assume rational, derive contradiction**
    - **√p is irrational if p is not a perfect square**
    - **Sum of rational and irrational is irrational**
    
    #### 5️⃣ Number Classification
    - **Natural Numbers:** 1, 2, 3, 4, ...
    - **Whole Numbers:** 0, 1, 2, 3, 4, ...
    - **Integers:** ..., -2, -1, 0, 1, 2, ...
    - **Rational Numbers:** p/q where p, q ∈ ℤ, q ≠ 0
    - **Irrational Numbers:** Cannot be expressed as p/q
    - **Real Numbers:** All rational and irrational numbers
    """)

def display_specific_formula(formula_type: str):
    formulas = {
        "HCF and LCM": """
### 🔢 HCF and LCM Formulas

**Using Prime Factorization:**
- **HCF = Product of smallest powers of common primes**
- **LCM = Product of greatest powers of all primes**

**Key Relationships:**
- HCF(a,b) × LCM(a,b) = a × b
- If gcd(a,b) = 1, then LCM(a,b) = a × b
- HCF(a,b) ≤ min(a,b)
- LCM(a,b) ≥ max(a,b)

**Example:**
For 12 = 2² × 3 and 18 = 2 × 3²
- HCF = 2¹ × 3¹ = 6
- LCM = 2² × 3² = 36
        """,
        
        "Prime Factorization": """
### 🧮 Prime Factorization

**Fundamental Theorem of Arithmetic:**
Every integer greater than 1 is either prime or can be expressed as a unique product of primes.

**Method:**
1. Start with smallest prime (2)
2. Divide repeatedly while possible
3. Move to next prime
4. Continue until quotient = 1

**Standard Form:**
n = p₁^a₁ × p₂^a₂ × ... × pₖ^aₖ

**Applications:**
- Finding HCF and LCM
- Simplifying fractions
- Solving Diophantine equations
        """,
        
        "Irrationality Proofs": """
### 🔍 Irrationality Proof Methods

**Proof by Contradiction:**
1. Assume the number is rational
2. Express as p/q in lowest terms
3. Derive mathematical contradiction
4. Conclude the assumption is false

**Common Types:**
- **√n:** Where n is not a perfect square
- **a ± √n:** Sum/difference with rational number
- **a/√n:** Reciprocal involving square root

**Key Principle:**
- Rational ± Irrational = Irrational
- Rational × Irrational = Irrational (if rational ≠ 0)
        """,
        
        "Euclidean Algorithm": """
### 🔄 Euclidean Algorithm

**For finding HCF(a,b):**

**Steps:**
1. Divide a by b: a = bq₁ + r₁
2. Divide b by r₁: b = r₁q₂ + r₂
3. Continue: r₁ = r₂q₃ + r₃
4. Stop when remainder = 0
5. Last non-zero remainder is HCF

**Extended Euclidean Algorithm:**
Finds integers x, y such that:
HCF(a,b) = ax + by

**Efficiency:**
- Faster than prime factorization for large numbers
- At most 5k steps for k-digit numbers
        """
    }
    st.markdown(formulas.get(formula_type, "❌ Unknown formula type"))

def display_practice_problems(difficulty: str):
    problems = {
        "Easy": [
            "Find HCF and LCM of 12 and 16.",
            "Prime factorization of 24.",
            "Prove √4 is rational or irrational.",
            "Use Euclidean algorithm to find HCF of 15 and 25."
        ],
        "Medium": [
            "Find HCF and LCM of 72, 108, and 144.",
            "Prime factorization of 360.",
            "Prove √2 + 3 is irrational.",
            "Find HCF of 1071 and 462 using Euclidean algorithm.",
            "Express 2/3 + 4/5 in simplest form."
        ],
        "Hard": [
            "If HCF(a,b) = 12 and LCM(a,b) = 180, find possible values of a and b.",
            "Prove that √2 + √3 is irrational.",
            "Find the smallest number that leaves remainder 2 when divided by 3, 4, 5, and 6.",
            "Use Extended Euclidean Algorithm to find integers x, y such that 35x + 15y = 5.",
            "Prove that 1/(2 + √3) is irrational."
        ]
    }
    st.markdown(f"### 📝 {difficulty} Problems")
    for i, q in enumerate(problems[difficulty], 1):
        st.markdown(f"{i}. {q}")

def display_question_bank():
    st.markdown("""
### 📚 Question Bank - Real Numbers

#### 🔢 Multiple Choice Questions

1. The HCF of 12 and 18 is:
   - a) 2
   - b) 3
   - c) 6 ✅
   - d) 9

2. Which of the following is irrational?
   - a) √16
   - b) √2 ✅
   - c) 3/4
   - d) 0.25

3. The LCM of 15 and 25 is:
   - a) 5
   - b) 75 ✅
   - c) 125
   - d) 375

4. The decimal expansion of a rational number is:
   - a) Always terminating
   - b) Always non-terminating and repeating ✅
   - c) Always non-terminating and non-repeating
   - d) Can be terminating or non-terminating repeating

#### ✏️ Short Answer Questions

1. Find the HCF and LCM of 36 and 48 using prime factorization.
2. Prove that √3 is irrational.
3. Express 0.overline{23} as a rational number in p/q form.
4. Find the largest number that divides 525 and 3000 leaving remainders 5 and 8 respectively.

#### 📝 Long Answer Questions

1. **Prime Factorization Problem:**
   Find the HCF and LCM of 144, 180, and 192.
   - Express each number in prime factorized form
   - Find HCF using the method of common prime factors
   - Find LCM using the method of highest powers
   - Verify your answer

2. **Irrationality Proof:**
   Prove that 2 + √3 is irrational.
   - Use the method of contradiction
   - Show all algebraic steps clearly
   - State the final conclusion

3. **Euclidean Algorithm:**
   Use the Euclidean algorithm to find HCF(1071, 1029).
   - Show all division steps
   - Find the HCF
   - Verify using prime factorization method

4. **Application Problem:**
   Three bells ring at intervals of 12, 15, and 18 minutes respectively.
   - When will they ring together again?
   - How many times will they ring together in 6 hours?
   - What mathematical concept is used to solve this?
""")