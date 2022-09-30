def digital_root(n):
    if len(str(n)) == 1 :
        return int(n)
    else:
        res =  int(str(n)[0]) + digital_root(str(n)[1:])
        if len(str(res)) > 1:
            return digital_root(res)
        return res


print(digital_root(942))
