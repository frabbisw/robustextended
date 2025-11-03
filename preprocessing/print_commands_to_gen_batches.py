langs = ["cpp", "java", "js"]
parts = [1,2,3,4,5]
gpu = 0
tm = "24:00:00"

for lang in langs:
    for part in parts:
        print(f"python create_batch_files.py {lang} {part} {tm} {gpu}")
