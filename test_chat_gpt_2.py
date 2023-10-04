def knapsack(actions, capacity):
    num_actions = len(actions['name'])

    # Initialiser le tableau dynamique
    dp = [[0] * (capacity + 1) for _ in range(num_actions + 1)]

    for i in range(1, num_actions + 1):
        action_name, action_price, action_profit = (
            actions['name'][i - 1],
            actions['price'][i - 1],
            (actions['price'][i - 1] * actions['profit'][i - 1]) / 100
        )
        for w in range(1, capacity + 1):
            if action_price > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - action_price] + action_profit)

    # Récupérer la meilleure combinaison et son profit
    max_profit = dp[num_actions][capacity]
    best_combination = []
    w = capacity
    for i in range(num_actions, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            action_name, action_price, action_profit = (
                actions['name'][i - 1],
                actions['price'][i - 1],
                (actions['price'][i - 1] * actions['profit'][i - 1]) / 100
            )
            best_combination.append((action_name, action_price, action_profit))
            w -= action_price

    return best_combination, max_profit


# Exemple d'utilisation avec votre tableau d'actions
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

# Calculer le profit comme le produit du prix et du profit, divisé par 100
for i in range(len(actions['price'])):
    actions['profit'][i] = (actions['price'][i] * actions['profit'][i])

capacity = 500

best_combination, max_profit = knapsack(actions, capacity)

print("Meilleure combinaison d'actions:")
print(best_combination)
for action in best_combination:
    print(f"Action : {action[0]}, Prix : {action[1]}, Profit : {action[2]}")
print("Profit maximum obtenu:", max_profit)


#20 19 17 13 12 6 5 4 # différent de

# combinaison de bruteforce 20 19 18 13 11 10 8 6 5 4