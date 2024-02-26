sum_to_pay = 0
qnt_tickets = int(input("Введите колличество билетов:"))
if qnt_tickets > 10:
    print()
    print(
        "Максимальное колличество билетов на один заказ: 10. Чтобы закать 11 и болeе билетов, обратитесь в службу заказов по телефону (905)999 999 99")
    exit()
else:
    for age in range(qnt_tickets):
        age = int(input("Введите возраст посетителя:"))
        if age < 18:
            sum_to_pay += 0
        elif 18 <= age < 25:
            sum_to_pay += 990
        elif age >= 25:
            sum_to_pay += 1390

print()
if qnt_tickets > 3:
    sum_to_pay *= 0.9
    print("Общая сумма к оплате за:", + qnt_tickets, "билет(а/ов) после 10% скидки: ", sum_to_pay, "руб")

else:
    print("Общая сумма к оплате за:", + qnt_tickets, "билет(а/ов): ", sum_to_pay, "руб")
print()
print("Спасибо за ваш заказ.")
