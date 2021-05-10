class Mot :
    
    def __init__(self, tour):
        self.tour = tour
        if tour=="1" :
            self.liste_mot = ["que pour la voir entièrement, on doit reculer de trois pas","qu'il faut deux pokéflutes pour la réveiller","qu'il y a un décalage horaire entre ses deux fesses"]
            self.rank = [1, 0, 2]
        if tour=="2" :
            self.liste_mot = ["4","5","6"]
            self.rank = [2, 0, 1]
        


        self.liste_reponse = ["Pas mal", "Jolie coup !", "Holala ! En plein dans le mille !"]
        
        

