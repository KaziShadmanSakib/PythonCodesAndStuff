inputFileName = input()
handle = open(inputFileName)
numList = list()
count = 0
for line in handle:
	if line.startswith("From "):
		emailList = line.split()
		numList.append(emailList[1])
		count = count + 1
	elif line.startswith("From:"):
		continue
for i in range(len(numList)):
	print(numList[i])
print("There were",count,"lines in the file with From as the first word")