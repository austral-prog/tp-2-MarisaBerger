def change():
    expense = 23.75
    money = 100
    print("ingresar gasto")
    print(expense)
    print("dinero recibido")
    print(money)
    print()
    print("vuelto")
    print()

    print("pesos:")
    print(int(money - expense))
    print("centavos:")
    print(int(((money-expense)-int(money-expense))*100))
