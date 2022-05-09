##ФАЙЛЫ

""" Режим А дописывает   что то в имеющий файл
    Режим R считать данные с файла
    Режим W Записывать и создавать если он не существует"""


""" colors = ['red', 'green', 'blue']
data=open('Example_lection2.txt', 'w') ##создается файл с данным расширением
data.writelines(colors) 

data.write('\nLine 2\n')
data.write('Line 3\n')
data.close()

with open('example_2_lection2.txt','w') as data: ## Вторая возможность создания 
    data.writelines(colors)
    data.write('\nLine 2\n')
    data.write('Line 3\n')
 """
""" path = 'example_2_lection2.txt'  ## Считывание файла и его печать
data=open(path, 'r')
for line in data:
    print(line)
data.close() """

## ФУНКЦИИ

""" import Lection_1 ## можем разделять программы и брать формулы с другого файла
print(Lection_1.f(1)) """

""" import Lection_1 as L1 ## тоже самое только используя сокращение, тем самым можно испозовать уже имеющиеся скрипты
print(L1.f(1)) """

##УМНОЖЕНИЕ СТРОК

""" def new_string(symbol, count): 
 return symbol * count
print(new_string('!', 5)) # !!!!!
print(new_string('!')) # TypeError

def new_string(symbol, count = 3):
 return symbol * count
print(new_string('!', 5)) # !!!!!
print(new_string('!')) # !!!
print(new_string(4)) # 12 """

## Возможность передачи несколько аргументов в ФУНКЦИЮ

""" def concatenatio(*params):
 res: str = "" ## явно прописали тип данных либо если числа int=0
 for item in params:
    res += item
 return res
print(concatenatio('a', 's', 'd', 'w')) # asdw
print(concatenatio('a', '1', 'd', '2')) """ # a1d2
# print(conсatenatio(1, 2, 3, 4))

## РЕКУРСИЯ

""" def fib(n):
    if n in [1,2]:
        return 1
    else:
        return fib(n-1)+fib(n-2)

list = []
for e in range(1,10):
    list.append(fib(e)) ## *append* Добавить объект в конец списка.
print(list) """

## КОРТЕЖИ
#это неизменяемый список
#если одно число обязательно в конце запятая

""" a = (3 , 4)
print(a[0])


t = tuple(['red', 'green', 'blue'])
red, green, blue = t
print('r:{} g:{} b:{}'.format(red, green, blue))
# r:red g:green b:blue """

## Словари
# Неупорядоченные коллекции самопроизвольных объектов с доступом по ключу

""" dictionary = {}
dictionary = \
 {
 'up': '↑',
 'left': '←',
 'down': '↓',
 'right': '→'
 }
print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left']) # ←

for k in dictionary.keys():## value 
    print(k)

print(dictionary['up']) # ↑
# типы ключей могут отличаться
dictionary['left'] = '⇐'
print(dictionary['left']) # ⇐
#print(dictionary['type']) # KeyError: 'type'
del dictionary['left'] # удаление элемента
for item in dictionary: # for (k,v) in dictionary.items():
 print('{}: {}'.format(item, dictionary[item]))
# up: ↑
# down: ↓
# right: → """

## Множества 
#Неупорядоченная совокупность элементов
""" a = {1, 2, 3, 5, 8}
b = {'2', '5', 8, 13, 21}
print(type(a)) # set
print(type(b)) # set

a = {1, 1, 1, 1, 1}
print(a) # {1}

colors = {'red', 'green', 'blue'}
print(colors) # {'red', 'green', 'blue'}

colors.add('gray')
print(colors) # {'red', 'green', 'blue','gray'}

colors.remove('red')
print(colors) # {'green', 'blue','gray'}

# colors.remove('red') # KeyError: 'red'

colors.discard('red') # ok Удаляет значение
print(colors) # {'green', 'blue','gray'}
colors.clear() # { } Очищает множество
print(colors) # set() """

# Разность, объединение и тд

""" a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # c = {1, 2, 3, 5, 8}
u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
i = a.intersection(b) # i = {8, 2, 5}
dl = a.difference(b) # dl = {1, 3}
dr = b.difference(a) # dr = {13, 21}
q = a \
 .union(b) \
 .difference(a.intersection(b))
# {1, 21, 3, 13}

# Неизменяемое множество
# нельзя добавить или удаления работать не будут """

## СПИСКИ

""" list1 =[1,2,3,4]
list2=list1

for e in list1:
    print(e)

print()

for e in list2:
    print(e)

list1[0]=123 
list2[1]=554

print()

for e in list1:
    print(e)

print()

for e in list2:
    print(e) """

##123 554 3 4 123 554 3 4
## Копирование данные одного списка в другом при любом изменениеодного ведут изменения в другом такая связь

""" list.pop(2) """ ## удаляет последний элемент в списке или ннужный элемент
"list.insert(2,11)" ## вставсляет элемент 11 под индекс 2
""" list.append(23) """ ## вставсляет в конец