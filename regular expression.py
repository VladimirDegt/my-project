from re import search, sub

def increment_string(strng):
    if strng:
        regex = search(r'[A-Za-z]$', strng)
        if regex:
            return strng + "1"
        else:
            regex = search(r'(\d+)$', strng)
            find = regex.group()
            l = len(find)
            x = int(find) + 1
            res = str(x).zfill(l)
            result = sub(r'(\d+)$', res, strng)
            return result
    else:
        return "1"

print(increment_string("fo99obar99"))
"""
Your job is to write a function which increments a string, to create a new string.

    If the string already ends with a number, the number should be incremented by 1.
    If the string does not end with a number. the number 1 should be appended to the new string.
Examples:
foo -> foo1
foobar23 -> foobar24
foo0042 -> foo0043
foo9 -> foo10
foo099 -> foo100
"""
