import os
from os import listdir
from os.path import isfile, join
from Fonctions import *

# Effectuer une liste des nom des fichiers du dossier "Speeches"
liste_fichiers = [f for f in listdir('Speeches') if
           isfile(join("Speeches", f))]
for i in range(len(liste_fichiers)):
    convertir_fichier(liste_fichiers[i])

#FONCTIONALITE
print("1. Afficher les mots moins importants")
print("2. Afficher les mots avec le score TD-IDF le plus élevé")
print("3. Indiquer les mots les plus répétés")
print("4. Indiquer les noms des présidents qui ont parlé de la Nation et celui qui l'a répété le plus ")
print("5. Indiquer le premier président qui a parler du climat et/ou de l'écologie")
print("6. Quels sont les mots que tous les présidents ont évoqués hormis les mots importants")
#demande a l'utilisateur de choisir une fonctionalité
numero=int(input("Pour éxécuter l'une des fonctionnalité suivante entrez tapez le numéro qui précède la fonctionnalité: "))
#saisie securise
while not 1<=numero<=6:
    numero=int(input("Veuillez rentrer un numero parmi ceux proposer: "))
#fonctionalité 1: affichage des mots les moins importants
if numero==1:
    tf_idf_cleaned=tf_idf('cleaned')#tf_idf du fichier cleaned
    liste_mot_non_important=[]#liste mot non important
    #ajout des mots non importants dans liste_mot_non_important
    for mot, valeur in tf_idf_cleaned.items():
        if tf_idf_cleaned[mot]==[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]:
            liste_mot_non_important.append(mot)
    print(liste_mot_non_important)
#fonctionnalité 2:Affichage les mots avec le score TD-IDF le plus élevé"
if numero==2:
    tf_idf_cleaned = tf_idf('cleaned')#tf_idf du fichier cleaned







    """for mot, valeur in 
    # affichage des mots les moins importants
    print("les mots les moins important dans le corpus sont:")
    for mot in liste_des_mots_moins_important:
        print(mot)






'''
print("afficher premiere list", liste_fichiers)

afficher_liste_de_nom(liste_fichiers)

for i in range(len(liste_fichiers)):
    convertir_fichier(liste_fichiers[i])


""with open(Cleaned,"r") as Cleaned:

    score_tf_idf_corpus = tf_idf(Cleaned)#
    mots_nom_importants = []
    for cle, valeur in score_tf_idf_corpus.items():
        if 0 in valeur:
            mots_nom_importants.append(cle)

    print("Les mots les plus imortants sont :", end=" ")
    for i in range(len(mots_nom_importants)):
        print(mots_nom_importants[i], ",", end = " " )""







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



print(dico)

for nom, prenom in dico.items() :
    print(nom, prenom)

"""
