def get_age():
    was_born = int(input("Введите год вашего рождения "))
    data = int(input("Введите текущий год"))

    age = data - was_born
    print("Ваш возраст ", age, " лет")


get_age()
