import numpy as np

file = open('input3.txt', 'r')
schematics = []
part_numbers = []

for line in file:
    line = line.strip()
    schematics.append(line+'.')

print(schematics)

nonSym = ['0','1','2','3','4','5','6','7','8','9','.']


for linNum in range(len(schematics)):
    colNum = 0
    # print(linNum)
    while colNum < len(schematics[linNum]):
        # print(schematics[linNum][colNum])
        # print(schematics[linNum][colNum].isdigit())
        if schematics[linNum][colNum].isdigit() == True:
            start = colNum
            colNum += 1
            while schematics[linNum][colNum].isdigit() == True:
                colNum += 1
            end = colNum-1

            include = 0
            # if linNum != 0:
            #     if start == 0 and end != len(schematics[linNum])-1:
            #         for entry in schematics[linNum - 1][start:end + 2]:
            #             if entry not in nonSym:
            #                 include = 1
            #     if end == len(schematics[linNum])-1 and start != 0:
            #         for entry in schematics[linNum - 1][start - 1:end]:
            #             if entry not in nonSym:
            #                 include = 1
            #     if end == len(schematics[linNum])-1 and start == 0:
            #         for entry in schematics[linNum - 1][start:end]:
            #             if entry not in nonSym:
            #                 include = 1
            #     else:
            #         for entry in schematics[linNum - 1][start-1:end+2]:
            #             if entry not in nonSym:
            #                 include = 1
            #
            # if linNum != len(schematics):
            #     # print('alpha')
            #     if start == 0 and end != len(schematics[linNum])-1:
            #         c = schematics[linNum+1][start:end+1]
            #         for entry in schematics[linNum + 1][start:end+2]:
            #             if entry not in nonSym:
            #                 include = 1
            #     if end == len(schematics[linNum])-1 and start != 0:
            #         for entry in schematics[linNum + 1][start-1:end]:
            #             if entry not in nonSym:
            #                 include = 1
            #     if end == len(schematics[linNum])-1 and start == 0:
            #         for entry in schematics[linNum + 1][start:end]:
            #             if entry not in nonSym:
            #                 include = 1
            #     if start != 0 and end != len(schematics[linNum]):
            #         # print('beta')
            #         for entry in schematics[linNum + 1][start-1:end+2]:
            #             if entry not in nonSym:
            #                 include = 1

            if linNum != 0:
                for entry in range(len(schematics[linNum-1])):
                    if schematics[linNum-1][entry] not in nonSym:
                        if start-1 <= entry <= end+1:
                            include = 1
            if linNum != len(schematics)-1:
                for entry in range(len(schematics[linNum])-1):
                    if schematics[linNum+1][entry] not in nonSym:
                        if start-1 <= entry <= end+1:
                            include = 1

            if start != 0:
                if schematics[linNum][start-1] not in nonSym:
                    include = 1
            if end != len(schematics[linNum]):
                if schematics[linNum][end+1] not in nonSym:
                    include = 1
            if include == 1:
                part_numbers.append(schematics[linNum][start:end+1])
        else:
            colNum += 1

print(part_numbers)
for i in range(len(part_numbers)):
    part_numbers[i] = int(part_numbers[i])

print(np.sum(part_numbers))




