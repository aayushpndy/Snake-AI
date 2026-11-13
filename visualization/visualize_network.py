import matplotlib.pyplot as plt
import numpy as np
input_size=11
hidden_size=256
output_size=3
fig, ax = plt.subplots(figsize=(14, 8))

ax.set_title("Snake AI - Neural Network Architecture", fontsize=18)

ax.axis("off")
input_x = 0
hidden_x = 1
output_x = 2

input_y = np.linspace(0, 1, input_size)
hidden_y = np.linspace(0, 1, hidden_size)
output_y = np.linspace(0, 1, output_size)
# Input to hidden connections
for y1 in input_y:
    for y2 in hidden_y:
        ax.plot([input_x, hidden_x], [y1, y2],
                color="gray", alpha=0.08, linewidth=0.5)

# Hidden to output connections
for y1 in hidden_y:
    for y2 in output_y:
        ax.plot([hidden_x, output_x], [y1, y2],
                color="gray", alpha=0.08, linewidth=0.5)

# Draw input neurons
ax.scatter(
    [input_x] * input_size,
    input_y,
    s=100,
    color="dodgerblue",
    edgecolors="black",
    zorder=3
)

# Draw hidden neurons
ax.scatter(
    [hidden_x] * hidden_size,
    hidden_y,
    s=15,
    color="seagreen",
    edgecolors="black",
    zorder=3
)

# Draw output neurons
ax.scatter(
    [output_x] * output_size,
    output_y,
    s=150,
    color="orange",
    edgecolors="black",
    zorder=3
)
# Layer labels
ax.text(input_x, -0.08, "Input Layer\n11 Neurons",
        ha="center", fontsize=12)

ax.text(hidden_x, -0.08, "Hidden Layer\n256 Neurons (ReLU)",
        ha="center", fontsize=12)

ax.text(output_x, -0.08, "Output Layer\n3 Actions",
        ha="center", fontsize=12)
ax.set_xlim(-0.3, 2.3)
ax.set_ylim(-0.15, 1.1)

plt.tight_layout()

plt.savefig("snake_ai_architecture.png", dpi=300)
plt.show()