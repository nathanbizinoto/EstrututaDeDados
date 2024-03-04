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
        