import pandas as pd
import pickle

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from typing import List, Any

def analyze_and_plot_combined_correlation(
    main_df: pd.DataFrame, 
    perturbation_type: str, 
    save_filename: str
) -> None:
    """
    Analyzes correlation with 'robust_drop' for each language found in the 
    'language' column, then plots a single, combined heatmap 
    stacking the results vertically for comparison.

    Args:
        main_df: DataFrame containing features, 'robust_drop', and 'language' columns.
        perturbation_type: Type of perturbation (e.g., 'Function Name') for the title.
        save_filename: Required filename to save the generated plot.
    """
    
    if 'robust_drop' not in main_df.columns or 'language' not in main_df.columns:
        print("Error: DataFrame must contain 'robust_drop' and 'language' columns.")
        return
    if not save_filename:
        print("Error: save_filename must be provided to save the plot.")
        return

    languages = sorted(main_df['language'].unique())
    all_correlation_series = {}
    
    analysis_title = f"Feature Correlation with Robustness Drop / {perturbation_type.title()} Perturbation"
    print("="*60)
    print(f"Running Analysis for: {analysis_title}")
    print(f"Found languages: {languages}")
    print("="*60)

    # --- 1. Calculate Correlation for Each Language ---
    for lang in languages:
        print(f"\nAnalyzing {lang.upper()}...")
        df_lang = main_df[main_df['language'] == lang].copy()
        
        numeric_df = df_lang.select_dtypes(include=[np.number]).copy()
        
        if 'robust_drop' not in numeric_df.columns:
            print(f"Skipping {lang}: 'robust_drop' column is not numeric.")
            continue
            
        numeric_df = numeric_df.replace([np.inf, -np.inf], np.nan).dropna(axis=0, how='any')
        non_constant_cols = numeric_df.columns[numeric_df.nunique() > 1]
        filtered_df = numeric_df[non_constant_cols]
        
        if 'robust_drop' not in filtered_df.columns or filtered_df.shape[1] < 2:
            print(f"Skipping {lang}: Insufficient variance in features or 'robust_drop' column.")
            continue
            
        correlation_matrix = filtered_df.corr()
        robust_drop_correlation = correlation_matrix['robust_drop']
        all_correlation_series[lang.upper()] = robust_drop_correlation
        
        # Print stats for this language
        result_df = pd.DataFrame({
            'Correlation': robust_drop_correlation,
            'Absolute_Correlation': np.abs(robust_drop_correlation)
        }).sort_values(by='Absolute_Correlation', ascending=False)
        print(f"Top correlations for {lang.upper()}:\n", result_df.drop('robust_drop', errors='ignore').head(5))

    if not all_correlation_series:
        print("Error: No valid correlation data was generated for any language.")
        return

    # --- 2. Combine DataFrames for Plotting ---
    
    # This automatically aligns all feature names (columns) and fills missing ones with NaN
    combined_corr_df = pd.DataFrame(all_correlation_series)
    
    # Transpose so languages are rows and features are columns
    plot_df = combined_corr_df.transpose()
    
    # CRITICAL: Sort columns (features) alphabetically for consistent ordering
    plot_df = plot_df.sort_index(axis=1, ascending=True)
    
    # Drop 'robust_drop' column from the plot
    plot_df = plot_df.drop('robust_drop', axis=1, errors='ignore')

    print("\n" + "="*60)
    print("Combined Correlation Matrix (Languages vs. Features):")
    print(plot_df)
    print("="*60)

    # --- 3. Plot Combined 1D Heatmap ---
    
    # Adjust size based on number of features and languages
    fig_width = max(12, plot_df.shape[1] * 0.9) # Width based on num features
    fig_height = max(4, plot_df.shape[0] * 0.8 + 2) # Height based on num languages
    
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))
    
    sns.heatmap(
        plot_df,
        annot=True,          # Show the correlation values
        fmt=".2f",           # Format to 2 decimal places
        cmap='coolwarm',     # Use a diverging colormap
        vmin=-1.0,           # Standardize scale from -1
        vmax=1.0,            # to +1
        cbar=True,           # Show the color bar
        cbar_kws={'label': "Pearson Correlation", 'shrink': 0.8, 'aspect': 15, 'pad': 0.05},
        linewidths=.5,
        ax=ax,
        annot_kws={"size": 10} # Adjust annotation font size
    )
    
    ax.set_title(analysis_title, fontsize=16, pad=20)
    ax.set_yticklabels(ax.get_yticklabels(), rotation=0, fontsize=12) # Language names
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', fontsize=10) # Feature names
    ax.set_ylabel("") # Remove 'None' ylabel

    fig.tight_layout() 
    
    # Save figure at 300 dpi
    plt.savefig(save_filename, dpi=300, bbox_inches='tight') 
    print(f"\nCombined heatmap saved successfully to: {save_filename}")
    
    plt.close(fig)


def get_df(df, lang, pert_type):
	filtered_df = df[(df["lang"] == lang) & (df["pert_type"] == pert_type)]
	filtered_df = filtered_df.drop(columns=["lang", "pert_type", "run_status", "model_name"])
	return filtered_df

with open("data_with_robust.pkl", "rb") as f:
	data_with_robust = pickle.load(f)

columns = data_with_robust[0]
rows = data_with_robust[1:]
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
analyze_and_plot_combined_correlation(
    main_df=main_df,
    perturbation_type="Function Name",  # Or whatever perturbation this is
    save_filename="func_name_heatmap.png"
)

# analyze_robustness_drop_correlation(get_df(df, "java", "func_name"), "Java", "func_name", "figures/java_heat.png")
# print(f"done java func_name")
# analyze_robustness_drop_correlation(get_df(df, "cpp", "func_name"), "Java", "func_name", "figures/cpp_heat.png")
# print(f"done java func_name")
# analyze_robustness_drop_correlation(get_df(df, "js", "func_name"), "Java", "func_name", "figures/js_heat.png")
# print(f"done java func_name")
