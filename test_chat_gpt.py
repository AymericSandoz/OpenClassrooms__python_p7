def knapsack(actions, capacity):
    num_actions = len(actions)

    # Initialiser le tableau dynamique
    dp = [[0] * (capacity + 1) for _ in range(num_actions + 1)]

    for i in range(1, num_actions + 1):
        action_name, action_price, action_profit = actions[i - 1]
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
            action_name, action_price, action_profit = actions[i - 1]
            best_combination.append((action_name, action_price, action_profit))
            w -= action_price

    return best_combination, max_profit


# Exemple d'utilisation
actions = [("Action1", 2, 10), ("Action2", 3, 7), ("Action3", 4, 5)]
capacity = 5

best_combination, max_profit = knapsack(actions, capacity)

print("Meilleure combinaison d'actions:")
for action in best_combination:
    print(f"Action : {action[0]}, Prix : {action[1]}, Profit : {action[2]}")
print("Profit maximum obtenu:", max_profit)
