from functools import reduce


# 1

# text = "Salom Dunyo!"
# harflar_sanash = reduce(
#     lambda acc, ch: {**acc, ch: acc.get(ch, 0) + 1} if ch.isalpha() else acc,
#     text,
#     {}
# )
# print("Harflar soni:", harflar_sanash)

# 2

# def fibonacci(n):
#     a, b = 0, 1
#     fibs = []
#     while a <= n:
#         fibs.append(a)
#         a, b = b, a + b
#     return fibs
#
#
# d = 50
# fib = fibonacci(d)
# toq_fib = list(filter(lambda x: x % 2 == 1, fib))
# print("Toq Fibonacci sonlar:", toq_fib)


# 3

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# kopaytma = list(map(lambda x: x[0] * x[1], zip(list1, list2)))
# print("Ko‘paytma:", kopaytma)


# 4

# nums = [1, 2, 3, 4, 5]
# kvadratlar = list(map(lambda x: x ** 2, nums))
# juft_kvadratlar = list(filter(lambda x: x % 2 == 0, kvadratlar))
# print("Juft kvadratlar:", juft_kvadratlar)

# 5

matn = "Bu bir murakkab misol bo'ladi"
sozlar = matn.split()
tartiblangan_sozlar = sorted(sozlar, key=lambda x: len(x))
print("So‘zlar uzunligi bo‘yicha:", tartiblangan_sozlar)
