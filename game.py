from Joueur import Joueur
from Mot import Mot
from Phrase import Phrase

class GAME :

    def __init__(self) :
        self.joueur1 = Joueur("Francis")
        self.joueur2 = Joueur("Maurice")
        self.Combat()


    def Combat(self) :
        x = 0
        print(self.joueur1.name + "VS" + self.joueur2.name)
        while(self.joueur1.pv > 0 and self.joueur2.pv > 0):
            print(self.joueur1)
            print(self.joueur2)
    

            print("Que voulez-vous faire ?")
            print("1 - Attaquer ?")
            print("2 - Boire une potion")
            Choice_action1 = input()

            if Choice_action1 == "1" :
                x = x + 1
                Motpropose = Mot(str(x))
                Phrasepropose = Phrase(str(x))
                print(Phrasepropose.phrase)
                i=0
                j=1
                while(i<len(Motpropose.liste_mot)):
                    proposition = ""
                    proposition = str(j) + ") -- " + Motpropose.liste_mot[int(i)] + " --"
                    print(proposition)
                    j = j + 1
                    i = i + 1
                
                print("Jouer 1 ! Veuillez choisir votre arme !")
                Choice_user1 = input()
                reponse1 = ""
                rank1 = ""
                if Choice_user1 == "1" :
                    reponse1 = Phrasepropose.phrase + Motpropose.liste_mot[0]
                    rank1 = Motpropose.rank[0]
                    print(reponse1)
                if Choice_user1 == "2" :
                    reponse1 = Phrasepropose.phrase + Motpropose.liste_mot[1]
                    rank1 = Motpropose.rank[1]
                    print(reponse1)
                if Choice_user1 == "3" :
                    reponse1 = Phrasepropose.phrase + Motpropose.liste_mot[2]
                    rank1 = Motpropose.rank[2]
                    print(reponse1)

                    
            print("Jouer 2 ! A votre tour !")
            print("Que voulez-vous faire ?")
            print("1 - Attaquer ?")
            print("2 - Boire une potion")
            Choice_action2 = input()

            if Choice_action2 == "1" :
                Motpropose = Mot(str(x))
                Phrasepropose = Phrase(str(x))
                print(Phrasepropose.phrase)
                i=0
                j=1
                while(i<len(Motpropose.liste_mot)):
                    proposition = ""
                    proposition = str(j) + ") -- " + Motpropose.liste_mot[int(i)] + " --"
                    print(proposition)
                    j = j + 1
                    i = i + 1
                Choice_user2 = input()
                reponse2 = ""
                rank2 = ""
                if Choice_user2 == "1" :
                    reponse2 = Phrasepropose.phrase + Motpropose.liste_mot[0]
                    rank2 = Motpropose.rank[0]
                    print(reponse2)
                if Choice_user2 == "2" :
                    reponse2 = Phrasepropose.phrase + Motpropose.liste_mot[1]
                    rank2 = Motpropose.rank[1]
                    print(reponse2)
                if Choice_user2 == "3" :
                    reponse2 = Phrasepropose.phrase + Motpropose.liste_mot[2]
                    rank2 = Motpropose.rank[2]
                    print(reponse2)
                print("Voyons lequel d'entre vous a été le plus inspiré !")
                print("Joueur 1 : " + reponse1)
                print(Motpropose.liste_reponse[rank1])
                print("Joueur 2 : " + reponse2)
                print(Motpropose.liste_reponse[rank2])
                self.joueur1.pv = self.joueur1.pv

                

        
