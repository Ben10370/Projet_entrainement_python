class Client:
    def __init__(self, nom, adresse_email, budget_projet):
        self.nom = nom
        self.adresse_email = adresse_email
        self.budget_projet = budget_projet

    def envoyer_facture(self, montant):
        print(f"Une facture de {montant}€ a été envoyée au client {self.nom}.")

    def __del__(self):
        print(f"L'instance du client {self.nom} a été supprimée.")


class ClientRegulier(Client):
    def __init__(self, nom, adresse_email, budget_projet, remise):
        super().__init__(nom, adresse_email, budget_projet)
        self.remise = remise

    def envoyer_facture(self, montant):
        reduction = self.remise * montant / 100
        montant_reduit = montant - reduction
        print(f"Une facture de {montant_reduit}€ a été envoyée au client régulier {self.nom}.")
        print(f"Réduction appliquée: {reduction}€ ({self.remise}%)")

    def appliquer_reduction(self):
        reduction = self.remise * self.budget_projet / 100
        self.budget_projet -= reduction



class ClientEntreprise(Client):
    def __init__(self, nom, adresse_email, budget_projet, numero_siret):
        super().__init__(nom, adresse_email, budget_projet)
        self.numero_siret = numero_siret

    def envoyer_facture(self, montant):
        montant_taxes = montant * 1.2
        taxes = montant_taxes - montant
        print(f"Une facture de {montant_taxes}€ a été envoyée à l'entreprise {self.nom}.")
        print(f"Taxes appliquées: {taxes}€ ({round((taxes/montant)*100, 2)}%)")

    def effectuer_paiement(self, montant):
        print(f"L'entreprise {self.nom} a effectué un paiement de {montant}€.")


class ClientIndividuel(Client):
    def __init__(self, nom, adresse_email, budget_projet, date_naissance):
        super().__init__(nom, adresse_email, budget_projet)
        self.date_naissance = date_naissance

    def envoyer_facture(self, montant):
        remise = montant * 0.1
        montant_remise = montant - remise
        print(f"Une facture de {montant_remise}€ a été envoyée au client individuel {self.nom}.")
        print(f"Remise appliquée: {remise}€ (10%)")

class ClientLongTerme(Client):
    def __init__(self, nom, adresse_email, budget_projet, date_debut_contrat):
        super().__init__(nom, adresse_email, budget_projet)
        self.date_debut_contrat = date_debut_contrat

    def envoyer_facture(self, montant):
        taxes = montant * 0.1
        montant_taxes = montant + taxes
        print(f"Une facture de {montant_taxes}€ a été envoyée au client à long terme {self.nom}.")
        print(f"Taxes appliquées: {taxes}€ (10%)")

    def modifier_contrat(self, nouvelle_date_debut):
        self.date_debut_contrat = nouvelle_date_debut


# Exemple d'utilisation
client1 = Client("Client 1", "client1@example.com", 500)
client2 = Client("Client 2", "client2@example.com", 1000)

print("Client 1:")
print("Nom:", client1.nom)
print("Adresse email:", client1.adresse_email)
print("Budget du projet:", client1.budget_projet)
client1.envoyer_facture(200)

print()

print("Client 2:")
print("Nom:", client2.nom)
print("Adresse email:", client2.adresse_email)
print("Budget du projet:", client2.budget_projet)
client2.envoyer_facture(350)

print()

client_regulier = ClientRegulier("Client régulier", "clientregulier@example.com", 1000, 10)
print("Client régulier:")
print("Nom:", client_regulier.nom)
print("Adresse email:", client_regulier.adresse_email)
print("Budget du projet:", client_regulier.budget_projet)
client_regulier.envoyer_facture(900)
client_regulier.appliquer_reduction()
print(f"Le budget du projet du client régulier est maintenant de {client_regulier.budget_projet}€.")


print()

client_entreprise = ClientEntreprise("Client entreprise", "cliententreprise@example.com", 2000, "123456789")
print("Client entreprise:")
print("Nom:", client_entreprise.nom)
print("Adresse email:", client_entreprise.adresse_email)
print("Budget du projet:", client_entreprise.budget_projet)
client_entreprise.envoyer_facture(1500)

print()

client_individuel = ClientIndividuel("Client individuel", "clientindividuel@example.com", 300, "01/01/1990")
print("Client individuel:")
print("Nom:", client_individuel.nom)
print("Adresse email:", client_individuel.adresse_email)
print("Budget du projet:", client_individuel.budget_projet)
client_individuel.envoyer_facture(100)

print()

client_long_terme = ClientLongTerme("Client à long terme", "clientlongterme@example.com", 5000, "01/01/2022")
print("Client à long terme:")
print("Nom:", client_long_terme.nom)
print("Adresse email:", client_long_terme.adresse_email)
print("Budget du projet:", client_long_terme.budget_projet)
client_long_terme.envoyer_facture(2000)

print()
