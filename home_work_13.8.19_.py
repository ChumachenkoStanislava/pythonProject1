tikets = int(input('Введите количество билетов:'))

sum = 0

for i in range(tikets):
    age = int(input('Введите возраст посетителя:'))
    if age > 25:
        sum += 1390
    elif age >= 18:
        sum += 990
if tikets > 5:
    sum = sum - (sum / 100 * 20)
print("Стоимость заказа:", sum)
