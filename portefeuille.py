class Client:
    def __init__(self, nom, adresse_email, budget_projet):
        self.nom = nom
        self.adresse_email = adresse_email
        self.budget_projet_initial = budget_projet
        self.budget_projet = budget_projet

    def envoyer_facture(self, montant):
        print(f"Une facture de {montant}€ a été envoyée au client {self.nom}.")

    def __del__(self):
        print(f"L'instance du client {self.nom} a été supprimée.")

    def obtenir_budget_final(self):
        return self.budget_projet

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
        reduction = self.remise * self.budget_projet_initial / 100
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

    def obtenir_budget_final(self):
        return self.budget_projet


class ClientIndividuel(Client):
    def __init__(self, nom, adresse_email, budget_projet, date_naissance):
        super().__init__(nom, adresse_email, budget_projet)
        self.date_naissance = date_naissance

    def envoyer_facture(self, montant):
        remise = montant * 0.1
        montant_remise = montant - remise
        print(f"Une facture de {montant_remise}€ a été envoyée au client individuel {self.nom}.")
        print(f"Remise appliquée: {remise}€ (10%)")

    def obtenir_budget_final(self):
        return self.budget_projet


class ClientLongTerme(Client):
    def __init__(self, nom, adresse_email, budget_projet, date_debut_contrat):
        super().__init__(nom, adresse_email, budget_projet)
        self.date_debut_contrat = date_debut_contrat

    def envoyer_facture(self, montant):
        taxes = montant * 0.15
        montant_taxes = montant + taxes
        print(f"Une facture de {montant_taxes}€ a été envoyée au client à long terme {self.nom}.")
        print(f"Taxes appliquées: {taxes}€ (15%)")

    def obtenir_budget_final(self):
        return self.budget_projet


# Exemple d'utilisation
client1 = Client("Client 1", "client1@example.com", 500)
client2 = Client("Client 2", "client2@example.com", 1000)

print("Client 1:")
print("Nom:", client1.nom)
print("Adresse email:", client1.adresse_email)
print("Budget du projet initial:", client1.budget_projet_initial)
print("Budget du projet final:", client1.obtenir_budget_final())
client1.envoyer_facture(200)

print()

print("Client 2:")
print("Nom:", client2.nom)
print("Adresse email:", client2.adresse_email)
print("Budget du projet initial:", client2.budget_projet_initial)
print("Budget du projet final:", client2.obtenir_budget_final())
client2.envoyer_facture(350)

print()

client_regulier = ClientRegulier("Client régulier", "clientregulier@example.com", 1000, 10)
print("Client régulier:")
print("Nom:", client_regulier.nom)
print("Adresse email:", client_regulier.adresse_email)
print("Budget du projet initial:", client_regulier.budget_projet_initial)
client_regulier.envoyer_facture(900)
client_regulier.appliquer_reduction()
print("Budget du projet final:", client_regulier.obtenir_budget_final())

print()

client_entreprise = ClientEntreprise("Client entreprise", "cliententreprise@example.com", 2000, "123456789")
print("Client entreprise:")
print("Nom:", client_entreprise.nom)
print("Adresse email:", client_entreprise.adresse_email)
print("Budget du projet initial:", client_entreprise.budget_projet_initial)
print("Numéro de SIRET:", client_entreprise.numero_siret)
client_entreprise.envoyer_facture(1500)
client_entreprise.effectuer_paiement(1500)
print("Budget du projet final:", client_entreprise.obtenir_budget_final())

print()

client_individuel = ClientIndividuel("Client individuel", "clientindividuel@example.com", 300, "01/01/1990")
print("Client individuel:")
print("Nom:", client_individuel.nom)
print("Adresse email:", client_individuel.adresse_email)
print("Budget du projet initial:", client_individuel.budget_projet_initial)
print("Date de naissance:", client_individuel.date_naissance)
client_individuel.envoyer_facture(100)
print("Budget du projet final:", client_individuel.obtenir_budget_final())

print()

client_long_terme = ClientLongTerme("Client à long terme", "clientlongterme@example.com", 5000, "01/01/2022")
print("Client à long terme:")
print("Nom:", client_long_terme.nom)
print("Adresse email:", client_long_terme.adresse_email)
print("Budget du projet initial:", client_long_terme.budget_projet_initial)
print("Date de début du contrat:", client_long_terme.date_debut_contrat)
client_long_terme.envoyer_facture(2000)
print("Budget du projet final:", client_long_terme.obtenir_budget_final())

print()