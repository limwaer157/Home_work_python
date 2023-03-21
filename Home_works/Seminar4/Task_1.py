#### 4.1[22]: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
#Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах. 
# Если таких чисел нет - выдать внятное диагностическое сообщение

# Наборы (списки) чисел можно считать заданными и не вводить с клавиатуры
    
# 	Примеры/Тесты:
#     Input1: 2 4 6 8 10 12 10 8 6 4 2
#     Input2: 3 6 9 12 15 18
#     Output: 6 12     Обратите внимание: Без скобочек, в одну строку

#     Input1: 2 4 6 8 10 10 8 6 4 2
#     Input2: 3 9 12 15 18
#     Output: Повторяющихся чисел нет


mnoj_list_1 = set([2 ,4, 6, 8 ,10 ,10 ,8 ,6 ,4 ,2])
mnoj_list_2 = set([3, 9, 12 ,15 ,18])

x = mnoj_list_1.isdisjoint(mnoj_list_2)  

if x == True:
    print("Повторяющихся чисел нет")
else:
    a = (mnoj_list_1.intersection(mnoj_list_2))
    print(a)
    new_list = a
    new_list_2 = list(new_list)
    new_list_2.sort()
    print(*new_list_2)






