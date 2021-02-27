inputFileName = input()
handle = open(inputFileName)
for line in handle:
	printLine = line.rstrip()
	mainLinePrint = printLine.upper()
	print(mainLinePrint)
