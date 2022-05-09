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