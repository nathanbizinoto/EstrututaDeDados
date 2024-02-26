# range() é uma função que gera uma faixa de números.
# É muito usada em associação com listas

# 1) range() COM *UM* PARÂMETRO
#   Gera uma faixa numérica que vai de 0 até o valor
#   do parâmetro -1
for num in range(10):
    print(num)

print("-" * 60)

# 2) range() COM *DOIS* PARÂMETROS
#     1° parâmetro ~> valor inicial da faixa
#     2° parãmetro ~> valor final da faixa( não incluídos)
for x in range(10, 16):
    print(x)

print("-" * 60)

# 3) range() com TRÊS PARAMETROS
#     1° parâmetro ~> valor inicial da faixa
#     2° parametro ~> valor final da faixa (não incluido)
#     3° parãmetros ~> passo (intervalo entre um número e outro)
for n in range(1, 22, 3):   # De 1 a 21 contando de 3 em 3
    print(n)

print("-" * 60)

# range() com passo negativo
for i in range(10, 0, -1): Contagem regressiva de 
