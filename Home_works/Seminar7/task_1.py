# 7.1[34]: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
#  Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 

# Написать функцию, которая принимает строку текста и проверяет ее ритм (по Винни-Пуху) 
# Если ритм есть, функция возвращает True, иначе возвращает False

# 	Примеры/Тесты:
# 	    <function_name>("пара-ра-рам рам-пам-папам па-ра-па-дам") -> True
# 	    <function_name>("пара-ра-рам рам-пум-пупам па-ре-по-дам") -> True
# 	    <function_name>("пара-ра-рам рам-пуум-пупам па-ре-по-дам") -> False
# 	    <function_name>("Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па") -> False
# 	    <function_name>("Пам-парам-пурум Пум-пурум-карам") -> True

# **Примечание.**

# - Подумайте об эффективности алгоритма. Какие структуры данных будут более эффективны по скорости.
# - Алгоритм должен работать так, чтобы не делать лишних проверок. Подумайте, возможно некоторые проверки не нужны.


data = "пара-ра-рам рам-пуум-пупам па-ре-по-дам"



def win_and_puh(data:str):
    result = []
    for word in data.split():
        voice = ['а','у' ,'е']
        count = 0
        for i in word:
            if i in voice:
                count += 1
        result.append(count)
    if len(set(result)) == 1:
        return(True)
    return(False)


print(win_and_puh(data))
