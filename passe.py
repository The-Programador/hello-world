from TEXTO.senha import cadrastro, lertexto, excluir
from utilidadesCeV.dado.validadados import leiaint
from os import system
print('\033[34m----PALAVRA PASSE----\033[m')
while True:
    print('-'*72)
    print('\033[32m1 - GRAVAR | 2 - EXIBIR | 3 LIMPAR TELA | 4 - EXCLUIR ARQUIVO | 5 - SAIR\033[m')
    print('-'*72)
    resp = leiaint('\033[36mDigite a opção:\033[m ')
    if resp == 1:
        cadrastro()
    elif resp == 2:
        lertexto()
    elif resp == 3:
        system('clear')
    elif resp == 4:
        excluir()
    elif resp == 5:
        break
print('\033[31mFIM DO PROGRAMA\033[m')
