##def permutations(string):
##    if len(string) == 0:
##        return []
##    if len(string) == 1:
##        return [string]
##    lst = []
##    for i in range(len(string)):
##        k = string[i]
##        qt = string[:i] + string[i+1:]
##        for j in permutations(qt):
##            lst.append(k+j)
####    for i in range(len(lst)):
####        lst[i] = ''.join(lst[i])
##    return lst
##
##print(permutations('aabb'))




