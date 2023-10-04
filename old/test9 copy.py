
#Version légèrement optimisé, s'arrete quand budget=500, explore toutes les combianaisons
import csv

import time

# Enregistrez le temps de début
temps_debut = time.time()


final_data = {'actions': [], 'profit': [], 'budget': []}

def Combinaison(actions, donnees, debut, fin, courant, k , initial_maximum_budget):
    if (courant == k):
        actions_itm = []  # stockage temporaire
        profit_itm = 0  # stockage temporaire
        price_itm = 0  # stockage temporaire

        for j in range(k):
            actions_itm.append(donnees[j]["name"])
            profit_itm += donnees[j]["profit"] * donnees[j]["price"]
            price_itm += donnees[j]["price"]

        if (price_itm <= initial_maximum_budget):
            final_data["actions"].append(actions_itm)
            final_data["profit"].append(profit_itm)
            final_data["budget"].append(price_itm)
            return
        else:
            return

    # la condition fin-i+1 >=k-courant s'assure que
    # l'inclusion d'un élément au "courant"
    # fera une combinaison avec les éléments restants
    # aux positions restantes
    i = debut
    while (i <= fin and fin - i + 1 >= k - courant):
        donnees[courant] = {"name": actions["name"][i], "price": actions["price"][i], "profit": actions["profit"][i]}
        Combinaison(actions, donnees, i + 1, fin, courant + 1, k, initial_maximum_budget)
        i += 1


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

n = len(actions["name"])
initial_maximum_budget = 500
for k in range(1, 21):  # for k in range(1, len(actions["name"]))):
    print(k)
    donnees = [0] * k
    Combinaison(actions, donnees, 0, n - 1, 0, k, initial_maximum_budget)

# Step 2: Sort the dictionary based on the "profit" values
sorted_data = {
    'actions': [],
    'profit': [],
    'budget': []
}

sorted_indices = sorted(range(len(final_data['profit'])), key=lambda k: final_data['budget'][k], reverse=True)

for key in final_data.keys():
    sorted_data[key] = [final_data[key][i] for i in sorted_indices]

# Affichage des meilleurs résultats
print("Top 3 Résultats :")
print("----------------------------")
for i in range(3):
    print(f"Résultat {i + 1}:")
    print("Actions:", sorted_data['actions'][i])
    print("Profit:", sorted_data['profit'][i])
    print("Budget:", sorted_data['budget'][i])
    print("----------------------------")


# with open("tableau2.csv", "w", newline="") as csvfile:
#     csvwriter = csv.writer(csvfile, delimiter=";")
#     csvwriter.writerow(["Combinaison(actions)", "Profit", "Budget"])

#     for i in range(len(sorted_data["actions"])):
#         csvwriter.writerow([sorted_data["actions"][i], sorted_data["profit"][i], sorted_data["budget"][i]])

# Enregistrez le temps de fin
temps_fin = time.time()

# Calculez la durée d'exécution en secondes
duree_execution = temps_fin - temps_debut
print("Le programme a mis", duree_execution, "secondes à s'exécuter.")