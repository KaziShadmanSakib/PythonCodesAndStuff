import os
import re
print("My current Directory is:",os.getcwd())
print()
os.chdir("/home/betmon69/Downloads")
print("After changing Directory:",os.getcwd())
print()
listOfFolders = os.listdir()
count = 0
for ffName in listOfFolders:
	if re.search("^The.Flash.+S04",ffName):
		count = count + 1
print("Total Flash Episodes:",count)
print()
fileCount = 0
fileList = list()
for ffName in listOfFolders:
	if re.search("^The.Flash.+S04",ffName):
		fileCount = fileCount + 1
		fileList.append(ffName)
		print(ffName)
print()
print("Total Flash Episodes After Writing Episode Names:",fileCount)
print()
i=0
j=1
episodeCount = 0
for i in range(len(fileList)):
	for j in range(len(fileList)):
		fileName1 = re.findall("(S04E[0-9]+)",fileList[i])
		fileName2 = re.findall("(S04E[0-9]+)",fileList[j])
		if fileName1 < fileName2:
			temp = fileList[i]
			fileList[i] = fileList[j]
			fileList[j] = temp
print("After sorting episode by episode we get:")
print()
totalFlash = 0
for flash in fileList:
	totalFlash = totalFlash + 1
	print(flash)
print()
print("Finally I am clear that in Flash Season 4 we have total episodes:",totalFlash)
print()
	

