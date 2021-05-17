class Mot :
    
    def __init__(self, tour):
        self.tour = tour
        if tour=="1" :
            self.liste_mot = ["bête qu'elle croit qu'elle va maigrir si elle évite de lire les caractères gras","bête qu'elle joue jamais au Millionnaire parce qu'elle comprend pas les règles","bête qu'elle met un timbre sur l'cran de son ordinateur pour envoyer un courrier électronique","radine que, quand elle vomit, elle sert les dents pour garder les morceaux","vieille que quand elle pète, elle fait de la poussière","bête qu'elle croit que c'est des noisettes qu'il faut qu'elle pose à la caisse d'épargne"]
            self.rank = [0, 2, 1, 0, 2, 1]
        if tour=="2" :
            self.liste_mot = ["qu'aux jeux olympiques de la connerie il a fini 2ème parce qu'il était trop bête pour finir première","qu'il a trébuché sur un téléphone sans fil","qu'il croit que la souris, c'est un micro pour donner des ordres à l'ordinateur","que quand elle fait une faute de frappe elle met du tipex sur l'ecran","qu'il arrive pas à sortir de son screen screen-saver","qu'il ramène sa télécommande au ciné"]
            self.rank = [0, 1, 2, 0, 1, 2]
        if tour=="3" :
            self.liste_mot = ["bête que qaund il joue avec le chien c'est lui qui va chercher la balle","poilue que quand il va au zoo c'est lui qu'on regarde"," bête qu'il enfile une capote sur son moniteur pour se protéger des virus","bête qu'il essaie d'ouvrir son écran pour recevoir la marchandise q'uil a commmandé sur Internet","bête que la seule façon qu'il a compiler ses programmmes sans erreur, c'est de mettre tout son code eb commentaires","bête qu'il préfere intermarrché à Internet parce que c'est moins cher"]
            self.rank = [1, 2, 0, 1, 2, 0]
        if tour=="4" :
            self.liste_mot = ["se prends trop pour une princesse, mais le seul trône sur lequel tu t'assois, c'est les chiottes","c'est comme une barbie en plastique et sans cerveau","je l'ai retrouvé sur mon GPS et devine comment ? j'ai tapé Cruella, il m'a emmené devant chez toi","est tellement poilue qu'elle se douche avec du shampooing"," est bête, que quand elle ne trouves pas la réponse à une question, elle donne vraiment sa langue au chat","est tellement conne qu'elle a fait une consultation avec Dr peper"]
            self.rank = [2, 0, 1, 2, 0, 1]
        if tour=="5" :
            self.liste_mot = ["tes grandes oreilles, tu peux entendre la langage des singes","j'ai compris que dieu avait le sens de l'humour","tes dents sales, que ton dentiste te soigne avec un caterpillar","attendre le bus c'est le camion poubelle qui passe","tes dents tellement jaunes je me dis que ton dentiste te soigne avec des lunettes de soleil","t'aime tellement manger les cacahuètes, tu chie des Snickers","ton violeur a porté plainte et il a gagné"]
            self.rank = [0, 1, 2, 0, 1, 2]
        if tour=="6" :
            self.liste_mot = ["que quand t'ouvre ta bouche pendant les repas, on s'en server comme poubelle de table","que quand tu te lave, la station d'épuration porte plainte","que quand tu rote, ça pue tellement qu'on dirait qu'elle a mangé un cimetière","que quand tu descends les poubelles, tu te jette toi même dans le container","que monsieur propre s'est suicidé","que quand tu changes d'eau de toilette, on te demande si t'as écrasé quelque chose"]
            self.rank = [1, 2, 0, 1, 2, 0]


        self.liste_reponse = ["Pas mal", "Jolie coup !", "Holala ! En plein dans le mille !"]


        

