# File: chapters/chapter14_probability/query_probability.py

import os
import re
import json
import base64
from io import BytesIO
from dotenv import load_dotenv
from groq import Groq

from chapters.chapter14_probability.sub_chapters.basic_probability.solver_basic import solve_basic_probability
from chapters.chapter14_probability.sub_chapters.conditional_probability.solver_conditional import solve_conditional_probability
from chapters.chapter14_probability.sub_chapters.combinations.solver_combinations import solve_combinations
from chapters.chapter14_probability.plot_probability import plot_dice_outcomes
from chapters.chapter14_probability.sub_chapters.basic_probability.solver_basic import (
    solve_dice_probability, solve_coin_probability, solve_card_probability, solve_ball_probability
)

# Load GROQ API key
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("❌ GROQ_API_KEY not found in .env")

client = Groq(api_key=api_key)

def interpret_query_probability(query: str) -> dict:
    """
    Uses LLM to classify the intent and extract parameters for a probability query.
    """
    prompt = f"""
        You are a math query classifier for CBSE Class 10 probability problems. 
        
        Classify the query and extract parameters. Return ONLY valid JSON.
        
        Intent categories:
        - "dice_probability": For dice rolling problems
        - "coin_probability": For coin tossing problems  
        - "card_probability": For card drawing problems
        - "ball_probability": For ball/marble drawing problems
        - "solve_basic": For basic probability calculations
        - "solve_conditional": For conditional probability problems
        - "solve_combinations": For combination/permutation problems
        - "formula_request": When asking for formulas
        
        Examples:
        Query: "What is the probability of getting sum 7 when rolling two dice?"
        Response: {{"intent": "dice_probability", "parameters": {{"num_dice": 2, "target_sum": 7}}}}
        
        Query: "What is the probability of not getting 3 when rolling a die?"
        Response: {{"intent": "dice_probability", "parameters": {{"num_dice": 1, "condition": "not_equal", "not_value": 3}}}}
        
        Query: "Find probability of getting at least 2 heads in 3 coin tosses"
        Response: {{"intent": "coin_probability", "parameters": {{"num_coins": 3, "target_heads": 2, "condition": "at_least"}}}}
        
        Query: "What is the probability of getting heads when a coin is tossed?"
        Response: {{"intent": "coin_probability", "parameters": {{"num_coins": 1, "target_heads": 1}}}}
        
        Query: "What is the probability of drawing a king from a deck of cards?"
        Response: {{"intent": "card_probability", "parameters": {{"target": "king", "deck_size": 52}}}}
        
        Query: "A bag contains 5 red and 3 blue balls. Find probability of drawing a red ball."
        Response: {{"intent": "ball_probability", "parameters": {{"red_balls": 5, "blue_balls": 3, "target": "red"}}}}
        
        Query: "A die is thrown. What is the probability of getting 4?"
        Response: {{"intent": "dice_probability", "parameters": {{"num_dice": 1, "target_sum": 4}}}}
        
        Query: "Two coins are tossed. What is the probability of getting at least one head?"
        Response: {{"intent": "coin_probability", "parameters": {{"num_coins": 2, "target_heads": 1, "condition": "at_least"}}}}
        
        Query: "{query}"
        
        Respond with valid JSON only:
        """

    # Multi-part detection moved BEFORE LLM call
    if any(x in query.lower() for x in ['a)', 'b)', 'c)', 'd)', 'i)', 'ii)', 'iii)']):
        if "coin" in query.lower():
            base_query = query.split("What is the probability of")[0] if "What is the probability of" in query else query.split("a)")[0]
            parts = re.split(r'[a-dA-D]\)\s*|[i-v]+\)\s*', query)
            sub_parts = [p.strip() for p in parts[1:] if p.strip()]
            return {
                "intent": "multi_part_coin_probability",
                "parameters": {"base": base_query.strip(), "parts": sub_parts}
            }
        elif any(word in query.lower() for word in ['ball', 'marble', 'bag']):
            base_query = query.split("What is the probability of")[0] if "What is the probability of" in query else query.split("a)")[0]
            parts = re.split(r'[a-dA-D]\)\s*|[i-v]+\)\s*', query)
            sub_parts = [p.strip() for p in parts[1:] if p.strip()]
            return {
                "intent": "multi_part_ball_probability",
                "parameters": {"base": base_query.strip(), "parts": sub_parts}
            }
        elif any(word in query.lower() for word in ['dice', 'die', 'roll']):
            base_query = query.split("a)")[0] if "a)" in query else query.split("i)")[0]
            parts = re.split(r'[a-dA-D]\)\s*|[i-v]+\)\s*', query)
            sub_parts = [p.strip() for p in parts[1:] if p.strip()]
            return {
                "intent": "multi_part_dice_probability",
                "parameters": {"base": base_query.strip(), "parts": sub_parts}
            }
        else:
            # Generic multi-part
            base_query = query.split("a)")[0] if "a)" in query else query.split("i)")[0]
            parts = re.split(r'[a-dA-D]\)\s*|[i-v]+\)\s*', query)
            sub_parts = [p.strip() for p in parts[1:] if p.strip()]
            return {
                "intent": "multi_part_card_probability",
                "parameters": {"base": base_query.strip(), "parts": sub_parts}
            }
 
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1,
            max_tokens=200
        )
        content = response.choices[0].message.content.strip()
        
        # Extract JSON from response
        start = content.find("{")
        end = content.rfind("}") + 1
        if start != -1 and end > start:
            json_str = content[start:end]
            parsed = json.loads(json_str)
            
            # Normalize intent names
            intent = parsed.get("intent", "unknown")
            if intent == "probability":
                intent = "solve_basic"
            parsed["intent"] = intent
            
            return parsed
        else:
            # Fallback parsing using regex
            return extract_probability_measurements(query)
            
    except Exception as e:
        print(f"LLM Error: {e}")
        # Fallback to rule-based parsing
        return extract_probability_measurements(query)

def extract_probability_measurements(query: str) -> dict:
    """Enhanced rule-based extraction as fallback."""
    measurements = {"intent": "unknown", "parameters": {}}
    
    # Extract numbers
    numbers = re.findall(r'\d+', query)
    q = query.lower()
    
    # Dice problems
    if any(word in q for word in ['dice', 'die', 'roll']):
        measurements["intent"] = "dice_probability"
        
        # Default to 1 die
        measurements["parameters"]["num_dice"] = 1
        
        # Check for multiple dice
        if 'two dice' in q or '2 dice' in q:
            measurements["parameters"]["num_dice"] = 2
        elif 'three dice' in q or '3 dice' in q:
            measurements["parameters"]["num_dice"] = 3
        elif numbers:
            # Check if first number refers to dice count
            first_num = int(numbers[0])
            if first_num <= 6 and ('dice' in q or 'die' in q):
                measurements["parameters"]["num_dice"] = first_num

        # Extract target value or condition
        if 'greater than' in q and numbers:
            measurements["parameters"]["condition"] = "greater_than"
            measurements["parameters"]["threshold"] = int(numbers[-1])
        elif 'less than' in q and numbers:
            measurements["parameters"]["condition"] = "less_than"
            measurements["parameters"]["threshold"] = int(numbers[-1])
        elif 'not' in q and numbers:
            # Find the number after "not"
            for n in numbers:
                val = int(n)
                if 1 <= val <= 6:
                    measurements["parameters"]["condition"] = "not_equal"
                    measurements["parameters"]["not_value"] = val
                    break
        elif 'sum' in q and numbers:
            measurements["parameters"]["target_sum"] = int(numbers[-1])
        elif 'even' in q:
            measurements["parameters"]["condition"] = "even"
        elif 'odd' in q:
            measurements["parameters"]["condition"] = "odd"
        elif 'prime' in q:
            measurements["parameters"]["condition"] = "prime"
        elif numbers:
            # For single die, look for target number
            for n in numbers:
                val = int(n)
                if 1 <= val <= 6:
                    measurements["parameters"]["target_sum"] = val
                    break

    # Coin problems
    elif any(word in q for word in ['coin', 'toss', 'flip', 'head', 'tail']):
        measurements["intent"] = "coin_probability"
        
        # Extract number of coins
        if 'one coin' in q or 'a coin' in q:
            measurements["parameters"]["num_coins"] = 1
        elif 'two coins' in q or '2 coins' in q:
            measurements["parameters"]["num_coins"] = 2
        elif 'three coins' in q or '3 coins' in q:
            measurements["parameters"]["num_coins"] = 3
        elif numbers:
            measurements["parameters"]["num_coins"] = int(numbers[0])
        else:
            measurements["parameters"]["num_coins"] = 1
        
        # Extract target heads/tails
        if 'tail' in q:
            measurements["parameters"]["target_heads"] = 0
        elif 'head' in q:
            if 'at least one head' in q or 'at least 1 head' in q:
                measurements["parameters"]["target_heads"] = 1
                measurements["parameters"]["condition"] = "at_least"
            elif 'exactly one head' in q or 'exactly 1 head' in q:
                measurements["parameters"]["target_heads"] = 1
                measurements["parameters"]["condition"] = "exactly"
            elif 'two heads' in q or '2 heads' in q:
                measurements["parameters"]["target_heads"] = 2
                measurements["parameters"]["condition"] = "exactly"
            elif 'three heads' in q or '3 heads' in q:
                measurements["parameters"]["target_heads"] = 3
                measurements["parameters"]["condition"] = "exactly"
            else:
                measurements["parameters"]["target_heads"] = 1
                
        # Extract conditions
        if 'at least' in q and 'target_heads' not in measurements["parameters"]:
            measurements["parameters"]["condition"] = "at_least"
        elif 'at most' in q:
            measurements["parameters"]["condition"] = "at_most"
        elif 'exactly' in q and 'condition' not in measurements["parameters"]:
            measurements["parameters"]["condition"] = "exactly"
    
    # Card problems
    elif any(word in q for word in ['card', 'deck', 'king', 'queen', 'jack', 'ace', 'spade', 'heart', 'diamond', 'club']):
        measurements["intent"] = "card_probability"
        measurements["parameters"]["deck_size"] = 52
        
        # Identify target
        if 'red card' in q or ('red' in q and 'card' in q):
            measurements["parameters"]["target"] = "red"
        elif 'black card' in q or ('black' in q and 'card' in q):
            measurements["parameters"]["target"] = "black"
        elif 'king' in q:
            measurements["parameters"]["target"] = "king"
        elif 'queen' in q:
            measurements["parameters"]["target"] = "queen"
        elif 'jack' in q:
            measurements["parameters"]["target"] = "jack"
        elif 'ace' in q:
            measurements["parameters"]["target"] = "ace"
        elif 'face card' in q or 'face' in q:
            measurements["parameters"]["target"] = "face"
        elif any(suit in q for suit in ['spade', 'heart', 'diamond', 'club']):
            for suit in ['spade', 'heart', 'diamond', 'club']:
                if suit in q:
                    measurements["parameters"]["target"] = suit
                    break
    
    # Ball problems
    elif any(word in q for word in ['ball', 'marble', 'bag']):
        measurements["intent"] = "ball_probability"

        # Extract ball counts and colors - improved regex
        red_match = re.search(r'(\d+)\s+red', q)
        blue_match = re.search(r'(\d+)\s+blue', q)
        green_match = re.search(r'(\d+)\s+green', q)
        white_match = re.search(r'(\d+)\s+white', q)
        black_match = re.search(r'(\d+)\s+black', q)
        
        if red_match:
            measurements["parameters"]["red_balls"] = int(red_match.group(1))
        if blue_match:
            measurements["parameters"]["blue_balls"] = int(blue_match.group(1))
        if green_match:
            measurements["parameters"]["green_balls"] = int(green_match.group(1))
        if white_match:
            measurements["parameters"]["white_balls"] = int(white_match.group(1))
        if black_match:
            measurements["parameters"]["black_balls"] = int(black_match.group(1))
        
        # Determine target
        if 'not red' in q:
            measurements["parameters"]["target"] = "not_red"
        elif 'not blue' in q:
            measurements["parameters"]["target"] = "not_blue"
        elif 'blue' in q and 'not blue' not in q:
            measurements["parameters"]["target"] = "blue"
        elif 'red' in q and 'not red' not in q:
            measurements["parameters"]["target"] = "red"
        elif 'green' in q:
            measurements["parameters"]["target"] = "green"
        elif 'white' in q:
            measurements["parameters"]["target"] = "white"
        elif 'black' in q:
            measurements["parameters"]["target"] = "black"
    
    # Formula requests
    elif any(word in q for word in ['formula', 'formulas', 'list']):
        measurements["intent"] = "formula_request"

    # Basic probability fallback
    if measurements["intent"] == "unknown" and numbers:
        measurements["intent"] = "solve_basic"
        if len(numbers) >= 2:
            measurements["parameters"]["favorable_outcomes"] = int(numbers[0])
            measurements["parameters"]["total_outcomes"] = int(numbers[1])
        elif len(numbers) == 1:
            measurements["parameters"]["favorable_outcomes"] = 1
            measurements["parameters"]["total_outcomes"] = int(numbers[0])
    
    return measurements

def solve_probability_query(query: str) -> dict:
    """
    Main interface that uses LLM + rules to route query to correct solver.
    """
    result = {"query": query}

    try:
        interpretation = interpret_query_probability(query)
        result["intent"] = interpretation.get("intent", "unknown")
        result["parameters"] = interpretation.get("parameters", {})

        intent = result["intent"]

        # Handle multi-part questions
        if intent == "multi_part_dice_probability":
            base = result["parameters"].get("base", "")
            parts = result["parameters"].get("parts", [])
            
            answers = []
            for i, part in enumerate(parts):
                full_question = f"{base} {part}"
                part_interpretation = interpret_query_probability(full_question)
                
                if part_interpretation["intent"] == "dice_probability":
                    answer = solve_dice_probability(part_interpretation["parameters"])
                    answers.append(f"**{chr(97+i)})** {answer}")
                else:
                    answers.append(f"**{chr(97+i)})** Could not solve: {part}")
            
            result["answer"] = "\n\n".join(answers)
        elif intent == "multi_part_coin_probability":
            base = result["parameters"].get("base", "")
            parts = result["parameters"].get("parts", [])
            answers = []
            for i, part in enumerate(parts):
                full_question = f"{base} {part}"
                part_interpretation = interpret_query_probability(full_question)
                if part_interpretation["intent"] == "coin_probability":
                    answer = solve_coin_probability(part_interpretation["parameters"])
                    answers.append(f"**{chr(97+i)})** {answer}")
                else:
                    answers.append(f"**{chr(97+i)})** Could not solve: {part}")
            result["answer"] = "\n\n".join(answers)

        elif intent == "multi_part_ball_probability":
            base = result["parameters"].get("base", "")
            parts = result["parameters"].get("parts", [])
            answers = []
            for i, part in enumerate(parts):
                full_question = f"{base} {part}"
                part_interpretation = interpret_query_probability(full_question)
                if part_interpretation["intent"] == "ball_probability":
                    answer = solve_ball_probability(part_interpretation["parameters"])
                    answers.append(f"**{chr(97+i)})** {answer}")
                else:
                    answers.append(f"**{chr(97+i)})** Could not solve: {part}")
            result["answer"] = "\n\n".join(answers)
        
        # Route to specific solvers
        elif intent == "dice_probability":
            result["answer"] = solve_dice_probability(result["parameters"])
        elif intent == "coin_probability":
            result["answer"] = solve_coin_probability(result["parameters"])
        elif intent == "card_probability":
            result["answer"] = solve_card_probability(result["parameters"])
        elif intent == "ball_probability":
            result["answer"] = solve_ball_probability(result["parameters"])
        elif intent == "solve_basic":
            result["answer"] = solve_basic_probability(result["parameters"])
        elif intent == "solve_conditional":
            result["answer"] = solve_conditional_probability(result["parameters"])
        elif intent == "solve_combinations":
            result["answer"] = solve_combinations(result["parameters"])
        elif intent == "formula_request":
            result["answer"] = get_probability_formulas()
        else:
            result["answer"] = "⚠️ Could not understand query. Try being more specific."
            result["measurements"] = extract_probability_measurements(query)

    except Exception as e:
        result["error"] = str(e)
        result["answer"] = "❌ Internal error while processing query."

    return result

# ADD this new function to handle formula requests:

def get_probability_formulas():
    """Returns common probability formulas for CBSE Class 10"""
    return """
## 📚 **Probability Formulas - CBSE Class 10**

### **Basic Probability**
- **P(E) = Number of favorable outcomes / Total number of outcomes**
- **0 ≤ P(E) ≤ 1**
- **P(not E) = 1 - P(E)**

### **Dice Probability**
- **Single die:** P(getting number n) = 1/6
- **Two dice:** Total outcomes = 36

### **Coin Probability**
- **Single coin:** P(Head) = P(Tail) = 1/2
- **n coins:** Total outcomes = 2ⁿ

### **Card Probability**
- **Standard deck:** 52 cards
- **P(King) = 4/52 = 1/13**
- **P(Red card) = 26/52 = 1/2**

### **Conditional Probability**
- **P(A|B) = P(A ∩ B) / P(B)**
- **P(A ∩ B) = P(A|B) × P(B)**
    """