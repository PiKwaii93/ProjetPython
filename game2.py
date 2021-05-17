from Joueur import Joueur
from Word import Word
from random import randint
import copy

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
                random = str(randint(1,1))
                print(random)
                Mot = Word(1)
                print("\n")
                print(self.joueur1.name + " laissez libre court à votre imagination !")
                reponse1 = ""
                tableau1 = []
                copy1 = copy.copy(Mot.aleatoire)
                copy2 = copy.copy(Mot.aleatoire)
                verif1 = False
                while verif1 == False:
                    i=0
                    j = 1

                    while(i<len(copy1)):
                        phrase = ""
                        phrase = str(j) + ") -- " + copy1[int(i)] + " --"
                        print(phrase)
                        i = i + 1
                        j = j +1
                    print("\n")
                    
                    print("\n")
                    Choice_user1 = input()
                    if Choice_user1 == "done" :
                        verif1 = True
                    else :
                        tableau1.append(copy1[int(Choice_user1) - 1])
                        reponse1 = reponse1 + copy1[int(Choice_user1) - 1] + " "
                        copy1.pop(int(Choice_user1) - 1)
                print("\n")
                print(reponse1)
                print("\n")

                print(self.joueur2.name + " voyons ce que vous avez dans le ventre !")

                reponse2 = ""
                tableau2 = []
                verif2 = False
                while verif2 == False:
                    i=0
                    j = 1

                    while(i<len(copy2)):
                        phrase = ""
                        phrase = str(j) + ") -- " + copy2[int(i)] + " --"
                        print(phrase)
                        i = i + 1
                        j = j +1
                    print("\n")
                    print("\n")
                    Choice_user2 = input()
                    if Choice_user2 == "done" :
                        verif2 = True
                    else :
                        tableau2.append(copy2[int(Choice_user2) - 1])
                        reponse2 = reponse2 + copy2[int(Choice_user2) - 1] + " "
                        copy2.pop(int(Choice_user2) - 1)
                print("\n")
                print(reponse2)
                print("\n")
                print("Voyons lequel d'entre vous a été le plus inspiré !")
                print("\n")
                print("Joueur 1 : " + reponse1)
                print("\n")
                print("Joueur 2 : " + reponse2)
                print("\n")
                valeur1 = ""
                for p in tableau1 :
                    valeur1 = valeur1 + str(Mot.proposition[p])
                print(valeur1)
                print(tableau1)
                print("\n")
                valeur2 = ""
                for m in tableau2 :
                    valeur2 = valeur2 + str(Mot.proposition[m])
                print(valeur2)
                print(tableau2)
                dmg1 = 0
                for n in Mot.combinaison :
                    if int(valeur1) == n :
                        dmg1 = dmg1 + Mot.combinaison[n]
                print(dmg1)
                dmg2 = 0
                for n in Mot.combinaison :
                    if int(valeur2) == n :
                        dmg2 = dmg2 + Mot.combinaison[n]
                print(dmg2)
                self.joueur1.pv = self.joueur1.pv - dmg2
                self.joueur2.pv = self.joueur2.pv - dmg1
                print(self.joueur1.pv)
                print(self.joueur2.pv)
        


        if(self.joueur2.pv <= 0) :
            print("\n")
            print("Le gagnant est " + self.joueur1.name)
            exit()
        elif(self.joueur1.pv <=0) :
            print("\n")
            print("Le gagnant est " + self.joueur2.name)
            exit()