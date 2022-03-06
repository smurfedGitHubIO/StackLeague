from functools import cmp_to_key

def cmp(first, second):
    if first[0] == second[0]:
        if first[1] > second[1]:
            return 1
        return -1
    if first[0] < second[0]:
        return 1
    return -1

def rank(st, we, n):
  if st.count(',') == 0:
    return 'No participants'
    
  sp = []
  for i in st.split(','):
      sp.append(i)
      
  if len(sp) == 0:
    return 'No participants'
  if n > len(sp):
    return 'Not enough participants'
    
  arr = []
  st = 0
  for i in sp:
    ctr = len(i)*2
    
    for j in i:
        ctr += (ord(j.upper()) - 65)
        
    ctr *= we[st]
    
    st += 1
    
    arr.append((ctr, i))
  
  arr.sort(key = cmp_to_key(cmp)) 
  
  return arr[n - 1][1]