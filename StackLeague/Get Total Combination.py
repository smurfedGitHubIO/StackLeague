def get_total_combination(money,coins, lst = []):
	if money == 0:
		return 1
	ans = 0
	for i in sorted(coins):
		if money >= i and len(lst) == 0:
			ans += get_total_combination(money-i,coins,lst+[i])
		elif money >= i and lst[-1] >= i:
			ans += get_total_combination(money-i,coins,lst+[i])
	return ans