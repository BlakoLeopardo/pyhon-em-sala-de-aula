# Isto é uma lista unidimensional
# frutas = ["Maça", "Laranja", "Banana", "Coco"]

# Lista Bidimensional

Compras = (("Maça", "Laranja", "Banana", "Coco"), 
           ("Aipo", "Cenoura", "Batatas"), 
           ("Galinha", "Peixe", "Peru")
)
# Se quiser mostrar cada item da lista individualmente, apenas passe dois for loops
for colecao in Compras:
    for comida in colecao:
        print(comida, end=" ")
    print()

# frutas[0] = "Abacaxi"
# print(Compras[0][0]) # Se você quiser o elemento especifico de uma lista, apenas coloque o indice do valor que você quer naquela lista