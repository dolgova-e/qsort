from random import randint
from multiprocessing import Process
import random
import timeit


# сортировка "пузырьком"
def bubbleSort(massive):
    for i in range(len(massive) - 1):
        for i in range(len(massive) - 1):
            if massive[i] <= massive[i + 1]:
                maxElem = massive[i + 1]
            else:
                maxElem = massive[i]
                massive[i] = massive[i + 1]
                massive[i + 1] = maxElem
    return massive


# сортировка Хоара
def hoarSort(massive):
    if len(massive) <= 1:
        return massive
    else:
        q = random.choice(massive)
        s_massive = []
        m_massive = []
        e_massive = []
        for n in massive:
            if n < q:
                s_massive.append(n)
            elif n > q:
                m_massive.append(n)
            else:
                e_massive.append(n)
        return hoarSort(s_massive) + e_massive + hoarSort(m_massive)


if __name__ == '__main__':
    print('Введите количество элементов: ', sep='', end='')
    N = int(input())
    sortElements = [randint(-1000, 1000) for i in range(N)]
    process_1 = Process(target=bubbleSort, args=('massive',))
    process_2 = Process(target=hoarSort, args=('massive',))
    process_1.start()
    process_2.start()
    process_1.join()
    process_2.join()
    print(*sortElements, '- исходный список')
    print(*bubbleSort([sortElements[i] for i in range(N)]), '- список отсортирован "Пузырьком" за',
          timeit.timeit("bubbleSort(sortElements)", globals=globals()), 'секунд')
    print(*hoarSort([sortElements[i] for i in range(N)]), '- список отсортирован сортировкой Хоара за',
          timeit.timeit("hoarSort(sortElements)", globals=globals()), 'секунд')
