""" The function fun() returns the sum of the digits of the input integer. """


def fun(n):
    if n < 10: return n
    else: return fun(n//10) + n%10

print("5 ", fun(5))
print("15 ", fun(15))
print("123 ", fun(123))