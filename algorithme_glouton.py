class ObjetSac: 
    def __init__(self, poids, valeur, indice): 
        self.indice = indice         
        self.poids = poids 
        self.valeur = valeur
        self.rapport = valeur // poids 
  #Fonction pour la comparaison entre deux ObjetSac
  #On compare le rapport calculé pour les trier
    def __lt__(self, other): 
        return self.rapport < other.rapport 
  

def getValeurMax(poids, valeurs, capacite): 
        tableauTrie = [] 
        for i in range(len(poids)): 
            tableauTrie.append(ObjetSac(poids[i], valeurs[i], i)) 
  
        #Trier les éléments du sac par leur rapport
        tableauTrie.sort(reverse = True) 
  
        compteurValeur = 0
        for objet in tableauTrie: 
            poidsCourant = int(objet.poids) 
            valeurCourante = int(objet.valeur) 
            if capacite - poidsCourant >= 0: 
                #on ajoute l'objet dans le sac
                #On soustrait la capacité
                capacite -= poidsCourant 
                compteurValeur += valeurCourante
                #On ajoute la valeur dans le sac 
        return compteurValeur 

names = [
        "Action-1", "Action-2", "Action-3", "Action-4", "Action-5",
        "Action-6", "Action-7", "Action-8", "Action-9", "Action-10",
        "Action-11", "Action-12", "Action-13", "Action-14", "Action-15",
        "Action-16", "Action-17", "Action-18", "Action-19", "Action-20"
    ]
valeurs = [5, 10, 15, 20, 17, 25, 7, 11, 13, 27, 17, 9, 23, 1, 3, 8, 12, 14, 21, 18]
profits = [20, 30, 50, 70, 60, 80, 22, 26, 48, 34, 42, 110, 38, 14, 18, 8, 4, 10, 24, 114]

poids = [(x * y) / 100 for x, y in zip(profits, valeurs)]

capacite = 500
valeurMax = getValeurMax(poids, valeurs, capacite) 
print("Valeur maxi dans le sac à dos =", valeurMax)