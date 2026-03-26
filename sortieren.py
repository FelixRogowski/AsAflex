import random


def sortieren(arr):
    array = arr.copy()
    #Hier soll der Code zum sortieren Eingefügt werden!

    return array

unsortiertes_array = [random.randint(1,50) for _ in range(15)]
sortiertes_array = sortieren(unsortiertes_array)




#Ausgaben zur Kontrolle
print("Das unsortierte Array:")
for wert in unsortiertes_array:
    print(f"[{wert:2}]", end=" ")
print("\n")

print("Das sortierte Array:")
for wert in sortiertes_array:
    print(f"[{wert:2}]", end=" ")
print()


