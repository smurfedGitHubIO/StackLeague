def pyramid_slide_down(pyramid):
	if len(pyramid) == 1:
		return pyramid[0][0]
	ans = 0
	for i in range(1,len(pyramid)):
		for j in range(len(pyramid[i])):
			if j == 0:
				pyramid[i][j] += pyramid[i-1][j]
			elif j == len(pyramid[i])-1:
				pyramid[i][j] += pyramid[i-1][j-1]
			else:
				pyramid[i][j] += max(pyramid[i-1][j-1],pyramid[i-1][j])
			if i == len(pyramid)-1:
				ans = max(ans,pyramid[i][j])
	return ans