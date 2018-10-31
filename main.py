from automato import *
import re
import os

def limpaTela(wait=True):
    if wait:
        input('Pressione ENTER para continuar...')
    os.system('cls' if os.name == 'nt' else 'clear')

    return

def parseFile(file):
    automato = {}
    lines = file.readlines()

    # Primeira linha -> Nome, estados, transicoes, estado inicial, estados finais
    args = lines[0].split('=')[1][1:-2]
    automato['nome'] = lines[0].split('=')[0]
    estados, transicoes, inicial, finais = re.findall(r'(?:\w+,)*\w+', args)

    # PARSE TRANSICOES
    automato['transicoes'] = transicoes.split(',')

    # PARSE ESTADOS
    automato['estados'] = {}
    for estado in estados.split(','):
        automato['estados'][estado] = {}
        for transicao in automato['transicoes']:
            automato['estados'][estado][transicao] = []



    # PARSE ESTADO INICIAL
    automato['inicial'] = inicial

    # PARSE ESTADOS FINAIS
    automato['finais'] = finais.split(',')

    regex = re.compile("=|\)|\(|,|\n")
    for line in lines[2:]:
        query = [x for x in regex.split(line) if x != '']
        automato['estados'][query[0]][query[1]].append(query[2])

    return automato

def main():
    file = open(input('Digite o nome do arquivo que possui os dados do automato COM EXTENSAO: '), 'r')
    automato = Automato(parseFile(file))
    file.close()
    print('Automato do arquivo:')
    print(automato, end='\n\n')
    automato.determinizar(True)

    while(True):
        print()
        print('Automato determinizado:')
        print(automato, end='\n\n')
        option = input('1 -> Inserir nome de um arquivo do qual as palavras para teste serao lidas\n2 -> Inserir palavra a ser reconhecida manualmente\n3 -> Encerrar programa\nEscolha: ')
        if option == '1':
            limpaTela(False)
            palavras = open(input('Digite o nome do arquivo COM EXTENSAO: '), 'r', encoding="windows-1252")
            for line in palavras.readlines():
                if automato.reconhece(line):
                    print('ACEITA')
                else:
                    print('REJEITA')
            limpaTela()
        elif option == '2':
            while(True):
                limpaTela(False)
                palavra = input('Insira a palavra separando as transicoes por virgula.\nCaso queira parar de inserir palavras, apenas pressione enter...\n')
                if palavra == '':
                    break
                if automato.reconhece(palavra):
                    print('ACEITA')
                else:
                    print('REJEITA')
                limpaTela()
            limpaTela(False)
        elif option == '3':
            limpaTela(False)
            print('====================\nENCERRANDO PROGRAMA\n====================')
            break;
        else:
            limpaTela(False)
            print('ENTRADA INVALIDA - SELECIONE UMA OPCAO VALIDA ABAIXO\n')

    return

if __name__ == "__main__":
    main()
