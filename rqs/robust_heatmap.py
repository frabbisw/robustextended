import pandas as pd
import pickle

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from typing import List, Any

def plot_correlation_bar_chart(correlation_series: pd.Series, title: str, save_filename: str) -> None:
    """
    Generates and saves a horizontal bar chart visualizing the correlation 
    of each feature with the target variable ('robust_drop').
    
    Args:
        correlation_series: A pandas Series of correlations (features vs. target).
        title: The descriptive title for the plot.
        save_filename: The required filename to save the generated plot.
    """
    if not save_filename:
        print("Error: save_filename must be provided to save the plot.")
        return
    
    # Drop the correlation of the target with itself for plotting
    plot_data = correlation_series.drop('robust_drop', errors='ignore')
    
    # Sort by correlation strength (absolute value) for better visual impact
    plot_data = plot_data.reindex(plot_data.abs().sort_values(ascending=False).index)
    
    fig, ax = plt.subplots(figsize=(10, len(plot_data) * 0.5 + 1)) # Dynamic height
    
    # Use different colors for positive and negative correlations
    colors = ['#1f77b4' if c >= 0 else '#d62728' for c in plot_data.values]
    
    ax.barh(plot_data.index, plot_data.values, color=colors)
    
    # Add correlation values (annotations)
    for index, value in enumerate(plot_data.values):
        ax.text(value, index, f'{value:.2f}', 
                ha='left' if value < 0 else 'right', 
                va='center', 
                fontsize=10, 
                color='black')
        
    ax.axvline(0, color='grey', linestyle='--', linewidth=1) # Zero line
    ax.set_xlabel("Pearson Correlation Coefficient with 'robust_drop'")
    ax.set_title(f"Feature Correlation with Robustness Drop ({title})", fontsize=14)
    ax.grid(axis='x', linestyle=':', alpha=0.6)
    
    fig.tight_layout() 
    
    # Save figure at 300 dpi for high-quality publication/report use
    plt.savefig(save_filename, dpi=300, bbox_inches='tight') 
    print(f"\nBar chart saved successfully to: {save_filename}")
    
    plt.close(fig)


def analyze_robustness_drop_correlation(
    df: pd.DataFrame, 
    language_name: str, 
    perturbation_type: str, 
    save_heatmap_filename: str
) -> None:
    """
    Analyzes the correlation of all numerical features in the DataFrame 
    with the 'robust_drop' column and generates a correlation bar chart.
    
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
    robust_drop_correlation = correlation_matrix['robust_drop']
    
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
    
    # Call the new bar chart function with the single correlation series
    plot_correlation_bar_chart(
        robust_drop_correlation, 
        title=analysis_title,
        save_filename=save_heatmap_filename
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
