import os
import shutil
from math import *

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
    fichier_modifife = open("Cleaned/{}".format(nom_fichier), "w", encoding='UTF-8')
    for ligne in lignes:
        fichier_modifife.write(changer_le_format(ligne))





# Supprime la ponctuation des fichiers et remplace les apostrophes par des la ou le
def changer_le_format(texte, supprime_ponctuation = True):
    global texte_sans_ponctuation
    if supprime_ponctuation:
        texte = texte.replace("-", " ")
        texte = texte.replace("'", " ")
        ponctuation = ['!', '"', '#', '&', '(', ')', '*', '+', ',', '.', '/', ':', '']
        texte_sans_ponctuation = ''.join([c for c in texte if c not in ponctuation])

    return texte_sans_ponctuation.lower()


def tf(chaine_de_caractere):
    # transformation de fichier en liste
    liste = chaine_de_caractere.split(" ")
    # determiantion de la frequence d'un mot dans un document
    dico_repetition_mot = {}
    for i in range(len(liste)):
        valeur_de_cle = liste.count(liste[i])
        # sauvegarde de la frequance de chaque mot dans un dictionaire
        dico_repetition_mot[liste[i]] = valeur_de_cle
    return dico_repetition_mot


dictionaire_general_rep_mot = {}


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

#fonction TF-IDF
def scoreTF_IDF(chemin_du_document):#le parametre est une liste qui doit contenir les differents fichiers
    matriceTF_idf = []
    #remplissage de la ligne
    for mot in dictionaire_general_rep_mot.keys():
        ligne_matriceTF_idf = []
        for fichier in chemin_du_document:
            f_tf = tf(fichier)
            value_tf=f_tf.get(mot,0)#key_tf prend la valeur attribuer a la clé de "mot" si elle existe dans le cas contraire c'est 0
            value_idf=dictionaire_general_rep_mot[mot]
            tf_idf= value_tf*value_idf
            ligne_matriceTF_idf.append(tf_idf)#ajout du score tf_idf du mot dans chaque document(correspond a la colonne)
        matriceTF_idf.append(ligne_matriceTF_idf)#ajout de la ligne du score tf_idf du mot dans la matrice

    return matriceTF_idf


