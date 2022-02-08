def find_emirp(n):
    sums, mx, cnt = 0, 0, 0
    for j in range(13,n):
        sj = str(j)
        qj = int(sj[::-1])
        check1, check2 = True, True
        i, k = 2, 2
        while i*i <= j:
            if j%i == 0:
                check1 = False
                break
            i += 1
        while k*k <= qj:
            if qj%k == 0:
                check2 = False
                break
            k += 1
        if check1 and check2 and j != qj:
            sums += j
            mx = max(mx,j)
            cnt += 1
    return [cnt,mx,sums]
print(find_emirp(200))