money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

while money_capital > 0:
    if month > 0:
        spend = spend + spend * increase
    money_capital = money_capital - spend + salary
    have_money_left = money_capital
    month += 1
    if spend > have_money_left:
        break


print(month)
