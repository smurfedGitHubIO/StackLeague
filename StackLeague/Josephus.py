def josephus(xs, k):
   cnt = 0
   lst = []
   while len(xs) != 0:
       cnt += k
       cnt = (cnt-1)%len(xs)
       lst.append(xs[cnt])
       del xs[cnt]
   return lst