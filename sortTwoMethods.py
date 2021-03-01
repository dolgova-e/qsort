from random import randint
import random
import timeit


# сортировка "пузырьком"
def bubbleSort(massive):
    for i in range(N - 1):
        for i in range(N - 1):
            if massive[i] <= massive[i + 1]:
                maxElem = massive[i + 1]
            else:
                maxElem = massive[i]
                massive[i] = massive[i + 1]
                massive[i + 1] = maxElem
    return massive


# сортировка Хоара
def hoarSort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
        s_nums = []
        m_nums = []
        e_nums = []
        for n in nums:
            if n < q:
                s_nums.append(n)
            elif n > q:
                m_nums.append(n)
            else:
                e_nums.append(n)
        return hoarSort(s_nums) + e_nums + hoarSort(m_nums)


print('Введите количество элементов: ', sep='', end='')
N = int(input())
sortElements = [randint(-1000, 1000) for i in range(N)]
print(*sortElements, '- исходный список')
print(*bubbleSort([sortElements[i] for i in range(N)]), '- список отсортирован "Пузырьком" за',
      timeit.timeit("bubbleSort(sortElements)", globals=globals()), 'секунд')
print(*hoarSort([sortElements[i] for i in range(N)]), '- список отсортирован сортировкой Хоара за',
      timeit.timeit("hoarSort(sortElements)", globals=globals()), 'секунд')
