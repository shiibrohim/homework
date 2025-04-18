from math import sqrt

# 1
# son = [2, 34, 456]
# a = list(map(lambda x: x * len(str(x)), son))
# print(a)


# 2
# def masala(a):
#     ka, ki = 0, 0
#     for i in a:
#         if i.isupper():
#             ka += 1
#         elif i.islower():
#             ki += 1
#     return ka, ki
#
#
# a = input("matin kiriting: ")
# print(masala(a))


# 4
# def yangi():
#     a = list(map(lambda x: ''.join(i for i in x if m.count(i) <= 2), m.split()))
#     return ''.join(a)
#
#
# m = input("matn kiriting: ")
# print(yangi())


# 5
# def zipp():
#     a = [a + b + c for a, b, c in zip(lst1, lst2, lst3) if a + b + c >= 100]
#     return a
#
#
# lst1 = [32, 64, 13, 95, 47]
# lst2 = [49, 2, 88, 16, 37]
# lst3 = [6, 88, 42, 22, 10]
# print(zipp())


# 6
# def factorial(a):
#     f, b = 1, [i for i in range(1, a + 1)]
#     for i in b:
#         f *= i
#     return f
#
#
# def factorial_yigindi():
#     a = list(map(lambda x: [factorial(int(i)) for i in str(x)], lst))
#     return [sum(i) for i in a]
#
#
# lst = [32, 64, 13, 95, 47]
# print(factorial_yigindi())


# 7
# def ildiz():
#     ildiz = list(map(lambda x: sqrt(x), liist))
#     b = list(filter(lambda x: x.is_integer(), ildiz))
#     return [int(i) for i in b]
#
#
# liist = [1, 5, 7, 8, 9, 13, 16, 19, 23, 29]
# print(ildiz())


# 8
# def tub(a):
#     if a < 2:
#         return False
#     for i in range(2, int(a ** 0.5) + 1):
#         if a % i == 0:
#             return False
#     return True
#
#
# def masala():
#     a = list(map(lambda x: x if tub(len(x)) else '', st.split()))
#     return [i for i in a if len(i) != 0]
#
#
# st = input("kiriting: ")
# print(masala())


# 9
# def masala():
#     a = list(map(lambda x: ''.join(x).capitalize(), sorted(st.split(), reverse=True)))
#     return a
#
#
# st = input("kiriting: ")
# print(masala())


# 10
# def juft_kvadrat():
#     juft = list(filter(lambda x: x % 2 == 0, lst))
#     kvadrat = list(map(lambda x: x ** 2 if x in juft else x, lst))
#     return kvadrat
#
#
# lst = [14, 67, 23, 88, 5, 42, 39]
# print(juft_kvadrat())


# 11
# def yigindi(a):
#     b = 0
#     for i in str(a):
#         b += int(i)
#     return b
#
#
# def change():
#     r = list(map(lambda x: yigindi(x), lst))
#     return r
#
#
# lst = [10, 55, 66, 3, 56, 89, 25, 641]
# print(change())


# 12
# def stt(a):
#     if a[0] * len(a) == a:
#         return a
#
#
# def matin():
#     r = list(map(lambda x: stt(x), st.split()))
#     return r
#
# st = input("matin kiriting: ")
# print(matin())


# 13
# def factorial(a):
#     f, b = 1, [i for i in range(1, a + 1)]
#     for i in b:
#         f *= i
#     return f
#
# def masala():
#     r = list(filter(lambda x: x % 3 == 0, lst))
#     return list(map(lambda x: factorial(x), r))
#
#
# lst = [1, 2, 3, 4, 5, 6, 9]
# print(masala())


# 14
# def masala():
#     r = list(map(lambda x: x * lst.index(x), lst))
#     return r
#
#
# lst = [4, 5, 6]
# print(masala())


# 15
# def masala():
#     a = list(filter(lambda x: x == x[::-1], lst))
#     r = list(map(lambda x: x.capitalize(), a))
#     return r
#
#
# lst = ['kalit', 'ovqat', 'moshina', 'radar', 'sumka']
# print(masala())


# uy ishi 16 aprel

from functools import reduce


# 1,

# def tub(a):
#     if a < 2:
#         return False
#     for i in range(2, int(a ** 0.5) + 1):
#         if a % i == 0:
#             return False
#     return True
#
#
# def masala():
#     a = list(filter(lambda x: tub(x), lst))
#     return a
#
#
# lst = [2, 5, 3, 11, 5, 66, 7, 88, 9, 100]
# print(masala())


# 2

# def factorial(a):
#     f, b = 1, [i for i in range(1, a + 1)]
#     for i in b:
#         f *= i
#     return f
#
#
# def masala():
#     a = list(map(lambda x: factorial(x), lst))
#     return a
#
#
# lst = [4, 12, 24, 5, 40]
# print(masala())


# 3

# def masala():
#     return list(map(lambda i: len(list(filter(lambda x: x in un, i))), st.split()))
#
#
# un = ['a', 'i', 'e', 'u', 'o', "o'"]
# st = input("Matini kiriting: ")
# print(masala())


# 4

# def masala():
#     return list(map(lambda x: x.capitalize(), list(filter(lambda x: x == x[::-1], lst))))
#
#
# lst = ['kiyik', 'salom', 'soz', 'radar', 'level']
# print(masala())


# 6

# def masala():
#     a = reduce(lambda x, y: x if len(x) > len(y) else y, lst)
#     return a
#
#
# lst = ["moshina", "IT", "noutbuk", "kalit"]
# print(masala())


# 7

# def masala():
#     katta = reduce(lambda x, y: x if x > y else y, lst)
#     kichik = reduce(lambda x, y: x if x < y else y, lst)
#     return katta - kichik
#
#
# lst = [1, 2, 3, 4, 5, 6, 7]
# print(masala())


# 8

# def masala():
#     a = ' '.join(list(map(lambda x: ''.join(list(filter(lambda y: y not in un, x))), st.split())))
#     return a
#
#
# un = ['a', 'i', 'e', 'u', 'o', "o'"]
# st = input("Matini kiriting: ")
# print(masala())


# 9

# def masala():
#     a = list(filter(lambda x: lst.count(x) == 1, lst))
#     return a
#
#
# lst = [1, 'moshina', 1, 'kalit', 2, 'kalit', 'moshina', 2, 3, 'noutbuk', 4, 'eshik', 5]
# print(masala())


# 10

def masala_10():
    a = list(filter(lambda x: len(x) >= 10, list(map(lambda x: x[0] + x[1], zip(matin.split(), matin1.split())))))
    return a


matin = input("1-Matini kiriting: ")
matin1 = input("2-Matini kiriting: ")
print(masala_10())
