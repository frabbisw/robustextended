#for the code generation model
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers import GPTJForCausalLM
import torch

device = "cuda:0" if torch.cuda.is_available() else "cpu"
#models_dict = {"codegen6bmulti": "Salesforce/codegen-6B-multi", "codegen2bmulti": "Salesforce/codegen-2B-multi", "incoder1b": "facebook/incoder-1B", "incoder6b": "facebook/incoder-6B", "magicoder7b": "ise-uiuc/Magicoder-S-DS-6.7B"}
models_dict = {"codegen6bmulti": "/home/f_rabbi/models/codegen-6B-multi", "magicoder7b": "/home/f_rabbi/code_trans/models/Magicoder-S-DS-6.7B"}

# checkpoint = models_dict[sys.argv[1]]
checkpoint = models_dict["codegen6bmulti"]

code_generaton_model = AutoModelForCausalLM.from_pretrained(checkpoint, torch_dtype=torch.bfloat16).to(device)
code_generaton_tokenizer = AutoTokenizer.from_pretrained(checkpoint)
# device_map = infer_auto_device_map(model, no_split_module_classes=["OPTDecoderLayer"])

def prompt_to_code(prompt):
    completion = code_generaton_model.generate(**code_generaton_tokenizer(prompt, return_tensors="pt").to(device), max_length=1536,temperature=0.2,top_p=0.95,do_sample = True)
    code = code_generaton_tokenizer.decode(completion[0])
    return code

prompt = '''
# C++
#include <iostream>
#include <vector>
#include <string>
using namespace std;

int lcs(const string &a, const string &b) {
    int n = a.size(), m = b.size();
    vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));

    for (int i = n - 1; i >= 0; i--) {
        for (int j = m - 1; j >= 0; j--) {
            if (a[i] == b[j]) {
                dp[i][j] = 1 + dp[i + 1][j + 1];
            } else {
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1]);
            }
        }
    }
    return dp[0][0];
}

#Python
def lcs(a, b):
'''

# cpp_code = prompt_to_code(prompt)

buggy_prompt = '''
// buggy code
/**
 * @brief Computes the average of an array of integers.
 * 
 * This function should take an array of integers and its size,
 * and return their arithmetic mean as a double.
 */
double average(const int arr[], int size) {
    // BUG: forgot to divide by size, returns sum instead
    double sum = 0.0;
    for (int i = 0; i < size; i++) {
        sum += arr[i];
    }
    return sum; // Wrong: should return sum / size
}
// fixed code
double average(const int arr[], int size) {
'''

print(cpp_code)
