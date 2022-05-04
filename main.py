tickets = int(input("Введите количество билетов "))

price_1 = 1390# руб
price_2 = 990 # руб
age = int(input("Введите возраст " ))
if age < 18:
       print("Проход бесплатный ")
elif tickets > 3 and age >= 18 or age <= 25:
    print("Итого со скидкой =", tickets*price_2 * (1 - 10 /100), "руб.")

elif tickets < 3 and age > 25:
    print("Итого =", tickets*price_1, "руб.")
