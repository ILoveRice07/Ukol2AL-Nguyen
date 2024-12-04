import random

#Vytvoření pole
array = [4, 98, 7, 24, 16, 0, 37, 63, 52, 86]

#Použití jednoduchého sortu k třídění pole
array.sort()
print(array)

#Bubble sort
#Definování buble sortu
def bubble_sort():
    n = len(array)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
            print(array)
    return array

print(bubble_sort())

#Bogo sort
array2 = [41, 17, 75, 3, 96, 19, 27, 16, 82, 34]
#Definování vytřídění
def is_sorted(array2):
    return all(array2[i] <= array2[i+1] for i in range(len(array2)-1))

#Definování bogo sortu
def bogo_sort(array2):
    attempts = 0
    while not is_sorted(array2):
        random.shuffle(array2)
        attempts += 1
        print(attempts)
    return attempts
    
print(bogo_sort(array2))
   
#Selection sort
array3 = [64, 34, 25, 5, 22, 11, 90, 12]
#Definování selection sortu
def selection_sort():
    n = len(array3)
    for i in range(n-1):
        min_index = i
        for j in range(i + 1, n):
            if array3[j] < array3[min_index]:
                min_index = j
        array3[i],array3[min_index] = array3[min_index],array3[i]
        print(array3)

print(selection_sort())
