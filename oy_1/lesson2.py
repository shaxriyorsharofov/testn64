#uyga vazifa

#13
import math

'''
r1 = int(input("R1 radiusni kiriting: "))
r2 = int(input("R2 radiusni kiriting: "))
s = math.pi*(r1**2-r2**2)
print(f"Natija: {s}")
'''

#12
'''
a = int(input("A katedni kiriting: "))
b = int(input("B katedni kiriting: "))
c = math.sqrt(a**2 + b**2)
p = a + b + c
print(f"Peremetri: {p}, c kated: {c}")
'''

#14
'''
l = int(input("Aylana uzunligini kiriting: "))
r = l/(2*math.pi)
s = math.pi*r**2
print(f"Radius: {r}, Yuzasi: {s}")
'''

#15
'''
s = int(input("Aylana yuzasini kiriting: "))
r = math.sqrt(s/math.pi)
d = r*2
print(f"Radius: {r}, diametri: {d}")
'''



#if
'''
n = int(input("Son kiriting:"))
if n == 0:
    print('nol')
elif n > 0:
    print("musbat")
else:
    print("manfiy")
'''


'''
n = int(input("Son kiriting:"))
if n % 2 == 0:
    print('juft')
else:
    print("toq") 
'''

'''
a = int(input("Son kiriting:"))
b = int(input("Son kiriting:"))
if a == b:
    print("teng")
elif a > b:
    print(a, b)
else:
    print(b, a)
'''

'''
a = int(input("Son kiriting:"))
b = int(input("Son kiriting:"))
c = int(input("Son kiriting:"))
if a == b and a == c:
    print("teng")
elif a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)
'''
'''    
n = int(input("Son kiriting:"))
if 100 >= n >= 0:
    if n == 100:
        print("!!!")
    elif n == 0:                    
        print("Imtihon topshirmagan")
    elif n >= 90:
        print("Zo'r")
    elif n >= 80:
        print("yaxshi")
    elif n >= 70:
        print("Ko'proq oqish kk")
    elif n >= 60:
        print("Qayta topshirish")
    else:
        print("Chopildi")
else:
    print("xato ball kiritdingiz")
'''

'''
n = int(input("Son kiriting:"))
if n > 0:
    print("MUSBAT")
elif n < 0:
    print("MANFIY")
    
if n %2 == 0:
    print("JUFT")    
else:
    print("TOQ")
'''


'''
n = int(input("Xaridingiz summasini kiriting:"))
if 1_000_000 >= n > 0:
    if n >= 500_000:
        print(f"Siz 50% skidka bilan {n*0.5}")
    elif n >= 300_000:                    
        print(f"Siz 25% skidka bilan {n*0.75}")
    elif n >= 100_000:
        print(f"Siz 5% skidka bilan {n*0.95}")
    else:
        print(f"Siz 0% skidka bilan {n}")

else:
    print("xato summa kiritdingiz")
'''













# while True:
#     a = int(input("Son kiriting:"))
#     b = int(input("Son kiriting:"))
#     c = int(input("Son kiriting:"))
#     x = 0
#     y = 0
#     if a > 0:
#         x = x + 1
#     else:
#         y = y + 1
#
#     if b > 0:
#         x = x + 1
#     else:
#         y = y + 1
#
#     if c > 0:
#         x = x + 1
#     else:
#         y = y + 1
#
#     print(x, y)
#


    
def kopaytirish(x, y):
    return x * y
