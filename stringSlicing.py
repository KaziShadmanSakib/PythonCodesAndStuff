string = "X-DSPAM-Confidence: 0.8475"
pos = string.find(":")
result = string[pos+1:]
print(float(result.lstrip()))
