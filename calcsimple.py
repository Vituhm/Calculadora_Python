# -*- coding: utf-8 -*-
"""CalcSimple.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WezEtB8kb5uKrqehGZ1smGprmqO-ULOy
"""

n1=(int(input("Informe um número: ")))
n2=(int(input("Informe um número: ")))

print("Escolha a operação a ser realizada: ")
print("1 = Adição (+)")
print("2 = Subtração (-)")
print("3 = Multiplicação (*)")
print("4 = Divisão (/)")

op=(int(input("Opção: ")))

if op == 1:
    print("Resultado: ", n1, "+", n2, "=", n1 + n2)
elif op == 2:
    print("Resultado: ", n1, "-", n2, "=", n1 - n2)
elif op == 3:
    print("Resultado: ", n1, "*", n2, "=", n1 * n2)
elif op == 4:
    if n2 == 0:
        print("Não é possível dividir por Zero.")
    else:
        print("Resultado: ", n1, "/", n2, "=", n1 / n2)
else:
    print("Opção inválida")