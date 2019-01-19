ids_with_two_chars = 0
ids_with_three_chars = 0

with open("data/02-inputdata.txt") as f:
    box_ids = [line for line in f]
    for box_id in box_ids:
        letter_counts = {}
        has_two_chars = False
        has_three_chars = False
        for i in range(len(box_id)):
            if box_id[i] in letter_counts:
                letter_counts[box_id[i]] += 1
            else:
                letter_counts[box_id[i]] = 1
        for letter in letter_counts:
            if letter_counts[letter] == 2:
                has_two_chars = True
            elif letter_counts[letter] == 3:
                has_three_chars = True
        if has_two_chars:
            ids_with_two_chars += 1
        if has_three_chars:
            ids_with_three_chars += 1

checksum = ids_with_two_chars * ids_with_three_chars
print("Checksum = ", checksum)