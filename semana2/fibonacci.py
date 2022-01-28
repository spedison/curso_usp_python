posicao = int(input("Informe a posicao (maior que 2):"))

anterior_do_anterior = 0
anterior = 1
contador = 2

while contador <= posicao:
    numero_atual = anterior + anterior_do_anterior
    anterior_do_anterior = anterior
    anterior = numero_atual
    contador += 1

print(numero_atual)