from ortools.algorithms import pywrapknapsack_solver
import operator
list1 = [
    20, 30, 50, 70, 60, 80, 22, 26, 48, 34, 42, 110, 38, 14, 18, 8, 4, 10, 24, 114
]
list2 = [
    5, 10, 15, 20, 17, 25, 7, 11, 13, 27, 17, 9, 23, 1, 3, 8, 12, 14, 21, 18
]
profits = list(map(operator.mul, list1, list2))
weights = [[
        20, 30, 50, 70, 60, 80, 22, 26, 48, 34, 42, 110, 38, 14, 18, 8, 4, 10, 24, 114
    ]]  # Remplacez par vos valeurs
capacity = [500]  # Le prix maximum à ne pas dépasser


solver = pywrapknapsack_solver.KnapsackSolver(
    pywrapknapsack_solver.KnapsackSolver.
    KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER, 'KnapsackExample')
solver.Init(profits, weights, capacity)

computed_value = solver.Solve()
print('Optimal value:', computed_value)

for i in range(len(weights[0])):
    if solver.BestSolutionContains(i):
        print('Action', i, 'is selected')
