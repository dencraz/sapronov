while True:
    try:
        a = int(input("Введите трехзначное число: "))
        if 100 <= a <= 999:
            print("Вы ввели трехзначное число.")
            reversed_number = str(a % 10) + str(a % 100 // 10) + str(a // 100)
            print("Перевернутое число =", reversed_number)
            break
        else:
            print("Число не трехзначное. Пожалуйста, попробуйте снова.")
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректное целое число.")