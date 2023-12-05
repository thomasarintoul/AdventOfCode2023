file = open('test_input3.txt', 'r')
schematics = []
part_numbers = []

for line in file:
    line = line.strip()
    schematics.append(line)

colNum = 0
linNum = 0
if schematics[linNum][colNum].isdigit() == True:
    start = 0
    colNum += 1
    while schematics[0][colNum].isdigit() == True:
        colNum += 1
    end = colNum - 1



