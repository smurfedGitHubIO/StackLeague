##def find_missing_number(a):
##    ans = ((len(a)+1)*(len(a)+2))//2
##    for i in a:
##        ans -= i
##    return ans
##print(find_missing_number([1,3,4]))
##print(find_missing_number([1,2,3]))
##print(find_missing_number([4,2,3]))

##def decomp(n):
##    ans = []
##    for i in range(2,n+1):
##        for j in get_prime_factors(i):
##            ans.append(j)
##    ans.sort()
##    dct = {}
##    for k in ans:
##        if k not in dct:
##            dct[k] = 1
##        else:
##            dct[k] += 1
##    lst = []
##    for i, j in dct.items():
##        lst.append(str(i) + ('' if j == 1 else '^' + str(j)))
##    return ' * '.join(lst)
##    
##def get_prime_factors(n):
##    lst, i = [], 2
##    while i*i <= n:
##        if n%i == 0:
##            while n%i == 0:
##                n /= i
##                lst.append(i)
##        i += 1
##    if n != 1:
##        lst.append(n)
##    return lst
##
##print(decomp(25))

##def nb_year(population, percent, additional, target):
##    ans = 0
##    while population < target:
##        population = int(population*(1.00+(percent*0.01))) + additional
##        ans += 1
##    return ans
##
##print(nb_year(1500,5,100,5000))
##print(nb_year(1500000,2.5,10000,2000000))

class ProtossProblem:

    def __init__(self, zealot_grid):
        self.zealot_grid = zealot_grid

    def get_most_hyper_connections(self):
        x = len(self.zealot_grid)
        adjlist = [[] for i in range(x)]
        ans = 0
        for i in range(x):
            for j in range(x):
                if self.zealot_grid[i][j] == 'Y' and self.zealot_grid[j][i] == 'Y':
                    self.zealot_grid[i][j] = self.zealot_grid[j][i] = 'N'
                    adjlist[i].append(j)
                    adjlist[j].append(i)
        check = [False]*x
        for i in range(x):
            if not check[i]:
                cur = 0
                newlst = [i]
                check[i] = True
                while len(newlst) != 0:
                    tp = newlst[0]
                    del newlst[0]
                    for k in adjlist[tp]:
                        if not check[k]:
                            cur += 1
                            check[k] = True
                            newlst.append(k)
                ans = max(ans,cur)
        return ans
p = ProtossProblem([["N", "Y", "N"],["Y", "N", "N"],["N", "Y", "N"]])
print(p.get_most_hyper_connections())
p = ProtossProblem([["N", "Y", "Y"],["Y", "N", "Y"],["Y", "Y", "N"]])
print(p.get_most_hyper_connections())
