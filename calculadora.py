print ("Calculadora em PYTHON")
print (" Escolha uma das alternativas abaixo /n")
print (" Digite 1 - para Soma: ")
print (" Digite 2 - para Subtração: ")
print (" Digite 3 - para Multiplicação: ")
print (" Digite 4 - para Divisão: ")
op = input(" Selecione a operação: ")
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
if op == "1":
    soma = num1 + num2
    print ((num1), ' + ', (num2), ' = ', (soma))
if op == "2":
    sub = num1 - num2
    print ((num1), " - ", (num2), " = ", (sub))
if op == "3":
    mult = num1 * num2
    print ((num1), " * ", (num2), " = ", (mult))
if op == "4":
    divide = num1 / num2
    print ((num1), " / ", (num2), " = ", (divide))


