
import random

def lancerJeu(nb_min, nb_max, nb_a_trouve, vies):
    nb_utilisateur = None

    while vies > 0 and nb_a_trouve != nb_utilisateur:

        try:
            nb_utilisateur = int(input(f"Quel est le nombre magique entre {nb_min} et {nb_max} ? "))
        except ValueError:
            print("Rentrez un nombre")
            continue

        if nb_utilisateur < nb_min or nb_utilisateur > nb_max:
            print(f"Le nombre doit être entre {nb_min} et {nb_max}")
            continue

        if nb_utilisateur == nb_a_trouve:
            print("Bravo vous avez trouvé le nombre !")
        else:
            vies -= 1

            if vies == 0:
                print(f"Dommage, vous avez perdu. Le nombre était {nb_a_trouver}")
            else:
                print(f"Il vous reste {vies} vies")

                if nb_utilisateur < nb_a_trouve:
                    print("Le nombre est plus grand")
                else:
                    print("Le nombre est plus petit")
                
nb_min = 1
nb_max = 10
nb_a_trouver = random.randint(nb_min, nb_max)
vies = 4

lancerJeu(nb_min, nb_max, nb_a_trouver, vies)