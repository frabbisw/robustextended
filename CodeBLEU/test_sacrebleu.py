from sacrebleu.metrics import BLEU, CHRF, TER
refs = [['The dog bit the man.', 'It was not unexpected.', 'The man bit him first.'],
        ['The dog had bit the man.', 'No one was surprised.', 'The man had bitten the dog.'],]
sys = ['The dog bit the man.', "It wasn't surprising.", 'The man had just bitten him.']

bleu = BLEU()

print(bleu.corpus_score(sys, refs))
# Out[3]: BLEU = 48.53 82.4/50.0/45.5/37.5 (BP = 0.943 ratio = 0.944 hyp_len = 17 ref_len = 18)

print(bleu.get_signature())
# Out[4]: nrefs:2|case:mixed|eff:no|tok:13a|smooth:exp|version:2.0.0

chrf = CHRF()

print(chrf.corpus_score(sys, refs))
# Out[6]: chrF2 = 59.73