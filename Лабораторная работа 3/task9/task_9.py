salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение
while months > 0:
    if months < 10:
        spend = spend + spend * increase
    have_money = salary - spend
    months -= 1
    need_money += have_money

print(abs(round(need_money)))
