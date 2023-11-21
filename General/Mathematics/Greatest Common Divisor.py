def gcd(x, y):
    if x < y:
        return gcd(y, x)

    while y != 0:
        (x, y) = (y, x % y)

    print("",x)
    return x

# a = 12
# b = 8

a = 66528
b = 52920

gcd(a, b)
