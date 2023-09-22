import csv

def generate_combinations(actions_data, budget):
    num_actions = len(actions_data["name"])
    combinations = []
    
    # Fonction auxiliaire récursive pour générer les combinaisons
    def generate_combinations_recursive(index, current_combination, current_cost, current_profit):
        if index == num_actions:
            combinations.append((current_combination, current_cost, current_profit))
            return
        
        # Inclure l'action actuelle
        if current_cost + actions_data["price"][index] <= budget:
            generate_combinations_recursive(index + 1, current_combination + [actions_data["name"][index]], 
                                            current_cost + actions_data["price"][index],
                                            current_profit + actions_data["profit"][index])
        
        # Ne pas inclure l'action actuelle
        generate_combinations_recursive(index + 1, current_combination, current_cost, current_profit)
    
    generate_combinations_recursive(0, [], 0, 0)
    
    return combinations

# Exemple d'utilisation avec des données factices
actions_data = {
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
combinations = generate_combinations(actions_data, budget)

# Exporter les combinaisons au format CSV
with open("combinations.csv", "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Combinaison", "Coût total", "Profit"])

    for combination, cost, profit in combinations:
        csvwriter.writerow([" & ".join(combination), cost, profit])

print("Les combinaisons ont été exportées dans le fichier 'combinations.csv'.")
