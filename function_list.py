def get_2_power_2_list():
    qnt = int(input("Введите число, до каких величин будет доходить список из 2   "))
    k = list(range(qnt+1))
    i = 0
    while qnt >= i:
        k[i] = 2**i
        i = i + 1

    print(k)


get_2_power_2_list()

