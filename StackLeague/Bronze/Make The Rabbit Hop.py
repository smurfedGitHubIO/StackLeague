def parse(data):
    ans = 0
    lst = []
    for i in range(len(data)):
        if data[i] == 'i' or data[i] == 'I':
            ans += 1
        elif data[i] == 'd' or data[i] == 'D':
            ans -= 1
        elif data[i] == 's' or data[i] == 'S':
            ans *= ans
        elif data[i] == 'o' or data[i] == 'O':
            lst.append(ans)
    return lst
