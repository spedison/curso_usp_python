populacao_inicial_pais_1 = int(input("Qual a população Inicial do Pais 1 : "))
populacao_inicial_pais_2 = int(input("Qual a população Inicial do Pais 2 : "))
taxa_crescimento_pais_1 = float(input("Qual a taxa de crescimento do Pais 1 : "))
taxa_crescimento_pais_2 = float(input("Qual a taxa de crescimento do Pais 2 : "))

ano = 0

populacao1 = populacao_inicial_pais_1
populacao2 = populacao_inicial_pais_2

while populacao1 < populacao2:

    populacao1 *= taxa_crescimento_pais_1
    populacao2 *= taxa_crescimento_pais_2
    ano += 1

print(f"No ano {ano}, a pop do pais 1 é {populacao1} e a pais 2 é {populacao_inicial_pais_2}")