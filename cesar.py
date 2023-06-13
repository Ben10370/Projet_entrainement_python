def chiffrement_cesar(message, cle):
    message_chiffre = ""
    for lettre in message:
        if lettre.isalpha():
            if lettre.islower():
                index = ord(lettre) - ord('a')
                lettre_chiffree = chr((index + cle) % 26 + ord('a'))
            else:
                index = ord(lettre) - ord('A')
                lettre_chiffree = chr((index + cle) % 26 + ord('A'))
            message_chiffre += lettre_chiffree
        else:
            message_chiffre += lettre
    return message_chiffre

def dechiffrement_cesar(message_chiffre):
    solutions = []
    for cle in range(26):
        message_dechiffre = chiffrement_cesar(message_chiffre, -cle)
        solutions.append(message_dechiffre)
    return solutions

def casser_cesar(message_chiffre):
    solutions = dechiffrement_cesar(message_chiffre)
    for solution in solutions:
        print("Clé :", solutions.index(solution))
        print("Message déchiffré :", solution)
        print()

# Demande à l'utilisateur de saisir la clé de chiffrement et le message à chiffrer
cle = int(input("Entrez la clé de chiffrement : "))
message = input("Entrez le message à chiffrer : ")

# Chiffre le message en utilisant la clé de chiffrement
message_chiffre = chiffrement_cesar(message, cle)

# Affiche le message chiffré
print("Message chiffré :", message_chiffre)
print()

# Attaque par force brute
print("Attaque par force brute :")
casser_cesar(message_chiffre)