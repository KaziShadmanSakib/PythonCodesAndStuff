def computepay(hour,rate):
	if hour>40:
		reg = hour * rate
		otp = (hour-40.0) * (rate*0.5)
		total = reg + otp
	else:
		total = hour*rate
	return total
inputHour = input()
inputRate = input()
hour = float(inputHour)
rate = float(inputRate)
ans = computepay(hour,rate)
print("Pay",ans)