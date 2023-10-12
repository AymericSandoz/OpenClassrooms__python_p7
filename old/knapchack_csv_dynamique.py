

import csv
import time

temps_debut = time.time()

# Chemins vers les fichiers CSV
chemin_fichier1 = 'dataset1.csv'
chemin_fichier2 = 'dataset2.csv'

# Liste pour stocker les données de chaque fichier
profit = []
weigth = []
names = []

# Lire les fichiers CSV et fusionner les données. Supprimer les actions dont le prix est inférieur à 0
with open(chemin_fichier1, 'r') as fichier1, open(chemin_fichier2, 'r') as fichier2:
    actions = csv.DictReader(fichier1)
    # lecteur_csv2 = csv.DictReader(fichier2)

    for action in actions:
        if (float(action["price"]) > 0 and float(action["profit"]) > 0 and float(action["profit"]) >= float(action["price"])):
            weigth.append(float(action["price"]))
            profit.append(float(action["price"]) * float(action["profit"]) / 100)
            names.append(action["name"])

# A naive recursive implementation
# of 0-1 Knapsack Problem

# Returns the maximum value that
# can be put in a knapsack of
# capacity W
# A Dynamic Programming based Python
# Program for 0-1 Knapsack problem
# Returns the maximum value that can 
# be put in a knapsack of capacity W
def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
  
    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                # K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
                K[i][w] = max(val[i-1] + K[i-1][int(w - wt[i-1])], K[i-1][w])

            else:
                K[i][w] = K[i-1][w]
  
    return K[n][W]

# This code is contributed by Bhavya Jain

if __name__ == '__main__':
    W = 500  # Capacité maximale du sac
    n = len(profit)  # Nombre d'actions
    print(knapSack(W, weigth, profit, n))

# This code is contributed by Nikhil Kumar Singh
# Enregistrez le temps de fin
temps_fin = time.time()

# Calculez la durée d'exécution en secondes
duree_execution = temps_fin - temps_debut
print("Le programme a mis", duree_execution, "secondes à s'exécuter.")