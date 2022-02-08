def number_to_roman(number):
    dct = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
    ans = ''
    for i, j in dct.items():
        if number >= i:
            ans += (number//i)*j
            number -= (number//i)*i
    return ans
print(number_to_roman(1))
print(number_to_roman(4))
print(number_to_roman(5))
print(number_to_roman(9))
print(number_to_roman(19))
print(number_to_roman(22))
print(number_to_roman(15))
##import math
##
##def list_squared(m,n):
##    lst = []
##    for i in range(m, n+1):
##        j, ans = 1, 0
##        while j*j <= i:
##            if i%j == 0:
##                ans += j*j
##                if j*j != i:
##                    ans += (i//j)*(i//j)
##            j += 1
##        if int(math.sqrt(ans))**2 == ans:
##            lst.append([i, ans])
##    return lst

##import math
##
##def tank_price(height, diameter, unit, quantity):
##    radius = 0.00000000
##    if unit == 'in':
##        height = height/39.3701
##        diameter = diameter/39.3701
##    elif unit == 'ft':
##        height = height/3.28084
##        diameter = diameter/3.28084
##    radius = diameter/2.0
##    return round(100.00+((2*math.pi*(radius**2) + 2*math.pi*radius*height)*100*quantity), 5)
