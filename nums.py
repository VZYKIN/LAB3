#Лабораторная 3
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
