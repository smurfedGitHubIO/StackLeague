def remove_duplicated_words(string):
   x = []
   string = string.split()
   for j in string:
       if len(x) == 0:
           x.append(j)
       elif j not in x:
           x.append(j)
   return ' '.join(str(i) for i in x)