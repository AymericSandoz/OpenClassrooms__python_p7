

import csv
import time

temps_debut = time.time()


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
    list1 = [
        20, 30, 50, 70, 60, 80, 22, 26, 48, 34, 42, 110, 38, 14, 18, 8, 4, 10, 24, 114
    ]
    list2 = [
        5, 10, 15, 20, 17, 25, 7, 11, 13, 27, 17, 9, 23, 1, 3, 8, 12, 14, 21, 18
    ]
    profit = [(x * y) / 100 for x, y in zip(list1, list2)]


    weight = [
        20, 30, 50, 70, 60, 80, 22, 26, 48, 34, 42, 110, 38, 14, 18, 8, 4, 10, 24, 114
    ]
    W = 500
    n = len(profit)
    print(knapSack(W, weight, profit, n))

# This code is contributed by Nikhil Kumar Singh
# Enregistrez le temps de fin
temps_fin = time.time()

# Calculez la durée d'exécution en secondes
duree_execution = temps_fin - temps_debut
print("Le programme a mis", duree_execution, "secondes à s'exécuter.")