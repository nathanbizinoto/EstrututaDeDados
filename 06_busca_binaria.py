def busca_binaria(lista, val):
    """
    ALGORITMO DE BUSCA BINÁRIA
    
    Dados uma lista, que deve estar PREVIAMENTE ORDENADA,
    e um valor de busca, divide a lista em duas partes,
    procurando pelo valor de busca apenas na metade onde
    o valor de busca poderia estar. Novas subdivisões são
    feitas até que se encontre o valor de busca ou que
    conclui que o valor de busca não existe na lista
    """

    ini = 0                # Posição inicial da lista
    fim = len(lista) - 1   # Posição final da lista

    while ini <= fim:
        # Calculando o meio da lista
        meio = (ini + fim) // 2     #Divisão inteira

        # Verifica se o valor que está no meio da lista
        # é igual ao valor de busca. Em caso afirmativo,
        # retornamos a posição do meio, pois o valor de
        # busca foi encontrado

        if val == lista[meio]:
            return meio
    
        # Senão, se o valor de busca é menor do que o
        # valor do meio, reinicia a busca na metade esquerda
        # da (sub)lista
        elif val < lista[meio]:
            fim = meio - 1

        # Por fim, se o valor de busca é MAIOR do que o 
        #valor do meio, reinicia a busca na metade direita
        # da (sub)lista
        else:
            ini = meio + 1

    # <- CUIDADO COM A IDENTAÇÃO AQUI!
    # Se chegamos a este ponto, é porque
    # o valor de busca não existe na lista
    return -1
    #######################################################################