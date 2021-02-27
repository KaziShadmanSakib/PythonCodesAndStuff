import re
fileName = input()
handle = open(fileName)
numDic = dict()
for line in handle:
	numbers = re.findall('[0-9]+',line)
	for number in numbers:
		numDic[number] = numDic.get(number,0)+1
total = 0
for key,value in numDic.items():
	totalTimes = int(key) * value
	total = total + totalTimes
print(total)