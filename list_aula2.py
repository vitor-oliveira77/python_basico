# CREATE, READ, UPDATE, DELETE (CRUD) 
#lista.clear() = limpa a lista.

lista = [10,20,30,40] 
lista[2] = 300
del lista [2] # deleta um elemento da lista
print(lista[2]) 

lista.append(50) #adiciona valores ao final da lista
lista.append(6) 
lista.append(31) 
print(lista) 

lista.pop() # remove o ultimo elemento da lista 

ultimo_valor = lista.pop() # é possivel remover o elemento e colocar em uma variável
print(lista, 'Removido', ultimo_valor) 

lista.insert (0,5) # insert inclui elementos na lista, 
#o primeiro número é o indice e o segundo o valor a ser adicionado.
