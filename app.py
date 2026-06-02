from lista_encadeada import Lista_encadeada
from pilha import Pilha

"""
nums = Lista_encadeada()

if nums.vazia():
    print("lista vazia")

nums.inserir_inicio(5)
nums.inserir_inicio(10)
nums.inserir_inicio(15)
nums.inserir_final(11)
nums.inserir_final(8)
nums.imprimir()
"""

p1 = Pilha()
p1.push(10)
p1.push(20)
p1.push(30)
p1.imprimir()

lista = Lista_encadeada()

lista.inserir_final(10)
lista.inserir_final(20)
lista.inserir_final(30)
lista.inserir_final(20)

lista.imprimir()

print("Menor:", lista.min())
print("Maior:", lista.max())
print("Soma:", lista.sum())
print("Quantidade:", lista.len())
print("Média:", lista.avg())

lista2 = Lista_encadeada()
lista2.inserir_final(40)
lista2.inserir_final(50)

lista.append(lista2)

lista.imprimir()

lista.reverse()

lista.imprimir()

print("===== TESTE PILHA =====")

p1 = Pilha()

p1.push(10)
p1.push(20)
p1.push(30)
p1.push(20)
p1.push(40)

p1.imprimir()

print("Buscar 30:", p1.buscar(30))
print("Buscar 100:", p1.buscar(100))

p1.editar(20, 99)

p1.imprimir()

p1.remover(30)

p1.imprimir()

p1.remover_repetidos()

p1.imprimir()

print("===== TESTE FILA =====")

f1 = Fila()

f1.enfileirar(10)
f1.enfileirar(20)
f1.enfileirar(30)
f1.enfileirar(20)
f1.enfileirar(40)

f1.imprimir_fila()

print("Buscar 30:", f1.buscar(30))
print("Buscar 100:", f1.buscar(100))

f1.editar(20, 99)

f1.imprimir_fila()

f1.remover(30)

f1.imprimir_fila()

f1.remover_repetidos()

f1.imprimir_fila()