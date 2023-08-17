salas = ["2", "4", "6", "8", "10"]
salas_eliminadas = []
num = 0
for num_sala_act in salas:
    num += 1
    if num != int(num_sala_act):
        salas_eliminadas.append(num)
        num += 1
print(salas_eliminadas)