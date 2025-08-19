import matplotlib.pyplot as plt
from collections import Counter

def two_dice_probabilities():
    # Possible sums range from 2 to 12
    sums = []
    
    # Simulate rolling two dice
    for die1 in range(1, 7):
        for die2 in range(1, 7):
            sums.append(die1 + die2)
    
    # Count frequencies
    counts = Counter(sums)
    total_outcomes = 36  # 6 * 6
    
    # Calculate probabilities
    probabilities = {s: counts[s] / total_outcomes for s in range(2, 13)}
    return probabilities

def plot_probabilities(probabilities):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())
    
    plt.bar(sums, probs, width=0.6, color='skyblue', edgecolor='black')
    plt.xlabel("Sum of Two Dice")
    plt.ylabel("Probability")
    plt.title("Probability Distribution of Two Dice Rolls")
    plt.xticks(range(2, 13))
    
    # Show values on top of bars
    for i, p in enumerate(probs):
        plt.text(sums[i], p + 0.005, f"{p:.2f}", ha='center')
    
    plt.show()

if __name__ == "__main__":
    probs = two_dice_probabilities()
    print("Probabilities of sums (2–12):")
    for s, p in probs.items():
        print(f"Sum {s}: {p:.2%}")
    
    plot_probabilities(probs)
