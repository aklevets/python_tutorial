# Функция для отображения букв из переданного аргументом текста

def show(txt):
    # Преобразование текста в список и его сортировка
    symbs = sorted(list(txt))
    # Отображение содержимого списка
    print(symbs)


# Вызов функции
show("Python")


# Функция для вычисления суммы квадратов натуральных чисел:
def sqsum(n):
    # Создание списка квадратов из натуральных чисел:
    nums = [k*k for k in range(1, n + 1)]
    # Результат функции
    return sum(nums)


# Переменная с числовым значением:
n = 10
# Вызов функции для вычисления суммы квадратов чисел:
print("Сумма квадратов чисел от 1 до ", str(n) + ":", sqsum(n))
