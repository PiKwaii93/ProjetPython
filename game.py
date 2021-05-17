from Joueur import Joueur
from Mot import Mot
from Phrase import Phrase
from random import randint

class GAME :

    def __init__(self) :
        self.joueur1 = Joueur("Francis")
        self.joueur2 = Joueur("Maurice")
        self.Combat()


    def Combat(self) :
        x = 0
        print("\n")
        print(self.joueur1.name + " VS " + self.joueur2.name)
        while(self.joueur1.pv > 0 and self.joueur2.pv > 0):
            x = x + 1
            print("\n")
            print("Tour " + str(x))
            print("\n")
            print("Que voulez-vous faire ?")
            print("1 - Attaquer ?")
            print("\n")
            Choice_user = input()

            if Choice_user == "1" :
                random = str(randint(1,10))
                Motpropose = Mot(random)
                Phrasepropose = Phrase(random)
                print("\n")
                print(Phrasepropose.exemple)
                print("\n")
        
                i=0
                j=1
                while(i<len(Motpropose.liste_mot)):
                    proposition = ""
                    proposition = str(j) + ") -- " + Motpropose.liste_mot[int(i)] + " --"
                    print(proposition)
                    j = j + 1
                    i = i + 1
                print("\n")
                print("Jouer 1 ! Veuillez choisir votre arme !")
                print("\n")
                Choice_user1 = input()
                reponse1= Phrasepropose.exemple + Motpropose.liste_mot[int(Choice_user1) - 1]
                rank1 = Motpropose.rank[int(Choice_user1) - 1]
                print("\n")
                print(reponse1)

                print("\n")
                print("Jouer 2 ! A votre tour !")
                print("\n")
                Choice_user2 = input()
                reponse2= Phrasepropose.exemple + Motpropose.liste_mot[int(Choice_user2) - 1]
                rank2 = Motpropose.rank[int(Choice_user2) - 1]
                print("\n")
                print(reponse2)
                print("\n")
                
                print("Voyons lequel d'entre vous a été le plus inspiré !")
                print("\n")
                print("Joueur 1 : " + reponse1)
                print("\n")
                print("Joueur 2 : " + reponse2)
                print("\n")
                if(int(rank1) > int(rank2)) :
                    print(Motpropose.liste_reponse[int(rank1)] + " " + self.joueur1.name)
                if(int(rank1) < int(rank2)) :
                    print(Motpropose.liste_reponse[int(rank2)] + " " + self.joueur2.name)
                if(int(rank1) == int(rank2)) :
                    print(Motpropose.liste_reponse[int(rank2)] + " vous deux")
                self.joueur1.pv = self.joueur1.pv - rank2 - 1
                print("PV de " + self.joueur1.name + " : " + str(self.joueur1.pv))
                self.joueur2.pv = self.joueur2.pv - rank1 - 1
                print("Pv de " + self.joueur2.name + " : " + str(self.joueur2.pv))
        if(self.joueur2.pv <= 0) :
            print("\n")
            print("Le gagnant est " + self.joueur1.name)
            exit()
        elif(self.joueur1.pv <=0) :
            print("\n")
            print("Le gagnant est " + self.joueur2.name)
            exit()

    