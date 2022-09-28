process = []
spell = ["q", "u", "a", "c", "k"]

sound = list(input())
result = -1

for s in sound:
    if s == "q":
        if process.count("k") > 0:
            process[process.index("k")] = s
        else:
            process.append("q")
    else:
        pre = spell[spell.index(s) - 1]
        if process.count(pre) > 0:
            process[process.index(pre)] = s
    # print(s, process)

if process.count("k") == len(process):
    result = process.count("k")
print(result)
