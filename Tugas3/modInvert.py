import math

def modInverse(a,m):

    if (math.gcd(a,m)!=1):
        print("tidak ada inverse")
    else:
        #jika a dan m prima
        #modulus Inversenya a^(m-2) mdoe m
        print("modular multiplicative inverse is ",
            pow(a, m - 2, m))

print(modInverse(3,13))