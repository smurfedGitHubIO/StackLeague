def xo(names, number):
   lst = []
   for i in names:
       cnt = 0
       for j in i:
           if j != ' ':
               cnt += 1
       if cnt <= number:
           lst.append(i)
   return lst