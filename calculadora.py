def calcular(valor1, operador, valor2):
    flag = 0
    try:
        valor1 = float(valor1)
        valor2 = float(valor2)
    except ValueError:
        flag = 1
    if operador == "/" and valor2 == 0:
        flag = 1
    if flag == 1:
        return None
    else:
        if operador == "+":
            return valor1 + valor2
        elif operador == "-":
            return valor1 - valor2
        elif operador == "*":
            return valor1 * valor2
        elif operador == "/":
            return valor1 / valor2
        elif operador == "^":
            return valor1 ** valor2
        else:
            return None