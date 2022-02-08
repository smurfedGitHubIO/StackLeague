def persistence(n):
	ans = 0
	while n >= 10:
		q = 1
		while n > 0:
			q *= n%10
			n //= 10
		n = q
		ans+=1
	return ans