#pareil que 11 mais avec panda
import csv
import time
import pandas as pd

temps_debut = time.time()


# Chemins vers les fichiers CSV
chemin_fichier1 = 'dataset1.csv'
chemin_fichier2 = 'dataset2.csv'


# Lire les fichiers CSV dans des DataFrames
donnees_fichier1 = pd.read_csv("dataset1.csv")
donnees_fichier2 = pd.read_csv("dataset2.csv")

# Fusionner les DataFrames
actions = pd.concat([donnees_fichier1, donnees_fichier2], ignore_index=True)
actions['price'] = pd.to_numeric(actions['price'], errors='coerce')
actions['profit'] = pd.to_numeric(actions['profit'], errors='coerce')



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

n = len(actions)
initial_maximum_budget = 500
for k in range(1, 5):  # for k in range(1, len(actions["name"]))):
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