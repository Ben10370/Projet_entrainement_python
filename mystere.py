import random

def jouer_jeu():
    nombre_mystere = random.randint(1, 100)
    nombre_tentatives = 0

    print("Bienvenue dans le jeu de devinette de nombres !\n")
    print("Un nombre mystère a été choisi entre 1 et 100.\n")
    print("Vous avez 10 tentatives pour le deviner.\n")

    while nombre_tentatives < 10:
        nombre_tentatives += 1
        nombre_propose = int(input(f"Tentative n°{nombre_tentatives} : Entrez un nombre : "))

        if nombre_propose < nombre_mystere:
            print("Le nombre est trop bas.")
        elif nombre_propose > nombre_mystere:
            print("Le nombre est trop élevé.")
        else:
            print(f"Félicitations ! Vous avez deviné le nombre mystère en {nombre_tentatives} tentatives.")
            break

    if nombre_tentatives == 10:
        print(f"Vous avez épuisé toutes vos chances ! Le nombre mystère était {nombre_mystere}.")
        
        
    while True:
        rejouer = input("Voulez-vous jouer à nouveau ? (Oui/Non) ")
        rejouer = rejouer.strip().lower()

        if rejouer == "oui":
            jouer_jeu()
            break
        elif rejouer == "non":
            print("Merci d'avoir joué. À bientôt !")
            break
        else:
            print("Veuillez entrer uniquement 'oui' ou 'non'.")

jouer_jeu()