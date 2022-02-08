def dbl_linear(n):
	lst = [1]
	a, b = 0, 0
	for i in range(1,n+1):
		lst.append(min(2*lst[a]+1,3*lst[b]+1))
		if lst[i] == 2*lst[a]+1:
			a += 1
		if lst[i] == 3*lst[b]+1:
			b += 1
	return lst[n]