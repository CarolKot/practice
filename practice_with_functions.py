# практика с функциями

# Задача. Напиши функцию, которая принимает два числа и возвращает их сумму.
while True:

    def summ():
     x = int(input('Введите число х: '))
     sign = input('Сделайте выбор: + - * / ')
     y = int(input('Введите число y: '))
     if sign == '+':
        return x + y
     if sign == '-':
        return x - y
     if sign == '*':
        return x * y
     if sign == '/':
        return x / y

    
    result = summ()
    print(f'Итого: {result}')