def operate(operator, *args):
    def add(*args):
        return sum(args)

    def subtract(x, *args):
        return x + sum(-y for y in args)

    def multiply(*args):
        result = 1
        for x in args:
            result *= x
        return result

    def divide(x, *args):
        result = x
        for value in args:
            result /= value
        return result

    if operator == "+":
        return add(*args)
    elif operator == "-":
        return subtract(*args)
    if operator == "*":
        return multiply(*args)
    if operator == "/":
        return divide(*args)

print(operate("+", 1, 2, 3))
print(operate("-", 1, 2, 3))
print(operate("*", 3, 4))
print(operate("/", 3, 4))