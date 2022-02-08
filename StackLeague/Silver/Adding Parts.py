def part_sums(ls):
    cur = 0
    ans = []
    for i in range(len(ls)):
        cur += ls[i]
    ans.append(cur)
    for i in range(len(ls)):
        cur -= ls[i]
        ans.append(cur)
    return ans
