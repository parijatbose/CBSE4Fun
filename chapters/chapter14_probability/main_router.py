# File: chapters/chapter14_probability/main_router.py
import json
from chapters.chapter14_probability.query_probability import interpret_query_probability
from chapters.chapter14_probability.sub_chapters.basic_probability.solver_basic import (
    solve_basic_probability, solve_card_probability, solve_coin_probability, solve_dice_probability, solve_ball_probability
)
from chapters.chapter14_probability.sub_chapters.conditional_probability.solver_conditional import (
    solve_conditional_probability
)
from chapters.chapter14_probability.sub_chapters.combinations.solver_combinations import (
    solve_combinations, solve_combination_probability, solve_permutation_probability
)
from chapters.chapter14_probability.plot_probability import (
    plot_dice_outcomes, plot_coin_outcomes, plot_card_outcomes
)
from chapters.chapter14_probability.query_probability import (
    interpret_query_probability, extract_probability_measurements
)


def route_query(query: str) -> str:
    try:
        interpretation = interpret_query_probability(query)
        intent = interpretation.get("intent", "unknown")
        params = interpretation.get("parameters", {})
        
        print(f"Debug - Intent: {intent}, Params: {params}")  # Debug line
        
        # Enhanced routing with better error handling
        if not intent or intent == "unknown":
            return """❌ Sorry, I couldn't understand the question. 

📝 **Try questions like:**
- "What is the probability of getting 4 when rolling a die?"
- "Find probability of getting 2 heads when tossing 3 coins"
- "What is the probability of drawing a king from a deck?"
- "A bag has 5 red and 3 blue balls. Find probability of drawing a red ball."
            """
        
        if intent == "dice_probability":
            return solve_dice_probability(params)
        elif intent == "coin_probability":
            return solve_coin_probability(params)
        elif intent == "card_probability":
            return solve_card_probability(params)
        elif intent == "ball_probability":
            return solve_ball_probability(params)
        elif intent == "solve_basic":
            return solve_basic_probability(params)
        elif intent == "solve_conditional":
            return solve_conditional_probability(params)
        elif intent == "solve_combinations":
            return solve_combinations(params)
        elif intent == "formula_request":
            return list_probability_formulas()
        elif intent == "multi_part_dice_probability":
            base = params.get("base", "")
            parts = params.get("parts", [])
            answers = []
            for part in parts:
                subquery = f"{base}, {part}"
                result = route_query(subquery)
                answers.append(f"➡️ {part}\n{result}")
            return "\n\n".join(answers)

        elif intent == "multi_part_dice_probability":
            base = params.get("base", "")
            parts = params.get("parts", [])
            answers = []
            for i, part in enumerate(parts):
                if part.strip():
                    # Create full subquery
                    if "die" in base.lower() or "dice" in base.lower():
                        subquery = f"{base} What is the probability of {part}"
                    else:
                        subquery = f"{part}"
                    
                    # Get interpretation for subquery
                    sub_interpretation = interpret_query_probability(subquery)
                    sub_intent = sub_interpretation.get("intent")
                    sub_params = sub_interpretation.get("parameters")
                    
                    if sub_intent == "dice_probability":
                        result = solve_dice_probability(sub_params)
                        answers.append(f"**{chr(97+i)})** {part}\n{result}")
                    else:
                        answers.append(f"**{chr(97+i)})** {part}\n⚠️ Could not interpret this part")
            return "\n\n".join(answers)
            
        elif intent == "multi_part_coin_probability":
            base = params.get("base", "")
            parts = params.get("parts", [])
            answers = []
            for i, part in enumerate(parts):
                if part.strip():
                    # Create full subquery
                    if "coin" in base.lower():
                        subquery = f"{base} What is the probability of {part}"
                    else:
                        subquery = f"{part}"
                    
                    # Get interpretation for subquery
                    sub_interpretation = interpret_query_probability(subquery)
                    sub_intent = sub_interpretation.get("intent")
                    sub_params = sub_interpretation.get("parameters")
                    
                    if sub_intent == "coin_probability":
                        result = solve_coin_probability(sub_params)
                        answers.append(f"**{chr(97+i)})** {part}\n{result}")
                    else:
                        answers.append(f"**{chr(97+i)})** {part}\n⚠️ Could not interpret this part")
            return "\n\n".join(answers)
            
        elif intent == "multi_part_card_probability":
            base = params.get("base", "")
            parts = params.get("parts", [])
            results = []
            for i, part in enumerate(parts):
                if part.strip():
                    # Create full subquery
                    if "card" in base.lower() or "deck" in base.lower():
                        subquery = f"{base} What is the probability of drawing {part}"
                    else:
                        subquery = f"What is the probability of drawing {part}"
                    
                    # Get interpretation for subquery
                    sub_interpretation = interpret_query_probability(subquery)
                    sub_intent = sub_interpretation.get("intent")
                    sub_params = sub_interpretation.get("parameters")

                    if sub_intent == "card_probability":
                        result = solve_card_probability(sub_params)
                        results.append(f"**{chr(97+i)})** {part}\n{result}")
                    elif sub_intent == "solve_basic":
                        result = solve_basic_probability(sub_params)
                        results.append(f"**{chr(97+i)})** {part}\n{result}")
                    else:
                        results.append(f"**{chr(97+i)})** {part}\n⚠️ Could not interpret sub-question")
            return "\n\n".join(results)
            
        elif intent == "multi_part_ball_probability":
            base = params.get("base", "")
            parts = params.get("parts", [])
            results = []
            for i, part in enumerate(parts):
                if part.strip():
                    # Create full subquery
                    if any(word in base.lower() for word in ['ball', 'marble', 'bag']):
                        subquery = f"{base} What is the probability of drawing {part}"
                    else:
                        subquery = f"What is the probability of drawing {part}"
                    
                    # Get interpretation for subquery
                    sub_interpretation = interpret_query_probability(subquery)
                    sub_intent = sub_interpretation.get("intent")
                    sub_params = sub_interpretation.get("parameters")

                    if sub_intent == "ball_probability":
                        result = solve_ball_probability(sub_params)
                        results.append(f"**{chr(97+i)})** {part}\n{result}")
                    elif sub_intent == "solve_basic":
                        result = solve_basic_probability(sub_params)
                        results.append(f"**{chr(97+i)})** {part}\n{result}")
                    else:
                        results.append(f"**{chr(97+i)})** {part}\n⚠️ Could not interpret sub-question")
            return "\n\n".join(results)
        else:
            return f"""⚠️ **Could not process your query.**

**🔍 Query:** "{query}"
**🤖 Detected Intent:** {intent}
**📊 Parameters:** {params}

**📝 Try being more specific or use simpler language.**
            """
    except Exception as e:
        return f"❌ **Error processing query:** {str(e)}\n\n**Query:** \"{query}\""


def list_probability_formulas() -> str:
    return """
### 📘 Common Probability Formulas

1. **Basic Probability**
   \[ P(E) = \frac{\text{Favorable Outcomes}}{\text{Total Outcomes}} \]

2. **Complementary Events**
   \[ P(E') = 1 - P(E) \]

3. **Conditional Probability**
   \[ P(A \mid B) = \frac{P(A \cap B)}{P(B)} \]

4. **Bayes' Theorem**
   \[ P(A \mid B) = \frac{P(B \mid A) \cdot P(A)}{P(B)} \]

5. **Combinations**
   \[ \binom{n}{r} = \frac{n!}{r!(n - r)!} \]

6. **Permutations**
   \[ P(n, r) = \frac{n!}{(n-r)!} \]

"""
