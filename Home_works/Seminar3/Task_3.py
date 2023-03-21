# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.

# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.

# Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово,
#  которое содержит либо только английские, либо только русские буквы и заранее известно какой алфавит надо использовать.

#     Примеры/Тесты:
#     Input:   ноутбук
#     Output:  12
    
#     Input:   notebook
#     Output:  14

# ```(*)``` **Примечание.**
# Подумайте о том какие структуры данных здесь наиболее удобно использовать, чтобы просто проверять 
# в какую группу попадает буква, а также просто накапливать сумму очков.

word = input('Введите слово для подсчета очков в игре Скрабл: ')

direct_1 = dict(
    **dict.fromkeys(['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'], 1), 
    **dict.fromkeys(['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'], 1), 
    **dict.fromkeys(['D', 'G'], 2),
    **dict.fromkeys(['Д', 'К', 'Л', 'М', 'П', 'У'], 2),
    **dict.fromkeys(['B', 'C', 'M', 'P'], 3),
    **dict.fromkeys(['Б', 'Г', 'Ё', 'Ь', 'Я'], 3),
    **dict.fromkeys(['F', 'H', 'V', 'W', 'Y'], 4),
    **dict.fromkeys(['Й', 'Ы'], 4),
    **dict.fromkeys(['K'], 5),
    **dict.fromkeys(['Ж', 'З', 'Х', 'Ц', 'Ч'], 5),
    **dict.fromkeys(['J', 'X'], 8),
    **dict.fromkeys(['Ш', 'Э', 'Ю'], 8),
    **dict.fromkeys(['Q', 'Z'], 10),
    **dict.fromkeys(['Ф', 'Щ', 'Ъ'], 10)
)

sum_of_points = 0


print(sum(direct_1[letter.upper()] for letter in word if letter.upper() in direct_1))

