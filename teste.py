from src.mochila import Item, InstanciaMochila, gerar_estado_inicial, fitness
from src.tempera_simulada import tempera_simulada
from src.algoritmo_genetico import algoritmo_genetico

itens = [Item(2, 3), Item(3, 4), Item(4, 5), Item(5, 6)]
instancia = InstanciaMochila(itens, capacidade=8)

print(f"capacidade máxima: {instancia.capacidade}")
for i, item in enumerate(instancia.itens):
    print(f"  item {i}: peso={item.peso}, valor={item.valor}")

estado = gerar_estado_inicial(instancia)
resultado_ts = tempera_simulada(instancia, estado)

print("\ntêmpera simulada:")
for i, (gene, item) in enumerate(zip(resultado_ts.genes, instancia.itens)):
    status = "dentro" if gene == 1 else "fora"
    print(f"  item {i} (peso={item.peso}, valor={item.valor}) → {status}")
print("fitness:", fitness(resultado_ts, instancia))

resultado_ag = algoritmo_genetico(instancia)

print("\nalgoritmo genético:")
for i, (gene, item) in enumerate(zip(resultado_ag.genes, instancia.itens)):
    status = "dentro" if gene == 1 else "fora"
    print(f"  item {i} (peso={item.peso}, valor={item.valor}) → {status}")
print("fitness:", fitness(resultado_ag, instancia))
