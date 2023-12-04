import numpy as np

input = np.loadtxt('input.txt', dtype='str')

# # PART 1 - Only real digits
print('Part 1')

calibration = []

for i in input:
    digits = ''
    for j in i:
        if j.isdigit():
            digits += j
    if len(digits) > 0:
        entry = int(digits[0] + digits[-1])
        calibration.append(entry)

print('Calibration:', np.sum(calibration))


# PART 2 - Numbers count as digits
print('Part 2')

# numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
# # numbers = ['nine', 'eight', 'seven', 'six', 'five', 'four', 'three', 'two', 'one']
# digit_list = [1,2,3,4,5,6,7,8,9]
# # digit_list = [9,8,7,6,5,4,3,2,1]
#
# test_array = np.array([
#     ['1',-1], ['2',-1], ['3',-1], ['4',-1], ['5',-1], ['6',-1], ['7',-1], ['8',-1], ['9',-1],
#     ['one',-1], ['two',-1], ['three',-1], ['four',-1], ['five',-1], ['six',-1], ['seven',-1], ['eight',-1], ['nine', -1]
# ], dtype=object)

# print(test_array)

# for q in range(len(input)):
#     test_array = np.array([
#         ['1', -1], ['2', -1], ['3', -1], ['4', -1], ['5', -1], ['6', -1], ['7', -1], ['8', -1], ['9', -1],
#         ['one', -1], ['two', -1], ['three', -1], ['four', -1], ['five', -1], ['six', -1], ['seven', -1], ['eight', -1],
#         ['nine', -1]
#     ], dtype=object)
#     test_string = 0
#     current_array = 0
#     digit_index = 0
#     sorted_indices = 0
#     mask = 0
#     final_num = 0
#     test_string = input[q]
#     current_array = test_array
#     for i in range(len(current_array[:,0])):
#         a = current_array[i,0]
#         if test_string.find(str(current_array[i,0])) >= 0:
#             index = test_string.index(str(current_array[i,0]))
#             current_array[i,1] = index
#
#     mask = current_array[:,1] != -1
#     current_array = current_array[mask]
#     sorted_indices = np.argsort(current_array[:, 1]).astype(int)
#     current_array = current_array[sorted_indices]
#
#     for k in range(len(current_array[:,0])):
#         if len(current_array[k,0]) > 1:
#             digit_index = np.where(test_array == current_array[k,0])[0]
#             current_array[k,0] = test_array[int(digit_index) - 9,0]
#
#     final_num = current_array[0,0] + current_array[-1,0]
#
#     input[q] = final_num

# print(input)



# calibration = []
#
# for i in input:
#     digits = ''
#     for j in i:
#         if j.isdigit():
#             digits += j
#     if len(digits) > 0:
#         entry = int(digits[0] + digits[-1])
#         calibration.append(entry)
# print(calibration)
# print('Calibration:', np.sum(calibration))


import os,sys

with open(os.path.join(sys.path[0], "input.txt"), "r", encoding="utf-8") as f:
    lines = f.read().splitlines(keepends=False)
result = 0
digits = { "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

for line in lines:
    first, last = None, None
    for i,c in enumerate(line):
        if c.isdigit():
            if first is None:
                first = int(c)
            last = int(c)
        else:
            if i < len(line) - 2 and line[i:i+3] in digits:
                if first is None:
                    first = digits[line[i:i+3]]
                last = digits[line[i:i+3]]
                continue
            if i < len(line) - 3 and line[i:i+4] in digits:
                if first is None:
                    first = digits[line[i:i+4]]
                last = digits[line[i:i+4]]
                continue
            if i < len(line) - 4 and line[i:i+5] in digits:
                if first is None:
                    first = digits[line[i:i+5]]
                last = digits[line[i:i+5]]
                continue
    result += first*10 + last
print(result)