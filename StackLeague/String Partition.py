class StringPartition:

   def __init__(self, strings):
       self.strings = strings

   def merge(self, start_index, end_index):
##        if start_index < 0 and end_index >= len(self.strings):
##            q = ''
##            for i in self.strings:
##                q += i
##            self.strings = [q]
       start_index = max(start_index,0)
       end_index = min(len(self.strings)-1,end_index)
       #else:
       ans = ''
       lst = []
       for i in range(start_index):
           lst.append(self.strings[i])
       for i in range(start_index, end_index+1):
           ans += self.strings[i]
       lst.append(ans)
       for i in range(end_index+1,len(self.strings)):
           lst.append(self.strings[i])
       self.strings = lst

   def divide(self, index, partitions):
       lst = []
       for i in range(index):
           lst.append(self.strings[i])
       ln, q = len(self.strings[index])//partitions, 0
       for i in range(0,len(self.strings[index]),ln):
           if q != partitions-1:
               ns = ''
               for j in range(ln):
                   ns += self.strings[index][i+j]
               lst.append(ns)
           else:
               lst.append(self.strings[index][i:])
               break
           q += 1
       for i in range(index+1,len(self.strings)):
           lst.append(self.strings[i])
       self.strings = lst

   def get_string_representation(self):
       
       # do not remove; for testing

       representation = ""

       for i in range(0, len(self.strings)):
           representation += self.strings[i] + " "

       return representation
s = StringPartition(["abcd", "efgh", "ijkl", "mnop", "qrst", "uvwx", "yz"])
s.merge(4, 10)
s.divide(4, 5)
print(s.get_string_representation())