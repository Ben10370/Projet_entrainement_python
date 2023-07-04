from tinydb import TinyDB, Query

db = TinyDB('database.json')

def ajouter_client():
    nom = input("Nom du client : ")
    adresse_email = input("Adresse email du client : ")
    budget_projet = float(input("Budget du projet : "))
    montant_facture = float(input("Montant de la facture : "))

    client = {
        'type': 'Client',
        'nom': nom,
        'adresse_email': adresse_email,
        'budget_projet_initial': budget_projet
    }

    table = db.table('clients')
    table.insert(client)

    facture = {
        'nom_client': nom,
        'montant': montant_facture
    }

    table_factures = db.table('factures')
    table_factures.insert(facture)

    print("Le client a été ajouté avec succès.")

def modifier_client():
    nom = input("Nom du client à modifier : ")

    table = db.table('clients')
    client = table.get(Query().nom == nom)

    if client:
        print("Veuillez entrer les nouvelles informations pour le client (laissez vide pour conserver les valeurs actuelles) :")
        new_nom = input(f"Nouveau nom du client [{client['nom']}] : ") or client['nom']
        new_adresse_email = input(f"Nouvelle adresse email du client [{client['adresse_email']}] : ") or client['adresse_email']
        new_budget_projet = input(f"Nouveau budget du projet [{client['budget_projet_initial']}] : ") or client['budget_projet_initial']
        
        if 'montant_facture' in client:
            new_montant_facture = input(f"Nouveau montant de la facture [{client['montant_facture']}] : ") or client['montant_facture']
        else:
            new_montant_facture = input("Nouveau montant de la facture : ")

        updated_client = {
            'type': client['type'],
            'nom': new_nom,
            'adresse_email': new_adresse_email,
            'budget_projet_initial': new_budget_projet,
            'montant_facture': new_montant_facture
        }

        # Mettre à jour le client
        table.update(updated_client, Query().nom == nom)
        print("Le client a été modifié avec succès.")

        # Mettre à jour les factures associées
        table_factures = db.table('factures')
        table_factures.update({'nom_client': new_nom}, Query().nom_client == nom)
        print("Les factures associées ont été mises à jour.")

    else:
        print(f"Le client {nom} n'existe pas.")


def supprimer_client():
    nom = input("Nom du client à supprimer : ")

    table = db.table('clients')
    client = table.get(Query().nom == nom)

    if client:
        # Supprimer le client
        table.remove(Query().nom == nom)
        print("Le client a été supprimé avec succès.")

        # Supprimer les factures associées
        table_factures = db.table('factures')
        table_factures.remove(Query().nom_client == nom)
        print("Les factures associées ont été supprimées.")
    else:
        print(f"Le client {nom} n'existe pas.")

def afficher_clients():
    table = db.table('clients')
    clients = table.all()

    if clients:
        print("Liste des clients :")
        for client in clients:
            print(f"Nom : {client['nom']}, Adresse email : {client['adresse_email']}, Budget du projet : {client['budget_projet_initial']}")
    else:
        print("Aucun client n'est enregistré.")

# Exemple d'utilisation
while True:
    print("1. Ajouter un client")
    print("2. Modifier un client")
    print("3. Supprimer un client")
    print("4. Afficher la liste des clients")
    print("5. Quitter")

    choix = input("Choix : ")

    if choix == "1":
        ajouter_client()
    elif choix == "2":
        modifier_client()
    elif choix == "3":
        supprimer_client()
    elif choix == "4":
        afficher_clients()
    elif choix == "5":
        break
    else:
        print("Choix invalide. Veuillez réessayer.")