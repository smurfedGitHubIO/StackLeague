##def ordered_string(sentence):
##    x = sentence.split()
##    lst = []
##    for i in x:
##        for j in i:
##            if j >= '1' and j <= '9':
##                lst.append((int(j),i))
##                break
##    lst.sort()
##    return ' '.join(str(i[1]) for i in lst)
##print(ordered_string("strin3gs order1 please4 2the"))

def party(first,second,maximum):
    lst = []
    i, j, cnt = 0, 0, 0
    while cnt < maximum:
        if i < len(first):
            if first[i] not in lst:
                lst.append(first[i])
                cnt += 1
            i += 1
        if cnt == maximum:
            break
        if j < len(second):
            if second[j] not in lst:
                lst.append(second[j])
                cnt += 1
            j += 1
        if i == len(first) and j == len(second):
            break
    return lst

print(party(['Camren'], ['Analy'], 0))

##import math
##
##def diophantus(n):
##    i = 1
##    lst = []
##    while i*i <= n:
##        if n%i == 0:
##            if (i+(n//i))%2 == 0 and ((n//i)-i)%4 == 0:
##                lst.append([(i+(n//i))//2,((n//i)-i)//4])
##        i += 1
##    return lst
##print(diophantus(12))

##class NumberBomb:
##    def get_sum_from_bomb(self,sequence,bomb,radius):
##        ans = 0
##        for i in range(len(sequence)):
##            if sequence[i] == bomb:
##                lft = max(i-radius,0)
##                while lft<=i:
##                    sequence[lft] = -1
##                    lft += 1
##                rgt = min(i+radius,len(sequence)-1)
##                while rgt>i:
##                    sequence[rgt] = -1
##                    rgt -= 1
##        for i in sequence:
##            ans += (i if i != -1 else 0)
##        return ans
##def get_sum_from_bomb(sequence,bomb,radius):
##    ans = 0
##    for i in range(len(sequence)):
##        if sequence[i] == bomb:
##            lft = i-radius
##            while lft<=i:
##                sequence[lft] = -1
##                lft += 1
##            rgt = i+radius
##            while rgt>i:
##                sequence[rgt] = -1
##                rgt -= 1
##    for i in sequence:
##        ans += (i if i != -1 else 0)
##    return ans
##print(get_sum_from_bomb([1, 2, 2, 4, 2, 2, 2, 9], 4, 2))
