## В заданном списке вещественных чисел найти разницу между максимальным и минимальным
# и минимальном значением дробной части элементов


""" list = [1.1, 1.3, 3.11, 5, 10.1]
list2=[]

for i in list:
    list2.append(round(i-int(i),2))
print(list2)

print(max(list2))
print(min(list2))
 """

## Строка содержит набор чисел. Показать большее и меньшее число
#символ разделитель пробео

""" str="12 58 68 44 9"
list=[]
max=0
min=100
count=""
for i in str:
    if(i!=" " and i!=''):
        count+=i
        if(len(i)==len(str)-1):
            list.append(count) 
            print(count) 
    else:
        list.append(count)
        count=''
for i in list:
   if(int(i)>max):
        max=int(i)
   if(int(i)<min):
        min=int(i)
print(max) 
print(min) """


""" str='12 58 68 44 9'
value = str.split(" ")
max=0
min=100

for i in value:
    if(int(i)>max):
        max=int(i)
    if(int(i)<min):
        min=int(i)
print(max) 
print(min) """

## Найти произведение пар чисел в списке
## парой считаем первый и последний
""" list = [2, 3, 5, 6, 7, 2] 
list2=[] 
list3=[]      
for i in range(len(list)//2):
    list2.append(list[i])
    list2.append(list[len(list)-1-i])
    list3.append(list[i]*list[len(list)-1-i])
print(list)
print(list2)
print(list3)
 """
## Найти корни квадратного уравнения АХ^2+bx+c=0

""" from cmath import sqrt
from re import X


a=float(input("Введите значение А= "))
b=float(input("Введите значение В= "))
c=float(input("Введите значение С= "))

d=b*b-4*a*c
print(d)
if d>0:
    x1=(-b+sqrt(d))/2*a
    x2=(-b-sqrt(d))/2*a
    print(x1)
    print(x2)
if d==0:
    x=-b/(2*a)
    print(x)
if d<0:
    print("Корней нет") """
    
##Программа перевода чисел из 10 в 2

number=8

n=''
while(number!=0):
    n=str(number%2)+n
    number//=2
print(n)








    
