def modpow(b, p):
    if p == 0:
        return 1
    if p == 1:
        return b
    x = modpow((b*b)%59, p>>1)
    if p&1:
        return (x*b)%59
    return x
    
def search(n, r):
    memo = []
    for i in range(n+1):
        memo.append(0)
    memo[0] = 1
    for i in range(1, n+1):
        k = min(i, r)
        while(k > 0):
            memo[k] = (memo[k]+memo[k-1])%59
            k -= 1
    return memo[r]
    
def choose(n, r):
    ans = 1
    if r > n:
        return 0
    for i in range(min(n-r, r)):
        ans=(ans*((n-i)*modpow(i+1, 57))%59)%59
    return ans%59

def lucasChoose(n, r):
    if r == 0:
        return 1
    x, y = n%59, r%59   
    return (choose(n//59,r//59)*search(x,y)) % 59;    

def count_soaps_v2(x, y):
    ct = 0
    try: ct = lucasChoose(x,y)
    except: ct = choose(x,y)
    return (modpow(2, x) - ct + 59) % 59