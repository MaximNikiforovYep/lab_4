def linear_function_generator():
    step = 0.01
    for i in range(0, 10001):
        try:
            x = i * step
            yield round(0.5 * x - 2, 3)
        except Exception as e:
            print(f"Ошибка при вычислении значения функции: {e}")
            break


gen = linear_function_generator()
for i in range(50):
    try:
        print(next(gen))
    except Exception as e:
        print(f"Ошибка при получении значения из генератора: {e}")