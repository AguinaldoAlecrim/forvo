from forvo import Forvo
from func import (
    gerar_menu,
    limpar_tela
)
import time

if __name__ == '__main__':
    f = Forvo()
    operations = {
                    '1': f.repetir_audio,
                    '3':exit
                }
    while True:
        limpar_tela()
        op_escolhida = gerar_menu(['Digitar uma palavra', 'Sair'])
        if (op_escolhida == '1'):
            limpar_tela()
            word = input('Digite a palavra para ouvir a pronúncia:\n')
            result = f.play(word)
            if result != True:
                print('+'*30, 'Expressão não encontrada. Retornando...', sep='\n')
                time.sleep(2)
                continue
            while True:
                limpar_tela()                
                op = gerar_menu(['Repetir', 'Voltar', 'Sair'])
                if op == '2': break
                if op in operations:operations[op]()
        if (op_escolhida == '2'):
            limpar_tela()
            exit()


