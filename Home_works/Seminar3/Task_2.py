# 3.2[18]: Требуется найти в списке целых чисел самый близкий по величине элемент к заданному числу X. 
# Пользователь вводит это число с клавиатуры, список можно считать заданным. Введенное число не обязательно содержится в списке.

#     Примеры/Тесты:
#     Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 0
#     Output: 2
#     Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 9

array = [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]

find = 1

for i in range(len(array)):
    for j in range(len(array)):
        if array[j] > array[i] :
            tmp = array[j]
            array[j] = array[i]
            array[i] = tmp

print(array)

for i in range(len(array)):
    if find < array[i]:
        result = array[i] - array[i-1]
        if result > 2 :
            print (array[i-1])
            break
        else:
            print (array[i])
            break
   

print(result )

