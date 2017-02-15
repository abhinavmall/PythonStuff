def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    # Your code here
    i=0
    while base**i <= num:
        i += 1

    print(i)
    print(abs(base**i - num))
    print(abs(base**(i-1) - num))
    if abs(base**i - num) >= abs(base**(i-1) - num):
        return i-1
    else:
        return i

print(closest_power(2, 192.0))
