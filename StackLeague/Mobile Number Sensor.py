def mobile_number_censor(number):
	if number[0] == '0' and number[1] == '9' and len(number) == 11:
		return number[0:2] + '*'*5 + number[7:11]
	if number[0:4] == '+639' and len(number) == 13:
		return number[0:4] + '*'*5 + number[9:13]
	return None