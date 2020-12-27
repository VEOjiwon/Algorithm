def Power(Base, Exponent):
    if Exponent == 1:
        return Base
    elif Exponent == 0:
        return 1
    if Exponent % 2 == 0:
        NewBase = Power(Base,Exponent/2)
        return NewBase * NewBase
    else:
        NewBase = Power(Base,(Exponent-1)/2)
        return (NewBase * NewBase) * Base

def iter_Power(Base,Exponent):
    Result=1
    cnt=0
    if Exponent == 1:
        return Base
    elif Exponent == 0:
        return 1
    tmp = Exponent
    result = 1
    while tmp >0:
        if tmp % 2 !=0:
            result *= Base
        Base*=Base
        tmp//=2
    return result

print(iter_Power(2,16))

print(Power(2,16))