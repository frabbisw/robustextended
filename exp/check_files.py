import sys
import jsonlines
import os

if len(sys.argv) < 2:
  model = "magicoder7b"
else:
  model = sys.argv[1]

result_root = "/home/f_rabbi/recode/robustextended/datasets"
BASE_DIR = os.path.join(result_root, model, "generated_pass5_1")

def check_file_completeness(filepath):
  cnt = 0
  with open(filepath, "r") as f:
    for line in f.readlines():
      data = json.loads(line)
      if "gc" in data.keys():
        cnt += 1
  return cnt

def main():
    languages = ["cpp", "js", "java"]
    single_file_cats = ["nominal", "partial"]
    scoped_cats = ["format", "nlaugmenter", "func_name", "natgen"]

    for lang in languages:
        lang_dir = os.path.join(BASE_DIR, lang)
        if not os.path.isdir(lang_dir):
            continue

        # case 1: nominal / partial (only one f_s0.jsonl file inside)
        for cat in single_file_cats:
            folder = os.path.join(lang_dir, cat)
            if not os.path.isdir(folder):
                continue
            for file in os.listdir(folder):
                if file.startswith("f_s") and file.endswith(".jsonl"):
                    abs_path = os.path.abspath(os.path.join(folder, file))
                    print(abs_path)

        # case 2: format / nlaugmenter / func_name / natgen
        for cat in scoped_cats:
            cat_dir = os.path.join(lang_dir, cat)
            if not os.path.isdir(cat_dir):
                continue
            for perturb in os.listdir(cat_dir):  # perturb folders like new_line_aftercode, etc.
                perturb_dir = os.path.join(cat_dir, perturb)
                if not os.path.isdir(perturb_dir):
                    continue
                for file in os.listdir(perturb_dir):
                    if file.startswith("f_s") and file.endswith(".jsonl"):
                        abs_path = os.path.abspath(os.path.join(perturb_dir, file))
                        print(abs_path)
                        print(check_file_completeness(abs_path))

if __name__ == "__main__":
    main()
