def word_to_number(string):
	string = string.lower()
	ones = ['','one','two','three','four','five','six','seven','eight','nine']
	tens = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
	tenu = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
	others = ['hundred','thousand','million']
	lst = string.split()
	for i in string:
		if i.isnumeric():
			return 'Input not a string'
	for i in range(len(lst)):
		q = lst[i]
		if '-' in q and q != '-':
			s = lst[i][:q.index('-')]
			e = lst[i][q.index('-')+1:]
			if s not in tenu:
				return 'Input not a string'
			if e not in ones:
				return 'Input not a string'
		elif (lst[i] == '-' and (lst[i-1] not in tenu or lst[i+1] not in ones)):
			return 'Input not a string'
		elif (lst[i] not in ones and lst[i] not in tens and lst[i] not in tenu and lst[i] not in others and lst[i] != 'and' and lst[i] != '-'):
			return 'Input not a string'
	qlst = []
	for i in range(len(lst)):
		q = lst[i]
		if '-' in q and q != '-':
			s = lst[i][:q.index('-')]
			e = lst[i][q.index('-')+1:]
			qlst += [s,e]
		elif lst[i] != 'and' and q != '-':
			qlst.append(lst[i])
	proc, ans = 0, 0
	for i in range(len(qlst)):
		if qlst[i] == 'and':
			continue
		if qlst[i] in ones:
			proc += ones.index(qlst[i])
		if qlst[i] == 'million':
			ans += proc*(10**6)
			proc = 0
		if qlst[i] == 'thousand':
			ans += proc*(10**3)
			proc = 0
		if qlst[i] == 'hundred':
			proc *= 100
		if qlst[i] in tenu:
			proc += (tenu.index(qlst[i])+2)*10
		if qlst[i] in tens:
			ans += (tens.index(qlst[i])+10)
	ans += proc
	return ans

word = 'four hundred and five'
word = 'FiFty - FouR miLLION and thirty-three thousand FiftY'
word = 'one billion'
word = 'Forty - thousand'
print(word_to_number(word))
