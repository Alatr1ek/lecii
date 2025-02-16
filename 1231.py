from math import factorial

def rukopozhatii(n):
    nfac = factorial(n)
    nmfac = factorial(n-2)
    mfac = 2
    res = nfac / (nmfac * mfac)
    print(res)
rukopozhatii(6)
