from lista_encadeada import Lista_encadeada
from pilha import Pilha
from fila import Fila

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

# Lista encadeada: métodos solicitados
nums = Lista_encadeada()
nums.inserir_final(5)
nums.inserir_final(10)
nums.inserir_final(15)
nums.inserir_final(11)
nums.inserir_final(8)
print("Lista inicial:")
nums.imprimir()
print("menor:", nums.min())
print("maior:", nums.max())
print("soma:", nums.sum())
print("média:", nums.avg())
print("tamanho:", nums.len())
print("buscar 10:", nums.buscar(10))
print("buscar 99:", nums.buscar(99))

outra = Lista_encadeada()
outra.inserir_final(100)
outra.inserir_final(200)
nums.append(outra)
print("Após append:")
nums.imprimir()
nums.reverse()
print("Após reverse:")
nums.imprimir()

# Pilha: métodos solicitados
p1 = Pilha()
p1.push(10)
p1.push(20)
p1.push(30)
print("Pilha inicial:")
p1.imprimir()
print("buscar 20 na pilha:", p1.buscar(20))
print("remover 20 da pilha:", p1.remover(20))
print("Pilha após remover 20:")
p1.imprimir()

p1.push(30)
p1.push(30)
p1.push(40)
print("Pilha antes de remover repetidos:")
p1.imprimir()
p1.remover_repetidos()
print("Pilha após remover repetidos:")
p1.imprimir()

# Fila: métodos solicitados
f = Fila()
f.enfileirar(10)
f.enfileirar(20)
f.enfileirar(30)
print("Fila inicial:")
f.imprimir_fila()
print("buscar 20 na fila:", f.buscar(20))
print("editar 20 para 25 na fila:", f.editar(20, 25))
print("Fila após editar:")
f.imprimir_fila()
print("remover 25 da fila:", f.remover(25))
print("Fila após remover:")
f.imprimir_fila()
f.enfileirar(30)
f.enfileirar(30)
f.enfileirar(40)
f.remover_repetidos()
print("Fila após remover repetidos:")
f.imprimir_fila()