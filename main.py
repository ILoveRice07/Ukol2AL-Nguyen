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
    for i in range(n-1): #Cyklus pro vrácení na začátek pole
        for j in range(0, n-i-1):
            if array[j] > array[j+1]: #Porovnání čísel
                array[j], array[j+1] = array[j+1], array[j] #Prohození čísel
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
        random.shuffle(array2) #Gambling
        attempts += 1
        print(attempts)
    return attempts
    
print(bogo_sort(array2))
   
#Selection sort
array3 = [64, 34, 25, 5, 22, 11, 90, 12]
#Definování selection sortu
def selection_sort():
    n = len(array3)
    for i in range(n-1): #Cyklus pro vrácení na začátek pole
        min_index = i
        for j in range(i + 1, n):
            if array3[j] < array3[min_index]: #Porovnání čísel
                min_index = j #Rozděluje pole na nesetřízené a setřízené
        array3[i],array3[min_index] = array3[min_index],array3[i] #Prohazování čísel
        print(array3)

print(selection_sort())

#Insertion sort
array4 = [4, 53, 82, 1, 91, 74, 89, 43, 17, 31]
#Definování insertion sortu
def insertion_sort():
    n = len(array4)
    for i in range(1,n): #Cyklus pro vrácení na začátek pole
        insert_index = i
        current_value = array4.pop(i)
        for j in range(i-1, -1, -1):
            if array4[j] > current_value: #Porovnání čísel
                insert_index = j #Určuje hodnotu kam se hodnota vloží
        array4.insert(insert_index, current_value) #Vložení hodnoty do správné části v poli
        print(array4)

print(insertion_sort())
