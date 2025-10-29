import pandas as pd
import pickle

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from typing import List, Any

def plot_feature_by_status_heatmap(
    main_df: pd.DataFrame, 
    perturbation_type: str, 
    save_filename: str
) -> None:
    """
    Analyzes feature averages across different 'run_status' (categorical)
    and 'language' groups.
    
    It calculates the Z-score (standard deviation from the overall mean) for
    each feature, for each group, and plots this as a heatmap.
    
    This helps identify which features are unusually high or low for
    specific outcomes (e.g., "COMPILATION" errors).

    Args:
        main_df: DataFrame containing features, 'run_status', and 'language' columns.
        perturbation_type: Type of perturbation (e.g., 'Function Name') for the title.
        save_filename: Required filename to save the generated plot.
    """
    
    if 'run_status' not in main_df.columns or 'language' not in main_df.columns:
        print("Error: DataFrame must contain 'run_status' and 'language' columns.")
        return
    if not save_filename:
        print("Error: save_filename must be provided to save the plot.")
        return

    # --- 1. Identify Numeric Features ---
    # Exclude any old target vars and non-numeric cols
    numeric_features = main_df.select_dtypes(include=[np.number]).columns.tolist()
    if not numeric_features:
        print("Error: No numeric features found in the DataFrame.")
        return

    print(f"Analyzing features: {numeric_features}")

    # --- 2. Standardization ---
    # First, calculate the *overall* mean and std dev for each feature
    # This will be our "baseline" for comparison
    overall_mean = main_df[numeric_features].mean()
    overall_std = main_df[numeric_features].std()

    # Handle features with zero variance (e.g., if a feature is constant)
    overall_std = overall_std.replace(0, 1) # Avoid division by zero

    # --- 3. Group and Calculate Mean Values ---
    # Group by both language and run_status, then get the mean of all features
    grouped_df = main_df.groupby(['language', 'run_status'])[numeric_features].mean()
    
    # --- 4. Calculate Z-Scores ---
    # (Group Mean - Overall Mean) / Overall Standard Deviation
    normalized_df = (grouped_df - overall_mean) / overall_std
    
    # Sort the index for a cleaner plot (optional, but good practice)
    normalized_df = normalized_df.sort_index()

    # Fill any NaN (e.g., if a language had 0 "TIMEOUT" errors)
    # A Z-score of 0 is appropriate as it represents "no deviation"
    plot_df = normalized_df.fillna(0)

    print("\n" + "="*60)
    print("Standardized Mean Feature Values (Z-Scores) by Group:")
    print(plot_df)
    print("="*60)
    print("\nInterpretation: High positive (red) means this group's average is")
    print("significantly *higher* than the overall average for that feature.")
    print("High negative (blue) means it's significantly *lower*.")
    print("-"*60)


    # --- 5. Plot Combined Heatmap (Pure Matplotlib) ---
    
    analysis_title = f"Standardized Feature Averages by Outcome / {perturbation_type.title()} Perturbation"
    
    # Adjust size
    fig_width = max(12, plot_df.shape[1] * 1.0)
    fig_height = max(6, plot_df.shape[0] * 0.9)
    
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))
    
    plot_data = plot_df.values
    
    # Use a diverging colormap centered at 0
    cmap = plt.get_cmap('coolwarm')
    # Center the colormap at 0. Find the max absolute value for symmetric range.
    v_max = np.nanmax(np.abs(plot_data))
    v_min = -v_max
    
    im = ax.imshow(plot_data, cmap=cmap, vmin=v_min, vmax=v_max, aspect='auto')

    cbar = fig.colorbar(im, ax=ax, shrink=0.8, aspect=15, pad=0.05)
    cbar.set_label("Z-Score (Standard Deviations from Overall Mean)", rotation=-90, va="bottom")

    ax.set_xticks(np.arange(plot_df.shape[1]))
    ax.set_yticks(np.arange(plot_df.shape[0]))
    
    # Use the MultiIndex for Y-axis labels
    y_labels = [f"{lang} / {status}" for lang, status in plot_df.index]
    ax.set_xticklabels(plot_df.columns, rotation=45, ha='right', fontsize=10)
    ax.set_yticklabels(y_labels, rotation=0, fontsize=10)

    # Loop over data and create text annotations
    for i in range(plot_df.shape[0]):
        for j in range(plot_df.shape[1]):
            value = plot_data[i, j]
            text_label = f"{value:.2f}"
            text_color = "black" if np.abs(value) < (v_max * 0.5) else "white"
                
            ax.text(j, i, text_label,
                    ha="center", va="center", color=text_color, size=9)

    ax.set_title(analysis_title, fontsize=16, pad=20)
    ax.set_ylabel("")

    fig.tight_layout() 
    
    plt.savefig(save_filename, dpi=300, bbox_inches='tight') 
    print(f"\nCombined feature/status heatmap saved successfully to: {save_filename}")
    
    plt.close(fig)


def get_df(df, lang, pert_type):
	filtered_df = df[(df["lang"] == lang) & (df["pert_type"] == pert_type)]
	filtered_df = filtered_df.drop(columns=["lang", "pert_type", "model_name"])
	return filtered_df

with open("all_data.pkl", "rb") as f:
	data = pickle.load(f)

columns = data[0]
rows = data[1:]
df = pd.DataFrame(rows, columns=columns)

df_java = get_df(df, "java", "func_name")
df_cpp = get_df(df, "cpp", "func_name")
df_js = get_df(df, "js", "func_name")

df_java['language'] = 'JAVA'
df_cpp['language'] = 'CPP'
df_js['language'] = 'JS'

# 2. Combine them into one main DataFrame
# ignore_index=True is important for a clean index
main_df = pd.concat([df_java, df_cpp, df_js], ignore_index=True)

# 3. Now, call the function with the combined DataFrame
plot_feature_by_status_heatmap(
    main_df=main_df,
    perturbation_type="Function Name",  # Or whatever perturbation this is
    save_filename="feature_by_status_heatmap.png"
)

# analyze_robustness_drop_correlation(get_df(df, "java", "func_name"), "Java", "func_name", "figures/java_heat.png")
# print(f"done java func_name")
# analyze_robustness_drop_correlation(get_df(df, "cpp", "func_name"), "Java", "func_name", "figures/cpp_heat.png")
# print(f"done java func_name")
# analyze_robustness_drop_correlation(get_df(df, "js", "func_name"), "Java", "func_name", "figures/js_heat.png")
# print(f"done java func_name")
