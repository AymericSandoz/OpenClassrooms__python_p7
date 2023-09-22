from itertools import combinations
import time

# Enregistrez le temps de début
temps_debut = time.time()

actions = {
    'name': [
        "Action-1", "Action-2", "Action-3", "Action-4", "Action-5",
        "Action-6", "Action-7", "Action-8", "Action-9", "Action-10",
        "Action-11", "Action-12", "Action-13", "Action-14", "Action-15",
        "Action-16", "Action-17", "Action-18", "Action-19", "Action-20"
    ],
    'price': [
        20, 30, 50, 70, 60, 80, 22, 26, 48, 34, 42, 110, 38, 14, 18, 8, 4, 10, 24, 114
    ],
    'profit': [
        5, 10, 15, 20, 17, 25, 7, 11, 13, 27, 17, 9, 23, 1, 3, 8, 12, 14, 21, 18
    ]
}


total_combinations = 0
# Générer et parcourir les combinaisons de différentes tailles
for r in range(1, len(actions["name"]) + 1):
    combinations_r = combinations(actions["name"], r)
    for combination in combinations_r:
        total_combinations += 1  # Incrémenter le compteur

print("Nombre total de combinaisons générées:", total_combinations)


# Enregistrez le temps de fin
temps_fin = time.time()

# Calculez la durée d'exécution en secondes
duree_execution = temps_fin - temps_debut
print("Le programme a mis", duree_execution, "secondes à s'exécuter.")