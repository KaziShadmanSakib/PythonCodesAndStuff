inputFileName = input()
handle = open(inputFileName)
numList = list()
for line in handle:
	lineSplit = line.split()
	i = 0
	while i < len(lineSplit):
		if lineSplit[i] not in numList:
			numList.append(lineSplit[i])
			i = i+1
		else: 
			i = i+1
numList.sort()
print(numList)