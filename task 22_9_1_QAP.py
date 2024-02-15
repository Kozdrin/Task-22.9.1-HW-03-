def binary_search(array, element): #Функция двоичного поиска
    left= 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_value = array[mid]
        if mid_value < element:
            left = mid + 1
        elif mid_value > element:
            right = mid - 1
        else:

           return mid

    return left

def check_input(): #Функция ввода данных
    while True:
        try:
            array = input("Введите последовательность чисел через пробел: ")
            lst_arr = list(map(int, array.split()))
            element = int(input("Введите число: "))
            return lst_arr, element
        except ValueError:
            print("Ошибка ввода. Пожалуйста, введите числа заново.")

def sort_list(lst_arr):  #Функция сортировки
    lst_arr.sort()

def main():  # Главная функция
    lst_arr, element = check_input()

    sort_list(lst_arr)

    index = binary_search(lst_arr, element)


    if index >= len(lst_arr):

        print("Ваше число больше всех чисел в последовательности.")

    elif index == 0 and element < lst_arr[0]:

        print("Ваше число меньше всех чисел в последовательности.")

    else:

        print("Индекс позиции, на которую должно быть вставлено ваше число:", index + 1)

    print("Список отсортированных чисел :", lst_arr)
if __name__ == "__main__":
    main()

