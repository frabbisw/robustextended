with open("/home/frabbi/Desktop/evalplusdata/cpp/CPP58/main.cpp", "r") as f:
    lines = f.readlines()

bb = "cout << toString(common({"
ee = "}));"
mm = "}, {"
# extra = "\t\tSystem.out.print(\"#\");\n"

modified = []

for i in range(len(lines)):
    line = lines[i]
    m=""
    if bb in line:
        m = line.replace(bb, "").replace(ee, "").replace(mm,", ")
        # print(m)
    # if "\"" in m or "." in m:
        # modified.append(line)
    if "\"" in m or "." in m:
        continue
    else:
        # print(line)
        modified.append(line)
        # continue

modified = ''.join(modified)

# with open("/home/frabbi/Desktop/evalplusdata/java/Java34/Main.java", "w") as f:
#     lines = f.readlines()

print(modified)