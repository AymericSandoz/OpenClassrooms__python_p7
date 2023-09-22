def Combinaison(tab, donnees, debut, fin, courant, k):
    if (courant == k):
        for j in range(k):
            print(donnees[j], end=" ")
        print()
        return
 
    # la condition fin-i+1 >=k-courant s'assure que
    # l'inclusion d'un élément au "courant"
    # fera une combinaison avec les éléments restants
    # aux positions restantes
    i = debut
    while(i <= fin and fin - i + 1 >= k - courant):
        donnees[courant] = tab[i]
        Combinaison(tab, donnees, i + 1, fin, courant + 1, k)
        i += 1
 

tab = [1, 2, 3, 4, 5]
k = 3
n = len(tab)
donnees = [0]*k
Combinaison(tab, donnees, 0, n - 1, 0, k)