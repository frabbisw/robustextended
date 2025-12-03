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
    different 'language' groups using a LOCAL baseline and weighting
    by the failure rate.
    
    This calculates an "Impact Score" = Z-Score * Failure Rate
    
    1. For each language (e.g., "JAVA"), it calculates the mean/std dev
       from ALL "JAVA" samples (passed/failed) to get a "local Java baseline".
    2. It calculates the Z-score for FAILED "JAVA" cases (how "weird" failures are).
    3. It calculates the "Failure Rate" for "JAVA" (how *often* failures happen).
    4. It multiplies (Z-Score * Failure Rate) to get the "Impact Score".
    
    This helps identify which features are *impactful* (both unusual and common)
    for failures in a specific language.

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

    # --- 2. Calculate "Impact Scores" (Z-Score * Failure Rate) ---
    
    languages = sorted(main_df['language'].unique())
    impact_score_rows = []

    print("\nCalculating Impact Scores (Z-Score * Failure Rate) using a LOCAL baseline...")

    for lang in languages:
        # Get all samples for this language
        lang_df = main_df[main_df['language'] == lang]
        
        if lang_df.empty:
            print(f"Skipping {lang}: No data found.")
            continue

        # --- A. Calculate Failure Rate ---
        total_samples = len(lang_df)
        failed_lang_df = lang_df[lang_df['run_status'].str.upper() != 'PASSED']
        failed_samples = len(failed_lang_df)

        if total_samples == 0:
            print(f"Skipping {lang}: No samples found.")
            continue
        
        failure_rate = failed_samples / total_samples
        print(f"  {lang}: Failure Rate = {failed_samples} / {total_samples} = {failure_rate:.4f}")

        # --- B. Calculate Local Baseline & Z-Score ---
        # Calculate the "local baseline" mean and std dev from ALL samples in this language
        local_mean = lang_df[numeric_features].mean()
        local_std = lang_df[numeric_features].std()

        # Handle features with zero variance
        local_std = local_std.replace(0, 1) # Avoid division by zero
        
        if failed_samples == 0:
            print(f"  {lang}: No FAILED cases found. Impact Score for all features will be 0.")
            # Z-Score is technically undefined, but impact is 0
            z_score_row = pd.Series(index=numeric_features, data=0.0)
        else:
            # Calculate the mean of the features for the failed cases
            failed_mean = failed_lang_df[numeric_features].mean()
            
            # Calculate the Z-score for this language's failed cases
            # (Failed Mean - Local Baseline Mean) / Local Baseline Std
            z_score_row = (failed_mean - local_mean) / local_std
        
        # --- C. Calculate Impact Score ---
        impact_score_row = z_score_row * failure_rate
        impact_score_row.name = lang
        
        impact_score_rows.append(impact_score_row)

    if not impact_score_rows:
        print("Error: No data processed. Ending analysis.")
        return

    # --- 3. Combine and Plot ---
    
    # Create the final DataFrame for plotting
    normalized_df = pd.DataFrame(impact_score_rows)
    
    # Fill any NaN (e.g., if a language had 0 failures)
    # An Impact Score of 0 is appropriate as it represents "no deviation"
    plot_df = normalized_df.fillna(0)

    print("\n" + "="*60)
    print("Feature Impact Score (Z-Score * Failure Rate) for FAILED Cases:")
    print("(Z-Score is calculated relative to the average of *all* samples in that *same* language)")
    print(plot_df)
    print("="*60)
    print("\nInterpretation: High positive (red) means this feature is *both*")
    print("significantly *higher* than the language average AND failures are common.")
    print("High negative (blue) means it's *lower* AND failures are common.")
    print("-"*60)


    # --- 4. Plot Combined Heatmap (Pure Matplotlib) ---
    
    analysis_title = (
        f"Feature Impact Score (Z-Score * Failure Rate) for FAILED Cases\n"
        f"{perturbation_type.title()} Perturbation"
    )
    
    # Adjust size
    fig_width = max(12, plot_df.shape[1] * 1.0)
    fig_height = max(4, plot_df.shape[0] * 1.5 + 2) # More vertical space per row
    
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))
    v_min, v_max = -.2, .2
    plot_data = plot_df.values
    
    # Use a diverging colormap centered at 0
    cmap = plt.get_cmap('coolwarm')
	# v_max = 0.2
	# v_min = -v_max
    # Center the colormap at 0. Find the max absolute value for symmetric range.
    # v_max = np.nanmax(np.abs(plot_data))
    # Handle case where v_max might be 0
    # if v_max == 0:
    #     v_max = 1 
    # v_min = -v_max
	
    im = ax.imshow(plot_data, cmap=cmap, vmin=v_min, vmax=v_max, aspect='auto')

    cbar = fig.colorbar(im, ax=ax, shrink=0.8, aspect=15, pad=0.05)
    cbar.set_label("Impact Score (Z-Score × Failure Rate)", rotation=-90, va="bottom")

    ax.set_xticks(np.arange(plot_df.shape[1]))
    ax.set_yticks(np.arange(plot_df.shape[0]))
    
    # Use the DataFrame index (language names) for Y-axis labels
    ax.set_xticklabels(plot_df.columns, rotation=45, ha='right', fontsize=14)
    ax.set_yticklabels(plot_df.index, rotation=0, fontsize=14) 

    # Loop over data and create text annotations
    for i in range(plot_df.shape[0]):
        for j in range(plot_df.shape[1]):
            value = plot_data[i, j]
            text_label = f"{value:.2f}"
            # Use a threshold to decide text color (light/dark)
            text_color = "white" if np.abs(value) > (v_max * 0.5) else "black"
                
            ax.text(j, i, text_label,
                    ha="center", va="center", color=text_color, size=14)

    # ax.set_title(analysis_title, fontsize=16, pad=20)
    ax.set_ylabel("")

    fig.tight_layout() 
    
    plt.savefig(save_filename, dpi=600, bbox_inches='tight') 
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

	main_df = pd.concat([df_java, df_cpp, df_js], ignore_index=True)
	return main_df

def get_pert_df_by_model_name(df, pert_type, model_name):
	filtered_df = df[df["model_name"] == model_name]
	return get_pert_df(filtered_df, pert_type)

df = get_whole_df()

pert_map = {"func_name": "FunctionName", "nlaugmenter": "DocString", "format": "Format", "natgen": "Syntax"}

for pert_type in ["func_name", "nlaugmenter", "format", "natgen"]:
	main_df = get_pert_df(df, pert_type)
	print(pert_type)
	plot_feature_by_status_heatmap(
		main_df=main_df,
		perturbation_type=f"{pert_map[pert_type]}",  # Or whatever perturbation this is
		save_filename=f"heatmaps/XX_{pert_type}_heatmap.png"
	)

for model_name in ["incoder1b", "incoder6b", "codegen2bmulti", "codegen6bmulti", "magicoder7b", "qwencoder"]:
	for pert_type in ["func_name", "nlaugmenter", "format", "natgen"]:
		main_df = get_pert_df_by_model_name(df, pert_type, model_name)
		print(pert_type, model_name)
		plot_feature_by_status_heatmap(
		    main_df=main_df,
		    perturbation_type=f"{pert_map[pert_type]}",  # Or whatever perturbation this is
		    save_filename=f"heatmaps/YY_{model_name}_{pert_type}_heatmap.png"
		)

# analyze_robustness_drop_correlation(get_df(df, "java", "func_name"), "Java", "func_name", "figures/java_heat.png")
# print(f"done java func_name")
# analyze_robustness_drop_correlation(get_df(df, "cpp", "func_name"), "Java", "func_name", "figures/cpp_heat.png")
# print(f"done java func_name")
# analyze_robustness_drop_correlation(get_df(df, "js", "func_name"), "Java", "func_name", "figures/js_heat.png")
# print(f"done java func_name")
