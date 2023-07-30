import sys, os

def limpar_tela():
	if sys.platform == "win32":
		os.system("cls")
	elif sys.platform == "linux":
		os.system("clear")
                

def gerar_menu(lista:list, text:str='') -> str:
    """
    Gera um menu a partir de uma lista de itens.

    Args:
        lista (list): A lista de itens do menu.

    Returns:
        str: Uma string com o menu formatado.

    Example:
        >>> lista = ['item1', 'item2', 'item3', 'item4']
        >>> resultado = gerar_menu(lista)
        >>> print(resultado)
        Menu:
        ---------------------
            [ 1 ] - item1
            [ 2 ] - item2
            [ 3 ] - item3
            [ 4 ] - item4
    """  

    if not lista:
        return "Menu vazio."

    menu_string = "Menu:\n---------------------\n"
    for i, item in enumerate(lista, start=1):
        menu_string += f"    [ {i} ] - {item}\n"
    print(menu_string)
    if text != '':print(text)
    opcao_escolhida = input("Informe o número da opção: ")
    if opcao_escolhida == '' or not opcao_escolhida.isnumeric():
        return '0'
    else:
        return opcao_escolhida