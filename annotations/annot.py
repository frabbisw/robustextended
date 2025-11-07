from sklearn.metrics import cohen_kappa_score
import numpy as np
import re

def bin_scores(scores):
    # Binning continuous scores into discrete categories (0, 0.25, 0.5, 0.75, 1.0)
    bins = [0, 0.125, 0.375, 0.625, 0.875, 1.01]
    labels = [0, 0.25, 0.5, 0.75, 1.0]
    binned_indices = np.digitize(scores, bins) - 1
    return np.array([labels[i] for i in binned_indices])

def parse_annotation_file(filename):
    # Parse file, extracting values for Perturbed prompt, Nominal prompt, and Semantic
    samples = []
    with open(filename, 'r') as f:
        content = f.read()
    # Split entries by blank lines or multiple newlines
    entries = re.split(r'\n\s*\n', content.strip())
    print(len(entries))
    
    for entry in entries:
        lines = entry.strip().split('\n')
        # Expecting 4 lines: ID, Perturbed prompt, Nominal prompt, Semantic
        if len(lines) < 4:
            continue
        # Parse the values after colon
        perturbed = float(lines[1].split(':')[1].strip())
        nominal = float(lines[2].split(':')[1].strip())
        semantic = float(lines[3].split(':')[1].strip())
        samples.append({
            'naturalness_perturbed': perturbed,
            'naturalness_nominal': nominal,
            'similarity': semantic
        })
    return samples

def evaluate_annotations(lang):
    file1 = f"{lang}_1.txt"
    file2 = f"{lang}_2.txt"
    
    annotator1 = parse_annotation_file(file1)
    annotator2 = parse_annotation_file(file2)
    
    # Sanity check: both must have the same number of samples
    if len(annotator1) != len(annotator2):
        print(len(annotator1), len(annotator2))
        print(annotator1[-1], annotator2[-1])
        
        raise ValueError("Annotator files have different number of samples")
    
    keys = ['naturalness_nominal', 'naturalness_perturbed', 'similarity']
    kappas = {}
    
    for key in keys:
        scores1 = np.array([sample[key] for sample in annotator1])
        scores2 = np.array([sample[key] for sample in annotator2])
        
        binned1 = bin_scores(scores1)
        binned2 = bin_scores(scores2)
        
        kappa = cohen_kappa_score(binned1, binned2)
        kappas[key] = kappa
    
    explanation = (
        "Scores were binned into five discrete categories to reflect the annotation scale. "
        "Cohen's Kappa was calculated on these binned scores to measure inter-annotator "
        "agreement, accounting for chance agreement and providing a robust measure of reliability."
    )
    
    return kappas, explanation

# Example usage:
print("CPP")
kappas, explanation = evaluate_annotations('cpp')
print(kappas)
print(explanation)
print("============")

print("Java")
kappas, explanation = evaluate_annotations('java')
print(kappas)
print(explanation)
print("============")

print("JS")
kappas, explanation = evaluate_annotations('js')
print(kappas)
print(explanation)
print("============")
