from turtle import clearscreen



##print('Hello world') Комментарии делаются в решетке
## Типы переменных

""" value=None
print(type(value))
a=123
b=3.14
c='привет'
value=11223
print(a)
print(type(a)) ## обозначение типа данных
print(b) ## Вывод данных
print(type(b))
print(c)
print(type(c))
print(value)
print(type(value)) """

""" str = 'hello \n"world"'  ##c новой строки и дополнительные ковычки
print(str)  """

""" str = 'hello "world"'
a=123
b=1.23
print(a,'-',b,'-',str)
print('{}-{}-{}'.format(a,b,str))
print('{1}-{2}-{0}'.format(a,b,str)) ##  печатать b str a
print(f'{a}-{b}-{str}') """ ## Вывод информации в терминал с помощью интерполяции

## Логическая Переменная
""" f=True
print(f) """

## Списки
""" list=['1','2','3']
print(list)

col=['hello',1.236]
print(col) """

## print input
""" print('Введите число а=');
a=int(input())## Если нужны вещественные значения float
print('Введите число b=');
b=int(input())
print('({0}+{1})'.format(a,b)) 
print(f'{a}+{b}={a+b}' """

## Арифметические операции
## Унарный плюс и минус это знак перед числом

""" a=125
b=-256
c=a+b
print(c) """

# / -это просто деление //-деление на цело %-деление остаток **-возведение в степень

""" a=1.35468
b=3
c=round(a*b,5)## округление до 5 знаков
print(c) """

""" a=3
a+=5
print(a) """

## Логические операции

""" a=1<4
print(a)

a=1<4 and 5>2 ## 1==2 1!=2 1<3<5<7
print(a)

a='qwe'
b='qwe'
print(a==b)

a=[1,2]
b=[1,2]
print(a==b) """

""" func=1
T=4
x=123
print(func<T>x)

f=1>2 or 4<6
print(f) """

""" f=[1,2,3,4]
print(f)
print(2 in f) ## Два есть в списке F, перед двойкой можно not добавить для отрицания

is_odd=f[0]%2==0
print(is_odd) """

## Логические ветвления 

##IF
""" a=int(input('a='))
b=int(input('b='))
if a>b:
    print(a)
if b>a: ## else:
    print(b)
 """

##ELIF
""" username=input('Введите имя: ')
if username=='Маша':
    print('Ура,это Маша')
elif username=='Марина':
    print('Привет Марина')
elif username=='Тимур':
    print('тимур братан')
else:
    print('Привет, ', username) """

## WHILE
""" original = 23
inverted = 0
while original != 0:
 inverted = inverted * 10 + (original % 10)
 original //= 10
print(inverted) """

##FOR
""" for i  in 1,2,3,4,5:
    print(i**2) """

""" list=[1,4,2,5]
for i in list:
    print(i) """

##r=range(10)
""" for i in range(1,10,2):
    print(i)

for i in 'qwerty':
    print(i) """

##Строки
""" text='Сколько волка не корми смотрит он в лес'
print(len(text))
print('волка' in text)
print(text.isdigit())## являются ли элементы строки числами
print(text.islower())## являются ли элементы строки символами нижнего регистра
print(text.replace('лес','ЛЕС')) 
print(text.istitle()) """  ##Возвращает True, если строка является строкой с заглавным регистром

## HELP 

""" help(text.istitle) """

""" text = 'съешь ещё этих мягких французских булок'
print(text[0]) # c
print(text[1]) # ъ
print(text[len(text)-1]) # к
print(text[-5]) # б
print(text[:]) # print(text)
print(text[:2]) # съ
print(text[len(text)-2:]) # ок
print(text[2:9]) # ешь ещё
print(text[6:-18]) # ещё этих мягких
print(text[0:len(text):6]) # сеикакл
print(text[::6]) # сеикакл
text = text[2:9] + text[-5] + text[:2] # ... """

## СПИСКИ:введение

""" numbers = [1, 2, 3, 4, 5]
print(numbers) # [1, 2, 3, 4, 5]
numbers = list(range(1, 6)) ##Приведение типа range в лист
print(numbers) # [1, 2, 3, 4, 5]
numbers[0] = 10
print(numbers) # [10, 2, 3, 4, 5]
for i in numbers:
 i *= 2
 print(i) # [20, 4, 6, 8, 10]
print(numbers) # [10, 2, 3, 4, 5] """

""" colors = ['red', 'green', 'blue']
for e in colors:
 print(e) # red green blue
for e in colors:
 print(e*2) # redred greengreen blueblue
colors.append('gray') # добавить в конец
print(colors == ['red', 'green', 'blue', 'gray']) # True
colors.remove('red') #del colors[0] # удалить элемент """

##ФУНКЦИИ

def f(x):
    if x==1:
        return 'целое'
    elif x==2.3:
        return 23
    else:
        return

""" arg =2
print(f(arg))
print(type(f(arg))) """