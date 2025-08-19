# Prompt von ChatGPT:
# Schreibe ein Python program, dass die Wahrscheinlichkeit für das Ergebnis 
# der Augenzahl mit drei Würfeln als Text visualiziert.

from collections import Counter

def drei_wuerfel_wahrscheinlichkeiten():
    summen = []
    for w1 in range(1, 7):
        for w2 in range(1, 7):
            for w3 in range(1, 7):
                summen.append(w1 + w2 + w3)

    counts = Counter(summen)
    gesamt = 6 ** 3  # 216 mögliche Ergebnisse

    # Wahrscheinlichkeitstabelle
    probs = {s: counts[s] / gesamt for s in range(3, 19)}
    return probs

def text_visualisierung(probs):
    max_balken = 50  # Länge des längsten Balkens
    max_wert = max(probs.values())

    for s in range(3, 19):
        p = probs[s]
        balkenlaenge = int(p / max_wert * max_balken)
        balken = "█" * balkenlaenge
        print(f"Summe {s:2d}: {p:.2%} {balken}")

if __name__ == "__main__":
    probs = drei_wuerfel_wahrscheinlichkeiten()
    text_visualisierung(probs)
