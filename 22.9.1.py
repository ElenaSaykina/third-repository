def custom_sort(array):
    for i in range(len(array)):
        idx_min = i
        for j in range(i + 1, len(array)):
            if array[j] < array[idx_min]:
                idx_min = j
        array[i], array[idx_min] = array[idx_min], array[i]
    return array

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

# Основная программа
sequence = input("Введите последовательность чисел через пробел: ")
numbers = list(map(int, sequence.split()))

target_number = int(input("Введите любое число: "))

sorted_numbers = custom_sort(numbers)
position = binary_search(sorted_numbers, target_number)

if position < len(sorted_numbers) and sorted_numbers[position] >= target_number:
    print(f"Элемент, который меньше {target_number}, находится на позиции {position - 1} , следующий за ним больше или равен {target_number}.")
else:
    print("Такого элемента, который меньше и следующий за ним больше или равен указанному числу, в массиве нет.")