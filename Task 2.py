# 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


# Вариант 1
def m_list(list):
    x = len(list) // 2 + 1 if len(list) % 2 != 0 else len(list) // 2 
    new_lst = [
        list[i]*list[len(list)-i-1] 
        for i in range(x)
        ]
    print(new_lst)

list = list(map(int, input("Введите числа через пробел: ").split()))
m_list(list) 