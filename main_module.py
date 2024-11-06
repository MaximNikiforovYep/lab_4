def sub_linear_function_generator():
    step = 0.01
    for i in range(0, 10001):
        try:
            x = i * step
            yield round(0.5 * x - 2, 3)
        except Exception as e:
            print(f"Ошибка при вычислении значения функции: {e}")
            break


def linear_function_generator():
    gen = sub_linear_function_generator()
    for i in range(50):
        try:
            print(next(gen))
        except Exception as e:
            print(f"Ошибка при получении значения из генератора: {e}")


def sub_triangle_generator():
    try:
        for a in range(2, 21):
            for b in range(a + 1, 21):
                for c in range(b + 1, 21):
                    is_triangle = a + b > c and a + c > b and b + c > a
                    yield (a, b, c, is_triangle)
    except Exception as e:
        print(f"Ошибка при генерации комбинации: {e}")


def triangle_generator():
    gen = sub_triangle_generator()
    for i in range(20):
        try:
            print(next(gen))
        except StopIteration:
            print("Генератор завершил работу.")
            break
        except Exception as e:
            print(f"Ошибка при получении значения из генератора: {e}")


def sub_get_top_four_unique_numbers(input_string):
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


def get_top_four_unique_numbers():
    input_string = input("Введите список целых чисел, разделённых пробелами: ")
    top_four = sub_get_top_four_unique_numbers(input_string)
    print("Четыре наибольших уникальных значения:", top_four)


def main():
    while True:
        print("\nВыберите задачу:")
        print("1 - Задание 1: Генерация значений линейной функции")
        print("2 - Задание 2: Проверка трёх целых чисел на возможность образовать треугольник")
        print("3 - Задание 3: Определение четырёх наибольших уникальных чисел из строки")
        print("0 - Выход")
        try:
            input_num = input()
            if input_num == '1':
                linear_function_generator()
            elif input_num == '2':
                triangle_generator()
            elif input_num == '3':
                get_top_four_unique_numbers()
            elif input_num == '0':
                break
            else:
                print("Неверный ввод.")
        except Exception as e:
            print("Ошибка" + e)


if __name__ == '__main__':
    main()