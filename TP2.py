#Édouard Thibert
#TP2

import random
import time
chiffre_a_trouver = random.randint(1,100)
nombre_dessais = 0

play_game = True
while play_game:
    essai = int(input("J'ai choisi un nombre entre 1 et 100, à vous de le deviner\n"))
    if essai == chiffre_a_trouver:
        print("Vous avez trouvé le bon nombre en", nombre_dessais + 1,"essais")
        time.sleep(3)
        print("Fin du programme")
        play_game = False
    elif essai < chiffre_a_trouver:
        nombre_dessais = nombre_dessais + 1
        print("Plus Haut Que", essai, "\n")
    elif essai > chiffre_a_trouver:
        print("Plus Bas Que", essai,"\n")
        nombre_dessais = nombre_dessais + 1
    else:
        print("C'est pas bon")
    if nombre_dessais == 10:
        print("Vous avez raté")
        time.sleep(3)
        print("Fin du programme")
        play_game = False

