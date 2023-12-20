from __init__ import ListaIdades, ListaSalarios, geraListaIdade, geraListaSalarios
import time

idades_obj = ListaIdades(geraListaIdade(5000))

start_time = time.time()
idades_obj.mostra_mediana()
elapsed_time = time.time() - start_time
print(f"Tempo para executar mostra_mediana: {elapsed_time} segundos")

start_time = time.time()
idades_obj.mostra_menor()
elapsed_time = time.time() - start_time
print(f"Tempo para executar mostra_menor: {elapsed_time} segundos")

start_time = time.time()
idades_obj.mostra_maior()
elapsed_time = time.time() - start_time
print(f"Tempo para executar mostra_maior: {elapsed_time} segundos")

salarios_obj = ListaSalarios(geraListaSalarios(5000))

start_time = time.time()
salarios_obj.mostra_mediana()
elapsed_time = time.time() - start_time
print(f"Tempo para executar mostra_mediana: {elapsed_time} segundos")

start_time = time.time()
salarios_obj.mostra_menor()
elapsed_time = time.time() - start_time
print(f"Tempo para executar mostra_menor: {elapsed_time} segundos")

start_time = time.time()
salarios_obj.mostra_maior()
elapsed_time = time.time() - start_time
print(f"Tempo para executar mostra_maior: {elapsed_time} segundos")