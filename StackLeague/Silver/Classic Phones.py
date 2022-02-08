def send_message(s):
    dct = {'1':'1-', '2':'2-', '3':'3-', '4':'4-','5':'5-','6':'6-','7':'7-','8':'8-','9':'9-','0':'0-','a':'2','b':'22','c':'222','d':'3','e':'33','f':'333', 'g':'4','h':'44','i':'444','j':'5','k':'55','l':'555','m':'6', 'n':'66', 'o':'666', 'p':'7', 'q':'77', 'r':'777', 's':'7777', 't':'8', 'u':'88', 'v':'888', 'w':'9', 'x':'99', 'y':'999', 'z':'9999', '.':'1', ',':'11','?':'111','!':'1111','#':'#-','*':'*-','\'':'*','-':'**','+':'***', '=':'****', ' ':'0'}
    capslock = False
    ans = ''
    for i in range(len(s)):
        if i == 0:
            if s[i].isupper() and capslock == False:
                capslock = True
                ans += '#'
                ans += dct[s[i].lower()]
            else:
                ans += dct[s[i]]
        else:
            if s[i].isupper() and capslock == False:
                capslock = True
                ans += '#'
                ans += dct[s[i].lower()]
            elif capslock and s[i].islower():
                capslock = False
                ans += '#'
                ans += dct[s[i]]
            else:
                if ans[-1] == dct[s[i]][0]:
                    ans += ' '
                ans += dct[s[i]]
    return ans
