# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.
import json
import pdb
import pickle
from tqdm import tqdm as tq
import os
import subprocess
import jsonlines
from collections import Counter
from os import listdir
from os.path import isfile, join

# -*- coding:utf-8 -*-
import argparse
import bleu
import weighted_ngram_match
import syntax_match
import dataflow_match

def load_codes(filename):
    prompts = {}
    with open(filename, encoding="utf8") as f:
        for line in f.readlines():
            prompt = json.loads(line)
            prompts[prompt["task_id"]] = prompt["prompt"]
    return prompts


# nominals = ["nominal", "partial"]
def load_partial_paths(lang):
    methods = ["natgen", "format"]
    # nominal_path = f"../datasets/nominal/HumanEval_{lang}.jsonl"
    partial_path = f"../datasets/nominal/humaneval{lang}_partial.jsonl"

    paths_dict = {}
    paths_dict["nominal"] = partial_path
    paths_dict["perturbed"] = []

    lang_dir = f"../datasets/perturbed/humaneval{lang}/full"

    for method in methods:
        method_dir = join(lang_dir, method)
        for filename in os.listdir(method_dir):
            if "s0.jsonl" in filename:
                perturbed_path = join(method_dir, filename)
                paths_dict["perturbed"].append(perturbed_path)
    return paths_dict

def load_partial_codes(paths_dict):
    perturbed_codes = {}
    nominal_codes = load_codes(paths_dict["nominal"])
    for key in nominal_codes.keys():
        perturbed_codes[key] = []

    for path in paths_dict["perturbed"]:
        contents = load_codes(path)
        for key in perturbed_codes.keys():
            perturbed_codes[key].append(contents[key])
    return nominal_codes, perturbed_codes

lang = "js"
paths_dict = load_partial_paths(lang)
nominal_codes, perturbed_codes = load_partial_codes(paths_dict)
lang = "javascript"
# for key in nominal_codes:
#     print(nominal_codes[key])
#     print(perturbed_codes[key])
#     print("*"*50)
#
# exit()

# print(nominal_codes.keys())
# exit()
# perturbed_dict = {}
# nominal_dict = {}


# parser = argparse.ArgumentParser()
# parser.add_argument('--refs', type=str, nargs='+', required=True,
#                         help='reference files')
# parser.add_argument('--hyp', type=str, required=True,
#                         help='hypothesis file')
# parser.add_argument('--lang', type=str, required=True,
#                         choices=['java','js','c_sharp','php','go','python','ruby','javascript'],
#                         help='programming language')
# parser.add_argument('--params', type=str, default='0.25,0.25,0.25,0.25',
#                         help='alpha, beta and gamma')

# args = parser.parse_args()

# lang = args.lang
# alpha,beta,gamma,theta = [float(x) for x in args.params.split(',')]

# preprocess inputs
# pre_references = [[x.strip() for x in open(file, 'r', encoding='utf-8').readlines()] \
#                 for file in args.refs]
# hypothesis = [x.strip() for x in open(args.hyp, 'r', encoding='utf-8').readlines()]

# print(nominal_codes.keys())
# exit()


# print(len(pre_references[0]))
# exit()
# print(type(pre_references[0]))
# exit()
# for i in pre_references:
#     print(i)
#
# exit()



syntax = []
dataflow = []

def get_score(task_id):
    alpha, beta, gamma, theta = 0.25, 0.25, 0.25, 0.25

    hypothesis = [x.strip() for x in nominal_codes[task_id].split("\n")]
    pre_references = [[x.strip() for x in contents.split("\n")] for contents in perturbed_codes[task_id]]

    max_length = max(len(p) for p in pre_references + [hypothesis])
    for i in range(len(pre_references)):
        #	assert len(hypothesis) == len(pre_references[i])
        if len(hypothesis) != len(pre_references[i]):
            # mx = max(len(pre_references[i]), len(hypothesis))
            pre_references[i] = pre_references[i] + ["//" for i in range(max_length - len(pre_references[i]))]
            hypothesis = hypothesis + ["//" for i in range(max_length - len(hypothesis))]
    references = []
    for i in range(len(hypothesis)):
        ref_for_instance = []
        for j in range(len(pre_references)):
            ref_for_instance.append(pre_references[j][i])
        references.append(ref_for_instance)

    syntax_match_score = syntax_match.corpus_syntax_match(references, hypothesis, lang)
    dataflow_match_score = dataflow_match.corpus_dataflow_match(references, hypothesis, lang)

    return syntax_match_score, dataflow_match_score

for task_id in nominal_codes.keys():
    try:
        syntax_match_score, dataflow_match_score = get_score(task_id)
        syntax.append(syntax_match_score)
        dataflow.append(dataflow_match_score)
    except:
        print("problem with:", task_id)

print(sum(syntax)/len(syntax))
print(sum(dataflow)/len(dataflow))

# for task_id in nominal_codes.keys():
#     try:
#         print(get_score(task_id))
#     except:
#         print(task_id)

# print(len(references), len(references[0]), len(pre_references), len(hypothesis))

# assert len(references) == len(pre_references)*len(hypothesis)


# calculate ngram match (BLEU)
# tokenized_hyps = [x.split() for x in hypothesis]
# tokenized_refs = [[x.split() for x in reference] for reference in references]
#
# ngram_match_score = bleu.corpus_bleu(tokenized_refs,tokenized_hyps)

# calculate weighted ngram match
# keywords = [x.strip() for x in open('keywords/'+lang+'.txt', 'r', encoding='utf-8').readlines()]
# def make_weights(reference_tokens, key_word_list):
#     return {token:1 if token in key_word_list else 0.2 \
#             for token in reference_tokens}
# tokenized_refs_with_weights = [[[reference_tokens, make_weights(reference_tokens, keywords)]\
#             for reference_tokens in reference] for reference in tokenized_refs]
#
# weighted_ngram_match_score = weighted_ngram_match.corpus_bleu(tokenized_refs_with_weights,tokenized_hyps)

# calculate syntax match
# syntax_match_score = syntax_match.corpus_syntax_match(references, hypothesis, lang)
#
# # calculate dataflow match
# dataflow_match_score = dataflow_match.corpus_dataflow_match(references, hypothesis, lang)

# print('ngram match: {0}, weighted ngram match: {1}, syntax_match: {2}, dataflow_match: {3}'.\
#                     format(ngram_match_score, weighted_ngram_match_score, syntax_match_score, dataflow_match_score))
#
# code_bleu_score = alpha*ngram_match_score\
#                 + beta*weighted_ngram_match_score\
#                 + gamma*syntax_match_score\
#                 + theta*dataflow_match_score
#
# print('CodeBLEU score: ', code_bleu_score)
#
# print(references)
# print(hypothesis)
#
#

