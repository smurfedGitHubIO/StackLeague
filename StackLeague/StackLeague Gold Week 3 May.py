class SnakesLadders():
    def __init__(self):
        self.board = {2:38,7:14,8:31,15:26,16:6,21:42,28:84,36:44,46:25,49:11,51:67,62:19,64:60,71:91,74:53,78:98,87:94,89:68,92:88,95:75,99:80}
        self.pos1 = 0
        self.pos2 = 0
        self.cnt = 0

    def play(self, die1, die2):
        if self.cnt%2 == 0:
            if die1 == die2:
                self.cnt += 2
            else:
                self.cnt += 1
            if self.pos2 == 100 or self.pos1 == 100:
                return 'Game over!'
            if self.pos1+die1+die2 <= 100:
                self.pos1 += die1+die2
            else:
                self.pos1 = 100 - (self.pos1+die1+die2)%100
            if self.pos1 in self.board:
                self.pos1 = self.board[self.pos1]
            elif self.pos1 == 100:
                return 'Player 1 Wins!'
            return 'Player 1 is on square ' + str(self.pos1)
        else:
            if die1 == die2:
                self.cnt += 2
            else:
                self.cnt += 1
            if self.pos1 == 100 or self.pos2 == 100:
                return 'Game over!'
            if self.pos2+die1+die2 <= 100:
                self.pos2 += die1+die2
            else:
                self.pos2 = 100 - (self.pos2+die1+die2)%100
            if self.pos2 in self.board:
                self.pos2 = self.board[self.pos2]
            elif self.pos2 == 100:
                return 'Player 2 Wins!'
            return 'Player 2 is on square ' + str(self.pos2)

##def extract (obj, propertyName):
##    ans = ''
##    for j in obj:
##        if j == propertyName:
##            return obj[j]
##        if type(obj[j]) == type({'a':1}):
##            q = extract(obj[j],propertyName)
##            ans = (q if q != '' else '')
##        if type(obj[j]) == type(['a']):
##            lst = [obj[j]]
##            while not len(lst) == 0:
##                qlst = lst[0]
##                del lst[0]
##                for caye in qlst:
##                    if type(caye) == type({'a':1}):
##                        q = extract(caye,propertyName)
##                        ans = (q if q != '' else '')
##                    elif type(caye) == type(['a']):
##                        lst.append(caye)
##    return ans
##def josephus(xs, k):
##    cnt = 0
##    lst = []
##    while len(xs) != 0:
##        cnt += k
##        cnt = (cnt-1)%len(xs)
##        lst.append(xs[cnt])
##        del xs[cnt]
##    return lst
##
##def buddy(start, limit):
##    for i in range(start,limit+1):
##        l, r = 1, 1
##        c = 2
##        while c*c <= i:
##            if i%c == 0:
##                l += c
##                if c*c != i:
##                    l += i//c
##            c += 1
##        c, qi = 2, l-1
##        while c*c <= qi:
##            if qi%c == 0:
##                r += c
##                if c*c != qi:
##                    r += qi//c
##            c += 1
##        if r-1 == i and qi != i:
##            return [i,qi]
##    return 'Nothing'
