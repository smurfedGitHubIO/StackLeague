def invites(s):
    lst = s.split(';')
    sepcheck = True
    anotherlst, dct = [], {}
    for i in range(len(lst)):
        q = lst[i].split(':')
        if len(q) != 2:
            raise Exception('Separator is missing')
        aq = '('+q[1].upper() + ', ' + q[0].upper()+')'
        if aq not in dct:
            dct[aq] = True
            anotherlst.append('('+q[1].upper() + ', ' + q[0].upper()+')')
    return ''.join([str(x) for x in sorted(anotherlst)])