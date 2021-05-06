from player import Player
from Mot import Mot
from Phrase import Phrase

class GAME :

    def __init__(self) :
        self.joueur1 = Player()
        self.joueur2 = Player()
        self.Combat()


def Combat(self) :
    while(self.Player.pv > 0 and self.monster.pv > 0):
        print(self.PLayer)
        print(self.monster)
    

    print(self.joueur1.name + "VS" + self.joueur2.name)
    print("Que voulez-vous faire ?")
    print("1 - Attaquer ?")
    print("2 - Boire une potion")
    Choice_user = input()

    if Choice_user == "1" :
        Mot1 = Mot("1")
        Phrase1 = Phrase("1")
        print(Phrase1.phrase)
        print(Mot1.liste_mot)
        print("Veuillez choisir votre arme !")

        
