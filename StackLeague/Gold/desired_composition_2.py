def gcd(x, y, s, i):
    if s == 0 or i == 0:
        return 100
    elif x%y == 0:
        return y
    else:
        return gcd(y, x%y, s, i)

def desired_composition(Steel, Iron):
  return 100//(gcd(Steel, Iron, Steel, Iron))