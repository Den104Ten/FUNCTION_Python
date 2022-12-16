"""def factorial(n):
    i = 1
    p = 1
    while i <= n:
        p = p * i
        i += 1
    print(p)
ter = int(input())
factorial(ter)"""


"""def get_sqrt(x):
    res = None if x < 0 else x ** 0.5
    return (res, x)                      #  res в данном случае ссылается на объект, который выводит корень числа
# Когда появляется оператор return, то функция заканчивает свою работу  #  без return здесь бы ничего не работало

a, b = get_sqrt(49)
print(a, b)"""


"""def get_max2(a, b):
    return a if a > b else b  # Используем тернарный оператор для нахождения большего числа


x, y = 5, 7                   # В качестве передаваемых чисел можно использовать даже переменные и input этих переменных  
print(get_max2(x, y))"""


"""def get_max3(a, b):           # Теперь найдем максимальное из трех чисел
    return a if a > b else b


x, y, z = 5, 7, 10
print(get_max3(x, get_max3(y, z)))  # Сначала найдет максимальное среди двух чисел (y, z) внутренней функции
                                    # Потом найдется максимальное среди x и максимального числа из внутренней функции от y, z"""


"""def get_max3(a, b, c):
    return get_max3(a, get_max3(b, c))


x, y, z = 5, 7, 10      # Более красивый и правильный вариант решения нахождения максимального числа из трех
print(get_max3(x, y, z))"""


"""perimeter = True
if perimeter:
    def get_rect(a, b):
        return 2 * (a + b)
else:
    def get_rect(a, b):
        return a * b
                        # Можно даже так использовать функции
print(get_rect(5, 4))"""


"""def even(x):
    return x % 2 == 0
                        # Если число четное, то вывоодим все четные числа в диапозоне от 1 до 20

for i in range(1, 20):
    if even(i):
        print(i)"""




# Задачи по функциям
"""def sqrt (a: float):    # Важно также указывать тип данных вводимых для функции
    return a ** 2


vvod = float(input())
print(sqrt(vvod))"""


"""def is_triangle(a, b, c):
    return True if a + b > c and a + c > b and b + c > a else False"""


"""def is_large(a: str):
    return False if len(a) < 3 else True"""


"""def sep2(a: int):
    return True if a % 2 == 0 else False


z = []
while (a1 := int(input())) != 1:
    if sep2(a1) == True:
        z.append(a1)

print()
print(*z, sep='\n')"""


"""def nokrat(a: int):
    return False if a % 2 == 0 else True

a1 = input().split()
z = []
if nokrat(a1) == True:
    z.append(a1)
print(*z)"""

"""a = list(map(int, input().split()))
b = [i for i in a if i % 2 == 1]
print(*b)"""


"""tp = input().strip()
if tp == 'RECT':
    def get_sq(a, b):
        return a * b
else:
    def get_sq(a):
        return a * a"""


"""def text(a: str):
    return False if len(a) < 6 else True


lst = []
string = input().split()
for i in string:
    if text(i) == True:
        lst.append(i)

print(*lst)"""


# Пример программы для добавления значения в словарь
def cortezh(a: str):
    return a and len(a)


a = input().split()

d = {}

for i in a:
    d[f'{i}'] = f'{len(i)}'

a = sorted(d, key=lambda x: d[x])
print(*a)



