import time
print("Calculo Fatorial")

while True:
    txt = input("Entre com um número inteiro : ")
    numero = int(txt, 10)
    if numero < 0:
        continue
    else:
        break



fatorial = 1
while numero > 0:
# Colocando o Delay
#    time.sleep(10)
    print('.',sep='',end='')
    fatorial *= numero
    numero -= 1
else:
    print("\n\nResultado: ", fatorial)
