# Listas - listas em pyhton são conjuntos ordenados de objetos, onde não é nescessário que todos tenham o mesmo tipo
# são criadas colocando os elementos separados por vírgula dentro de colchetes []
lista = ["Bananas", "morangos", "maças", "peras"]
print(lista)
lista = [1, 4, 6, 2, 7, 10]
print(lista)
lista = ["Bananas", 4, 6, "maças", 7, 10]
print(lista)
# podemos pegar o tamanho da lista pela função len
print(len(lista))
# Por serem ordenadas podemos pegar o elemento da lista pelo indice começando por 0
print(lista[0])
print(lista[2])
# podemos alterar o elemento da lista
lista[2] = "peras"
print(lista)
# e podemos remover algum elemento da lista
lista.remove(7)
print(lista)

# ToDo crie duas listas de compras dentro de outra lista
# a primeira lista deve ser colocado os itens pera, maça e banana
compras1 = ["pera", "maça", "banana"]

# e na segunda deve ser colocada arroz, fejão, macaxeira e tapioca
compras2 = ["arroz", "feijão", "mandioca", "tapioca"]

# imprima a lista, Resultado esperado [['pera', 'maça', 'banana'], ['arroz', 'fejão', 'macaxeira', 'tapioca']]
sacoladecompras = [compras1, compras2]
print(sacoladecompras)

#ToDo, substitua o item maça por pêssego, e remova o item tapioca da segunda lista
print(compras1[2])
compras1[2] = "pêssego"
print(compras1[2])
compras2.remove("tapioca")

# imprima a lista, Resultado esperado [['pera', 'pêssego', 'banana'], ['arroz', 'fejão', 'macaxeira']]
print(compras1)
print(compras2)


# compras1 = ["filé mignon", "ferango", "mantega", "requeijão", "maça", "banana"]
# compras2 = ["coxinha", "nescau", "leite", "maconha medicinal", "cigarro", "arroz", "feijão", "mandioca", "tapioca"]
# sacolacompras = []
# sacoladecompras = [compras1, compras2]

# sacolacompras.append(compras1)
# sacolacompras.append(compras2)
# print(sacoladecompras)

# Tuples - Tuples tem todas as caracteristicas de listas com uma pequena diferença,
# após criados, seus elementos não podem ser modificados
# são criadas colocando os elementos separados por vírgula dentro de parênteses ()
tup = ("Bananas", "morangos", "maças", "peras")
print(tup)
tup = (1, 4, 6, 2, 7, 10)
print(tup)
tup = ("Bananas", 4, 6, "maças", 7, 10)
print(tup)
# podemos pegar o tamanho da tuple pela função len
print(len(tup))
# Por serem ordenadas podemos pegar o elemento da tuple pelo indice começando por 0
print(tup[0])
print(tup[2])
# NÃO podemos alterar o elemento da tuple
tup[2] = "peras" # essa linha gera erro
print(tup)

# PS - É permitido criar Listas de Listas, Listas de Tuples, Tuple de listas ou Tuple de Tuples
LL = [[1, 2], [3], [4, 5, 6]]
print(LL)
LT = [(1, 2), (3), (4, 5, 6)]
print(LT)
TL = ([1, 2], [3], [4, 5, 6])
print(LT)
TT = ((1, 2), (3), (4, 5, 6))
print(TT)
# também podemos criar listas e tuples vazias
LVazia = []
print(LVazia)
TVazia = ()
print(TVazia)

# Filas - Python não tem uma estrutura específica para filas, mas podemos usar as funções append e pop(0) para simulá-la
# https://docs.python.org/2/tutorial/datastructures.html#using-lists-as-stacks

# metodo lento:
fila = []
fila.append(4)
fila.append(5)
print(fila)
print(fila.pop(0))
print(fila)

# metodo rápido:
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves
queue.popleft()                 # The second to arrive now leaves
print(queue)                           # Remaining queue in order of arrival

# Pilas - Python não tem uma estrutura específica para pilas, mas podemos usar as funções append e pop() para simulá-la
# https://docs.python.org/2/tutorial/datastructures.html#using-lists-as-stacks
pilha = []
pilha.append(4)
pilha.append(5)
print(pilha)
print(pilha.pop())
print(pilha)

teste = []
teste1 = [1, 2, 3, 4, 5]
teste2 = [6, 7, 8, 9, 10]

# teste.append(10)
# teste.append(50)
# teste.append(teste1)
# teste.append(teste2)

# print(teste)
# print(teste.pop())

# print(teste)
# print(teste.pop(0))

#ToDo: crie uma pilha e uma fila

fila = []
pilha = []

for i in range(100):
  fila.append(i)
  pilha.append(i)
  #adicione os elementos i dentro da fila e da pilha

for i in range(100):
  print(fila.pop(0))
  #imprima o resultado do pop da fila
  #resultado esperado 0, 1,... 98, 99


for i in range(100):
  print(pilha.pop())
  #imprima o resultado do pop da pilha
  #resultado esperado 99, 98,... 1, 0

  # A heap é um tipo de fila especial que faz com que o primeiro elemento sepre seja o número com menor prioridade
# para colocar a prioridade na heap armazenamos o elemento como uma tuple, onde o primeiro elemento é a prioridade
# para ver outras funções: https://docs.python.org/3.6/library/heapq.html#module-heapq
import heapq
# Covert to a heap
H = [(21, 1),(1, 2),(45, 3),(78, 4),(3, 5),(5, 6)]
heapq.heapify(H)
print(H)
# Add element
heapq.heappush(H,(2, 7))
print(H)
# Remove element from the heap
print(heapq.heappop(H))
print(H)

# ToDo crie uma fila para gerenciar as entradas de um hostipal,
# As entradas devem ser uma tupla contendo o nome do paciente e sua prioridade
# Os pcientes são : Ana : 9, Bruno : 3, Cesar : 5, Diego : 15, Eduardo : 8, Felipe : 13
# remova e imprimas os pacientes com maior prioridade até o de menor prioridade
# Resultado esperado: Diego, Felipe, Ana, Eduardo, Cesar, Bruno

# Sets ou conjuntos são uniões de elementos não ordenados e não repetidos
# são criados colocando os elementos separados por vírgula dentro de chaves {}
# https://docs.python.org/2/tutorial/datastructures.html#sets
s = {2, 5, 7, 3, 6, 2, 8, 2}
print(s)
# existem duas funções úteis em conjuntos, a funão in para saber se o elemento está no conjunto
# é muito otimizado, mais rapido que testar se está em uma lista
print(2 in s)
print(4 in s)
s.add(4)
print(4 in s)
s.remove(2)
print(2 in s)
# E a função union que cria outro set com a união de dois conjuntos
s.union({1, 9, 10})
print(9 in s)

# Dicionários são parcidos nas estruturas de listas, mas em vez de serem associados com índices, são associados com 'chaves' (keys)
# declaração, para saber mais: https://docs.python.org/2/tutorial/datastructures.html#dictionaries
a = {}

# inclusão de elementos
a["c"] = 3
a["s"] = 2
print(a)
# acesso a um elemento
int tmp = a["c"]

# alteração de valores
a["c"] = 5

# número de elementos
print(a)

# remoção de um elemento
del a["c"]
print(a)

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)