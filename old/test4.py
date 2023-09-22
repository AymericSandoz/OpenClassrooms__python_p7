import csv

data = {
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

budget = 500
current_budget = 0  # montant total dépensé
selected_actions = []
tableau = {'actions': [], 'combinaison': [], 'profit': [], 'budget': []}

for i in range(len(data['name'])):
    for k in range(len(data['name'])):
        selected_actions = []
        # si on est dans lebudget on continue, sinon on s'arrête
        if data['price'][i] <= budget:
            current_budget = data['price'][i]
            selected_actions.append(data['name'][i])
            current_budget = data['price'][i]
            total_profit = 0
        else:
            continue
        if k == i:
            continue

        # j correspond à l'actions qu'on va sauter à chaque fois
        for j in range(len(data['name'])):
            print(i, k, j)
            if j == i or j == k:
                continue
            if current_budget + data['price'][j] <= budget:
                selected_actions.append(data['name'][j])
                current_budget += data['price'][j]
                profit = data['price'][j] * data['profit'][j] / 100
                total_profit += profit
                tableau["combinaison"].append(f'{i+1}, {k+1}, {j+1}')  #+1 car en fait actions[0] c'est l'actions 1
        tableau["actions"].append(selected_actions)
        tableau["profit"].append(total_profit)
        tableau["budget"].append(current_budget)


# Exporter les combinaisons au format CSV
with open("tableau.csv", "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=";")
    csvwriter.writerow(["Combinaison(actions)", "combinaison(i,k,j)", "Profit", "Budget"])

    for i in range(len(tableau["actions"])):
        csvwriter.writerow([tableau["actions"][i], tableau["combinaison"][i], tableau["profit"][i], tableau["budget"][i]])

print("nb de combi", len(tableau["profit"]))
# print("Les combinaisons ont été exportées dans le fichier 'combinations.csv'.", tableau["profit"])

print("Profit : ")
for i in range(10):
    print(tableau["actions"][i])
    print(tableau["profit"][i])

# total_cost = sum(data['price'][data['name'].index(action)] for action in selected_actions)
# total_profit = sum(data['profit'][data['name'].index(action)] for action in selected_actions)

# print("Coût total des actions sélectionnées:", total_cost, "euros")
# print("Bénéfice total des actions sélectionnées:", total_profit)
