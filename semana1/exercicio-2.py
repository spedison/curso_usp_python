entrada_str = input("Informe texto com mais de 3 caracteres : ")

if len(entrada_str) < 3:
    print("Entrada deve ser maior que 3 carcteres.")
else:
    entrada_sem_3 = entrada_str[0:2] + entrada_str[3:]
    print("Entrada = ", entrada_str)
    print("Saida   = ", entrada_sem_3)


