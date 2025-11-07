from sklearn.metrics import cohen_kappa_score
import numpy as np

def discretize(values):
    """
    Convert float values [0, 0.25, 0.5, 0.75, 1.0]
    to integer categories [0, 1, 2, 3, 4] for kappa calculation.
    """
    mapping = {0.0: 0, 0.25: 1, 0.5: 2, 0.75: 3, 1.0: 4}
    rounded = [round(v * 4) / 4 for v in values]  # fix small float deviations
    return np.array([mapping.get(v, 4) for v in rounded], dtype=int)

def evaluate_annotation_lists(ann1, ann2):
    """
    ann1, ann2: lists of samples, each sample = [naturalness_nominal, naturalness_perturbed, similarity]
    """
    if len(ann1) != len(ann2):
        raise ValueError("Both annotator lists must have the same number of samples")

    ann1 = np.array(ann1)
    ann2 = np.array(ann2)
    keys = ['naturalness_nominal', 'naturalness_perturbed', 'similarity']

    avg_scores, kappas = {}, {}

    for i, key in enumerate(keys):
        vals1 = ann1[:, i].astype(float)
        vals2 = ann2[:, i].astype(float)

        # Average across annotators
        avg_scores[key] = float(np.mean(np.concatenate([vals1, vals2])))

        # Convert to discrete categories for Cohen’s kappa
        d1, d2 = discretize(vals1), discretize(vals2)
        kappas[key] = cohen_kappa_score(d1, d2)

    explanation = (
        "Scores are averaged across both annotators. "
        "Cohen’s kappa is computed after discretizing ratings into five ordinal bins "
        "(0, 0.25, 0.5, 0.75, 1.0), ensuring categorical consistency. "
        "This measures inter-annotator agreement beyond chance."
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

    return lst_1, lst_2

    # print(len(lst_1))    
    # print(len(lst_2))    

# Example usage:
# ann1 = [[1, 0.75, 1], [0.5, 0.25, 0.5], ...]
# ann2 = [[1, 0.75, 1], [0.5, 0.5, 0.5], ...]
# avg_scores, kappas, explanation = evaluate_annotation_lists(ann1, ann2)
# print(avg_scores)
# print(kappas)
# print(explanation)


# Example usage:

# print(get_lists("cpp"))

# exit(0)
print("CPP")
lst_1, lst_2 = get_lists("cpp")
print(lst_1)
print(lst_2)

avg_scores, kappas, explanation = evaluate_annotation_lists(lst_1, lst_2)
print(avg_scores)
print("------------")
print(kappas)
print("------------")
print(explanation)
print("============")


exit(0)

print("Java")
avg_scores, kappas, explanation = evaluate_annotation_lists(get_lists("java"))
print(avg_scores)
print("------------")
print(kappas)
print("------------")
print(explanation)
print("============")

print("JS")
avg_scores, kappas, explanation = evaluate_annotation_lists(get_lists("js"))
print(avg_scores)
print("------------")
print(kappas)
print("------------")
print(explanation)
print("============")
