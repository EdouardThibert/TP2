#Édouard Thibert
#TP2

import random

chiffre_a_trouver = random.randint(1,100)
essai = int(input("Devinez le nombre"))

play_game = True
point_de_vie = 10
while play_game:
    print("Il faut deviner le nombre")
    point_de_vie -= 2
    if point_de_vie < 0:
        play_game = False

if essai == chiffre_a_trouver:
    print("Vous avez trouvé le bon nombre")
elif essai < chiffre_a_trouver:
    print("Plus Haut")
elif essai > chiffre_a_trouver:
    print("Plus Petit")
else:
    print("C'est pas bon")