import pandas as pd

df1 = pd.read_csv('../data_1.csv')
df2 = pd.read_csv('../data_2.csv')

data = pd.concat([df1, df2], ignore_index=True)
data = pd.DataFrame(data)

print(data)


def calculate_profit(initial_investment, data):
    profits = []

    for index, action in data.iterrows():
        action_name = action["name"]
        action_price = action["price"]
        if action_price <= 0:
            continue
        action_profit = action["profit"]
        # nombre d'actions achetées
        number_of_action = int(initial_investment / action_price)
        rest = initial_investment % action_price
        final_amount = (number_of_action * action_profit * action_price / 100) + rest
        profits.append((action_name, final_amount))

    return profits


initial_investment = 500
results = calculate_profit(initial_investment, data)

for action_name, final_amount in results:
    print(f"Pour l'action {action_name}, le montant après 2 ans serait : {final_amount:.2f} euros")

