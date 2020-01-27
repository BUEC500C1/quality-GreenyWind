romans = [["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    , ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    , ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    , ["", "M", "MM", "MMM"]
    , ]

def a2r(input_):
    retVal = ""
    if isinstance(input_, int):
        if input_ <= 0:
            retVal = "invalid input: not a positive integer"
        elif input_ > 3999:
            retVal = "invalid input: integer out of range [1, 3999]"
        else:
            num = input_
            for i in range(4):
                digit = num % 10
                retVal = romans[i][digit] + retVal
                num = num // 10
    else:
        if isinstance(input_, float):
            retVal = "invalid input: not an integer"
        else:
            retVal = "invalid input: not a number"

    return retVal