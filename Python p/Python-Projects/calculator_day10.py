
# Calculator

# Add
def add(n1, n2):
    return n1 + n2

# Subtract


def subtract(n1, n2):
    return n1 - n2

# Multiply


def multiply(n1, n2):
    return n1 * n2

# Divide


def divide(n1, n2):
    return n1 / n2


operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = int(input("What's the first number?: "))
for symbol in operators:
    print(symbol)
operator_symbol = input("Pick an operation from the line above: ")
num2 = int(input("What's the second number?: "))
calculation_function = operators[operator_symbol]
calculation_function(num1, num2)
answer = calculation_function(num1, num2)
print(f"{num1} {operator_symbol} {num2} = {answer} ")

