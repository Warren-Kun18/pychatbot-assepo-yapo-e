import os
from os import listdir
from os.path import isfile, join
from Fonctions import *

print("1. Aficher les mots moins importants")
print("2. Aficher les mots avec le score TD-IDF le plus élevé")
print("3. Indiquer les mots les plus répétés")
print("4. Indiquer les noms des présidents qui ont parlé de la Nation et celui qui l'a répété le plus ")
print("5. Indiquer le premier président qui a parler du climat et/ou de l'écologie")
print("6. Quels sont les mots que tous les présidents ont évoqués hormis les mots importants")

# Effectuer une liste des nom des fichiers du dossier "Speeches"
liste_fichiers = [f for f in listdir('C:/Users/warre/PycharmProjects/ProjectSemestre2/Speeches') if
           isfile(join("C:/Users/warre/PycharmProjects/ProjectSemestre2/Speeches", f))]

print(liste_fichiers)
"supprime_ponctuation(test)"
afficher_liste_de_nom(liste_fichiers)

for i in range(len(liste_fichiers)):
    convertir_fichier(liste_fichiers[i])

fichier_cleaned = []
for i in range (len(liste_fichiers)):
    fichier_cleaned[i] =



"""
liste_de_nom = []
#Ajoute à chaque élément de ma liste "liste_de_nom"
for i in range(len(liste_fichiers)):
    liste_de_nom.append(extraire_nom(liste_fichiers[i]))




# Chemin d'accès des différents fichiers
chemin-vers-discours_des_presiednts




nom = os.path.basename(Chirac)
print(nom)
nom_pres = nom[11:-4]
if (nom_pres[-1] =='1') or (nom_pres[-1] == '2'):
    nom_pres = nom[11:-5]
print(nom_pres)
"""

""""

print(dico)

for nom, prenom in dico.items() :
    print(nom, prenom)

"""
