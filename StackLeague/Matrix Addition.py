def matrix_addition(a, b):
	for i in range(len(a)):
		for j in range(len(a[0])):
			a[i][j] += b[i][j]
	return a