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

