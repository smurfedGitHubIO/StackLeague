def parse_molecule(formula):
    print(formula)
    ans = {}
    startclause = ['(', '{', '[']
    endclause = [')', '}', ']']
    curelement, curval = '', 0
    stck = []
    multiplier, i = 1, 0
    def findlast(string):
        q = []
        ind = 0
        for i in range(len(string)):
            if string[i] in startclause:
                q.append(string[i])
            elif string[i] in endclause:
                q.pop()
            if len(q) == 0:
                return i
    while i < len(formula):
        if formula[i].isupper():
            if i > 0 and formula[i-1].isnumeric():
                if curelement not in ans:
                    ans[curelement] = (1 if curval == 0 else curval)
                    curelement = ''
                else:
                    ans[curelement] += (1 if curval == 0 else curval)
            elif curelement != '':
                if curelement not in ans:
                    ans[curelement] = (1 if curval == 0 else curval)
                    curelement = ''
                else:
                    ans[curelement] += (1 if curval == 0 else curval)
            curval = 0
            curelement = formula[i]
        elif formula[i].islower():
            curelement += formula[i]
        elif formula[i].isnumeric():
            curval = curval*10 + int(formula[i])
        elif formula[i] in startclause:
            if curelement != '':
                if curelement not in ans:
                    ans[curelement] = (1 if curval == 0 else curval)
                    curelement = ''
                else:
                    ans[curelement] += (1 if curval == 0 else curval)
                curval = 0
            print(formula[i+1:i+findlast(formula[i:])+1])
            q = parse_molecule(formula[i+1:i+findlast(formula[i:])+1])
            i += findlast(formula[i:])+1
            print(formula[i], 'wew')
            if i <= len(formula)-1 and formula[i].isnumeric():
                multiplier = 0
                while i < len(formula) and formula[i].isnumeric():
                    multiplier = multiplier*10 + int(formula[i])
                    i += 1
                for val, key in q.items():
                    if val not in ans:
                        ans[val] = key*multiplier
                    else:
                        ans[val] += key*multiplier
            else:
                for val, key in q.items():
                    if val not in ans:
                        ans[val] = key
                    else:
                        ans[val] += key
        else:
            if curelement != '':
                if curelement not in ans:
                    ans[curelement] = (1 if curval == 0 else curval)
                    curelement = ''
                else:
                    ans[curelement] += (1 if curval == 0 else curval)
            break
        i += 1
    if curelement != '':
        if curelement not in ans:
            ans[curelement] = (1 if curval == 0 else curval)
            curelement = ''
        else:
            ans[curelement] += curval
    return ans

print(parse_molecule("((N42)24(OB40Li30CHe3O48LiNN26)33(C12Li48N30H13HBe31)21(BHN30Li26BCBe47N40)15(H5)16)14"))