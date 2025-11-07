from sklearn.metrics import cohen_kappa_score
import numpy as np

def bin_scores(scores):
    # Bin continuous scores into discrete categories (0, 0.25, 0.5, 0.75, 1.0)
    bins = [0, 0.125, 0.375, 0.625, 0.875, 1.01]
    labels = [0, 0.25, 0.5, 0.75, 1.0]
    binned_indices = np.digitize(scores, bins) - 1
    return np.array([labels[i] for i in binned_indices])

def evaluate_annotation_lists(ann1, ann2):
    """
    ann1, ann2: lists of samples, each sample is [naturalness_nominal, naturalness_perturbed, similarity]
    Example:
    ann1 = [[1, 0.75, 1], [0.5, 0.25, 0.5], ...]
    ann2 = [[1, 0.75, 1], [0.5, 0.5, 0.5], ...]
    
    Returns:
    avg_scores: dict with average scores per key across both annotators
    kappas: dict with Cohen's kappa per key after binning
    explanation: string describing methodology
    """
    if len(ann1) != len(ann2):
        raise ValueError("Annotation lists must have the same length")
    
    ann1 = np.array(ann1)
    ann2 = np.array(ann2)
    
    keys = ['naturalness_nominal', 'naturalness_perturbed', 'similarity']
    avg_scores = {}
    kappas = {}
    
    for i, key in enumerate(keys):
        scores1 = ann1[:, i]
        scores2 = ann2[:, i]
        
        avg_scores[key] = float(np.mean(np.concatenate([scores1, scores2])))
        
        binned1 = bin_scores(scores1)
        binned2 = bin_scores(scores2)
        
        kappas[key] = cohen_kappa_score(binned1, binned2)
    
    explanation = (
        "Scores are averaged over the two annotators to summarize the annotation values. "
        "Since the annotations are given on a discrete scale (0, 0.25, 0.5, 0.75, 1), "
        "scores are binned accordingly before calculating Cohen's Kappa to measure inter-annotator agreement, "
        "which accounts for agreement occurring by chance."
    )
    
    return avg_scores, kappas, explanation

def process_lang(contents):
    stop_token = "\n\n"

    lang_group = []
    groups = contents.split(stop_token)
    for group in groups:
        if group == "":
            continue
        try:
            group = group.strip()
            if len(group.split("\n")) == 4:
                _, nom, pert, sem  = group.split("\n")
            else:
                nom, pert, sem  = group.split("\n")
            pert = float(pert.split(":")[-1].strip())
            nom = float(nom.split(":")[-1].strip())
            sem = float(sem.split(":")[-1].strip())
            lang_group.append([pert, nom, sem])
        except Exception as e:
            print(e)
            print(group)
            print("==========")
            
    return lang_group

def get_lists(lang):
    with open(f"{lang}_1.txt", "r") as f:
        contents_1 = f.read()
    with open(f"{lang}_2.txt", "r") as f:
        contents_2 = f.read()
    
    lst_1 = process_lang(contents_1)
    lst_2 = process_lang(contents_2)
    
    print(len(lst_1))    
    print(len(lst_2))    

# Example usage:
# ann1 = [[1, 0.75, 1], [0.5, 0.25, 0.5], ...]
# ann2 = [[1, 0.75, 1], [0.5, 0.5, 0.5], ...]
# avg_scores, kappas, explanation = evaluate_annotation_lists(ann1, ann2)
# print(avg_scores)
# print(kappas)
# print(explanation)


# Example usage:
print("CPP")
get_lists("cpp")
print("============")

print("Java")
get_lists("java")
print("============")

print("JS")
get_lists("js")
print("============")
