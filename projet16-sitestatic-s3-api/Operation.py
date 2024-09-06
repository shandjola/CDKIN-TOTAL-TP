
def depot(sender, receiver , montant, devise) :
    montant = int(montant)
    devise = int(devise)
    if devise == 1 :
        sender.soldeUSD -= montant 
        receiver.soldeUSD += montant
    else : 
        sender.soldeCDF -= montant 
        receiver.soldeCDF += montant
    print("Opération fait avec succes")

def retrait(sender,montant, devise):
    montant = int(montant)
    if devise == 1 :
        sender.soldeUSD -= montant 
    else : 
        sender.soldeCDF -= montant 
    print("Opération fait avec succes")

def achatForfait(sender, forfait,devise):
    montant = int(montant)
    if devise == 1 :
        sender.soldeUSD -= montant 
    else : 
        sender.soldeCDF -= montant 
    print("Opération fait avec succes")
