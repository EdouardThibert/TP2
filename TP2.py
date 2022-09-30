#Édouard Thibert
#TP2

import random
import time
chiffre_a_trouver = random.randint(1,100)
nombre_dessais = 10

play_game = True
while play_game:
    essai = int(input("Devinez le nombre entre 1 et 100\n"))
    if essai == chiffre_a_trouver:
        print("Vous avez trouvé le bon nombre")
        time.sleep(3)
        print("Fin du programme")
        play_game = False
    elif essai < chiffre_a_trouver:
        nombre_dessais = nombre_dessais - 1
        print("Plus Haut\n")
    elif essai > chiffre_a_trouver:
        print("Plus Bas\n")
        nombre_dessais = nombre_dessais - 1
    else:
        print("C'est pas bon")
    if nombre_dessais == 1:
        print("Vous avez raté")
        time.sleep(3)
        print("Fin du programme")
        play_game = False

