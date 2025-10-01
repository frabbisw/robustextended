import sacrebleu

def bleu(hypothesis, reference):
    return sacrebleu.sentence_bleu(hypothesis, [reference]).score

print(bleu("this is a test", "this is a test"))
