def extract (obj, propertyName):
   ans = ''
   for j in obj:
       if j == propertyName:
           return obj[j]
       if type(obj[j]) == type({'a':1}):
           q = extract(obj[j],propertyName)
           ans = (q if q != '' else '')
       if type(obj[j]) == type(['a']):
           lst = [obj[j]]
           while not len(lst) == 0:
               qlst = lst[0]
               del lst[0]
               for caye in qlst:
                   if type(caye) == type({'a':1}):
                       q = extract(caye,propertyName)
                       ans = (q if q != '' else '')
                   elif type(caye) == type(['a']):
                       lst.append(caye)
   return ans
