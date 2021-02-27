largeNumber = None
smallNumber = None
while True:
	inputX = input()
	try: 
		x = int(inputX)
	except:
		if inputX == "done":
			break
		else:
			print("Invalid input")
	if largeNumber is None and smallNumber is None:
		largeNumber = x
		smallNumber = x
	elif largeNumber<x:
		largeNumber = x
	elif smallNumber>x:
		smallNumber = x
print("Maximum is",largeNumber)
print("Minimum is",smallNumber)
