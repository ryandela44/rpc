import random

your_life = 3
cpu_life = 3
while your_life != 0 and cpu_life != 0:
    player_move = input("Quel est votre prochain coup? (roche,papier,ciseau) : ")
    choices = ["roche", "papier", "ciseau"]
    for x in range(len(choices)):
        if player_move == choices[x]:
            break
        while player_move != "roche" and player_move != "papier" and player_move != "ciseau" and x == len(choices) - 1:
            print("Entree Invalide")
            player_move = input("Quel est votre prochain coup? (roche,papier,ciseau) : ")

    cpu_move = choices[random.randint(0, len(choices) - 1)]
    if player_move == cpu_move:
        print("Egalite!")
    elif player_move == "roche" and cpu_move == "papier":
        your_life -= 1
        print("l'ordinateur utilise : " + cpu_move + " les points de vie " + str(cpu_life) + " sont de " + str(
            your_life) + " pour vous")
    elif player_move == "papier" and cpu_move == "ciseau":
        your_life -= 1
        print("l'ordinateur utilise : " + cpu_move + " les points de vie " + str(cpu_life) + " sont de " + str(
            your_life) + " pour vous")
    elif player_move == "ciseau" and cpu_move == "roche":
        your_life -= 1
        print("l'ordinateur utilise : " + cpu_move + " les points de vie " + str(cpu_life) + " sont de " + str(
            your_life) + " pour vous")
    else:
        cpu_life -= 1
        print("l'ordinateur utilise : " + cpu_move + " les points de vie " + str(cpu_life) + " sont de " + str(
            your_life) + " pour vous")
if your_life > cpu_life:
    print("Felicitations vous avez gagne , il vous reste" + str(your_life) + " de vie")
else:
    print("Vous avez perdu :( l'ordinateur avait encore " + str(cpu_life) + " points de vie")
