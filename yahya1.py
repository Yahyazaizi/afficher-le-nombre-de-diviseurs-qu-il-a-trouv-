
entier = int(input("Entrez un entier : "))


compteur_diviseurs = 0


print(f"Les diviseurs de {entier} sont :")
for diviseur in range(1, entier + 1):
    if entier % diviseur == 0:
        print(diviseur)
        compteur_diviseurs += 1


print(f"Il y a {compteur_diviseurs} diviseurs de {entier}.")
