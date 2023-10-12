

import csv
import time

temps_debut = time.time()

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
    list1 = [20, 30, 50, 70, 60, 80, 22, 26, 48, 34, 42, 110, 38, 14, 18, 8, 4, 10, 24, 114]
    list2 = [5, 10, 15, 20, 17, 25, 7, 11, 13, 27, 17, 9, 23, 1, 3, 8, 12, 14, 21, 18]
    profit = [(x * y) / 100 for x, y in zip(list1, list2)]
    weight = [
        20, 30, 50, 70, 60, 80, 22, 26, 48, 34, 42, 110, 38, 14, 18, 8, 4, 10, 24, 114
    ]
    names = [
        "Action-1", "Action-2", "Action-3", "Action-4", "Action-5",
        "Action-6", "Action-7", "Action-8", "Action-9", "Action-10",
        "Action-11", "Action-12", "Action-13", "Action-14", "Action-15",
        "Action-16", "Action-17", "Action-18", "Action-19", "Action-20"
    ]
    W = 500
    W = 500  # Capacité maximale du sac
    n = len(profit)  # Nombre d'actions
    max_profit, selected_actions = knapSack(W, weight, profit, n)

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