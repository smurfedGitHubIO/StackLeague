def calculate_expenses(daily_expenses, daily_travels):
    sums = 0.0
    for i in daily_travels:
        hours, path, price = i.split()
        hours, price = int(hours), float(price)
        cnt, cur = 0, 0
        while cnt != hours:
            if path[cnt%len(path)] == 'B':
                cur += price
            cnt += 1
        sums += cur
    dibs = sums/float(len(daily_travels))
    if dibs < daily_expenses:
        return 'Hard times. Money needed: ' + str(format(daily_expenses*len(daily_travels) - sums,'.2f'))
    else:
        return 'Good earnings. Extra money per day: ' + str(format(dibs-daily_expenses,'.2f'))
print(calculate_expenses(250, ["5 MMZBQQQQ 37", "11 ZZBBBQ 80"]))
