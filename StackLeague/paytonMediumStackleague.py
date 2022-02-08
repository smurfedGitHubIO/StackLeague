def moving_shift(string, shift):
	divider = len(string)//5 + (1 if len(string)%5 != 0 else 0)
	lst = []
	i, cnt = 0, shift
	for j in range(1,5):
		ans = ''
		while i < divider*j:
			if string[i].isalpha():
				print(string[i], divider, j)
				if string[i].isupper():
					ans += chr((ord(string[i])+cnt-65)%26 + 65)
				else:
					ans += chr((ord(string[i])+cnt-97)%26 + 97)
				cnt+=1
			else:
			    ans += string[i]
			i += 1
		print(ans)
		lst.append(ans)
	if i < len(string):
		while i < len(string):
			if string[i].isalpha():
				if string[i].isupper():
					ans += chr((ord(string[i])+cnt-65)%26 + 65)
				else:
					ans += chr((ord(string[i])+cnt-97)%26 + 97)
				cnt+=1
			else:
				ans += string[i]
			i += 1
		lst.append(ans)
	return lst

def demoving_shift(string,shift):
	shift = 26-shift
	string = ''.join(x for x in string)
	print(string)
	divider = len(string)//5 + (1 if len(string)%5 != 0 else 0)
	lst = []
	i, cnt = 0, shift
	for j in range(1,5):
		ans = ''
		while i < divider*j:
			if string[i].isalpha():
				print(string[i], divider, j)
				if string[i].isupper():
					ans += chr((ord(string[i])+cnt-65)%26 + 65)
				else:
					ans += chr((ord(string[i])+cnt-97)%26 + 97)
				cnt-=1
			else:
			    ans += string[i]
			i += 1
		print(ans)
		lst.append(ans)
	if i < len(string):
		while i < len(string):
			if string[i].isalpha():
				if string[i].isupper():
					ans += chr((ord(string[i])+cnt-65)%26 + 65)
				else:
					ans += chr((ord(string[i])+cnt-97)%26 + 97)
				cnt-=1
			else:
				ans += string[i]
			i += 1
		lst.append(ans)
	return (''.join(x for x in lst))

def moving_shift(string, shift):
	divider = len(string)//5 + (1 if len(string)%5 != 0 else 0)
	lst = []
	i, cnt = 0, shift
	for j in range(1,5):
		ans = ''
		while i < divider*j:
			if string[i].isalpha():
				if string[i].isupper():
					ans += chr((ord(string[i])+cnt-65)%26 + 65)
				else:
					ans += chr((ord(string[i])+cnt-97)%26 + 97)
				cnt %= 26
			else:
			    ans += string[i]
			i += 1
			cnt += 1
		lst.append(ans)
	ans = ''
	if i < len(string):
		while i < len(string):
			if string[i].isalpha():
				if string[i].isupper():
					ans += chr((ord(string[i])+cnt-65)%26 + 65)
				else:
					ans += chr((ord(string[i])+cnt-97)%26 + 97)
			else:
				ans += string[i]
			i += 1
			cnt += 1
		lst.append(ans)
	else:
	    lst.append('')
	return lst

def demoving_shift(string,shift):
	shift = 26-shift
	string = ''.join(x for x in string)
	divider = len(string)//5 + (1 if len(string)%5 != 0 else 0)
	lst = []
	i, cnt = 0, shift
	for j in range(1,5):
		ans = ''
		while i < divider*j:
			if string[i].isalpha():
				if string[i].isupper():
					ans += chr((ord(string[i])+cnt-65)%26 + 65)
				else:
					ans += chr((ord(string[i])+cnt-97)%26 + 97)
			else:
			    ans += string[i]
			i += 1
			cnt -= 1
		lst.append(ans)
	ans = ''
	if i < len(string):
		while i < len(string):
			if string[i].isalpha():
				if string[i].isupper():
					ans += chr((ord(string[i])+cnt-65)%26 + 65)
				else:
					ans += chr((ord(string[i])+cnt-97)%26 + 97)
			else:
				ans += string[i]
			i += 1
			cnt -= 1
		lst.append(ans)
	return (''.join(x for x in lst))

def parse_molecule(formula):
	dct = {}
	st, i = '', 0
	while i < len(formula):
		if formula[i].isdigit():
			if i+1 < len(formula):
				if formula[i+1].isdigit():
					dct[st] += int(formula[i:i+2]) - 1
					i += 1
				else:
					dct[st] += int(formula[i]) - 1
			else:
				dct[st] += int(formula[i])-1
		elif formula[i] in [')',']','}']:
			return [i+1,dct]
		elif formula[i] in ['(','[','{']:
			tmp = parse_molecule(formula[i+1:])
			i += tmp[0]
			if i+1 < len(formula):
				if formula[i+1].isdigit():
					i += 1
					for k,j in tmp[1].items():
						tmp[1][k] = j*int(formula[i])
			for k in tmp[1]:
				if k in dct:
					dct[k] += tmp[1][k]
				else:
					dct[k] = tmp[1][k]
		else:
			if formula[i].isupper():
				if i+1 < len(formula):
					if formula[i+1].islower():
						if formula[i:i+2] in dct:
							dct[formula[i:i+2]] += 1
							st = formula[i:i+2]
							i += 1
						else:
							dct[formula[i:i+2]] = 1
							st = formula[i:i+2]
					else:
						if formula[i] in dct:
							dct[formula[i]] = 1
							st = formula[i]
						else:
							dct[formula[i]] = 1
							st = formula[i]
				else:
					if formula[i] in dct:
						dct[formula[i]] = 1
						st = formula[i]
					else:
						dct[formula[i]] = 1
						st = formula[i]
		i += 1
	return dct
