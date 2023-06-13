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
    def __init__(self, nom, adresse_email, budget_projet, reductions):
        super().__init__(nom, adresse_email, budget_projet)
        self.reductions = reductions

    def appliquer_reduction(self):
        reduction = sum(self.reductions.values())
        self.budget_projet -= reduction


# Exemple d'utilisation
client1 = Client("Client 1", "client1@example.com", 500)
client2 = Client("Client 2", "client2@example.com", 1000)

print("Client 1:")
print("Nom:", client1.nom)
print("Adresse email:", client1.adresse_email)
print("Budget du projet:", client1.budget_projet)

print()

print("Client 2:")
print("Nom:", client2.nom)
print("Adresse email:", client2.adresse_email)
print("Budget du projet:", client2.budget_projet)

print()

client1.envoyer_facture(200)
client2.envoyer_facture(350)

print()

client1 = None  # Suppression de l'instance client1

print()

client_regulier = ClientRegulier("Client régulier", "clientregulier@example.com", 1000, {"remise": 100})

print()

client_regulier.envoyer_facture(900)

print()

client_regulier.appliquer_reduction()

print()

print(f"Le budget du projet du client régulier est maintenant de {client_regulier.budget_projet}€.")

print()