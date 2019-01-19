frequency_change_list = []
with open('data/01-inputdata.txt') as f:
    frequency_change_list = [int(line) for line in f]

dupe_check = {}
result = 0
duplicate_found = False

while not duplicate_found:
    for num in frequency_change_list:
        result += num
        if result in dupe_check:
            print("Frequency ", result, " has been seen twice")
            duplicate_found = True
            break
        else:
            dupe_check[result] = 1

print("Frequency ",result," has been seen twice")