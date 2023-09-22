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

///boucle qui va balyer toute les actions de 1 à 20

(sauter toujours 1 pour 1)
1 jusqua que j'ai plus de sous
1 en sautant 2 jusqua que j'ai plus de sous
1 en sautant 3 jusqua que j'ai plus sous
etc........

(sauter toujours 2 pour 2)
2 jusqua que j'ai plus de sous
2 en sautant 1 jusqua que j'ai plus de sous
2 en sautant 3 jusqua que j'ai plus de sous


def calculate_profit(budget, actions_data):
    num_actions = len(actions_data["name"])

    tableau = {'actions': [], 'profit': []}

    for i in range(1, num_actions):
        selected_actions = []
        total_cost = 0
        total_profit = 0

        for j in range(num_actions):
            action_name = actions_data["name"][j]
            cost = actions_data["price"][j]
            profit_percentage = actions_data["profit"][j]

            if total_cost + cost <= budget:
                selected_actions.append(action_name)
                total_cost += cost
                profit = cost * profit_percentage / 100
                total_profit += profit

        tableau["actions"].append([selected_actions])
        tableau["profit"].append(total_profit)

    return tableau


budget = 500
result = calculate_profit(budget, data)
print(result)


