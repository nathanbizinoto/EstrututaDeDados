"""
DICIONÁRIO é uma estrutura de dados nativa da linguagem Python
capaz de armazenar múltiplos valores em uma única variável, por
meio de pares de chave-valor (key-value)
Um dicionário é delimitado por chaves {}. Diferentemente da
lista, que tem opções numeradas, o dicionário possui posições NOMEADAS.
Cada uma das posições nomeadas de um dicionário (ou
seja, cada par de chave-valor) é chamado de PROPRIEDADE.
"""

pessoa = {
    "nome": "Orozimo Oliveira Osório",
    "sexo": "M",
    "idade": 72,
    "peso": 76,
    "altura": 1.66,
    "aposentado": True,
    "filhos": ["Zeferino", "Adamastor", "Gercina"]
}

# Acessando o valor das propriedades
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Aposentado:", pessoa["aposentado"])

# Calculando o IMC
imc = pessoa["peso"] / pessoa["altura"] ** 2

# Nas f-strings delimitadas por aspas duplas, é necessário usar
# aspas simples nos nomes das propriedades, e vice versa
print(f"O IMC de {pessoa['nome']} é {imc}.")

########################################################################################

# Usando dicionários para representar formas geométricas planas

forma1 = {
    "base": 7.5,
    "altura": 12,
    "tipo": "R"         #Retãngulo
}

forma2 = {
    "base": 6,
    "altura": 2.5,
    "tipo": "T"    #Triângulo
}

forma3 = {
    "base": 5,
    "altura": 3,
    "tipo": "E"    #Elispse/círculo
}