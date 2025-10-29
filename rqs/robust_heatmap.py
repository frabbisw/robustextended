import pandas as pd
import pickle

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from typing import List, Any

def plot_correlation_heatmap(correlation_matrix: pd.DataFrame, title: str, save_filename: str) -> None:
    """
    Generates and saves a heatmap for the given correlation matrix using Matplotlib
    to bypass known dependency issues with Seaborn's heatmap function.
    
    Args:
        correlation_matrix: The pandas DataFrame containing the correlation results.
        title: The descriptive title for the plot.
        save_filename: The required filename (e.g., 'java_func_name_heatmap.png') 
                       to save the generated plot.
    """
    if not save_filename:
        print("Error: save_filename must be provided to save the plot.")
        return
        
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # --- Matplotlib-based Heatmap Generation ---
    # Using plt.pcolormesh to bypass the problematic sns.heatmap function
    
    # Prepare data for pcolormesh
    data = correlation_matrix.values
    
    # Define colors and normalization
    cmap = plt.cm.get_cmap('coolwarm')
    vmin = -1.0 # Correlation ranges from -1 to 1
    vmax = 1.0
    
    cax = ax.pcolormesh(
        data, 
        cmap=cmap, 
        vmin=vmin, 
        vmax=vmax
    )
    
    # Add color bar
    fig.colorbar(cax, ax=ax, label='Pearson Correlation Coefficient')
    
    # Set ticks and labels
    ax.set_xticks(np.arange(data.shape[1]) + 0.5, minor=False)
    ax.set_yticks(np.arange(data.shape[0]) + 0.5, minor=False)
    ax.set_xticklabels(correlation_matrix.columns, rotation=90)
    ax.set_yticklabels(correlation_matrix.index)
    
    # Add annotation (correlation values)
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            # Use white or black text depending on cell color for contrast
            text_color = 'white' if abs(data[i, j]) > 0.6 else 'black'
            ax.text(j + 0.5, i + 0.5, f'{data[i, j]:.2f}',
                    ha='center', va='center', color=text_color, fontsize=10)
    
    # Set plot title and limits
    ax.set_title(f"Feature Correlation Heatmap: {title}", fontsize=14)
    ax.set_xlim(0, data.shape[1])
    ax.set_ylim(0, data.shape[0])
    ax.invert_yaxis() # Heatmaps usually have y-axis inverted
    
    # --- End Matplotlib-based Heatmap Generation ---
    
    fig.tight_layout() 
    
    # Save figure at 300 dpi for high-quality publication/report use
    plt.savefig(save_filename, dpi=300, bbox_inches='tight') 
    print(f"\nHeatmap saved successfully to: {save_filename}")
    
    plt.close(fig) # Close the figure using the figure object for safety


def analyze_robustness_drop_correlation(
    df: pd.DataFrame, 
    language_name: str, 
    perturbation_type: str, 
    save_heatmap_filename: str
) -> None:
    """
    Analyzes the correlation of all numerical features in the DataFrame 
    with the 'robust_drop' column and generates a correlation heatmap.
    
    Args:
        df: DataFrame containing features and the 'robust_drop' column.
        language_name: Name of the language being analyzed (e.g., 'JAVA', 'CPP').
        perturbation_type: Type of perturbation being analyzed (e.g., 'Function Name', 'DocString').
        save_heatmap_filename: Required filename to save the generated plot.
    """
    
    if 'robust_drop' not in df.columns:
        print("Error: DataFrame must contain a column named 'robust_drop'.")
        return

    # --- 1. Preprocessing and Feature Selection ---
    
    # Ensure all columns are suitable for correlation (numeric)
    numeric_df = df.select_dtypes(include=[np.number]).copy()
    
    # Check if 'robust_drop' is still present after filtering (it should be)
    if 'robust_drop' not in numeric_df.columns:
        print("Error: 'robust_drop' column is not numeric. Please ensure it is cast to float or int.")
        return

    # Handle NaNs and columns with zero variance (correlation is undefined)
    # Note: Using dropna(axis=0, how='any') removes rows with any NaN value in the numeric subset
    numeric_df = numeric_df.replace([np.inf, -np.inf], np.nan).dropna(axis=0, how='any')
    
    # Filter out columns that have no variance (i.e., all values are the same)
    non_constant_cols = numeric_df.columns[numeric_df.nunique() > 1]
    filtered_df = numeric_df[non_constant_cols]
    
    if filtered_df.shape[1] < 2:
        print("Warning: Insufficient variance in features or 'robust_drop' column. Cannot calculate meaningful correlation.")
        print(f"Current 'robust_drop' unique values: {filtered_df['robust_drop'].nunique()}")
        return

    # --- 2. Calculate Correlation Matrix ---

    # Calculate the correlation matrix
    correlation_matrix = filtered_df.corr()
    
    # Extract the correlation values of metrics with 'robust_drop'
    robust_drop_correlation = correlation_matrix['robust_drop'].sort_values(ascending=False)
    
    # --- 3. Print Statistical Results ---
    
    analysis_title = f"{language_name.upper()} / {perturbation_type.title()} Perturbation"
    
    print("="*60)
    print(f"Correlation Analysis: Feature Impact on Robustness Drop ({analysis_title})")
    print("="*60)
    
    print("Correlation with 'robust_drop' (Higher absolute value indicates stronger linear relationship):\n")
    
    # Print the absolute correlation values to emphasize strength
    result_df = pd.DataFrame({
        'Correlation': robust_drop_correlation,
        'Absolute_Correlation': np.abs(robust_drop_correlation)
    }).sort_values(by='Absolute_Correlation', ascending=False)
    
    # Drop the 'robust_drop' row itself for cleaner output
    print(result_df.drop('robust_drop', errors='ignore'))
    
    print("\nInterpretation:")
    print(" - A Positive Correlation means that as the feature value increases (e.g., larger change in function name), the robustness drop also increases (worse performance).")
    print(" - A Negative Correlation means that as the feature value increases, the robustness drop decreases (better performance/less drop).")
    
    # --- 4. Plot Visualization ---
    plot_correlation_heatmap(
        correlation_matrix, 
        title=analysis_title,
        save_heatmap_filename=save_heatmap_filename
    )

def get_df(df, lang, pert_type):
	filtered_df = df[(df["lang"] == lang) & (df["pert_type"] == pert_type)]
	filtered_df = filtered_df.drop(columns=["lang", "pert_type", "run_status", "model_name"])
	return filtered_df

with open("data_with_robust.pkl", "rb") as f:
	data_with_robust = pickle.load(f)

columns = data_with_robust[0]
rows = data_with_robust[1:]
df = pd.DataFrame(rows, columns=columns)

print(columns)
print(df.columns)

print()

analyze_robustness_drop_correlation(get_df(df, "java", "func_name"), "Java", "func_name", "figures/java_heat.png")
print(f"done java func_name")
analyze_robustness_drop_correlation(get_df(df, "cpp", "func_name"), "Java", "func_name", "figures/cpp_heat.png")
print(f"done java func_name")
analyze_robustness_drop_correlation(get_df(df, "js", "func_name"), "Java", "func_name", "figures/js_heat.png")
print(f"done java func_name")
