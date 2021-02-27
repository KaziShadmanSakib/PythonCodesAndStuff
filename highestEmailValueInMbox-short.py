fileName = input()
handle = open(fileName)
emailList = list()
count = dict()
for line in handle:
	if line.startswith("From "):
		email = line.split()
		emailList.append(email[1])
	elif line.startswith("From: "):
		continue
for email in emailList:
	count[email] = count.get(email,0) + 1
highestEmailValue = None
highestEmail = None
for email,value in count.items():
	if highestEmailValue is None and highestEmail is None:
		highestEmailValue = value
		highestEmail = email
	elif value > highestEmailValue:
		highestEmailValue = value
		highestEmail = email
print(highestEmail,highestEmailValue)