# #### 5.1[26]: Напишите рекурсивную функцию для возведения числа a в степень b. 
# Разрешается использовать только операцию умножения. Циклы использовать нельзя

#     Примеры/Тесты:
#     <function_name>(2,0) -> 1
#     <function_name>(2,1) -> 2
#     <function_name>(2,3) -> 8
#     <function_name>(2,4) -> 16

a=int(input("number -  "))
b = int(input("math pow -  "))

def math_pow(a,b):
    if b == 0 : return 1
    
    return a * math_pow(a , b- 1)
        
        

print(math_pow(a,b))
