import pandas as pd

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

def generate_combinations(actions, remaining_budget, current_combination=[]):
    combinations = []

    for i, action in enumerate(actions):
        if action['price'] <= remaining_budget:
            new_combination = current_combination + [action['name']]
            new_budget = remaining_budget - action['price']

            if new_budget >= 0:
                combinations.append((new_combination, budget - new_budget))

            # Generate combinations recursively
            combinations += generate_combinations(actions[i+1:], new_budget, new_combination)

    return combinations

actions = [{'name': name, 'price': price, 'profit': profit} for name, price, profit in zip(data['name'], data['price'], data['profit'])]
all_combinations = generate_combinations(actions, budget)

# Créer un DataFrame pandas avec deux colonnes : Combinaison d'actions et Prix dépensé
df = pd.DataFrame(all_combinations, columns=["Combinaison d'actions", "Prix dépensé"])

# Enregistrer le DataFrame dans un fichier Excel
df.to_excel("combinaisons_actions.xlsx", index=False)
