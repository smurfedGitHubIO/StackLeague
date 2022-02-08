def calculate_expenses(daily_expenses, daily_travels):
    cur = 0
    for i in range(len(daily_travels)):
        a, b, c = daily_travels[i].split()
        a = int(a)
        c = float(c)
        for j in range(a):
            if b[j%len(b)] == 'B':
                cur += c
    cur /= len(daily_travels)
    kek = str("%.2f"%(cur-daily_expenses))
    lol = str("%.2f"%(daily_expenses*len(daily_travels)-cur*len(daily_travels)))
    if cur > daily_expenses:
        return "Good earnings. Extra money per day: " + kek
    return "Hard times. Money needed: " + lol
