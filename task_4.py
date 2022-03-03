print('Задача 4. Калькулятор скидки')

# Андрей переехал на новую квартиру, и ему нужно купить три стула в разные комнаты.
# Естественно, цена на стулья в разных магазинах различается,
# а где-то ещё и скидка есть. 
# Вот для одного из таких магазинов он и написал калькулятор скидки, 
# чтобы проще ориентироваться в ценах.
 
# Напишите программу,
# которая запрашивает три стоимости товара и вычисляет сумму чека. 
# Если сумма чека превышает 10 000 рублей,
# то нужно вычесть из этой суммы скидку 10% (умножить на 10, разделить на 100). 
# В конце вывести итоговую сумму на экран.

chair1 = int(input('Введите сумму первого стула: '))
chair2 = int(input('Введите сумму второго стула: '))
chair3 = int(input('Введите сумму трерьего стула: '))

summ = chair1 + chair2 + chair3

if summ > 10000:
  summ = summ - summ * 0.1

print('Итоговая сумма:', summ)