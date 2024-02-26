# LISTAS são uma estrututa de dados nativa da
# linguagem Python. Elas permitem que vários
# valores possam ser associados a uma única 
# varíavel

#Lista de strings
legumes = ["batata", "cenoura", "beterraba", "mandioquinha", "batata doce"]

#Lista de números
nums = [3, 10, -7, 12.8, -0.5]

#Lista com valores de vários tipos
mistureba = ["Joaquim", 37, 1.81, 88, True]

## OPERAÇÕES SOBRE LISTAS ##

# 1) PERCURSO
# Percorrer uma lista significa visitar cada um de 
# seus itens e fazer algo com ele. No exemplo abaixo,
# vamos dar um print() em cada um dos legumes da lista
for leg in legumes:
        print(leg)

# Traço separador
print("-" * 60)        
        
# 3) INSERÇÃO DE UM NOVO ELEMENTO NA POSIÇÃO ESPECIFICADA: insert()
#    Parâmetros:
#    1° ~> a posição onde será feita a inserção
#    2° ~> O novo elemento a ser inserido

#Inserindo um novo elemento na QUARTA posiçao
legumes.insert(3, "tomate")
print(legumes) 

# Traço separador
print("-" * 60)

#4) ACESSANDO VALORES, INFORMANDO A RESPECTIVA POSIÇÃO
print("Elemento na QUINTA posição: ", legumes[4])
print("Elemento na PRIMEIRA posição: ", legumes[1])
print("Elemento na ÚLTIMA posição: ", legumes[-1])
print("Elemento na PENÚLTIMA posição: ", legumes[-2])

# Traço separador
print("-" * 60)

#5) SUBTITUINDO VALORES EXISTENTES

print("ANTES: ", legumes)

#Substituindo o valor na posição  3 (QUARTA posição)
legumes[3] = "vagem"
#Substituindo o valor na posição  0 (PRIMEIRA posição)
legumes[0] = "nabo"
#Substituindo o valor na posição -1 (ÚLTIMA posição)
legumes[-1] = "inhame"

print("DEPOIS", legumes)

#Traço separador
print("-" * 60)

# 6) DETERMINANDO A QUANTIDADE
print("Quantidade de elementos da lista de legumes: ", len(legumes))
print("Quantidade de elementos da lista de números: ",len(legumes) )

# Traço separador
print("-" * 60)

# 7) REMOVENDO O ÚLTIMO ELEMENTO B DE UMA LISTA: pop() (sem parãmetro)
print("ANTES:", legumes)
removido = legumes.pop()
print("Valor removido: ", removido)
print("DEPOIS: ", legumes)

#Traço separador
print("-" * 60)

# 8) REMOVENDO UM ELEMENTO POR SUA POSICAO: pop() com parâmetro
removido = legumes.pop(3)       #Remove o elemento da posição 3
print(legumes)

removido = legumes.pop(0)       #Remove o primeiro elemento
print("Valor removido da primeira posição: ", removido)
print(legumes)

# 9) REMOVENDO UM ELEMENTO POR SEU VALOR: remove()
removido = legumes.remove("mandioquinha")
print("Valor removido:", removido)
print(legumes)

# Traços separador
print("-" * 60)

# 10) JUNTANDO (CONCATENANDO) DUAS LISTAS: extend()
mais_legumes = ["abobrinha", "quiabo", "jiló", "cabotiá", "cará"]
legumes.extend(mais_legumes)

print(legumes)

#Traço separador
print("-" * 60)

# 11) FATIANDO UMA LISTA
#      Fatiar significa copiar um pedaço da lista (uma sublista)
#      para uma nova lista

# Cria uma sublista que contém os elementos das posições 2 a 5
# (posição 6 NÃO entra)
sublista2_5 = legumes[2:6]
print("Sublista de 2 a 5:", sublista2_5)

# Cria uma sublista que contém os elementos desde o início até a
# posição 6 (posição 7 NÃO entra)
sublista_inicio_6 = legumes[:7]
print("Sublista do início até a posição 6:", sublista_inicio_6)

# Cria uma sublista que contém os elementos da posição 4 até o final
sublista_4_fim = legumes[4:]
print("Sublista da posição 4 até o final:", sublista_4_fim)

