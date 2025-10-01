import sacrebleu
import sys

jsonl_path = sys.argv[1]

def load_prompts(filename):
    prompts = []
    with open(filename, encoding="utf8") as f:
        for line in f.readlines():
            prompts.append(json.loads(line))
    return prompts
def save_prompts(filename, prompts):
    with jsonlines.open(filename, mode='w') as writer:
        for line in prompts:
            jsonlines.Writer.write(writer, line)

def bleu(hypothesis, reference):
    return sacrebleu.sentence_bleu(hypothesis, [reference]).score

prompts = load_prompts(jsonl_path)
bleu_scores = []

for prompt in prompts:
    bleu_scores.append(bleu(prompt["nl"], prompt["filtered_nl"]))

print(sum(bleu_scores)/len(bleu_scores))
