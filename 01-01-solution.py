result = 0
with open('data/01-inputdata.txt') as f:
    frequency_change = [int(line) for line in f]
    result = sum(frequency_change)

print(result)