# File: chapters/chapter14_probability/plot_probability.py

import matplotlib.pyplot as plt
import numpy as np

def plot_dice_outcomes(num_dice=2, target_sum=7, save_path=None):
    """
    Plots all possible sums of two dice and highlights the target sum.
    Saves to file or buffer.
    """
    outcomes = [i + j for i in range(1, 7) for j in range(1, 7)]
    values, counts = np.unique(outcomes, return_counts=True)

    fig, ax = plt.subplots(figsize=(8, 4))
    bars = ax.bar(values, counts, edgecolor="black")

    if target_sum in values:
        bars[list(values).index(target_sum)].set_color("red")

    ax.set_title(f"🎲 Sum Outcomes for {num_dice} Dice")
    ax.set_xlabel("Sum")
    ax.set_ylabel("Frequency")
    ax.grid(True, linestyle="--", alpha=0.5)

    if save_path:
        plt.savefig(save_path, format="png", bbox_inches="tight")
    else:
        plt.show()

    plt.close()
    
def plot_coin_outcomes(num_coins=2, target_heads=1, save_path=None):
    import matplotlib.pyplot as plt
    from math import comb
    outcomes = range(num_coins + 1)
    probs = [comb(num_coins, k) / 2**num_coins for k in outcomes]
    fig, ax = plt.subplots()
    bars = ax.bar(outcomes, probs)
    if 0 <= target_heads <= num_coins:
        bars[target_heads].set_color("red")
    ax.set_xlabel("Number of Heads")
    ax.set_ylabel("Probability")
    ax.set_title(f"Probability Distribution for {num_coins} Coin Tosses")
    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()
    plt.close()

def plot_card_outcomes():  # You can define a custom visualization as needed
    pass
