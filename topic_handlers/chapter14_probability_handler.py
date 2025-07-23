# File: topic_handlers/chapter14_probability_handler.py

import streamlit as st
import math
from fractions import Fraction
from chapters.chapter14_probability.main_router import route_query

def handle_chapter14_probability(topic: str):
    st.subheader(f'Selected: {topic}')
    
    if 'Simple Probability' in topic and 'Question Bank' not in topic:
        st.markdown('### 🎲 Probability Calculator')
        
        # Add tabs for different sections
        tab1, tab2, tab3, tab4 = st.tabs(["🎯 Calculate", "📊 Examples", "📚 Formulas", "🎯 Practice"])
        
        with tab1:
            st.markdown("#### Enter your probability query or select a problem type:")
            trigger_calculation = False
            
            # Quick selection buttons
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                if st.button("🎲 Dice Problems"):
                    st.session_state['probability_input'] = "What is the probability of getting 4 when rolling a die?"
                    trigger_calculation = True
            with col2:
                if st.button("🪙 Coin Problems"):
                    st.session_state['probability_input'] = "Find probability of getting 2 heads when tossing 3 coins"
                    trigger_calculation = True
            with col3:
                if st.button("🃏 Card Problems"):
                    st.session_state['probability_input'] = "What is the probability of drawing a king from a deck?"
                    trigger_calculation = True
            with col4:
                if st.button("⚽ Ball Problems"):
                    st.session_state['probability_input'] = "A bag has 5 red and 3 blue balls. Find probability of drawing a red ball."
                    trigger_calculation = True
            
            # Input field
            default_value = st.session_state.get('probability_input', '')
            user_query = st.text_area(
                'Enter your probability question:',
                value=default_value,
                placeholder="Examples:\n• What is the probability of getting sum 7 when rolling two dice?\n• Find probability of getting at least 2 heads in 3 coin tosses\n• What is the probability of drawing a red card?\n• A bag contains 4 red and 6 blue balls. Find probability of drawing blue ball.",
                height=120
            )
            
            if user_query and (trigger_calculation or st.button("✅ Solve")):
                with st.spinner('Calculating probability...'):
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
                "Select problem type:",
                ["Dice Probability", "Coin Probability", "Card Probability", "Ball Probability", "Conditional Probability", "Combinations"]
            )

            if example_type == "Dice Probability":
                st.markdown("**🎲 Dice Probability Calculator**")
                
                dice_type = st.selectbox("Problem type:", ["Single Die", "Two Dice", "Conditions"])
                
                if dice_type == "Single Die":
                    col1, col2 = st.columns(2)
                    with col1:
                        condition = st.selectbox("Condition:", 
                            ["Specific Number", "Greater Than", "Less Than", "Not Equal", "Even", "Odd", "Prime"])
                    
                    if condition == "Specific Number":
                        with col2:
                            target = st.selectbox("Target number:", [1, 2, 3, 4, 5, 6])
                        query = f"What is the probability of getting {target} when rolling a die?"
                    elif condition == "Greater Than":
                        with col2:
                            threshold = st.selectbox("Greater than:", [1, 2, 3, 4, 5])
                        query = f"What is the probability of getting greater than {threshold} when rolling a die?"
                    elif condition == "Less Than":
                        with col2:
                            threshold = st.selectbox("Less than:", [2, 3, 4, 5, 6])
                        query = f"What is the probability of getting less than {threshold} when rolling a die?"
                    elif condition == "Not Equal":
                        with col2:
                            not_value = st.selectbox("Not equal to:", [1, 2, 3, 4, 5, 6])
                        query = f"What is the probability of not getting {not_value} when rolling a die?"
                    elif condition == "Even":
                        query = "What is the probability of getting an even number when rolling a die?"
                    elif condition == "Odd":
                        query = "What is the probability of getting an odd number when rolling a die?"
                    elif condition == "Prime":
                        query = "What is the probability of getting a prime number when rolling a die?"
                
                elif dice_type == "Two Dice":
                    sum_target = st.selectbox("Target sum:", list(range(2, 13)))
                    query = f"What is the probability of getting sum {sum_target} when rolling two dice?"
                
                if st.button("Calculate Dice Probability"):
                    with st.spinner('Calculating...'):
                        try:
                            result = route_query(query)
                            st.markdown(result)
                        except Exception as e:
                            st.error(f"Error: {str(e)}")

            elif example_type == "Coin Probability":
                st.markdown("**🪙 Coin Probability Calculator**")
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    num_coins = st.selectbox("Number of coins:", [1, 2, 3, 4, 5])
                with col2:
                    target_heads = st.selectbox("Target heads:", list(range(0, num_coins + 1)))
                with col3:
                    condition = st.selectbox("Condition:", ["Exactly", "At least", "At most"])
                
                if condition == "Exactly":
                    query = f"Find probability of getting exactly {target_heads} heads when tossing {num_coins} coins"
                elif condition == "At least":
                    query = f"Find probability of getting at least {target_heads} heads when tossing {num_coins} coins"
                else:  # At most
                    query = f"Find probability of getting at most {target_heads} heads when tossing {num_coins} coins"
                
                if st.button("Calculate Coin Probability"):
                    with st.spinner('Calculating...'):
                        try:
                            result = route_query(query)
                            st.markdown(result)
                        except Exception as e:
                            st.error(f"Error: {str(e)}")

            elif example_type == "Card Probability":
                st.markdown("**🃏 Card Probability Calculator**")
                
                card_type = st.selectbox("Card type:", 
                    ["King", "Queen", "Jack", "Ace", "Red Card", "Black Card", "Face Card", "Spade", "Heart", "Diamond", "Club"])
                
                query = f"What is the probability of drawing a {card_type.lower()} from a deck of cards?"
                
                if st.button("Calculate Card Probability"):
                    with st.spinner('Calculating...'):
                        try:
                            result = route_query(query)
                            st.markdown(result)
                        except Exception as e:
                            st.error(f"Error: {str(e)}")

            elif example_type == "Ball Probability":
                st.markdown("**⚽ Ball Drawing Probability**")
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    red_balls = st.number_input("Red balls:", min_value=0, max_value=20, value=5, step=1)
                with col2:
                    blue_balls = st.number_input("Blue balls:", min_value=0, max_value=20, value=3, step=1)
                with col3:
                    target_color = st.selectbox("Draw:", ["Red", "Blue", "Not Red", "Not Blue"])
                
                total_balls = red_balls + blue_balls
                if total_balls > 0:
                    query = f"A bag contains {red_balls} red and {blue_balls} blue balls. Find probability of drawing a {target_color.lower()} ball."
                    
                    if st.button("Calculate Ball Probability"):
                        with st.spinner('Calculating...'):
                            try:
                                result = route_query(query)
                                st.markdown(result)
                            except Exception as e:
                                st.error(f"Error: {str(e)}")
                else:
                    st.warning("Please specify at least one ball.")

            elif example_type == "Conditional Probability":
                st.markdown("**🔗 Conditional Probability**")
                
                prob_type = st.selectbox("Problem type:", ["Card Given Card", "Dice Given Dice", "Custom"])
                
                if prob_type == "Card Given Card":
                    query = "What is the probability of drawing a king given that the card is red?"
                elif prob_type == "Dice Given Dice":
                    query = "What is the probability of getting greater than 3 given that the number is even when rolling a die?"
                
                if st.button("Calculate Conditional Probability"):
                    with st.spinner('Calculating...'):
                        try:
                            result = route_query(query)
                            st.markdown(result)
                        except Exception as e:
                            st.error(f"Error: {str(e)}")

            elif example_type == "Combinations":
                st.markdown("**🔢 Combination Problems**")
                
                col1, col2 = st.columns(2)
                with col1:
                    n = st.number_input("n (total items):", min_value=1, max_value=20, value=5, step=1)
                with col2:
                    r = st.number_input("r (selected items):", min_value=0, max_value=int(n), value=2, step=1)
                
                query = f"Calculate C({n}, {r})"
                
                if st.button("Calculate Combinations"):
                    with st.spinner('Calculating...'):
                        try:
                            result = route_query(query)
                            st.markdown(result)
                        except Exception as e:
                            st.error(f"Error: {str(e)}")
        
        with tab3:
            st.markdown("#### 📚 Probability Formulas")
            formula_type = st.selectbox(
                "Select formula category:",
                ["All Formulas", "Basic Probability", "Conditional Probability", "Combinations", "Common Problems"]
            )
            if formula_type == "All Formulas":
                display_all_probability_formulas()
            else:
                display_specific_probability_formula(formula_type)
        
        with tab4:
            st.markdown("#### 🎯 Practice Problems")
            difficulty = st.select_slider(
                "Select difficulty:",
                options=["Easy", "Medium", "Hard"],
                value="Medium"
            )
            display_probability_practice_problems(difficulty)
    
    elif 'Question Bank' in topic:
        display_probability_question_bank()

def display_all_probability_formulas():
    st.markdown("""
    ### 📊 Complete Formula Sheet - Probability
    
    #### 1️⃣ Basic Probability
    - **P(E) = Number of favorable outcomes / Total number of outcomes**
    - **0 ≤ P(E) ≤ 1**
    - **P(not E) = 1 - P(E)**
    - **P(certain event) = 1**
    - **P(impossible event) = 0**
    
    #### 2️⃣ Dice Probability
    - **Single die:** P(any specific number) = 1/6
    - **Two dice:** Total outcomes = 36
    - **P(sum = 7) = 6/36 = 1/6** (most likely sum)
    - **P(even number) = P(odd number) = 1/2**
    
    #### 3️⃣ Coin Probability
    - **Single coin:** P(Head) = P(Tail) = 1/2
    - **n coins:** Total outcomes = 2ⁿ
    - **P(exactly k heads) = C(n,k) / 2ⁿ**
    
    #### 4️⃣ Card Probability
    - **Standard deck:** 52 cards
    - **P(King) = 4/52 = 1/13**
    - **P(Red card) = 26/52 = 1/2**
    - **P(Face card) = 12/52 = 3/13**
    
    #### 5️⃣ Conditional Probability
    - **P(A|B) = P(A ∩ B) / P(B)**
    - **P(A ∩ B) = P(A|B) × P(B)**
    - **For independent events:** P(A ∩ B) = P(A) × P(B)
    
    #### 6️⃣ Combinations
    - **C(n,r) = n! / [r!(n-r)!]**
    - **P(n,r) = n! / (n-r)!**
    - **C(n,0) = C(n,n) = 1**
    """)

def display_specific_probability_formula(formula_type: str):
    formulas = {
        "Basic Probability": """
### 🎯 Basic Probability Formulas

**Fundamental Formula:**
P(E) = Number of favorable outcomes / Total number of outcomes

**Properties:**
- 0 ≤ P(E) ≤ 1
- P(E) + P(not E) = 1
- P(certain event) = 1
- P(impossible event) = 0

**For equally likely outcomes:**
If all outcomes are equally likely, then probability of any single outcome = 1/n
where n = total number of outcomes

**Example Applications:**
- Rolling a die: P(getting 3) = 1/6
- Drawing a card: P(Ace) = 4/52 = 1/13
- Tossing a coin: P(Head) = 1/2
        """,
        
        "Conditional Probability": """
### 🔗 Conditional Probability Formulas

**Main Formula:**
P(A|B) = P(A ∩ B) / P(B)

**Multiplication Rule:**
P(A ∩ B) = P(A|B) × P(B) = P(B|A) × P(A)

**Bayes' Theorem:**
P(A|B) = [P(B|A) × P(A)] / P(B)

**Independence Test:**
Events A and B are independent if:
P(A|B) = P(A) or P(A ∩ B) = P(A) × P(B)

**Common Examples:**
- P(King | Red card) = 2/26 = 1/13
- P(Even | Greater than 3) for dice = 2/3
        """,
        
        "Combinations": """
### 🔢 Combinations and Permutations

**Combinations (order doesn't matter):**
C(n,r) = n! / [r!(n-r)!]

**Permutations (order matters):**
P(n,r) = n! / (n-r)!

**Key Properties:**
- C(n,r) = C(n,n-r)
- C(n,0) = 1
- C(n,n) = 1
- C(n,1) = n

**Probability with Combinations:**
P(selecting r specific items from n) = C(n,r) / Total ways

**Examples:**
- C(5,2) = 10 ways to choose 2 items from 5
- Probability in lottery, card selection
        """,
        
        "Common Problems": """
### 📝 Common Probability Problems

**Dice Problems:**
- P(sum = 7 with two dice) = 6/36 = 1/6
- P(at least one 6 in two throws) = 1 - (5/6)² = 11/36

**Coin Problems:**
- P(at least one head in n tosses) = 1 - (1/2)ⁿ
- P(exactly k heads in n tosses) = C(n,k) / 2ⁿ

**Card Problems:**
- P(both cards are aces) = (4/52) × (3/51) = 1/221
- P(at least one face card in 2 draws) = 1 - (40/52) × (39/51)

**Ball Problems:**
- Without replacement: probabilities change
- With replacement: probabilities remain same
        """
    }
    st.markdown(formulas.get(formula_type, "❌ Unknown formula type"))

def display_probability_practice_problems(difficulty: str):
    problems = {
        "Easy": [
            "What is the probability of getting 4 when rolling a die?",
            "Find the probability of getting heads when tossing a coin.",
            "What is the probability of drawing a red card from a deck?",
            "A bag has 3 red and 2 blue balls. Find probability of drawing a red ball.",
            "What is the probability of getting an even number on a die?"
        ],
        "Medium": [
            "Find the probability of getting sum 8 when rolling two dice.",
            "What is the probability of getting at least 2 heads in 3 coin tosses?",
            "Find the probability of drawing a king given that the card is a face card.",
            "A bag has 5 red, 3 blue, and 2 green balls. Find probability of not drawing red.",
            "What is the probability of getting exactly 2 heads in 4 coin tosses?"
        ],
        "Hard": [
            "Three coins are tossed. Find probability of getting at least 2 heads.",
            "Two cards are drawn without replacement. Find probability both are aces.",
            "A die is rolled twice. Find probability that product of numbers is even.",
            "Find probability that in a group of 4 people, at least 2 have same birthday month.",
            "A bag has balls numbered 1-10. Two balls drawn without replacement. Find probability sum is odd."
        ]
    }
    
    st.markdown(f"### 📝 {difficulty} Practice Problems")
    for i, problem in enumerate(problems[difficulty], 1):
        with st.expander(f"Problem {i}: {problem}"):
            if st.button(f"Solve Problem {i}", key=f"practice_{difficulty}_{i}"):
                with st.spinner('Solving...'):
                    try:
                        result = route_query(problem)
                        st.markdown(result)
                    except Exception as e:
                        st.error(f"Error: {str(e)}")

def display_probability_question_bank():
    st.markdown("""
### 📚 Question Bank - Probability

#### 🔢 Multiple Choice Questions

1. The probability of getting an even number when rolling a die is:
   - a) 1/6
   - b) 1/3
   - c) 1/2 ✅
   - d) 2/3

2. In a deck of 52 cards, the probability of drawing a king is:
   - a) 1/13 ✅
   - b) 4/52
   - c) 1/4
   - d) 1/52

3. When two coins are tossed, the probability of getting at least one head is:
   - a) 1/4
   - b) 1/2
   - c) 3/4 ✅
   - d) 1

4. The probability of an impossible event is:
   - a) 1
   - b) 1/2
   - c) 0 ✅
   - d) Cannot be determined

#### ✏️ Short Answer Questions

1. A die is thrown. Find the probability of getting a prime number.
2. Two coins are tossed simultaneously. Find the probability of getting exactly one head.
3. From a deck of 52 cards, what is the probability of drawing a red king?
4. A bag contains 4 red, 3 blue, and 2 green balls. Find the probability of drawing a blue ball.

#### 📝 Long Answer Questions

1. **Dice Problem:**
   Two dice are thrown simultaneously. Find the probability of:
   - a) Getting sum equal to 9
   - b) Getting sum less than or equal to 4
   - c) Getting same number on both dice
   - d) Getting different numbers on both dice

2. **Card Problem:**
   Two cards are drawn from a deck without replacement. Find the probability that:
   - a) Both are aces
   - b) Both are of the same suit
   - c) One is red and one is black
   - d) At least one is a face card

3. **Conditional Probability:**
   In a class of 30 students, 18 play cricket and 15 play football. 8 play both games.
   - a) Find probability that a randomly selected student plays cricket
   - b) Find probability that a student plays football given that he plays cricket
   - c) Are the events independent?

4. **Application Problem:**
   A bag contains 5 red and 3 white balls. Two balls are drawn one after another without replacement.
   - a) Find probability that both balls are red
   - b) Find probability that both balls are of different colors
   - c) If the first ball drawn is red, what is the probability that second is white?
""")