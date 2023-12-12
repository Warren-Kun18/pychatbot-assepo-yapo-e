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
    tf_idf_cleaned=tf_idf('Cleaned')#tf_idf du fichier cleaned
    liste_mot_non_important=[]#liste mot non important
    #ajout des mots non importants dans liste_mot_non_important
    for mot, valeur in tf_idf_cleaned.items():
        if tf_idf_cleaned[mot]==[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]:
            liste_mot_non_important.append(mot)
    print(liste_mot_non_important)
    print(tf_idf_cleaned)
#fonctionnalité 2:Affichage les mots avec le score TD-IDF le plus élevé"
if numero==2:
    tf_idf_cleaned = tf_idf('Cleaned')#tf_idf du fichier cleaned
    liste_mot_important=[]
    #somme des tf-idf de chaque mot
    for mot, valeur in tf_idf_cleaned.items():
        liste_tf_idf=tf_idf_cleaned[mot]#recuperation de la valeur(liste tf-idf) de la clé(du mot)
        somme_tf_idf = 0
        #recuperation de la somme de tf_idf de chaque mot
        for i in range(len(tf_idf_cleaned[mot])):
            somme_tf_idf=somme_tf_idf+liste_tf_idf[i]
        #ajout du mot et de la somme de son tf-idf
        if liste_mot_important==[]:
            liste_mot_important.append((mot,somme_tf_idf))
        #si la somme tf_idf du prochain mot est superieur a celle du mot deja dans list_mot_important il est écrasé par le nouveau
        elif somme_tf_idf > liste_mot_important[0][1]:
            liste_mot_important=[(mot,somme_tf_idf)]
        #si la somme tf_idf du prochain mot est egale a celle du mot deja dans list_mot_important il est ajouté
        elif somme_tf_idf== liste_mot_important[0][1]:
            liste_mot_important.append((mot,somme_tf_idf))
    print(liste_mot_important)
#fonction 3: mot le plus prononcé par chirac
if numero==3:
    tf_idf_cleaned = tf_idf('Cleaned')  # tf_idf du fichier cleaned
    liste_mot_plus_repete_chirac = []
    # somme des tf-idf des mots chirac
    for mot, valeur in tf_idf_cleaned.items():
        liste_tf_idf = tf_idf_cleaned[mot]  # recuperation de la valeur(liste tf-idf) de la clé(du mot)
        somme_tf_idf = 0












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


with open(Cleaned, "r") as Cleaned:







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
