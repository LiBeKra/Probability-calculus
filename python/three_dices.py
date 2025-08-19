from collections import Counter
import itertools

def text_prob_chart_three_dice(width=50, bar_char="#"):
    # Parameters
    sides = 6
    n_dice = 3

    # All outcomes and their sums
    outcomes = itertools.product(range(1, sides + 1), repeat=n_dice)
    sums = [sum(o) for o in outcomes]

    # Count frequencies
    counts = Counter(sums)
    total = sides ** n_dice

    # Compute probabilities for sums 3..18
    totals = list(range(n_dice, n_dice * sides + 1))
    probs = {t: counts[t] / total for t in totals}

    # Scale bars relative to the maximum probability
    max_prob = max(probs.values())

    # Header
    print("Probability distribution of the sum of three six-sided dice (text chart)\n")
    print(f"{'Sum':>3} | {'Bar'.ljust(width)} | Prob")
    print("-" * (7 + width + 7))

    # Rows
    for t in totals:
        p = probs[t]
        bar_len = max(1, int(round((p / max_prob) * width))) if p > 0 else 0
        bar = bar_char * bar_len
        print(f"{t:>3} | {bar.ljust(width)} | {p:6.2%}")

if __name__ == "__main__":
    # Adjust width or bar_char if you like, e.g., bar_char='█'
    text_prob_chart_three_dice(width=50, bar_char="#")
