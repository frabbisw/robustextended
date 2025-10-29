import pandas as pd
import pickle

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from typing import List, Any
from collections import Counter

def plot_feature_by_status_heatmap(
    main_df: pd.DataFrame, 
    perturbation_type: str, 
    save_filename: str
) -> None:
    """
    Analyzes feature averages for FAILED cases, comparing them across
    different 'language' groups using a LOCAL baseline.
    
    For each language (e.g., "JAVA"), it first calculates the mean/std dev
    from ALL "JAVA" samples (passed and failed) to get a "local Java baseline".
    
    It then calculates the mean feature values for FAILED "JAVA" cases and
    computes the Z-score (standard deviation from the "local Java baseline").
    
    This helps identify which features are unusually high or low for
    failures *relative to other samples in that same language*.

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
    numeric_features = main_df.select_dtypes(include=[np.number]).columns.tolist()
    if not numeric_features:
        print("Error: No numeric features found in the DataFrame.")
        return

    print(f"Analyzing features: {numeric_features}")

    # --- 2. Calculate Z-Scores using LOCAL (per-language) baselines ---
    
    languages = sorted(main_df['language'].unique())
    z_score_rows = []

    print("\nCalculating Z-Scores using a LOCAL (per-language) baseline...")

    for lang in languages:
        # Get all samples for this language
        lang_df = main_df[main_df['language'] == lang]
        
        if lang_df.empty:
            print(f"Skipping {lang}: No data found.")
            continue

        # Calculate the "local baseline" mean and std dev from ALL samples in this language
        local_mean = lang_df[numeric_features].mean()
        local_std = lang_df[numeric_features].std()

        # Handle features with zero variance (e.g., if a feature is constant *within* this language)
        local_std = local_std.replace(0, 1) # Avoid division by zero

        # Get *only* the failed cases for this language
        failed_lang_df = lang_df[lang_df['run_status'].str.upper() != 'PASSED']
        
        if failed_lang_df.empty:
            print(f"Skipping {lang}: No FAILED cases found to analyze.")
            # We can append a row of NaNs or 0s if we want to show it in the plot
            z_score_row = pd.Series(index=numeric_features, data=np.nan, name=lang)
        else:
            # Calculate the mean of the features for the failed cases
            failed_mean = failed_lang_df[numeric_features].mean()
            
            # Calculate the Z-score for this language's failed cases
            # (Failed Mean - Local Baseline Mean) / Local Baseline Std
            z_score_row = (failed_mean - local_mean) / local_std
            z_score_row.name = lang
        
        z_score_rows.append(z_score_row)

    if not z_score_rows:
        print("Error: No data processed. Ending analysis.")
        return

    # --- 3. Combine and Plot ---
    
    # Create the final DataFrame for plotting
    normalized_df = pd.DataFrame(z_score_rows)
    
    # Fill any NaN (e.g., if a language had 0 failures)
    # A Z-score of 0 is appropriate as it represents "no deviation"
    plot_df = normalized_df.fillna(0)

    print("\n" + "="*60)
    print("Standardized Mean Feature Values (Z-Scores) for FAILED Cases:")
    print("(Calculated relative to the average of *all* samples in that *same* language)")
    print(plot_df)
    print("="*60)
    print("\nInterpretation: High positive (red) means a FAILED case in this language")
    print("has a feature value significantly *higher* than the average for that language.")
    print("High negative (blue) means it's significantly *lower*.")
    print("-"*60)


    # --- 4. Plot Combined Heatmap (Pure Matplotlib) ---
    
    analysis_title = (
        f"Standardized Feature Averages for FAILED Cases (vs. Local Language Average)\n"
        f"{perturbation_type.title()} Perturbation"
    )
    
    # Adjust size
    fig_width = max(12, plot_df.shape[1] * 1.0)
    fig_height = max(4, plot_df.shape[0] * 1.5 + 2) # More vertical space per row
    
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))
    
    plot_data = plot_df.values
    
    # Use a diverging colormap centered at 0
    cmap = plt.get_cmap('coolwarm')
    # Center the colormap at 0. Find the max absolute value for symmetric range.
    v_max = np.nanmax(np.abs(plot_data))
    # Handle case where v_max might be 0
    if v_max == 0:
        v_max = 1 
    v_min = -v_max
    
    im = ax.imshow(plot_data, cmap=cmap, vmin=v_min, vmax=v_max, aspect='auto')

    cbar = fig.colorbar(im, ax=ax, shrink=0.8, aspect=15, pad=0.05)
    cbar.set_label("Z-Score (Standard Deviations from Local Language Mean)", rotation=-90, va="bottom")

    ax.set_xticks(np.arange(plot_df.shape[1]))
    ax.set_yticks(np.arange(plot_df.shape[0]))
    
    # Use the DataFrame index (language names) for Y-axis labels
    ax.set_xticklabels(plot_df.columns, rotation=45, ha='right', fontsize=10)
    ax.set_yticklabels(plot_df.index, rotation=0, fontsize=12) 

    # Loop over data and create text annotations
    for i in range(plot_df.shape[0]):
        for j in range(plot_df.shape[1]):
            value = plot_data[i, j]
            text_label = f"{value:.2f}"
            # Use a threshold to decide text color (light/dark)
            text_color = "white" if np.abs(value) > (v_max * 0.5) else "black"
                
            ax.text(j, i, text_label,
                    ha="center", va="center", color=text_color, size=10)

    ax.set_title(analysis_title, fontsize=16, pad=20)
    ax.set_ylabel("")

    fig.tight_layout() 
    
    plt.savefig(save_filename, dpi=300, bbox_inches='tight') 
    print(f"\nCombined feature/status heatmap saved successfully to: {save_filename}")
    
    plt.close(fig)

def get_lang_df(df, lang, pert_type):
	filtered_df = df[(df["lang"] == lang) & (df["pert_type"] == pert_type)]
	filtered_df = filtered_df.drop(columns=["lang", "pert_type", "model_name"])
	return filtered_df

def get_whole_df():
	with open("all_data.pkl", "rb") as f:
		data = pickle.load(f)
	
	columns = data[0]
	rows = data[1:]
	df = pd.DataFrame(rows, columns=columns)
	return df

def get_pert_df(df, pert_type):
	df_java = get_lang_df(df, "java", pert_type)
	df_cpp = get_lang_df(df, "cpp", pert_type)
	df_js = get_lang_df(df, "js", pert_type)

	df_java['language'] = 'JAVA'
	df_cpp['language'] = 'CPP'
	df_js['language'] = 'JS'

	# 2. Combine them into one main DataFrame
	# ignore_index=True is important for a clean index
	main_df = pd.concat([df_java, df_cpp, df_js], ignore_index=True)
	return main_df


df = get_whole_df()

# df_filtered = df[(df['lang'] == 'java') & (df['score'] > 90)]
# df_filtered = df[(df['lang'] == 'java') & (df['pert_type'] == 'natgen')]

# print(list(df_filtered['run_status']))

# exit(1)
# print(df.columns)


pert_map = {"func_name": "FunctionName", "nlaugmenter": "DocString", "format": "Format", "natgen": "Syntax"}
for pert_type in ["func_name", "nlaugmenter", "format", "natgen"]:
	main_df = get_pert_df(df, pert_type)
	print(pert_type)
	plot_feature_by_status_heatmap(
	    main_df=main_df,
	    perturbation_type=f"{pert_map[pert_type]}",  # Or whatever perturbation this is
	    save_filename=f"figures/{pert_type}_heatmap.png"
	)

# analyze_robustness_drop_correlation(get_df(df, "java", "func_name"), "Java", "func_name", "figures/java_heat.png")
# print(f"done java func_name")
# analyze_robustness_drop_correlation(get_df(df, "cpp", "func_name"), "Java", "func_name", "figures/cpp_heat.png")
# print(f"done java func_name")
# analyze_robustness_drop_correlation(get_df(df, "js", "func_name"), "Java", "func_name", "figures/js_heat.png")
# print(f"done java func_name")
