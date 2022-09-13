from art import logo
print(logo)
print('Welcome to Calculator')


def add(n1, n2):
    return n1 + n2
def substract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2


operations = {'+': add, '-': substract, '*': multiply, '/': divide}
def calculator():
    num1 = float(input('What\'s the first number? '))
    add_operation = True

    for symbol in operations:
        print(symbol)
    while add_operation:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input('What\'s the next number? '))
        function = operations[operation_symbol]
        answer = function(num1, num2)
        print(f'{num1}{operation_symbol}{num2}={answer}')

        decision = input(f'Type "y" to continue with {answer}, or type "n" to start new calculation:')
        if decision == 'y':
            num1 = answer
        else:
            add_operation = False
            calculator()

calculator()

