# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo. Não exibi valores invertidos.
# Permutação - Ordem importa, exibi todas as possibilidades de combinação
# Produto - Ordem importa e repete valores únicos

from itertools import combinations, permutations, product


def print_iter(iterator):
    print(*list(iterator), sep='\n')


pessoas = [
    'João', 'Joana', 'Luiz', 'Leticia',
]

camisetas = [
    ['Preta', 'Branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unissex'],
    ['algodão', 'poliéster']
]

print_iter(combinations(pessoas, 2))
print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas))
