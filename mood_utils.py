# mood_utils.py
import matplotlib.pyplot as plt

def plot_mood_graph(predictions):
    labels = [p[0] for p in predictions]
    scores = [p[1] for p in predictions]

    plt.figure(figsize=(5, 3))
    bars = plt.bar(range(len(scores)), scores, color=["red" if l == "Depressed" else "green" for l in labels])
    plt.xticks(range(len(scores)), [f"Chat {i+1}" for i in range(len(scores))], rotation=45)
    plt.ylim(0, 1)
    plt.title("Mood Prediction Confidence")
    plt.tight_layout()
    return plt
