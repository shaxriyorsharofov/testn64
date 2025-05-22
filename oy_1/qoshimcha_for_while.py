#a = int(input("Son kiriting"))
'''
if a > 0:
    print("musbat")
else:
    print("manfiy")
'''

'''
result = 'nol' if a == 0 else ('mubat' if a > 0 else 'manfiy')
print(result)
'''
'''
90-100 --> zor
80-90 --> yaxshi
70-80 --> ortacha
70> --> yomon
'''

'''
a = int (input('a = '))
result = 'alo' if 100 > a >= 90 else ('zor' if 90 > a >= 80 else ( 'yaxshi' if 80 > a >= 70 else 'yomon'))
print(result)
'''


'''
a = 0
b = 0
for i in range(40):
    print(f"{i} ning kvadrati:{i**2}, kubi:{i**3}")
    a += i**2 #== a = a + i**2
    b += i**3

print(f"Kvadratlari yigindisi:{a}, kubilari yigindisi:{b}")
'''

'''
a = int(input("Son kiriting"))
for i in range(oy_1, a+oy_1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
'''


'''
a = int(input("Son kiriting"))
for i in range(oy_1, a+oy_1):
    print("FizzBuzz" if i % 3 == 0 and i % 5 == 0 else("Fizz" if i % 3 == 0 \
                    else("Buzz" if i % 5 == 0 else i)))
'''

'''
a = int(input("Son kiriting"))
i = 0
while i < a:
    i += oy_1
    if i % 2 == 0:
        print(i)
'''


'''
a = int(input("Son kiriting"))
n = a
s = 0
while n > oy_1:
    n -= oy_1
    if a % n == 0:
        s += n

if s == a:
    print(True)
else:
    print(False)
'''



a = int(input("Son kiriting"))
i = 0
s = 0
while i < a:
    i += 1
    if a % i == 0:
        s += 1

if s == 2:
    print(True)
else:
    print(False)






