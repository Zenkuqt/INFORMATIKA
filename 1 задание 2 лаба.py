money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
count = 0
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
money_x = money_capital  # подушка безопасности в данном месяце
spend_x = spend  # расходы в данном месяце
while True:
    if money_x + salary < spend_x:
        break
    count += 1
    money_x = money_x + salary - spend_x
    spend_x *= (1 + increase)
print("Количество месяцев, которое можно протянуть без долгов:", count)
