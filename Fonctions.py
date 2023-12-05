import os
import shutil
from math import *
from os import listdir #renvoie une liste contenant les noms des fichier dans le répertoire spécifié
from os.path import isfile, join #vérifie si un chemin donné correspond à un fichier régulier (renvoi un booleen)

# Créer un dictionnaire qui asssocie à chaque nom, un prénom
nom_des_presidents = {
    "Chirac": "Jacques", "Giscard dEstaing": "Valérie", "Hollande": "François",
    "Macron": "Emmanuel", "Miterrand": "François", "Sarkozy": "Nicolas"
}


# fonction pour extraire le nom des presidents des noms des fichiers
def extraire_nom(nom_du_fichier):
    # Extraire le nom des présiedents
    nom_president_avec_extension = nom_du_fichier.split('_')
    nom_president_sans_extension = nom_president_avec_extension[1].split('.')
    nom_president = nom_president_sans_extension[0]

    # Verifier si le nom du president comporte un nombre. Si oui, on le supprime.
    if (nom_president[-1] == '1') or (nom_president[-1] == '2'):
        nom_president = nom_president[:-1]

    return nom_president


def associer_prenom(nom, nom_des_presidents):
    # Retourne le dictionnaire 'nom_des_presidents'
    return nom_des_presidents[nom]

#fonction affichage de la liste de nom
def afficher_liste_de_nom(noms_des_fichiers):
    liste_de_nom = []
    # Ajoute à chaque élément de ma liste "liste_de_nom"
    for i in range(len(noms_des_fichiers)):
        liste_de_nom.append(extraire_nom(noms_des_fichiers[i]))
        liste_de_nom = list(set(liste_de_nom))
    print(liste_de_nom)

#fonction de conversion de chaque fichier en minuscule
def convertir_fichier(nom_fichier):
    # Copie le contenu du fichier
    fichier_origine = open("Speeches/{}".format(nom_fichier), "r", encoding='UTF-8')#ouverture du fichier a modifier
    lignes = fichier_origine.readlines()
    fichier_origine.close()
    # Créer un nouveau fichier dans le dossier Cleaned et transformer tout le dossier en minuscule
    fichier_modifie = open("Cleaned/{}".format(nom_fichier), "w", encoding='UTF-8')#ouverture d'un nouveau fichier clean
    for ligne in lignes:
        fichier_modifie.write(changer_le_format(ligne))
    fichier_modifie.close()


# Supprime la ponctuation des fichiers
def changer_le_format(texte, supprime_ponctuation=True):
    texte_sans_ponctuation = ""
    if supprime_ponctuation:
        texte = texte.replace("-", " ")
        texte = texte.replace("'", " ")
        ponctuation = ['!', '"', '#', '&', '(', ')', '*', '+', ',', '.', '/', ':', '']
        texte_sans_ponctuation = ''.join([c for c in texte if c not in ponctuation])

    return texte_sans_ponctuation.lower()

#fonction tf
def tf(chemin):

    fichier = open(chemin, "r", encoding='UTF-8')
    lignes = fichier.readlines()
    dico_repetition_mot = {}
    # transformation de fichier en liste
    liste = []
    for i in range(len(lignes)):
        liste.append(lignes[i].strip().split(" "))
    for i in range(len(liste)):
        for j in range(len(liste[i])):
            if len(liste[i][j]) <= 1:
                continue

            valeur_de_cle = 0
            if liste[i][j] in dico_repetition_mot:
                valeur_de_cle = dico_repetition_mot[liste[i][j]] + 1
            else:
                valeur_de_cle = 1

            # sauvegarde de la frequence de chaque mot dans un dictionaire
            dico_repetition_mot[liste[i][j]] = valeur_de_cle

    return dico_repetition_mot


dictionaire_general_rep_mot = {}

""""
def idf(nom_fichier):
    # remplissage du dictionnaire de tout le corpus avec la fonction tf
    for fichier in nom_fichier:
        f_tf = tf(fichier)
        for mot, value in f_tf.items():
            if mot not in dictionaire_general_rep_mot:
                dictionaire_general_rep_mot[mot] = 1
            else:
                dictionaire_general_rep_mot[mot] += 1
    # calcule du idf pour chaque mot puis rangement dans le dictionaire_general_rep_mot
    dico_idf = {}
    for mot, count in dictionaire_general_rep_mot.items():
        # il faut changer le 2
        dico_idf[mot] = int(log((2 / (count)) + 1))

    return dico_idf
"""
def idf(repertoire):
    liste_dico =[]
    contenu = os.listdir(repertoire)
    chemins_complets = [os.path.join(repertoire, element) for element in contenu]


    for i in range(len(chemins_complets)):
        liste_dico.append(tf(chemins_complets[i]))

    dico_global = {}
    for i in range(len(liste_dico)):
        for mot, recurrence in liste_dico[i].items():
            if mot in dico_global:
                dico_global[mot] = dico_global[mot] +1
            else:
                dico_global[mot] = 1
    for mot_global, recurrence_global in dico_global.items():
        dico_global[mot_global] = log(len(chemins_complets)/recurrence_global)
    return dico_global

# fonction TF-IDF
"""def scoreTF_IDF(chemin_du_document):  # le parametre est une liste qui doit contenir les differents fichiers
    matriceTF_idf = []
    # remplissage de la ligne
    for mot in dictionaire_general_rep_mot.keys():
        ligne_matriceTF_idf = []
        for fichier in chemin_du_document:
            f_tf = tf(fichier)
            value_tf = f_tf.get(mot,
                                0)  # key_tf prend la valeur attribuer a la clé de "mot" si elle existe dans le cas contraire c'est 0
            value_idf = dictionaire_general_rep_mot[mot]
            tf_idf = value_tf * value_idf
            ligne_matriceTF_idf.append(
                tf_idf)  # ajout du score tf_idf du mot dans chaque document(correspond a la colonne)
        matriceTF_idf.append(ligne_matriceTF_idf)  # ajout de la ligne du score tf_idf du mot dans la matrice

    return matriceTF_idf
"""

def tf_idf(repertoire):
    #Création d'une liste regroupant les tf de chaque fichier
    tf_global = []
    #Appel de la fonction idf
    idf_global = idf(repertoire)
    #Faire une liste des chemins du dossier choisi
    contenu = os.listdir(repertoire)
    chemins_complets = [os.path.join(repertoire, element) for element in contenu]

    for i in range(len(chemins_complets)):
        #Mettre à chaque élément de la liste son score tf
        tf_global.append(tf(chemins_complets[i]))

    matrice_tf_idf = {}#matrice est un dictionaire
    for i in range(len(tf_global)):
        for mot, score_tf in tf_global[i].items():#parcours de la liste tf_global contenant les tf"dico" de chaque fichier

            if mot in matrice_tf_idf:
                matrice_tf_idf[mot].append(score_tf * idf_global[mot])#ajout du score tf_idf de chaque mot dans la liste de associer a chaque mot
            else:
                matrice_tf_idf[mot] = [score_tf * idf_global[mot]]#creation du mot et ajout du score tf_idf du mot dans la liste de associer a ce mot

    return matrice_tf_idf

#PARTIE 2

#fonction tokenisation de la question
def tf_idf_question(question):
    question_clean=changer_le_format(question)#permet d'enlever toutes les ponctuations et de lower la question
    liste_de_mot=question_clean.split(" ")
    return liste_de_mot
#fonction calcul de la similarité
def produit_scalaire(vectA,vectB):















def recherche_mot(liste_question, matrice_tf_idf):
    list_mot_trouves = []
    for mot in liste_question:
        if mot in matrice_tf_idf :
            list_mot_trouves.append(mot)
    return list_mot_trouves

def calcul_tf_idf(liste_mot_trouves, liste_question):
