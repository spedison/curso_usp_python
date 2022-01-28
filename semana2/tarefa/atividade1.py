'''
ATIVIDADE 1 - ENUNCIADO
Neste exercício você deverá produzir um pequeno programa que recebe um texto do usuário
e imprime na tela uma codificação vetorial desse texto, no estilo bag-of-words.
Uma codificação vetorial bag-of words é uma lista de números inteiros, cada um correspondendo
a uma palavra de um vocabulário pré-definido. O inteiro é 1 se a palavra correspondente aparece
no texto e 0, caso contrário.
Para produzir o programa, siga os seguintes passos:
PASSO 1 - Peça o texto de entrada ao usuário e salve-o numa variável.
PASSO 2 - Separe o texto numa lista contendo as palavras que o compõe.
PASSO 3 - Percorra a lista de palavras e, para cada palavra, verifique se o último caractere da palavra
é um dos sinais de pontuação contidos na variavel pontuacao. Se for, remova esse sinal
de pontuacao da palavra.
PASSO 4 - Percorra as palavras do vocabulário, armazenado na variável vocab, e verifique se cada uma
delas está contina na lista de palavras do texto ou não, adicionando valor 0 na posição dela na codificação, caso
ela não esteja, e 1 caso ela esteja.
PASSO 5 - Imprima na tela a codificação produzida.

Exemplo:
A entrada "A água corre sempre para o mar." deve retornar a seguinte resposta:
[0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0]

ADICIONE O SEU PROGRAMA NA PARTE INDICADA, SEM MOFDIFICAR AS OUTRAS LINHAS DESTE ARQUIVO.
ENTREGUE APENAS ESTE ARQUIVO NO MOODLE.

NOME COMPLETO DOS ALUNOS DO GRUPO:
Afranio Silva
Edison Ribeiro Araújo
Giovana da Silva Menas Muhl
Rafael Vieira Bonangelo
'''

vocab = ['a', 'amizade', 'ação', 'corre', 'do', 'filha', 'mar', 'não', 'o', 'para', 'pensamento',
         'preço', 'sempre', 'tem', 'água', 'é']

pontuacao = [',', '.', '!', '?']
#Insira sua resolução a partir daqui. Não altere os comandos anteriores.

texto_de_entrada = input("Informe o texto para processar :")

## Array de saida do vocabulário [0 ,0, 0, 0,....]
vocab_saida = [0] * len(vocab)

## Troca a pontucao por espaco
for ch_troca_por_espaco in pontuacao:
    texto_de_entrada = texto_de_entrada.replace(ch_troca_por_espaco, ' ')

## Extraindo palavra a palavra
palavras_separadas = texto_de_entrada.lower().split()

## Roda o dicionário para ver se existe ou não e marca a saída.
for posicao in range(len(vocab)):
    vocab_saida[posicao] = int(vocab[posicao] in palavras_separadas)

## Exibe a saída do processamento
print(vocab_saida)



