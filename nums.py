#Лабораторная 3
Print('Это функция,которая получает список nums  длины n в котором находятся числа nums[I] в диапазоне [1, n], и возвращает список чисел в диапазоне [1, n], которых нет в списке nums.')
def find_missing_nums(nums):
    r = len(nums)
    s = []
    y = False
    for i in range (1,r+1):
        for j in range (0,r):
            if i == nums[j]:
                y = True
                continue
        if not y:
            s.append(i)
        y = False
    return s 
#Вывод функции
