import math

def iter_pi(epsilon):
   cnt, now = 0, 1.0000
   neg, odd = -1, 3.0000
   while True:
       cnt += 1
       now += neg*(1.0000/odd)
       if abs(math.pi - 4*now) <= epsilon:
           break
       odd += 2.00000
       neg *= -1
   return [cnt+1, round(4*now,10)]
print(iter_pi(0.1))