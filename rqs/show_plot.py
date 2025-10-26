import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def visualize_metrics(data_points, column_names, title="Metrics Relationship", save_path=None):
    """
    Visualize relationships between two metrics, colored by pass status and shaped by language.
    
    Parameters:
        data_points: list of [metric1, metric2, pass_status, language]
        column_names: ["Metric 1 Name", "Metric 2 Name", "Pass Status Label", "Language Label"]
        title: optional plot title
        save_path: optional path to save figure (e.g., 'figures/plot.png')
    """
    
    # Extract columns
    metric1_name, metric2_name, _, _ = column_names
    x_vals = [d[0] for d in data_points]
    y_vals = [d[1] for d in data_points]
    statuses = [d[2].lower() for d in data_points]
    langs = [d[3].lower() for d in data_points]

    # Define colors for pass status
    color_map = {
        "pass": "green",
        "compilation": "red",
        "assertion": "violet"
    }

    # Define markers for language
    marker_map = {
        "java": "o",     # circle
        "cpp": "s",      # square
        "python": "D",   # diamond
        "js": "^"        # triangle
    }

    plt.figure(figsize=(8, 6))

    # Plot each point
    for x, y, status, lang in zip(x_vals, y_vals, statuses, langs):
        color = color_map.get(status, "gray")
        marker = marker_map.get(lang, "x")
        plt.scatter(x, y, c=color, marker=marker, s=80, edgecolors="black", alpha=0.8)

    # Labels and title
    plt.xlabel(metric1_name, fontsize=12)
    plt.ylabel(metric2_name, fontsize=12)
    plt.title(title, fontsize=14, fontweight="bold")

    # Legends
    color_patches = [mpatches.Patch(color=v, label=k.capitalize()) for k, v in color_map.items()]
    marker_patches = [plt.Line2D([0], [0], marker=v, color="w", label=k.capitalize(),
                                 markerfacecolor="gray", markersize=10, markeredgecolor="black")
                      for k, v in marker_map.items()]
    
    legend1 = plt.legend(handles=color_patches, title="Pass Status", loc="upper right")
    plt.gca().add_artist(legend1)
    plt.legend(handles=marker_patches, title="Language", loc="lower right")

    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()

    # Save figure if requested
    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, dpi=300, bbox_inches="tight")
        print(f"✅ Figure saved at: {save_path}")

    plt.show()

data = [
    [5.3, 0.12, "pass", "java"],
    [4.1, 0.32, "compilation", "cpp"],
    [6.8, 0.15, "assertion", "python"],
    [5.5, 0.08, "pass", "cpp"],
]

cols = ["Cyclomatic Complexity", "Change %", "Pass Status", "Language"]

visualize_metrics(data, cols, title="Cyclomatic Complexity vs Change%", save_path="figures/complexity_vs_change.png")
