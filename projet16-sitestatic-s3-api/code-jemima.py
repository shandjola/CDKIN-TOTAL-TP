from Operation import *
# Code python de la simulation des opérations mpesa 

# Creation de la classe abonné 

class Abonné : 
    
    def __init__(self,nom = "aucun",prenom = "aucun",numéro = "243",pin = 0, solde = 0) -> None:
        # les attributs 
        self.nom = nom 
        self.prenom = prenom 
        self.numéro  = numéro 
        self.pin = pin 
        self.soldeUSD = solde
        self.soldeCDF = solde 
        
def traitement(ans,client):
    if ans[-1] == "1" :
        if ans[1] == '1':
            # operation du depot 
            depot(client,ans[3], ans[4], ans[0])
        elif ans[1] == '2' :
            # operation du retrait 
            retrait(client,ans[4], ans[0])
        elif ans[1] == '3' :
            # Operation d'achat de forfait 
            achatForfait(client,ans[4],ans[0])
    else :
        print("Operation annule")
        
    
def process(client) :
    main_step = ["choix de divise \n\n 1:USD\n 2:CDF",
                 "choix des operation \n\n 1:Faire un depot\n 2:Faire un retrait\n 3: Acheter un forfait",
                 "Choix des types d'envoi \n\n 1:Envoi dollar\n 2:Envois sans frais de retrait\n 3:Envoi avec frais de retrait",
                 "Tapez numéro du téléphone du bénéficiaire",
                 "Tapez le montant",
                 "Inserer le PIN",
                 f"Voici le solde de votre compte {client.soldeUSD} USD et {client.soldeCDF} CDF \n 0:Continuer",
                 "Confirmer l'opération \n 1:Oui 2:Non"
                ]
    main_answer = []
    for i in range(len(main_step)): 
        print(f"=== abonne : {client.prenom} {client.nom} ===")
        print(main_step[i])
        main_answer.append(input('> ')) 
        if i == 5 : 
            count = 0 
            while main_answer[-1] != client.pin :
                print('pin incorrect')
                main_answer[-1] = input('> ')
                count += 1 
                if count > 1 :
                    exit()
        if i == 6 :
            if int(main_answer[4]) > client.soldeUSD and main_answer[0] == "1" :
                print('solde insuffissant') 
                exit()
            elif int(main_answer[4]) > client.soldeCDF and main_answer[0] == "2" :
                print('solde insuffissant') 
                exit()
        elif i == 3 :
            count = 0
            for i in database :
                if main_answer[-1] == i.numéro :
                    main_answer[-1] = i  
                    count = 1
            if count == 0 :
                print("le numéro n'existe pas")
                exit()
        elif i == len(main_step) - 1 : 
            traitement(main_answer,client)     

if __name__ == '__main__' : 
    junior = Abonné(
        nom="MEME",
        prenom="Junior",
        numéro="1234567890",
        pin="2001",
        solde=20000
    )
    david = Abonné(
        nom = "MUGWELA",
        prenom="Jemima",
        numéro="0123456789",
        pin="2134",
        solde=10000
    )
    
    database = [junior,david]
    cmd = input("code USSD : ")
    if cmd == "*1122#" : 
        process(junior)
    else :
        print("Code ussd incorrecte")