def soma(n1, n2):
    return n1, n2

print('',soma(1, 2), '\n', soma(3, 5), '\n')
def printFunction():
    print("I'm a function.")
    print("I'm learning python")
printFunction()

print()

def thisIsEven(x):
    return x % 2 == 0
x = 11
print('Is the number {} even? The answer is {}.\n'.format(x, thisIsEven(x)))

def foo(*args):
    return sum(*args)

print(foo([1,2,3,4,5]))
print(foo([1,2]),'\n')

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n-1)
print(fatorial(5), '\n')

def printName(name = 'desconhecido'):
    print(name)
printName()

print()

def somar(x, y, z, f):
    return x + f(y, z)

def f(n1, n2):
    return n1 + n2
print(somar(10, 20, 30, f), '\n')

a = lambda x: x*2
print('',a(4), '\n', a(10))


