print('Задача 8. Тяжёлая жизнь')

# Георгий работает по часам и неофициально
# на какой-то сомнительной работе,
# на которой его зарплата высчитывается по следующей формуле: 
# 200 * hours / 2 ** 3 + hours
 
# Он хочет понять, сколько часов нужно отработать, 
# чтобы хватило на погашение кредита и на еду.
 
# Напишите программу,
# которая запрашивает у пользователя три числа:
# количество отработанных часов,
# остаток по кредиту и количество денег на еду.
# После этого рассчитывается зарплата по формуле,
# и если зарплата больше либо равна сумме денег на кредит и еду,
# то выводится сообщение: «Часов хватает. Можно отдохнуть»,
# в противном случае: «Часов не хватает. Придётся работать!».
 
# Пример:
# Введите отработанные часы: 80
# Введите остаток по кредиту: 1000
# Введите траты на еду: 5000
# Часов не хватает. Придётся поработать!

hours = int(input('Введите отработанные часы: '))
credit = int(input('Введите остаток по кредиту: '))
food = int(input('Введите траты на еду: '))

summ = 200*hours / 2**3 + hours

if summ >= credit + food:
  print('Часов хватает. Можно отдохнуть')
else:
  print('Часов не хватает. Придётся работать!') 