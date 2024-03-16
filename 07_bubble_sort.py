comps = trocas = passd = 0

def bubble_sort(lista):

    global comps, trocas, passd
    comps = trocas = passd = 0
    while True:
        trocou = False

        for pos in range(len(lista) - 1):
            comps += 1
            if lista[pos + 1 ] < lista[pos]:
                lista[pos + 1], lista[pos] = lista[pos], lista[pos + 1]
                trocou = True
        
        if not trocou:
            break




#nums = [7, 5, 9, 0, 3, 4, 8, 1, 6, 2]
nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print('ANTES', nums)
bubble_sort(nums)
print('Depois:', nums)
print(f"Passadas: {passd}; comparações: {comps}; trocas: {trocas}")

import sys
sys.dont_write_bytecode = True # Impede a criação do cache
from time import time

from nomes_desord import nomes
hora_ini = time()
bubble_sort(nomes)
hora_fim = time()
print(nomes)
print(f"Tempo gasto: {(hora_fim - hora_ini) * 100}ms\n")
print(f"Passadas: {passd}; comparações: {comps}; trocas: {trocas}")  

exit()
