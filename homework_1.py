#Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов. 
# Т е для k = 8, список будет выглядеть так: [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

""" list=[]
list1=[]
list2=[]
count=0
k=int(input("Введите число для Негафибоначи= "))
for i in range(k+1):
    if i in [0]:
        list.append(0)

    if i in [1,2]:
         list.append(1)
         list1.append(-1) 
    if i >2:
        i=list[i-2]+list[i-1]
        list.append(i)
        list1.append(-i) 

for i in range(len(list1)):
    if(i%2!=1):
        list1[i]=-list1[i]

list1=list1[::-1]
list2=list1+list
print(list2) """

## Найти НОК двух чисел
""" simple_numbers=[] ##3,5,7,11,13,17
for i in range(2,301):
    for j in range (2,i):
        if i%j==0:
            break
    else: simple_numbers.append(i)


a=int(input("Введите первое число: "))
b=int(input("Введите второе число: "))

for i in simple_numbers:
    if a%i==0 and b%i==0:
        print(f"НОК = {i} ")
        break
    if a%b==0:
        print(f"НОК = {b} ")
        break
    if b%a==0:
        print(f"НОК = {a} ")
        break
    else:
        print("Нет НОКа")
        break """

#Вычислить число  c заданной точностью d
#	Пример: при d = 0.001,  = 3.141. 10-1d10-10
## pi= 2piR/2R
## π = (4/1) - (4/3) + (4/5) - (4/7) + (4/9) - (4/11) + (4/13) - (4/15)

""" from datetime import datetime
from time import time

start_time=time()
pi=0
list=[]

for i in range(1,10000000):
    if i%2!=0:
        list.append(i)


for i in range(len(list)):
    if i%2!=0:
        list[i]=-list[i]
    pi+=4/list[i]
print(pi)
print(time()-start_time) """

##Составить список простых множителей натурального числа N


""" simple_numbers=[] ##3,5,7,11,13,17
for i in range(2,301):
    for j in range (2,i):
        if i%j==0:
            break
    else: simple_numbers.append(i)

n=int(input("Введите число n= "))
count=""
for i in simple_numbers:  
    if n%i==0:
        count+=f"{i} "
        n//=i
        if n%2==0:
            count+=" 2 "  
            n//=2
            print(f"число {n}")
            print(f"Множитель {count}")        
print(count)
     """

