def selection_sort(lista, val):
    """
    ALGORITMO DE ORDENACAO SELECTION SORT
    Isola (seleciona) o primeiro elemento da lista, e em seguida,
    encontra o menor valor no restante da lista. Se o valor
    encontrado fro menor entre eles. Continuando, seleciona o segundo
    elemento da lista, buscando pelo menor valor das posições
    subsequentes. Faz a troca entre os dois valores, se necessário.
    O processo se repete até que o penultimo elemento da lista
    seja selecionado, comparado com o último e feita a troca entre
    eles, se for o caso.
    """
    global comps, trocas, passd
    comps = trocas = passd = 0

    # Loop que vai da primeira até a a PENÚTLIMA posição, para
    # selecionar o elemento que será comparado aos demais
    for pos_sel in range(len(lista) - 1):

        passd += 1

        # Inicia supondo que a posição do menor valor do resto 
        # da lista é o que está imediatamente à frente do selecionado
        pos_menor = pos_sel + 1

        # Percorre o restante da lista, da posição seguinte a pos_menor
        #até a última posição
        for pos in range(pos_menor + 1, len(lista)):
            #Se o valor encontrado na posição pos for MENOR do que o 
            # valor atual de pos_menor, então atualiza pos_menor para 
            # a memsa posição de pos
            comps += 1
            if lista[pos] < lista[pos_menor]: pos_menor = pos
        
        # <~ CUIDADO COM A IDENTAÇÃO!
        # Neste ponto, já terminamos de percorrer o restante da lista e 
        # já sabemos a posição do menor elemento que há nele. Comparamos,
        # então, os valores das posições pos_menor e pos_sel. Se o 
        # primeiro for MENOR do que o segundo, fazemos a troca entre eles
        comps += 1
        if lista[pos_menor] < lista[pos_sel]:
            lista[pos_menor], lista[pos_sel] = lista[pos_sel], lista[pos_menor]
            trocas += 1

###################################################################################

nums = [7, 5, 9, 0, 3, 4, 8, 1, 6, 2]

print('ANTES', nums)
selection_sort(nums)
print('Depois:', nums)
#print(f"Passadas: {passd}; comparações: {comps}; trocas: {trocas}")