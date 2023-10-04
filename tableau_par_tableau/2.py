

import csv
import time

temps_debut = time.time()


# Chemins vers les fichiers CSV
chemin_fichier2 = '../dataset2.csv'

# Liste pour stocker les données de chaque fichier
profit = []
weigth = []
names = []

# Lire les fichiers CSV et fusionner les données. Supprimer les actions dont le prix est inférieur à 0
with open(chemin_fichier2, 'r') as fichier2:
    actions = csv.DictReader(fichier2)

    for action in actions:
        # if (float(action["price"]) > 0):
        if (float(action["price"]) > 0 and float(action["profit"]) > 0 ):
            weigth.append(float(action["price"]))
            profit.append(float(action["price"]) * float(action["profit"]) / 100)
            names.append(action["name"])

def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
  
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][int(w - wt[i-1])], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
  
    # Retourner le profit maximal et la liste des actions sélectionnées
    return K[n][W], get_selected_actions(K, wt, n, W)

def get_selected_actions(K, wt, n, W):
    selected_actions = []
    i, w = n, W

    while i > 0 and w > 0:
        if K[i][w] != K[i-1][w]:
            selected_actions.append(i-1)  # L'indice est décalé de 1 à cause de la représentation 0-indexed
            w = int(w - wt[i-1])
        i -= 1

    return selected_actions


if __name__ == '__main__':
    W = 500  # Capacité maximale du sac
    n = len(profit)  # Nombre d'actions
    max_profit, selected_actions = knapSack(W, weigth, profit, n)

    print("Profit maximal obtenu:", max_profit)
    print("Liste des actions sélectionnées pour le profit maximal:")
    for idx in selected_actions:
        print(f"- Action {idx}: {names[idx]}")



# This code is contributed by Nikhil Kumar Singh
# Enregistrez le temps de fin
temps_fin = time.time()

# Calculez la durée d'exécution en secondes
duree_execution = temps_fin - temps_debut
print("Le programme a mis", duree_execution, "secondes à s'exécuter.")