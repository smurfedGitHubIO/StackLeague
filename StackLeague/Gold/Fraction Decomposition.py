import math

def decompose(n):
    lst = []
    ans = []
    if '.' in n:
        q = n.split('.')
        if len(q) > 2:
            return []
        x = len(q[1])
        if str(q[0]) != '0':
            ans.append(str(q[0]))
        gc = math.gcd(int(q[1]),10**x)
        n = str(int(q[1])//gc)+'/'+str((10**x)//gc)
    lst = n.split('/')
    if lst[0] == '0':
        return []
    elif len(lst) == 1:
        return lst
    elif len(lst) == 2 and lst[1] == '0':
        return 'Not a valid input'
    lst[0], lst[1] = int(lst[0]), int(lst[1])
    while True:
        if lst[0] == 0:
            return []
        if lst[1]%lst[0] == 0 and lst[1] != lst[0]:
            ans.append('1/'+str(lst[1]//lst[0]))
            break
        if lst[0]%lst[1] == 0:
            ans.append(str(lst[0]//lst[1]))
            break
        if lst[0] > lst[1]:
            ans.append(str(lst[0]//lst[1]))
            lst = [lst[0]%lst[1], lst[1]]
        else:
            n = lst[1]//lst[0] + 1
            ans.append('1/' + str(n))
            lst = [lst[0]*n-lst[1],lst[1]*n]
    return ans

def is_numeric(n):
    try:
        f = Fraction(n)
    except Exception:
        raise ValueError('Not a valid input')
        return False
    return True