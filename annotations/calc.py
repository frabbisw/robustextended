def cal_avg(filename):
    p, n , s = 0, 0, 0
    total = {"Perturbed":0, "Nominal": 0, "Semantic": 0}
    problems = {"Perturbed":0, "Nominal": 0, "Semantic": 0}
    with open(filename, "r") as f:
        lines = f.read().split("\n")
        for line in lines:
            for t in total:
                if t in line:
                    try:
                        total[t] += (float(line.split(":")[-1].strip()))
                        # print("*",total[t], line,"*")
                    except:
                        # print(line)
                        problems[t] += 1
    # print(total)
    return  round(total["Perturbed"]/(100-problems["Perturbed"]),2), round(total["Nominal"]/(100-problems["Nominal"]),2), round(total["Semantic"]/(100-problems["Semantic"]),2)

print(cal_avg("cpp.txt"))
print(cal_avg("java.txt"))
print(cal_avg("js.txt"))