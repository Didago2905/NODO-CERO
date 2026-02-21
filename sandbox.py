print("=== Experimento 1 ===")

lista1 = [10, 20, 30]
lista2 = lista1

lista1.append(40)

print("lista1:", lista1)
print("lista2:", lista2)
print("IDs:", id(lista1), id(lista2))


print("\n=== Experimento 2 ===")

lista3 = [10, 20, 30]
lista4 = lista3.copy()

lista3.append(40)

print("lista3:", lista3)
print("lista4:", lista4)
print("IDs:", id(lista3), id(lista4))


print("\n=== Experimento 3 ===")

lista5 = [10, 20, 30]
lista6 = lista5

lista5 = lista5 + [40]

print("lista5:", lista5)
print("lista6:", lista6)
print("IDs:", id(lista5), id(lista6))
