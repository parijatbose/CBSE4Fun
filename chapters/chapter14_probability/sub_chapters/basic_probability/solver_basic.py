# File: chapters/chapter14_probability/sub_chapters/basic_probability/solver_basic.py

from fractions import Fraction
from math import comb

def solve_basic_probability(params: dict) -> str:

    if 'num_dice' in params:
        num_dice = params.get('num_dice', 1)
        condition = params.get('condition')
        threshold = params.get('threshold')

        if num_dice != 1:
            return "⚠️ Calculation for multiple dice not yet implemented. Only single die supported."

        # Single die sample space
        sample_space = [1, 2, 3, 4, 5, 6]

        # Apply condition
        if condition == "greater_than":
            favorable = [x for x in sample_space if x > threshold]
        elif condition == "less_than":
            favorable = [x for x in sample_space if x < threshold]
        elif condition == "equal_to":
            favorable = [x for x in sample_space if x == threshold]
        else:
            return "⚠️ Unsupported condition."

        total = len(sample_space)
        favorable_count = len(favorable)
        prob = favorable_count / total
        prob_frac = Fraction(favorable_count, total)

        return f"""
## 🎲 Die Probability

**Given:** Rolling 1 die  
**Condition:** {condition.replace('_', ' ')} {threshold}  
**Sample Space:** {sample_space}  
**Favorable outcomes:** {favorable}  
**Total outcomes = {total}, Favorable = {favorable_count}**

🎯 P(E) = {favorable_count}/{total} = {prob_frac} ≈ {prob:.3f}

✅ **Answer:** {prob_frac} or {round(prob * 100, 1)}%
"""
    
    return "⚠️ Could not understand the die-based question."

def solve_dice_probability(params: dict) -> str:
    """Enhanced dice probability solver with CBSE-style explanation"""
    num_dice = params.get("num_dice", 1)
    target_sum = params.get("target_sum")
    condition = params.get("condition")
    threshold = params.get("threshold")
    not_value = params.get("not_value")

    if num_dice == 1:
        sample_space = [1, 2, 3, 4, 5, 6]

        if condition == "greater_than" and threshold is not None:
            favorable = [x for x in sample_space if x > threshold]
            condition_text = f"greater than {threshold}"
        elif condition == "less_than" and threshold is not None:
            favorable = [x for x in sample_space if x < threshold]
            condition_text = f"less than {threshold}"
        elif condition == "not_equal" and not_value is not None:
            favorable = [x for x in sample_space if x != not_value]
            condition_text = f"not getting {not_value}"
        elif condition == "even":
            favorable = [2, 4, 6]
            condition_text = "an even number"
        elif condition == "odd":
            favorable = [1, 3, 5]
            condition_text = "an odd number"
        elif condition == "prime":
            favorable = [2, 3, 5]
            condition_text = "a prime number"
        else:
            if target_sum and 1 <= target_sum <= 6:
                favorable = [target_sum]
                condition_text = f"getting {target_sum}"
            else:
                return f"❌ Invalid target value {target_sum} for a single die."

        if not favorable:
            return f"❌ No favorable outcomes found."

        favorable_count = len(favorable)
        total = len(sample_space)
        prob = Fraction(favorable_count, total)

        return f"""
## 🎲 **Single Die Probability**

**Given:** Rolling one die  
**Find:** Probability of {condition_text}

**Solution:**
- **Sample Space (S):** {{{', '.join(map(str, sample_space))}}}
- **Total outcomes:** {total}
- **Event E:** {condition_text.capitalize()}
- **Favorable outcomes:** {{{', '.join(map(str, favorable))}}}
- **Number of favorable outcomes:** {favorable_count}

**Using the formula:**
P(E) = Number of favorable outcomes / Total number of outcomes
P(E) = {favorable_count}/{total} = {prob}

**Answer:** The probability is **{prob}** ≈ **{float(prob):.3f}** or **{float(prob):.1%}**
        """
    
    elif num_dice == 2:
        # Generate all possible outcomes for two dice
        all_outcomes = []
        favorable_outcomes = []
        
        for i in range(1, 7):
            for j in range(1, 7):
                outcome = (i, j)
                sum_outcome = i + j
                all_outcomes.append(outcome)
                
                if condition == "greater_than" and threshold is not None:
                    if sum_outcome > threshold:
                        favorable_outcomes.append(outcome)
                elif condition == "less_than" and threshold is not None:
                    if sum_outcome < threshold:
                        favorable_outcomes.append(outcome)
                elif condition == "not_equal" and not_value is not None:
                    if sum_outcome != not_value:
                        favorable_outcomes.append(outcome)
                elif condition == "even_sum":
                    if sum_outcome % 2 == 0:
                        favorable_outcomes.append(outcome)
                elif condition == "odd_sum":
                    if sum_outcome % 2 == 1:
                        favorable_outcomes.append(outcome)
                elif condition == "same_number":
                    if i == j:
                        favorable_outcomes.append(outcome)
                elif target_sum is not None and sum_outcome == target_sum:
                    favorable_outcomes.append(outcome)

        total_outcomes = 36
        favorable_count = len(favorable_outcomes)
        
        if favorable_count == 0:
            return "❌ No favorable outcomes found."

        probability = Fraction(favorable_count, total_outcomes)
        
        # Format outcomes for display
        favorable_display = [f"({i},{j})" for i, j in favorable_outcomes[:12]]  # Show first 12
        if len(favorable_outcomes) > 12:
            favorable_display.append("...")

        # Determine condition text
        if condition == "greater_than":
            condition_text = f"sum greater than {threshold}"
        elif condition == "less_than":
            condition_text = f"sum less than {threshold}"
        elif condition == "not_equal":
            condition_text = f"sum not equal to {not_value}"
        elif condition == "even_sum":
            condition_text = "even sum"
        elif condition == "odd_sum":
            condition_text = "odd sum"
        elif condition == "same_number":
            condition_text = "same number on both dice"
        elif target_sum:
            condition_text = f"sum of {target_sum}"
        else:
            condition_text = "the specified condition"

        return f"""
## 🎲 **Two Dice Probability**

**Given:** Rolling two dice  
**Find:** Probability of getting {condition_text}

**Solution:**
- **Total outcomes:** 6 × 6 = {total_outcomes}
- **Event E:** Getting {condition_text}
- **Favorable outcomes:** {', '.join(favorable_display)}
- **Number of favorable outcomes:** {favorable_count}

**Using the formula:**
P(E) = Number of favorable outcomes / Total number of outcomes
P(E) = {favorable_count}/{total_outcomes} = {probability}

**Answer:** The probability is **{probability}** ≈ **{float(probability):.3f}** or **{float(probability):.1%}**
        """

    else:
        return f"⚠️ Calculation for {num_dice} dice not implemented. Try 1 or 2 dice."

def solve_coin_probability(params: dict) -> str:
    """Enhanced coin probability solver for 1, 2, and 3 coins"""
    num_coins = params.get("num_coins", 1)
    target_heads = params.get("target_heads", 1)
    condition = params.get("condition", "exactly")
    
    if num_coins == 1:
        if target_heads == 0:
            return f"""
## 🪙 **Single Coin Probability**

**Given:** Tossing one coin
**Find:** Probability of getting Tail (0 heads)

**Solution:**
- **Sample Space (S):** {{H, T}}
- **Total outcomes:** 2
- **Event E:** Getting Tail
- **Favorable outcomes:** {{T}}
- **Number of favorable outcomes:** 1

**Using the formula:**
P(E) = Number of favorable outcomes / Total number of outcomes
P(Tail) = 1/2

**Answer:** The probability is **1/2** or **0.5** or **50%**
            """
        else:  # target_heads == 1
            return f"""
## 🪙 **Single Coin Probability**

**Given:** Tossing one coin
**Find:** Probability of getting Head

**Solution:**
- **Sample Space (S):** {{H, T}}
- **Total outcomes:** 2
- **Event E:** Getting Head  
- **Favorable outcomes:** {{H}}
- **Number of favorable outcomes:** 1

**Using the formula:**
P(E) = Number of favorable outcomes / Total number of outcomes
P(Head) = 1/2

**Answer:** The probability is **1/2** or **0.5** or **50%**
            """
    
    elif num_coins == 2:
        sample_space = ["HH", "HT", "TH", "TT"]
        total_outcomes = 4
        
        if condition == "at_least" and target_heads == 1:
            favorable_outcomes = ["HH", "HT", "TH"]
            favorable_count = 3
            
            return f"""
## 🪙 **Two Coins Probability**

**Given:** Tossing two coins
**Find:** Probability of getting at least one head

**Solution:**
- **Sample Space (S):** {{{", ".join(sample_space)}}}
- **Total outcomes:** 2² = {total_outcomes}
- **Event E:** Getting at least one head
- **Favorable outcomes:** {{{", ".join(favorable_outcomes)}}}
- **Number of favorable outcomes:** {favorable_count}

**Using the formula:**
P(E) = Number of favorable outcomes / Total number of outcomes
P(at least one head) = {favorable_count}/4 = 3/4

**Answer:** The probability is **3/4** or **0.75** or **75%**
            """
        
        elif condition == "exactly":
            if target_heads == 0:
                favorable_outcomes = ["TT"]
                favorable_count = 1
                condition_text = "no heads (2 tails)"
            elif target_heads == 1:
                favorable_outcomes = ["HT", "TH"]
                favorable_count = 2
                condition_text = "exactly one head"
            elif target_heads == 2:
                favorable_outcomes = ["HH"]
                favorable_count = 1
                condition_text = "exactly two heads"
            
            prob_fraction = Fraction(favorable_count, total_outcomes)
            
            return f"""
## 🪙 **Two Coins Probability**

**Given:** Tossing two coins
**Find:** Probability of getting {condition_text}

**Solution:**
- **Sample Space (S):** {{{", ".join(sample_space)}}}
- **Total outcomes:** 2² = {total_outcomes}
- **Event E:** Getting {condition_text}
- **Favorable outcomes:** {{{", ".join(favorable_outcomes)}}}
- **Number of favorable outcomes:** {favorable_count}

**Using the formula:**
P(E) = Number of favorable outcomes / Total number of outcomes
P({condition_text}) = {favorable_count}/{total_outcomes} = {prob_fraction}

**Answer:** The probability is **{prob_fraction}** or **{float(prob_fraction):.3f}** or **{float(prob_fraction):.1%}**
            """
    
    elif num_coins == 3:
        sample_space = ["HHH", "HHT", "HTH", "HTT", "THH", "THT", "TTH", "TTT"]
        total_outcomes = 8
        
        # Count heads in each outcome
        outcomes_by_heads = {
            0: ["TTT"],
            1: ["HTT", "THT", "TTH"],
            2: ["HHT", "HTH", "THH"],
            3: ["HHH"]
        }
        
        if condition == "exactly":
            if target_heads in outcomes_by_heads:
                favorable_outcomes = outcomes_by_heads[target_heads]
                favorable_count = len(favorable_outcomes)
                
                if target_heads == 0:
                    condition_text = "no heads (3 tails)"
                elif target_heads == 1:
                    condition_text = "exactly one head"
                elif target_heads == 2:
                    condition_text = "exactly two heads"
                elif target_heads == 3:
                    condition_text = "exactly three heads"
                
                prob_fraction = Fraction(favorable_count, total_outcomes)
                
                return f"""
## 🪙 **Three Coins Probability**

**Given:** Tossing three coins
**Find:** Probability of getting {condition_text}

**Solution:**
- **Sample Space (S):** {{{", ".join(sample_space)}}}
- **Total outcomes:** 2³ = {total_outcomes}
- **Event E:** Getting {condition_text}
- **Favorable outcomes:** {{{", ".join(favorable_outcomes)}}}
- **Number of favorable outcomes:** {favorable_count}

**Using combination formula:** C(3,{target_heads}) = {favorable_count}

**Using the formula:**
P(E) = Number of favorable outcomes / Total number of outcomes
P({condition_text}) = {favorable_count}/{total_outcomes} = {prob_fraction}

**Answer:** The probability is **{prob_fraction}** or **{float(prob_fraction):.3f}** or **{float(prob_fraction):.1%}**
                """
        
        elif condition == "at_least":
            favorable_outcomes = []
            for heads in range(target_heads, 4):
                favorable_outcomes.extend(outcomes_by_heads[heads])
            
            favorable_count = len(favorable_outcomes)
            prob_fraction = Fraction(favorable_count, total_outcomes)
            
            return f"""
## 🪙 **Three Coins Probability**

**Given:** Tossing three coins
**Find:** Probability of getting at least {target_heads} heads

**Solution:**
- **Sample Space (S):** {{{", ".join(sample_space)}}}
- **Total outcomes:** 2³ = {total_outcomes}
- **Event E:** Getting at least {target_heads} heads
- **Favorable outcomes:** {{{", ".join(favorable_outcomes)}}}
- **Number of favorable outcomes:** {favorable_count}

**Using the formula:**
P(E) = Number of favorable outcomes / Total number of outcomes
P(at least {target_heads} heads) = {favorable_count}/{total_outcomes} = {prob_fraction}

**Answer:** The probability is **{prob_fraction}** or **{float(prob_fraction):.3f}** or **{float(prob_fraction):.1%}**
            """
    
    # For more than 3 coins, use combination formula
    else:
        total_outcomes = 2 ** num_coins
        
        if condition == "exactly":
            favorable = comb(num_coins, target_heads)
            prob_fraction = Fraction(favorable, total_outcomes)
            
            return f"""
## 🪙 **Multiple Coins Probability**

**Given:** Tossing {num_coins} coins
**Find:** Probability of getting exactly {target_heads} heads

**Solution:**
- **Total outcomes:** 2^{num_coins} = {total_outcomes}
- **Using combination formula:** C({num_coins}, {target_heads}) = {favorable}
- **Favorable outcomes:** {favorable}

**Using the formula:**
P(exactly {target_heads} heads) = C({num_coins}, {target_heads}) / 2^{num_coins}
P(exactly {target_heads} heads) = {favorable}/{total_outcomes} = {prob_fraction}

**Answer:** The probability is **{prob_fraction}** ≈ **{float(prob_fraction):.3f}**
            """
        
        elif condition == "at_least":
            favorable = sum(comb(num_coins, k) for k in range(target_heads, num_coins + 1))
            prob_fraction = Fraction(favorable, total_outcomes)
            
            return f"""
## 🪙 **Multiple Coins Probability**

**Given:** Tossing {num_coins} coins
**Find:** Probability of getting at least {target_heads} heads

**Solution:**
- **Total outcomes:** 2^{num_coins} = {total_outcomes}
- **At least {target_heads} means:** {target_heads}, {target_heads+1}, ..., {num_coins} heads
- **Favorable outcomes:** {favorable}

**Using the formula:**
P(at least {target_heads} heads) = {favorable}/{total_outcomes} = {prob_fraction}

**Answer:** The probability is **{prob_fraction}** ≈ **{float(prob_fraction):.3f}**
            """
    
    return "⚠️ Condition not recognized or invalid parameters."

def solve_card_probability(params: dict) -> str:
    """Enhanced card probability solver with basic, face cards, and conditional probability"""
    target = params.get("target", "king").lower()
    deck_size = params.get("deck_size", 52)
    condition = params.get("condition")
    given_info = params.get("given")
    
    # Define card counts
    card_counts = {
        "king": 4, "queen": 4, "jack": 4, "ace": 4,
        "spade": 13, "heart": 13, "diamond": 13, "club": 13,
        "red": 26, "black": 26, "red_card": 26, "black_card": 26,
        "face": 12, "face_card": 12, "picture": 12, "picture_card": 12,
        "number": 36, "number_card": 36
    }
    
    # Handle conditional probability
    if condition == "given" and given_info:
        return solve_conditional_card_probability(target, given_info, deck_size)
    
    # Handle basic card probability
    if target in card_counts:
        favorable = card_counts[target]
        prob_fraction = Fraction(favorable, deck_size)
        
        # Determine card description and details
        if target in ["king", "queen", "jack", "ace"]:
            card_type = target.title()
            explanation = f"There are 4 {card_type}s in a standard deck (one in each suit)"
        elif target in ["spade", "heart", "diamond", "club"]:
            card_type = target.title()
            explanation = f"There are 13 {card_type}s in a standard deck"
        elif target in ["red", "red_card"]:
            card_type = "Red card"
            explanation = "Red cards include all Hearts (13) and Diamonds (13)"
        elif target in ["black", "black_card"]:
            card_type = "Black card"
            explanation = "Black cards include all Spades (13) and Clubs (13)"
        elif target in ["face", "face_card", "picture", "picture_card"]:
            card_type = "Face card"
            explanation = "Face cards are Kings, Queens, and Jacks (4 each × 3 = 12 total)"
        elif target in ["number", "number_card"]:
            card_type = "Number card"
            explanation = "Number cards are 2, 3, 4, 5, 6, 7, 8, 9, 10 (9 each × 4 suits = 36 total)"
        
        return f"""
## 🃏 **Playing Cards Probability**

**Given:** A standard deck of 52 cards
**Find:** Probability of drawing a {card_type}

**Solution:**
- **Total cards in deck:** {deck_size}
- **Event E:** Drawing a {card_type}
- **Number of {card_type.lower()}s:** {favorable}
- **Explanation:** {explanation}

**Using the formula:**
P(E) = Number of favorable outcomes / Total number of outcomes
P({card_type}) = {favorable}/{deck_size} = {prob_fraction}

**Answer:** The probability is **{prob_fraction}** ≈ **{float(prob_fraction):.3f}** or **{float(prob_fraction):.1%}**

**Deck composition:**
- 4 suits: Spades ♠, Hearts ♥, Diamonds ♦, Clubs ♣
- 13 cards per suit: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K
- Face cards: J, Q, K (12 total)
- Red cards: Hearts + Diamonds (26 total)
- Black cards: Spades + Clubs (26 total)
        """
    
    return f"⚠️ Unknown card type: {target}"

def solve_conditional_card_probability(target: str, given: str, deck_size: int = 52) -> str:
    """Solve conditional card probability problems"""
    
    # Example: P(King | Red card)
    if given.lower() == "red" and target.lower() == "king":
        total_red = 26  # Hearts + Diamonds
        red_kings = 2   # King of Hearts + King of Diamonds
        
        prob_fraction = Fraction(red_kings, total_red)
        
        return f"""
## 🃏 **Conditional Card Probability**

**Given:** A card is drawn from a standard deck and it is RED
**Find:** Probability that it is a King

**Solution:**
- **Given condition:** Card is Red
- **Total red cards:** 26 (13 Hearts + 13 Diamonds)
- **Event E:** Card is a King given it's red
- **Red Kings:** 2 (King of Hearts + King of Diamonds)

**Using conditional probability formula:**
P(King | Red) = P(King ∩ Red) / P(Red)
P(King | Red) = Number of red Kings / Total red cards
P(King | Red) = {red_kings}/{total_red} = {prob_fraction}

**Answer:** The probability is **{prob_fraction}** ≈ **{float(prob_fraction):.3f}** or **{float(prob_fraction):.1%}**
        """
    
    # Example: P(Red | Face card)
    elif given.lower() == "face" and target.lower() == "red":
        total_face = 12  # 4 Jacks + 4 Queens + 4 Kings
        red_face = 6     # 2 red Jacks + 2 red Queens + 2 red Kings
        
        prob_fraction = Fraction(red_face, total_face)
        
        return f"""
## 🃏 **Conditional Card Probability**

**Given:** A card is drawn from a standard deck and it is a FACE CARD
**Find:** Probability that it is Red

**Solution:**
- **Given condition:** Card is a Face card (J, Q, K)
- **Total face cards:** 12 (4 Jacks + 4 Queens + 4 Kings)
- **Event E:** Card is red given it's a face card
- **Red face cards:** 6 (2 red Jacks + 2 red Queens + 2 red Kings)

**Using conditional probability formula:**
P(Red | Face) = Number of red face cards / Total face cards
P(Red | Face) = {red_face}/{total_face} = {prob_fraction}

**Answer:** The probability is **{prob_fraction}** = **0.5** or **50%**
        """
    
    return f"⚠️ Conditional probability for {target} given {given} not implemented."

def solve_ball_probability(params: dict) -> str:
    """Enhanced ball probability solver with mixed colors and conditional probability"""
    
    # Extract ball counts
    red_balls = params.get("red_balls", 0)
    blue_balls = params.get("blue_balls", 0)
    green_balls = params.get("green_balls", 0)
    white_balls = params.get("white_balls", 0)
    black_balls = params.get("black_balls", 0)
    yellow_balls = params.get("yellow_balls", 0)
    
    total_balls = red_balls + blue_balls + green_balls + white_balls + black_balls + yellow_balls
    target = params.get("target", "red").lower()
    condition = params.get("condition")
    replacement = params.get("replacement", True)  # With or without replacement
    
    if total_balls == 0:
        return "⚠️ No balls specified in the problem"
    
    # Create bag description
    ball_types = []
    if red_balls > 0: ball_types.append(f"{red_balls} red")
    if blue_balls > 0: ball_types.append(f"{blue_balls} blue")
    if green_balls > 0: ball_types.append(f"{green_balls} green")
    if white_balls > 0: ball_types.append(f"{white_balls} white")
    if black_balls > 0: ball_types.append(f"{black_balls} black")
    if yellow_balls > 0: ball_types.append(f"{yellow_balls} yellow")
    
    bag_description = ", ".join(ball_types) + " balls"
    
    # Handle conditional probability (e.g., second draw given first draw)
    if condition == "second_draw":
        first_draw = params.get("first_draw", "red")
        return solve_conditional_ball_probability(params, first_draw, target, replacement)
    
    # Determine favorable outcomes
    if target == "red":
        favorable = red_balls
        color = "red"
    elif target == "blue":
        favorable = blue_balls
        color = "blue"
    elif target == "green":
        favorable = green_balls
        color = "green"
    elif target == "white":
        favorable = white_balls
        color = "white"
    elif target == "black":
        favorable = black_balls
        color = "black"
    elif target == "yellow":
        favorable = yellow_balls
        color = "yellow"
    elif target == "not_red":
        favorable = total_balls - red_balls
        color = "not red"
    elif target == "not_blue":
        favorable = total_balls - blue_balls
        color = "not blue"
    elif target == "not_green":
        favorable = total_balls - green_balls
        color = "not green"
    elif target == "red_or_blue":
        favorable = red_balls + blue_balls
        color = "red or blue"
    elif target == "red_or_green":
        favorable = red_balls + green_balls
        color = "red or green"
    elif target == "blue_or_green":
        favorable = blue_balls + green_balls
        color = "blue or green"
    else:
        return f"⚠️ Unknown target: {target}"
    
    prob_fraction = Fraction(favorable, total_balls)
    
    return f"""
## ⚽ **Ball Drawing Probability**

**Given:** A bag containing {bag_description}
**Find:** Probability of drawing a {color} ball

**Solution:**
- **Total balls:** {total_balls}
- **Event E:** Drawing a {color} ball
- **Number of {color} balls:** {favorable}

**Ball composition:**
{chr(10).join([f"- {ball_type.capitalize()}" for ball_type in ball_types])}

**Using the formula:**
P(E) = Number of favorable outcomes / Total number of outcomes
P({color} ball) = {favorable}/{total_balls} = {prob_fraction}

**Answer:** The probability is **{prob_fraction}** ≈ **{float(prob_fraction):.3f}** or **{float(prob_fraction):.1%}**
    """

def solve_conditional_ball_probability(params: dict, first_draw: str, second_target: str, replacement: bool = False) -> str:
    """Solve conditional probability for ball drawing (with/without replacement)"""
    
    red_balls = params.get("red_balls", 0)
    blue_balls = params.get("blue_balls", 0)
    green_balls = params.get("green_balls", 0)
    total_balls = red_balls + blue_balls + green_balls
    
    # Create initial bag description
    ball_types = []
    if red_balls > 0: ball_types.append(f"{red_balls} red")
    if blue_balls > 0: ball_types.append(f"{blue_balls} blue")
    if green_balls > 0: ball_types.append(f"{green_balls} green")
    bag_description = ", ".join(ball_types) + " balls"
    
    if replacement:
        # With replacement - probabilities don't change
        if second_target == "red":
            favorable = red_balls
        elif second_target == "blue":
            favorable = blue_balls
        elif second_target == "green":
            favorable = green_balls
        
        prob_fraction = Fraction(favorable, total_balls)
        
        return f"""
## ⚽ **Conditional Ball Probability (With Replacement)**

**Given:** A bag containing {bag_description}
**First draw:** {first_draw.capitalize()} ball (replaced back)
**Find:** Probability of drawing a {second_target} ball on second draw

**Solution:**
- **Since ball is replaced, total remains:** {total_balls}
- **Event E:** Drawing {second_target} ball on second draw
- **Number of {second_target} balls:** {favorable}

**Using conditional probability:**
P({second_target} on 2nd | {first_draw} on 1st with replacement) = P({second_target})
P({second_target} ball) = {favorable}/{total_balls} = {prob_fraction}

**Answer:** The probability is **{prob_fraction}** ≈ **{float(prob_fraction):.3f}** or **{float(prob_fraction):.1%}**
        """
    
    else:
        # Without replacement - adjust counts
        if first_draw == "red":
            new_red = red_balls - 1
            new_blue = blue_balls
            new_green = green_balls
        elif first_draw == "blue":
            new_red = red_balls
            new_blue = blue_balls - 1
            new_green = green_balls
        elif first_draw == "green":
            new_red = red_balls
            new_blue = blue_balls
            new_green = green_balls - 1
        
        new_total = new_red + new_blue + new_green
        
        if second_target == "red":
            favorable = new_red
        elif second_target == "blue":
            favorable = new_blue
        elif second_target == "green":
            favorable = new_green
        
        prob_fraction = Fraction(favorable, new_total)
        
        return f"""
## ⚽ **Conditional Ball Probability (Without Replacement)**

**Given:** A bag containing {bag_description}
**First draw:** {first_draw.capitalize()} ball (not replaced)
**Find:** Probability of drawing a {second_target} ball on second draw

**Solution:**
- **After removing {first_draw} ball:**
  - Total balls remaining: {new_total}
  - Red balls remaining: {new_red}
  - Blue balls remaining: {new_blue}
  - Green balls remaining: {new_green}
- **Event E:** Drawing {second_target} ball on second draw
- **Number of {second_target} balls remaining:** {favorable}

**Using conditional probability:**
P({second_target} on 2nd | {first_draw} on 1st without replacement) = {favorable}/{new_total}

**Answer:** The probability is **{prob_fraction}** ≈ **{float(prob_fraction):.3f}** or **{float(prob_fraction):.1%}**
        """

# Example usage and test cases
if __name__ == "__main__":
    from fractions import Fraction
    
    # Test case 1: Basic probability
    params1 = {
        "red_balls": 3,
        "blue_balls": 2,
        "green_balls": 1,
        "target": "red"
    }
    print(solve_ball_probability(params1))
    
    # Test case 2: Conditional probability without replacement
    params2 = {
        "red_balls": 4,
        "blue_balls": 3,
        "green_balls": 2,
        "condition": "second_draw",
        "first_draw": "red",
        "target": "blue",
        "replacement": False
    }
    print(solve_ball_probability(params2))
    
    # Test case 3: Conditional probability with replacement
    params3 = {
        "red_balls": 5,
        "blue_balls": 3,
        "green_balls": 2,
        "condition": "second_draw",
        "first_draw": "blue",
        "target": "red",
        "replacement": True
    }
    print(solve_ball_probability(params3))