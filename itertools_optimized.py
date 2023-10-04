from itertools import combinations
import time
import csv

# Enregistrez le temps de début
temps_debut = time.time()

# Chemins vers les fichiers CSV
chemin_fichier1 = 'dataset1.csv'
chemin_fichier2 = 'dataset2.csv'

# Liste pour stocker les données de chaque fichier
donnees_fichier1 = []
donnees_fichier2 = []

# Lire les fichiers CSV et fusionner les données
with open(chemin_fichier1, 'r') as fichier1, open(chemin_fichier2, 'r') as fichier2:
    lecteur_csv1 = csv.DictReader(fichier1)
    lecteur_csv2 = csv.DictReader(fichier2)

    for action in lecteur_csv1:
        if (float(action["price"]) > 0):
            donnees_fichier1.append(action["name"])

    for action in lecteur_csv2:
        if (float(action["price"]) > 0):
            donnees_fichier2.append(action["name"])
actions = donnees_fichier1 + donnees_fichier2

total_combinations = 0

print(actions[0:5])
# Générer et parcourir les combinaisons de différentes tailles
print(len(actions))
for r in range(1, len(actions) + 1):
    print(r)
    combinations_r = combinations(actions, r)
    for combination in combinations_r:
        total_combinations += 1  # Incrémenter le compteur

print("Nombre total de combinaisons générées:", total_combinations)


# Enregistrez le temps de fin
temps_fin = time.time()

# Calculez la durée d'exécution en secondes
duree_execution = temps_fin - temps_debut
print("Le programme a mis", duree_execution, "secondes à s'exécuter.")