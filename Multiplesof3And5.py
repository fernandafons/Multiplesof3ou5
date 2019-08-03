"""
Exercício ID 1 do project Euler:
EN: If we list all natural numbers bellow 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples
is 23. Find the sum of all the multiples of 3 or 5 below 1000.
PT: Encontre a soma de todos os multiplos de 3 ou 5 abaixo de 1000.
"""

print(sum([i for i in range(1, 1000) if (i % 3 == 0) or (i % 5 == 0)]))

"""
Explicação:

A ideia foi por meio de uma list comprehention retirar do intervalo entre 1 e 1000 todos os multiplos de 3 ou 5 e fazer
uma lista destes números para que os mesmos fossem somados e printados na tela.

#print
    imprime resultado na tela
#sum
    função que realiza a soma
#for
    laço de repetição
#range
    intervalo de números que deve ser realizada a verificação de multiplos
#if
    condicional que verifica se o resto da divisão entre i e 3 ou 5 é igual a 0


#Resolução alternativa 1 

soma = 0
for i in range(1,1000):
    if (i % 3 == 0) or (i % 5 == 0):
        soma = soma + i
        
print(soma)


#Resolução alternativa 2

print(sum(list(filter(lambda x: x if (x % 3 == 0) or (x % 5 == 0) else None, [i for i in range(1, 1000)]))))

"""
