data <- read.csv("stat.csv")
data = data[c("passed", "assertion", "compilation", "timeout", "runtime")]

# doc_data <- data[c(1, 3), ]
# doc_result <- fisher.test(doc_data)
# print("DocString: ", doc_result$p.value)
#
# func_data <- data[c(1, 6), ]
# func_result <- fisher.test(func_data)
# print("Function: ", func_result$p.value)
#
# synt_data <- data[c(1, 6), ]
# synt_result <- fisher.test(synt_data)
# print("Syntax: ", synt_result$p.value)
#
# form_data <- data[c(1, 6), ]
# form_result <- fisher.test(form_data)
# print("Syntax: ", form_result$p.value)

for (i in 0:1) {
  for (j in 0:2) {
    row_num = i*18 + j*6
    doc_data <- data[c(row_num+1, row_num+3), ]
    doc_result <- fisher.test(doc_data)
    # print("DocString: ", doc_result$p.value)
    print(doc_result$p.value)

    func_data <- data[c(row_num+1, row_num+6), ]
    func_result <- fisher.test(func_data)
    # print("Function: ", func_result$p.value)
    print(func_result$p.value)

    synt_data <- data[c(row_num+2, row_num+4), ]
    synt_result <- fisher.test(synt_data)
    # print("Syntax: ", synt_result$p.value)
    print(synt_result$p.value)

    form_data <- data[c(row_num+2, row_num+5), ]
    form_result <- fisher.test(form_data)
    # print("Syntax: ", form_result$p.value)
    print(form_result$p.value)
    cat("end of lang ",  j, "\n")
  }
  cat("end of model ", i, "\n")
}