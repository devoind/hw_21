from my_class import Request, storage_1, storage_2, shop_1

print("Здравствуйте!")

while True:
    print("Текущая операция!")
    print(f"storage_1: {storage_1}")
    print(f"storage_2: {storage_2}")
    print(f"shop_1: {shop_1}")

    user_input = input("Введите команду:\n")

    if user_input == "стоп":
        break
    else:
        try:
            req = Request(user_input)
            req.move()
        except Exception as e:
            print(f"Произошла ошибка{e}, перемещайте дальше")


