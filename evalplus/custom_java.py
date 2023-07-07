with open("/home/frabbi/Desktop/evalplusdata/java/Java133/Main.java", "r") as f:
    lines = f.readlines()

bb = "System.out.print(s.sumSquares(new ArrayList<>(Arrays.asList("
ee = "))));"
mm = ")), new ArrayList<>(Arrays.asList("
extra = "\t\tSystem.out.print(\"#\");\n"

modified = []

for i in range(len(lines)):
    line = lines[i]
    if extra in line:
        continue
    m=""
    if bb in line:
        m = line.replace(bb, "").replace(ee, "")
        # print(m)
    if "\"" in m or "." in m:
        modified.append(line)
        # continue
    else:
        # print(line)
        # modified.append(line)
        continue

modified = ''.join(modified)

# with open("/home/frabbi/Desktop/evalplusdata/java/Java34/Main.java", "w") as f:
#     lines = f.readlines()

print(modified)