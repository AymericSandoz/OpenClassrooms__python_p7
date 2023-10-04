#Version légèrement optimisé, s'arrete quand budget=500, et prend un fichier comme données explore toutes les combianaisons


import csv
import time

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

    for ligne in lecteur_csv1:
        donnees_fichier1.append([ligne["name"], float(ligne["price"]), float(ligne["profit"])])

    for ligne in lecteur_csv2:
        donnees_fichier2.append([ligne["name"], float(ligne["price"]), float(ligne["profit"])])

# Fusionner les données dans un seul tableau
actions = donnees_fichier1 + donnees_fichier2

final_data = {'actions': [], 'profit': [], 'budget': []}

def Combinaison(actions, donnees, debut, fin, courant, k , initial_maximum_budget):
    if (courant == k):
        actions_itm = []  # stockage temporaire
        profit_itm = 0  # stockage temporaire
        price_itm = 0  # stockage temporaire

        for j in range(k):
            actions_itm.append(donnees[j][0])
            profit_itm += donnees[j][2] * donnees[j][1]
            price_itm += donnees[j][1]

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
        donnees[courant] = (actions[i][0], actions[i][1], actions[i][2])  # Utilisation d'un tuple
        Combinaison(actions, donnees, i + 1, fin, courant + 1, k, initial_maximum_budget)
        i += 1

n = len(actions)
initial_maximum_budget = 500
for k in range(1, 3):  # for k in range(1, len(actions["name"]))):
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