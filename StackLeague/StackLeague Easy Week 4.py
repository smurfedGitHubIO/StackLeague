def likedIt(likers):
    if len(likers) == 0:
        return 'Nobody likes this post'
    elif len(likers) == 1:
        return likers[0] + ' likes this post'
    elif len(likers) == 2:
        return likers[0] + ' and ' + likers[1] + ' like this post'
    elif len(likers) == 3:
        return likers[0] + ', ' + likers[1] + ' and ' + likers[2] + ' like this post'
    else:
        return likers[0] + ', ' + likers[1] + ' and ' + str(len(likers)-2) + ' others like this post'

def find_the_digit(str1, str2):
    dct = {1:[1], 2:[6,2,4,8], 3:[1,3,9,7], 4:[6,4],5:[5], 6:[6], 7:[1,7,9,3], 8:[6,8,4,2], 9:[1,9], 0:[0]}
    if int(str1[0]) == 0 and int(str2) == 0:
        return 1
    if int(str2) == 0:
        return 1
    end = int(str1[-1])
    return dct[end][int(str2)%len(dct[end])]

print(find_the_digit('9','7'))
