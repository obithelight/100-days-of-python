from calc_functions import add, subtract, multiply, divide

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

choice = ""
for symbol in operations:
    choice += f"{symbol} "
