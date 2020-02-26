from random import randint

def quick_sort(arr):
    i_key = randint(0,len(arr)-1)
    arr_left = []
    arr_right = []
    
    for i in range(len(arr)):
        if arr[i] < arr[i_key]:
            arr_left.append(arr[i])
        elif i != i_key:
            arr_right.append(arr[i])
    
    if len(arr_left) > 1:
        arr_left = quick_sort(arr_left)
    if len(arr_right) > 1:
        arr_right = quick_sort(arr_right)
        
    arr_left.append(arr[i_key])
    for i in range(len(arr_right)):
        arr_left.append(arr_right[i])

    return arr_left
    
def print_arr(arr):
    for i in range(len(arr)):
        print(arr[i], end = ' ')
    print()

arr = input('Введите массив через пробел: ').split()
for i in range(len(arr)):
    arr[i] = int(arr[i])

print('\nИсходный массив:')
print_arr(arr)

arr = quick_sort(arr)

print('Отсортированный массив:')
print_arr(arr)

