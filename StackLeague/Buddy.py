def buddy(start, limit):
   for i in range(start,limit+1):
       l, r = 1, 1
       c = 2
       while c*c <= i:
           if i%c == 0:
               l += c
               if c*c != i:
                   l += i//c
           c += 1
       c, qi = 2, l-1
       while c*c <= qi:
           if qi%c == 0:
               r += c
               if c*c != qi:
                   r += qi//c
           c += 1
       if r-1 == i and qi != i:
           return [i,qi]
   return 'Nothing'