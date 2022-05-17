""" Сформировать список из  N членов последовательности.
Для N = 5: 1, -3, 9, -27, 81 и т.д.
Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

Написать программу получающую набор произведений чисел от 1 до N.

Задать список из n чисел последовательности (1+1n)n и вывести на экран их сумму
Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число
Реализовать алгоритм перемешивания списка. 
Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора псевдослучайных чисел
Определить, присутствует ли в заданном списке строк, некоторое число 
Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
Примеры
список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
список: [], ищем: "123", ответ: -1

Найти сумму чисел списка стоящих на нечетной позиции
Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д. Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 
В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов. Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
Написать программу преобразования десятичного числа в двоичное
Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов. 
 Т е для k = 8, список будет выглядеть так: [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи
Строка содержит набор чисел. Показать большее и меньшее число
Символ-разделитель - пробел
Найти корни квадратного уравнения Ax² + Bx + C = 0
Найти НОК двух чисел
Вычислить число  c заданной точностью d
	Пример: при d = 0.001,  = 3.141. 10-1d10-10
Составить список простых множителей натурального числа N """

## Сформировать список из  N членов последовательности. Для N = 5: 1, -3, 9, -27, 81 и т.д.
## Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1. Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
## Написать программу получающую набор произведений чисел от 1 до N.
## Пример: пусть N = 4, тогда
## [ 1, 2, 6, 24 ]


## Сформировать список из  N членов последовательности. Для N = 5: 1, -3, 9, -27, 81 и т.д.
""" list=[]
n=1
input = 5
for e in range(input):
    list.append(n) ## *append* Добавить объект в конец списка.
    n*=-3
print(list) """

## Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1. Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


""" dictionary = {}
n=int(input('Введите число= '))
for i in range(1, n+1):
    dictionary[i]=3*i+1
print(dictionary) """



##Написать программу получающую набор произведений чисел от 1 до N
""" count=1
n=int(input('Введите число: '))
for i in range(1, n+1):
    count= i*count
    print(count) """
    
## Задать список из n чисел последовательности (1+1/n)^n и вывести на экран их сумму

""" dictionary = {}
sum=0

n=int(input('Введите число= '))
for i in range(1, n+1):

    dictionary[i]=((1+(1/i))**i)
    sum=sum+dictionary[i]

print(dictionary)
print()
print(sum) """

## Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число

""" list=[]
sum=1
n = int(input('Введите число= '))
for i in range(-n-1,n+1):
    list.append(i)

data=open('example_03.txt','r')

for i in data:
    index = int(i)
    print (index)
    print()
    sum=sum*list[index]
    print(list[index])
    print()
    print(sum)
data.close() """

## Определить, присутствует ли в заданном списке строк, некоторое число 

""" list= ['a,3,5,b,c,7,g']

n=3

for i in range(len(list)):
    for a in list[i]:
        if a ==str(n):
            print("Присутствует")
            break
    else:
        print("Не присутствует") """

## Реализовать алгоритм перемешивания списка, ## как смешивать то?? 

""" from random import randint

list1 = list(range(0,30,2))
list2 = []
index=0
print(list1)

while len(list2)<len(list1):
    index= randint(0, len(list1)-1)
    if list1[index] not in list2:
        list2.append(list1[index])
print(list2) """


## Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора псевдослучайных чисел

""" import time

result = time.localtime()
generator=result.tm_sec
print(generator)

 """

""" st=set()
for i in range(10):
    st.add(str(i))
print(st)
for i in st:
    print(int(i))
    break  """

##Найти сумму чисел списка стоящих на нечетной позиции
""" from random import randint


list = []
for i in range(randint(1,3)):
    list.append(randint(10,30))
print(list)

sum=0
for i in range(0,len(list),2):
    sum+=list[i]

print(sum) """

## Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
#Примеры

""" list=["йцу", "фыв", "ячс", "цук", "йцуrt"]
search="йцу"
count=0
for i in range(len(list)):
    if(list[i]==search):
        count+=1
        if (count==2):
            print(i)
            break

if (count<2):
    print('-1') """


##список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
#список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
#список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
#список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
#список: [], ищем: "123", ответ: -1