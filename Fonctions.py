import os
import shutil
from math import *
from os import listdir
from os.path import isfile, join

# Créer un dictionnaire qui asssocie à chaque nom, un prénom
nom_des_presidents = {
    "Chirac": "Jacques", "Giscard dEstaing": "Valérie", "Hollande": "François",
    "Macron": "Emmanuel", "Miterrand": "François", "Sarkozy": "Nicolas"
}


# Extraire le nom des president des noms des fichiers
def extraire_nom(nom_du_fichier):
    # Extraire le nom des présiedents
    nom_president_avec_extension = nom_du_fichier.split('_')
    nom_president_sans_extension = nom_president_avec_extension[1].split('.')
    nom_president = nom_president_sans_extension[0]

    # Verifier si le nom du president comporte un 1 ou un 2 au dernier caractère. Si oui, on le supprime.
    if (nom_president[-1] == '1') or (nom_president[-1] == '2'):
        nom_president = nom_president[:-1]

    return nom_president


def associer_prenom(nom, nom_des_presidents):
    # Retourne le dictionnaire crée précedemment
    return nom_des_presidents[nom]


def afficher_liste_de_nom(noms_des_fichiers):
    liste_de_nom = []
    # Ajoute à chaque élément de ma liste "liste_de_nom"
    for i in range(len(noms_des_fichiers)):
        liste_de_nom.append(extraire_nom(noms_des_fichiers[i]))
        liste_de_nom = list(set(liste_de_nom))
    print(liste_de_nom)


def convertir_fichier(nom_fichier):
    # Copie le contenu du fichier
    fichier_origine = open("Speeches/{}".format(nom_fichier), "r", encoding='UTF-8')
    lignes = fichier_origine.readlines()
    fichier_origine.close()
    # Créer un nouveau fichier dans le dossier Cleaned et transformer tout le dossier en minuscule
    fichier_modifie = open("Cleaned/{}".format(nom_fichier), "w", encoding='UTF-8')
    for ligne in lignes:
        fichier_modifie.write(changer_le_format(ligne))
    fichier_modifie.close()


# Supprime la ponctuation des fichiers et remplace les apostrophes par des la ou le
def changer_le_format(texte, supprime_ponctuation=True):
    texte_sans_ponctuation = ""
    if supprime_ponctuation:
        texte = texte.replace("-", " ")
        texte = texte.replace("'", " ")
        ponctuation = ['!', '"', '#', '&', '(', ')', '*', '+', ',', '.', '/', ':', '']
        texte_sans_ponctuation = ''.join([c for c in texte if c not in ponctuation])

    return texte_sans_ponctuation.lower()

def tf(chemin):
    print("Test pour debud", chemin)
    fichier = open(chemin, "r", encoding='UTF-8')
    ligne = fichier.readlines()
    dico_repetition_mot = {}
    # transformation de fichier en liste
    liste = []
    for i in range(len(ligne)):
        liste.append(ligne[i].strip().split(" "))
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

    print("Est-ce que c'est toi ?",chemins_complets)

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
    tf_global = []
    idf_global = idf(repertoire)
    contenu = os.listdir(repertoire)
    chemins_complets = [os.path.join(repertoire, element) for element in contenu]
    for i in range(len(chemins_complets)):
        tf_global.append(tf(chemins_complets[i]))

    matrice_tf_idf = {}
    for i in range(len(tf_global)):
        for mot, score_tf in tf_global[i].items():

            if mot in matrice_tf_idf:
                matrice_tf_idf[mot].append(score_tf * idf_global[mot])
            else:
                matrice_tf_idf[mot] = [score_tf * idf_global[mot]]








