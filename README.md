# Probability-calculus

Leider erst in Klasse 9 kam die 9a32 dazu, das alte Thema der 7. Klasse zur Wahrscheinlichkeitsberechnung im Matheunterricht durchzunehmen. Dabei macht es so viel Spass!

Hier ein paar Hausaufgaben als Beispiele:

## 6 aus 49

> Schreibe ein Pythonprogramm um die Wahrscheinlichkeiten für 6 aus 49 auszurechnen.

``` py
import math

def comb(n, k):
    return math.comb(n, k)  # ab Python 3.8 verfügbar

def lotto_probabilities():
    total = comb(49, 6)  # alle möglichen Tipps
    probs = {}

    for k in range(7):  # 0 bis 6 Richtige
        # Anzahl der günstigen Fälle:
        # k Richtige aus den 6 gezogenen Zahlen, und (6-k) Falsche aus den 43 übrigen
        favorable = comb(6, k) * comb(49 - 6, 6 - k)
        probs[k] = favorable / total
    return probs

# Ausgabe
probs = lotto_probabilities()
print("Wahrscheinlichkeiten für 6 aus 49:\n")
for k, p in probs.items():
    print(f"{k} Richtige: {p:.10f} ({p*100:.8f}%)")
```

Mehr folgt später
