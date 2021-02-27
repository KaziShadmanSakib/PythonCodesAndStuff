fileName = input()
handle = open(fileName)
hourList = list()
for line in handle:
	if line.startswith("From "):
		time = line.split()
		hour = time[5].split(":")
		hourList.append(hour[0])
	elif line.startswith("From:"):
		continue
hourDic = dict()
for hour in hourList:
	hourDic[hour] = hourDic.get(hour,0) + 1
temp = list()
#Could have been done like this also:
#temp = sorted([(k,v) for k,v in hourDic.items()])
for key,value in hourDic.items():
	newTup = (key,value)
	temp.append(newTup)
temp = sorted(temp)
for key,value in temp:
	print(key,value)
