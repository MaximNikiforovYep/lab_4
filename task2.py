def triangle_generator():
    try:
        for a in range(2, 21):
            for b in range(a + 1, 21):
                for c in range(b + 1, 21):
                    is_triangle = a + b > c and a + c > b and b + c > a
                    yield (a, b, c, is_triangle)
    except Exception as e:
        print(f"Ошибка при генерации комбинации: {e}")


gen = triangle_generator()
for i in range(20):
    try:
        print(next(gen))
    except StopIteration:
        print("Генератор завершил работу.")
        break
    except Exception as e:
        print(f"Ошибка при получении значения из генератора: {e}")
