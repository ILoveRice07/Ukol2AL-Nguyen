#Vytvoření pole
array = [4, 98, 7, 24, 16, 0, 37, 63, 52, 86]

#Použití jednoduchého sortu k třídění pole
array.sort()
print(array)

#Tvorba bubble sortu
def bubble_sort():
    n = len(array)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
            print(array)
    return array

print(bubble_sort())
