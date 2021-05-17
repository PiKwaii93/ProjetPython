import random
class Word :

    def __init__(self, tour):
        if tour==1 :
            self.mot1 = ["ta mère", "ta femme"]
            self.mot2 = ["est", "elle est"]
            self.mot3 = ["tellement grosse", "comme une éponge"]
            self.mot4 = ["qu'il faut", "elle sert"]
            self.mot6 = ["deux pokeflutes","qu'à faire"]
            self.mot7 = ["pour la réveiller", "la vaiselle"]

            self.proposition = {"ta mère":1, "ta femme":2, "est":3, "elle est":4, 
                                "tellement grosse":5,"comme une éponge":6, "qu'il faut":7, 
                                "elle sert":8,"deux pokeflutes":9,"qu'à faire":10,"pour la réveiller":11, 
                                "la vaiselle":12}

            self.liste = ["ta mère", "ta femme","est", "elle est","tellement grosse", "comme une éponge",
                        "qu'il faut", "elle sert","deux pokeflutes","qu'à faire","pour la réveiller", "la vaiselle"]
            self.compteur = ["ta mère", "ta femme","est", "elle est","tellement grosse", "comme une éponge",
                        "qu'il faut", "elle sert","deux pokeflutes","qu'à faire","pour la réveiller", "la vaiselle"]
            self.aleatoire = []

            random.random()
            y=0
            for x in self.compteur :
                self.aleatoire.append(random.choice(self.liste))
                self.liste.remove(self.aleatoire[y])
                y = y +1
        
            self.reponse = ""
            self.combinaison = {1357911 : 7, 24681012 : 7, 2357911: 6, 14681012: 6, 1810126 : 5, 2810126 : 5, 181012 : 4, 281012 : 4}

