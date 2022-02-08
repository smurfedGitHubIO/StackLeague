def draw_eye(value):
	ans = ''
	for i in range(value+1):
		if i == 0 or i == value:
			ans += '.'*value + '#'*value + '.'*value + ('\n' if i != value else '')
		elif i < (value+1)//2:
			ans += '.'*(value-i*2) + '#'*2 + '.'*((i-1)*2) + '#' + '.'*(value-2) + '#' + '.'*((i-1)*2) + '#'*2 + '.'*(value-i*2) + '\n'
		else:
			ans += '.'*(2*((i-(value+1)//2)+1)-1)  + '#'*2 + '.'*((value-i-1)*2) + '#' + '.'*(value-2) + '#' + '.'*((value-i-1)*2) + '#'*2 + '.'*(2*((i-(value+1)//2)+1)-1) + '\n'
	return ans