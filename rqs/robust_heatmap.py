import pandas as pd
import pickle

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from typing import List, Any

def plot_correlation_heatmap(correlation_matrix: pd.DataFrame, title: str, save_filename: str) -> None:
    """
    Generates and saves a heatmap for the given correlation matrix.
    
    Args:
        correlation_matrix: The pandas DataFrame containing the correlation results.
        title: The descriptive title for the plot.
        save_filename: The required filename (e.g., 'java_func_name_heatmap.png') 
                       to save the generated plot.
    """
    if not save_filename:
        # Enforce saving behavior as requested by the user
        print("Error: save_filename must be provided to save the plot.")
        return
        
    fig, ax = plt.subplots(figsize=(10, 8))
    
    sns.heatmap(
        correlation_matrix, 
        annot=True, 
        cmap='coolwarm', 
        fmt=".2f",
        linewidths=.5,
        cbar_kws={'label': 'Pearson Correlation Coefficient'},
        ax=ax,
        robust=True 
    )
    plt.title(f"Feature Correlation Heatmap: {title}", fontsize=14)
    
    fig.tight_layout() 
    
    # Save figure at 300 dpi for high-quality publication/report use
    plt.savefig(save_filename, dpi=300, bbox_inches='tight') 
    print(f"\nHeatmap saved successfully to: {save_filename}")
    plt.close(fig) # Close the figure to free up memory


def analyze_robustness_drop_correlation(df: pd.DataFrame, language_name: str, perturbation_type: str, save_heatmap_filename: str) -> None:
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
        save_filename=save_heatmap_filename
    )

def get_df(df, lang, pert_type):
	filtered_df = df[(df["lang"] == lang) & (df["pert_type"] == pert_type)]
	filtered_df = filtered_df.drop(columns=["lang", "pert_type", "run_status", "model_name"])
	
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
