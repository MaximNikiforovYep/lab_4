# Math Generators App

## Описание
Math Generators App — это приложение на Python, которое решает три задачи с использованием генераторов. В каждой задаче генерируются данные и производятся расчёты согласно условиям. Программа подходит для демонстрации работы с генераторами и итераторами в Python.

### Задания:

1. **Генерация значений линейной функции**
   - Генерируются значения линейной функции \( f(x) = 0.5x - 2 \) для значений \( x \) от 0 до 100 с шагом 0.01.
   - Выводятся первые 50 сгенерированных значений.

2. **Проверка тройки чисел на возможность образовать треугольник**
   - Программа перебирает все комбинации трёх целых положительных чисел в диапазоне от 2 до 20.
   - Для каждой комбинации проверяется, могут ли числа быть длинами сторон треугольника. Результатом является булево значение (True или False).
   - Выводятся первые 20 комбинаций и их результат.

3. **Выбор четырёх наибольших уникальных значений**
   - На вход подаётся строка целых чисел, разделённых пробелами.
   - Программа выбирает четыре наибольших уникальных значения из этого списка и выводит их в отсортированном порядке.

## Инструкции по запуску
1. Убедитесь, что у вас установлен Python 3.12+
2. Скачайте или клонируйте репозиторий с приложением.
3. Перейдите в директорию с проектом
4. Запустите файл main_module.py:
python main_module.py

## Краткая справка
- **Задание 1**:
  - Функция `linear_function_generator()` генерирует значения функции \( f(x) = 0.5x - 2 \) с шагом 0.01 для \( x \) от 0 до 100.
  - Выводятся первые 50 значений.

- **Задание 2**:
  - Функция `triangle_generator()` генерирует все комбинации трёх чисел в диапазоне от 2 до 20.
  - Проверяет, могут ли числа быть длинами сторон треугольника, возвращает кортеж `(a, b, c, is_triangle)`.
  - Выводятся первые 20 комбинаций.

- **Задание 3**:
  - Функция `get_top_four_unique_numbers(numbers_str)` принимает строку с числами, разделёнными пробелами, и возвращает четыре наибольших уникальных числа в отсортированном порядке.
  
## Пример использования
Программа автоматически выводит первые 50 значений для задачи 1, первые 20 результатов для задачи 2, и результат работы функции для задачи 3.
