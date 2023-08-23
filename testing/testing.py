from nltk.tokenize import word_tokenize
import numpy as np

pelis_simila = []
peliculas = ["one uno", "two dos", "three tres"]
pelis = [peli_2 for peli_2 in peliculas]
peli_ingre = input("Ingrese una peli: ")
for peli in pelis:
    peli_uno_separada = word_tokenize(peli)
    peli_dos_separada = word_tokenize(peli_ingre)
    peli_uno_set = set(peli_uno_separada)
    peli_dos_set = set(peli_dos_separada)
    union_set = peli_uno_set.union(peli_dos_set)
    peli_uno_contiene = []
    peli_dos_contiene = []
    for palabra in union_set:
        if palabra in peli_uno_separada:
            peli_uno_contiene.append(1)
        else:
            peli_uno_contiene.append(0)
        if palabra in peli_dos_separada:
            peli_dos_contiene.append(1)
        else:
            peli_dos_contiene.append(0)
    x_peli = np.array(peli_uno_contiene)
    y_peli = np.array(peli_dos_contiene)
    porcen_simili = (x_peli @ y_peli) / (np.linalg.norm (x_peli)) * (np.linalg.norm (y_peli))
    if porcen_simili > 0.0:
        pelis_simila.append(peli)
print(pelis_simila)