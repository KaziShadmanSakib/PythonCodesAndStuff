inputFileName = input()
handle = open(inputFileName)
count = 0.0
total = 0.0
for line in handle:
	if not line.startswith("X-DSPAM-Confidence:"):
		continue
	else:
		count = count + 1
		pos = line.find(":")
		stringOfNumber = line[pos+1:]
		total = total + float(stringOfNumber.lstrip())
average = (total/count)
print("Average spam confidence:",average)