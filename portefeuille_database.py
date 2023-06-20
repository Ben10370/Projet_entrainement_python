from tinydb import TinyDB, Query

# Création de la base de données
db = TinyDB('database.json')

# Définition des classes Client et Facture
class Client:
    def __init__(self, nom, adresse_email, budget_projet):
        self.nom = nom
        self.adresse_email = adresse_email
        self.budget_projet_initial = budget_projet
        self.budget_projet = budget_projet

    def envoyer_facture(self, montant):
        facture = Facture(self.nom, montant)
        facture.sauvegarder()

    def __del__(self):
        print(f"L'instance du client {self.nom} a été supprimée.")

    def obtenir_budget_final(self):
        return self.budget_projet

    def sauvegarder(self):
        table = db.table('clients')
        table.insert({'nom': self.nom, 'adresse_email': self.adresse_email, 'budget_projet': self.budget_projet})

    @staticmethod
    def charger():
        table = db.table('clients')
        clients = []
        for item in table.all():
            client = Client(item['nom'], item['adresse_email'], item['budget_projet'])
            clients.append(client)
        return clients


class Facture:
    def __init__(self, nom_client, montant):
        self.nom_client = nom_client
        self.montant = montant

    def sauvegarder(self):
        table = db.table('factures')
        table.insert({'nom_client': self.nom_client, 'montant': self.montant})

    @staticmethod
    def charger():
        table = db.table('factures')
        factures = []
        for item in table.all():
            facture = Facture(item['nom_client'], item['montant'])
            factures.append(facture)
        return factures


# Exemple d'utilisation
client1 = Client("Client 1", "client1@example.com", 500)
client2 = Client("Client 2", "client2@example.com", 1000)

# Sauvegarde des clients dans la base de données
client1.sauvegarder()
client2.sauvegarder()

# Chargement des clients depuis la base de données
clients = Client.charger()
for client in clients:
    print("Nom:", client.nom)
    print("Adresse email:", client.adresse_email)
    print("Budget du projet initial:", client.budget_projet_initial)
    print("Budget du projet final:", client.obtenir_budget_final())
    print()

# Envoi d'une facture pour le client1
client1.envoyer_facture(200)

# Chargement des factures depuis la base de données
factures = Facture.charger()
for facture in factures:
    print("Nom du client:", facture.nom_client)
    print("Montant:", facture.montant)
    print()

# Suppression du client1 de la base de données
table_clients = db.table('clients')
table_clients.remove(Query().nom == "Client 1")

# Vérification que le client1 a été supprimé
clients = Client.charger()
for client in clients:
    print("Nom:", client.nom)
    print("Adresse email:", client.adresse_email)
    print("Budget du projet initial:", client.budget_projet_initial)
    print("Budget du projet final:", client.obtenir_budget_final())
    print()
