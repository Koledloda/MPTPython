import math

print('Введите операцию:')
print('plus')
print('minus')
print('mult')
print('div')
print('sqrt')
print('pow')
print('factorial')
print('sin')
print('cos')
print('tg')

operation = input()

while (operation == 'plus' or 'minus' or 'mult' or 'div' or 'sqrt' or 'pow' or 'factorial' or 'sin' or 'cos' or 'tg'):

    if operation == 'plus':
        print('Первое число: ');
        q = int(input())
        print('Второе число: ');
        w = int(input())
        print(q + w)
    elif operation == 'minus':
        print('Первое число: ');
        q = int(input())
        print('Второе число: ');
        w = int(input())
        print(q - w)
    elif operation == 'mult':
        print('Первое число: ');
        q = int(input())
        print('Второе число: ');
        w = int(input())
        print(q * w)
    elif operation == 'div':
        print('Первое число: ');
        q = int(input())
        print('Второе число: ');
        w = int(input())
        if w != 0:
            print(q / w)
        else:
            print('Ошибка!')
    elif operation == 'sqrt':
        e = float(input('Введите число:'))
        print(math.sqrt(e))
    elif operation == 'pow':
        print('Первое число: ');
        q = int(input())
        print('Второе число: ');
        w = int(input())
        print(q ** w)
    elif operation == 'factorial':
        e = int(input('Введите число:'))
        print(math.factorial(e))
    elif operation == 'sin':
        e = float(input('Введите число:'))
        print(math.sin(e))
    elif operation == 'cos':
        e = float(input('Введите число:'))
        print(math.cos(e))
    elif operation == 'tg':
        e = float(input('Введите число:'))
        print(math.tan(e))
    operation = input('Введите операцию: ')