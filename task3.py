def get_top_four_unique_numbers(input_string):
    try:
        numbers = list(map(int, input_string.split()))
        unique_numbers = sorted(set(numbers), reverse=True)
        return unique_numbers[:4]
    except ValueError:
        print("Ошибка: введены некорректные данные. Убедитесь, что строка содержит только целые числа.")
        return []
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")
        return []


input_string = input("Введите список целых чисел, разделённых пробелами: ")
top_four = get_top_four_unique_numbers(input_string)
print("Четыре наибольших уникальных значения:", top_four)
