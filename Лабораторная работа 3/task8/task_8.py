money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

while spend < money_capital:
    if month > 0:
        spend = spend + spend * increase
    money_capital = money_capital - spend + salary
    month += 1



print(month)
