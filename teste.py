from src.mochila import Item, InstanciaMochila, gerar_estado_inicial, fitness
from src.tempera_simulada import tempera_simulada

itens = [Item(2, 3), Item(3, 4), Item(4, 5), Item(5, 6)]
instancia = InstanciaMochila(itens, capacidade=8)
estado = gerar_estado_inicial(instancia)

print(f"capacidade máxima: {instancia.capacidade}")
for i, item in enumerate(instancia.itens):
    print(f"  item {i}: peso={item.peso}, valor={item.valor}")

resultado = tempera_simulada(instancia, estado)

print("\nresultado:")
for i, (gene, item) in enumerate(zip(resultado.genes, instancia.itens)):
    status = "dentro" if gene == 1 else "fora"
    print(f"  item {i} (peso={item.peso}, valor={item.valor}) → {status}")
print("fitness:", fitness(resultado, instancia))
