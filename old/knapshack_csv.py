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

print("la")
# A naive recursive implementation
# of 0-1 Knapsack Problem

# Returns the maximum value that
# can be put in a knapsack of
# capacity W


def knapSack(W, wt, val, n, names):
    # Base Case
    if n == 0 or W == 0:
        return 0

    # If weight of the nth item is
    # more than Knapsack of capacity W,
    # then this item cannot be included
    # in the optimal solution
    if (wt[n-1] > W):
        print(W)
        return knapSack(W, wt, val, n-1, names)

    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(
            val[n-1] + knapSack(
                W-wt[n-1], wt, val, n-1,names),
            knapSack(W, wt, val, n-1,names))

# end of function knapSack


# Driver Code
if __name__ == '__main__':

    W = 500
    n = 20  # n = len(profit)
    print(knapSack(W, weigth, profit, n, names))

# This code is contributed by Nikhil Kumar Singh
# Enregistrez le temps de fin
temps_fin = time.time()

# Calculez la durée d'exécution en secondes
duree_execution = temps_fin - temps_debut
print("Le programme a mis", duree_execution, "secondes à s'exécuter.")