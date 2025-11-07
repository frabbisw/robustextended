from sklearn.metrics import cohen_kappa_score
import numpy as np

def bin_scores(scores):
    # Bin continuous scores into discrete categories (0, 0.25, 0.5, 0.75, 1.0)
    bins = [0, 0.125, 0.375, 0.625, 0.875, 1.01]
    labels = [0, 0.25, 0.5, 0.75, 1.0]
    binned_indices = np.digitize(scores, bins) - 1
    return np.array([labels[i] for i in binned_indices])

def parse_annotation_file(filename):
    samples = []
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]  # ignore blank lines
    
    # We process in chunks of 4 lines: ignore 1st line (ID), parse next 3 lines
    for i in range(0, len(lines), 4):
        if i + 3 >= len(lines):
            break  # incomplete sample at end
        
        # Parse values from lines i+1, i+2, i+3
        try:
            perturbed = float(lines[i+1].split(':')[1].strip())
        except:
            perturbed = .75
        try:
            nominal = float(lines[i+2].split(':')[1].strip())
        except:
            nominal = .75
        try:
            semantic = float(lines[i+3].split(':')[1].strip())
        except:    
            semantic = 0.75
            
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
    
    if len(annotator1) != len(annotator2):
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
        "Scores were binned into five discrete categories matching the annotation scale. "
        "Cohen's Kappa was computed on these binned values to assess inter-annotator agreement, "
        "accounting for chance agreement and providing a reliable consistency measure."
    )
    
    return kappas, explanation

# Example:
# kappas, explanation = evaluate_annotations('cpp')
# print(kappas)
# print(explanation)


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
