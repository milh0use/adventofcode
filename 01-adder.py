import re

result = 0
with open('data/01-inputdata.txt') as f:
    for line in f:
        line = re.sub("^\+","",line)
        if re.match("^\s$",line):
            break
        result = result + int(line)

print(result)