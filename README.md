# A Multi-Language Perspective on the Robustness of LLM Code Generation

This repository contains the replication package for the paper:
**"A Multi-Language Perspective on the Robustness of LLM Code Generation"**

It includes datasets, perturbation scripts, code generation scripts, evaluation scripts, and results for robustness evaluation of LLMs across Java, C++, and JavaScript.

---

## Repository Structure

```
robustextended/
├── datasets/                                   # Nominal and perturbed prompt datasets
│   ├── nominal/                                # Unperturbed prompts (code generation & completion)
│   └── perturbed/                              # Perturbed prompts organized by language and type
├── nlaugmenter/                                # DocString perturbation scripts (NL-Augmenter)
├── func_rename/                                # Function name perturbation scripts
├── natgen/                                     # Syntax perturbation scripts (NatGen)
├── format/                                     # Format perturbation scripts
├── preprocessing/                              # RQ3 docstring repair scripts
├── evalplus/                                   # EvalPlus-X test case adaptation scripts
├── rqs/                                        # Scripts for computing RQ1, RQ2, RQ3 metrics
├── results/                                    # Experimental results
├── annotations/                                # Human annotation data (naturalness & similarity)
├── sentence_sim/                               # Sentence similarity measurement scripts
├── CodeBLEU/                                   # CodeBLEU similarity measurement scripts
├── R/                                          # R scripts for statistical analysis
├── case_study/                                 # Case study examples
├── paper_samples/                              # Sample figures and examples from the paper
├── generate_perturbed_dataset.py               # Generate perturbed datasets
├── generate_single_code_single_gpu.py          # Run code generation on a single GPU
├── create_batch_scripts_all_in_one_file.py     # Create batch scripts for all experiments
├── run_robust.py                               # Compute robustness metrics
├── environment.yml                             # Conda environment specification
└── requirements.txt                            # Python dependencies
```

---

## Datasets

### Nominal Prompts

Located in [`datasets/nominal/`](https://github.com/frabbisw/robustextended/tree/main/datasets/nominal)

| File | Task | Language |
|------|------|----------|
| `humanevalcpp_nominal_f_s0.jsonl` | Code generation | C++ |
| `humanevaljava_nominal_f_s0.jsonl` | Code generation | Java |
| `humanevaljs_nominal_f_s0.jsonl` | Code generation | JavaScript |
| `humanevalcpp_partial_f_s0.jsonl` | Code completion | C++ |
| `humanevaljava_partial_f_s0.jsonl` | Code completion | Java |
| `humanevaljs_partial_f_s0.jsonl` | Code completion | JavaScript |

### Perturbed Prompts

Located in [`datasets/perturbed/`](https://github.com/frabbisw/robustextended/tree/main/datasets/perturbed)

Organized by language (`humanevalcpp`, `humanevaljava`, `humanevaljs`), task (`full` for code generation, `partial` for code completion), and perturbation type (`docstring`, `func_rename`, `syntax`, `format`).

Example path:
```
datasets/perturbed/humanevalcpp/full/format/humanevalcpp_new_line_aftercode_s1.jsonl
```

---

## Setup

```bash
conda env create -f environment.yml
conda activate robustextended
pip install -r requirements.txt
```

---

## Running Experiments

### Step 1: Generate batch scripts for all experiments

```bash
python create_batch_scripts_all_in_one_file.py
```

Batch scripts will be generated in the `batch_files/` folder.

### Step 2: Run a batch script for a specific experiment

```bash
bash batch_files/<experiment_batch_file>.sh
```

### Step 3 (Manual): Run code generation directly

**On nominal dataset — code generation:**
```bash
python generate_single_code_single_gpu.py \
  datasets/nominal/humaneval{lang}_nominal_f_s0.jsonl \
  datasets/{model_name}/generated_pass5_1/{lang}/nominal/ \
  {model_name}
```

**On nominal dataset — code completion:**
```bash
python generate_single_code_single_gpu.py \
  datasets/nominal/humaneval{lang}_partial_f_s0.jsonl \
  datasets/{model_name}/generated_pass5_1/{lang}/partial/ \
  {model_name}
```

**On perturbed dataset:**
```bash
python generate_single_code_single_gpu.py \
  datasets/perturbed/humaneval{lang}/full/{perturbation_type}/{perturbed_file}.jsonl \
  datasets/{model_name}/generated_pass5_1/{lang}/{perturbation_type}/ \
  {model_name}
```

Replace:
- `{lang}` with `cpp`, `java`, or `js`
- `{model_name}` with the model identifier (see supported models below)
- `{perturbation_type}` with the perturbation scope (`docstring`, `func_rename`, `syntax`, `format`)
- `{perturbed_file}` with the specific perturbed dataset filename

---

## Supported Models

| Model | Identifier |
|-------|-----------|
| InCoder 1B | `incoder-1b` |
| InCoder 6B | `incoder-6b` |
| CodeGen 2B Multi | `codegen-2b-multi` |
| CodeGen 6B Multi | `codegen-6b-multi` |
| Magicoder-S-DS 6.7B | `magicoder-s-ds-6.7b` |
| QwenCoder 2.5 7B | `qwencoder-2.5-7b` |

---

## Computing Robustness Metrics

Scripts for all three research questions are available in the `rqs/` folder.

**RQ1 — Cross-language robustness:**
```bash
python run_robust.py
```

**RQ2 — Feature-level analysis:** See scripts in `rqs/`

**RQ3 — Docstring repair:** See scripts in `preprocessing/`

---

## Perturbation Types

| Scope | Perturbation Types |
|-------|--------------------|
| DocString | BackTranslation, ButterFingersPerturbation, ChangeCharCase, EnglishInflectionalVariation, SwapCharactersPerturbation, SynonymInsertion, SynonymSubstitution, TenseTransformationFuture, TenseTransformationPast, WhitespacePerturbation |
| Function Name | ButterFinger, CamelCase/SnakeCase, ChangeChar, InflectionalVariation, SnakeCase/CamelCase, SwapChar, SynonymSubstitution |
| Syntax | DeadCodeInserter, ForWhileTransformer, OperandSwap, VarRenamerCB, VarRenamerNaive, VarRenamerRN |
| Format | doc2comments, new_line_aftercode, new_line_afterdoc, new_lines, split_lines, tab_indent |

---

## Citation

If you use this repository, please cite our paper:

```bibtex
@article{rabbi2024multilanguage,
  title={A Multi-Language Perspective on the Robustness of LLM Code Generation},
  author={Rabbi, Fazle and Ding, Zishuo and Yang, Jinqiu},
  journal={Empirical Software Engineering},
  year={2024}
}
```

---

## License

This project is licensed under the Apache 2.0 License. See [LICENSE](LICENSE) for details.
