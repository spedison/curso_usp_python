"""
Desafio -
    Faça um programa que verifique o tipo de uma variável e escreva na tela str se a variável for uma string,
    int se ela for um inteiro e float se ela for um número decimal.
Observação 1:   O programa deve escrever na tela apenas int e não <class 'int'>.
                O mesmo vale para os outros tipos.
Observação 2: O mesmo programa deve funcionar para todos os tipos citados sem alterações.
Observação 3: Nesse programa você não deve pedir o valor da variável para o usuário, você deve você mesmo colocá-lo diretamente no código.


"""


def imprime_tipo_var(val):
    print("\n\nEntrada = [", val, "]")

    print("Saída 1 = ", sep="", end="")
    imprime_tipo_var1(val)

    print("\nSaída 2 = ", sep="", end="")
    imprime_tipo_var2(val)


def imprime_tipo_var1(val):
    if type(val) == type(0.0):
        print("É um Float", sep="", end="")
    elif type(val) == type(True):
        print("É um boolean", sep="", end="")
    elif type(val) == type(0):
        print("É um inteiro", sep="", end="")
    elif type(val) == type(' '):
        print("É um string", sep="", end="")
    else:
        print("Tipo não definido", sep="", end="")


def imprime_tipo_var2(val):
    tipo = str(type(val))
    tipo = tipo[8:]
    tipo = tipo[0:-2]
    print(tipo, sep="", end="")


floatvar = 32.0
intvar = 32
strvar = 'String'
boolvar = False

imprime_tipo_var(floatvar)
imprime_tipo_var(intvar)
imprime_tipo_var(strvar)
imprime_tipo_var(boolvar)
