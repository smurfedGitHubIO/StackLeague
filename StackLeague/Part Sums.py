def part_sums(lst):
   qlst = [0]*len(lst)
   for i in range(len(lst)-1,-1,-1):
       if i == len(lst)-1:
           qlst[i] = lst[i]
       else:
           qlst[i] = lst[i]+qlst[i+1]
   return qlst+[0]