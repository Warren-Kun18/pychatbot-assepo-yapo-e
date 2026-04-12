import os
import shutil
from math import *
from os import listdir  # renvoie une liste contenant les noms des fichier dans le répertoire spécifié
from os.path import isfile, join  # vérifie si un chemin donné correspond à un fichier régulier (renvoi un booleen)

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


# fonction affichage de la liste de nom
def afficher_liste_de_nom(noms_des_fichiers):
    liste_de_nom = []
    # Ajoute à chaque élément de ma liste "liste_de_nom"
    for i in range(len(noms_des_fichiers)):
        liste_de_nom.append(extraire_nom(noms_des_fichiers[i]))
        liste_de_nom = list(set(liste_de_nom))

    return liste_de_nom


# fonction de conversion de chaque fichier en minuscule
def convertir_fichier(nom_fichier):
    # Copie le contenu du fichier
    fichier_origine = open("Speeches/{}".format(nom_fichier), "r", encoding='UTF-8')  # ouverture du fichier a modifier
    lignes = fichier_origine.readlines()
    fichier_origine.close()
    
    # Vérifier que le dossier Cleaned existe (si non en le crée)
    if not os.path.exists("Cleaned"):
        os.makedirs("Cleaned")
        
    # Créer un nouveau fichier dans le dossier Cleaned et transformer tout le dossier en minuscule
    fichier_modifie = open("Cleaned/{}".format(nom_fichier), "w",
                           encoding='UTF-8')  # ouverture d'un nouveau fichier clean
    for ligne in lignes:
        fichier_modifie.write(changer_le_format(ligne))
    fichier_modifie.close()


# Supprime la ponctuation des fichiers
def changer_le_format(texte, supprime_ponctuation=True):  # Si on ne met pas la parametre ça supprime la ponctuation
    texte_sans_ponctuation = ""
    if supprime_ponctuation: #Remplace les ponctuations par des espaces
        texte = texte.replace("-", " ")
        texte = texte.replace("'", " ")
        ponctuation = ['!', '"', '#', '&', '(', ')', '*', '+', ',', '.', '/', ':', '']
        texte_sans_ponctuation = ''.join([c for c in texte if c not in ponctuation]) #Le texte sans ponctuation est mis dans une variable

    return texte_sans_ponctuation.lower()


# fonction tf
def tf(chemin):
    fichier = open(chemin, "r", encoding='UTF-8')
    lignes = fichier.readlines()
    dico_repetition_mot = {}
    # transformation de fichier en liste
    liste = [] #Création d'une liste
    for i in range(len(lignes)): #Parcours de chaque ligne du fichier
        liste.append(lignes[i].strip().split(" "))  #Met tous les mots du fichier dans la liste qu'on a créé
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
    liste_dico = []  # Création d'une liste qui se nomme Liste dico
    contenu = os.listdir(repertoire) #Prend tous les chemins des fichiers d'un repertoire
    chemins_complets = [os.path.join(repertoire, element) for element in contenu]

    for i in range(len(chemins_complets)):
        liste_dico.append(tf(chemins_complets[i]))

    dico_global = {}#Création d'un dico
    for i in range(len(liste_dico)): #Parcours de la liste dico
        for mot, recurrence in liste_dico[i].items(): #Parcours de
            if mot in dico_global:
                dico_global[mot] = dico_global[mot] + 1
            else:
                dico_global[mot] = 1
    for mot_global, recurrence_global in dico_global.items():
        dico_global[mot_global] = log(len(chemins_complets) / recurrence_global)
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


def tf_idf(repertoire, transposee=False):  # Si il n'y a pas de parametre pour la transposée ça ne met pas la transposée
    # Création d'une liste regroupant les tf de chaque fichier
    liste_mots = []
    tf_global = []
    nb_mot_unique = 0
    # Appel de la fonction idf
    idf_global = idf(repertoire)
    # Faire une liste des chemins du dossier choisi
    contenu = os.listdir(repertoire)
    chemins_complets = [os.path.join(repertoire, element) for element in contenu]

    for i in range(len(chemins_complets)):
        # Mettre à chaque élément de la liste son score tf
        tf_fichier = tf(chemins_complets[i])
        tf_global.append(tf_fichier)

        for mot, occurence in tf_fichier.items():
            if mot not in liste_mots:
                liste_mots.append(mot)

    nb_mot_unique += len(liste_mots)
    matrice_tf_idf = {}  # matrice est un dictionaire
    for i in range(nb_mot_unique):
        for j in range(len(tf_global)):

            if liste_mots[i] in matrice_tf_idf:
                score = 0.0
                if liste_mots[i] in tf_global[j]:  # Si le mot n'apparait pas dans le fichier on met 0.0
                    score = tf_global[j][liste_mots[i]] * idf_global[liste_mots[i]]
                matrice_tf_idf[liste_mots[i]].append(
                    score)  # ajout du score tf_idf de chaque mot dans la liste de associer a chaque mot
            else:
                score = 0.0
                if liste_mots[i] in tf_global[j]:  # Si le mot n'apparait pas dans le fichier on met 0.0
                    score = tf_global[j][liste_mots[i]] * idf_global[liste_mots[i]]
                matrice_tf_idf[liste_mots[i]] = [
                    score]  # creation du mot et ajout du score tf_idf du mot dans la liste de associer a ce mot

    if transposee: #Si la la variable transposée est vrai alors on transpose la matrice
        matrice_tf_idf = transposee_matrice(matrice_tf_idf)

    return matrice_tf_idf


def transposee_matrice(matrice_tf_idf):
    B = []

    for i in range(len(list(matrice_tf_idf.values())[0])):
        c = []
        for j in range(len(matrice_tf_idf.values())):
            c.append(list(matrice_tf_idf.values())[j][i])
        B.append(c)

    return B


# PARTIE 2

# fonction tokenisation de la question
def tokenisation_question(question):
    question_clean = changer_le_format(question)  # permet d'enlever toutes les ponctuations et de lower la question
    liste_de_mot_question = question_clean.split(" ")
    return liste_de_mot_question


# fonction calcul de la similarité

def recherche_mot(liste_mot_question, matrice_tf_idf):
    list_mot_trouves = []# Création d'une liste
    for mot in liste_mot_question: #Parcours de la liste
        if mot in matrice_tf_idf: #Si le mot se trouve dans la matrice tf_idf amors ça l'ajoute à liste qu'on vient créer
            list_mot_trouves.append(mot)

    return list_mot_trouves


def tf_question(liste_mot_question, matrice_tf_idf):
    dico_tf_question = {}  # création d'un dico
    for mot in matrice_tf_idf.keys():  # Parcours de la matrice tf-idf
        if mot in liste_mot_question:  # Si le mot de la question se trouve dans le corpus on calcule le TF
            dico_tf_question[mot] = liste_mot_question.count(mot) / len(liste_mot_question)
        else:  # Sinon on met 0 en valeur
            dico_tf_question[mot] = 0
    return dico_tf_question


def calcul_vecteur_tf_idf_question(chemin, liste_mot_question, matrice_tf_idf, avec_cle=False):
    idf_qst = idf(chemin)  # Appel de la fonction IDF
    tf_qst = tf_question(liste_mot_question, matrice_tf_idf)  # Appel de la fonction TF de la question
    # print(tf_qst)
    tf_idf_qst = 0
    if avec_cle:  # Si cette variable est vrai alors liste vecteur est dico
        liste_vecteur = {}
    else:  # Sinon liste vecteur est une liste
        liste_vecteur = []
    for mot in idf_qst.keys():
        if avec_cle:
            tf_idf_qst += idf_qst[mot] * tf_qst[mot]
            liste_vecteur[mot] = idf_qst[mot] * tf_qst[mot]
        else:
            tf_idf_qst += idf_qst[mot] * tf_qst[mot]
            liste_vecteur.append(idf_qst[mot] * tf_qst[mot])


    return liste_vecteur


def produit_scalaire(vectA, vectB):
    sommeAB = 0  # Initialisation d'une variable somme
    m = len(vectB)
    for i in range(0, m):
        """print(i)
        print("Vecteur A : ", vectA[i])
        print("Vecteur B : ", vectB[i])"""
        sommeAB = sommeAB + (float(vectA[i]) * float(
            vectB[i]))  # Somme du produit de  chaque élément du produits des vecteurs A et B
    # print("Somme AB :",sommeAB)
    return sommeAB


def norme_vecteur(vect):
    somme = 0
    m = len(vect)
    for i in range(0, m):
        somme = somme + (vect[i] * vect[i])  # Somme des carrées de chaquue élément du vecteur A

    somme = sqrt(somme)  # Racine carée de la somme du des carrées de chaque élément du vecteur A
    """print("Norme :",somme)"""
    return somme


def calcul_similarité(vectA, vectB):
    """print("Vecteur A : " ,vectA)
    print("Vecteur B :",vectB)"""
    resultat = produit_scalaire(vectA, vectB) / (norme_vecteur(vectA) * norme_vecteur(vectB))  # Calcul de la similarité

    return resultat


def calcul_document_pertinent(matrice_tf_idf, vecteur_tf_idf_question, liste_noms_fichiers):
    matval = len(matrice_tf_idf)  # calcul la longueur de la matrice
    similariteMax = 0  # initialisation de la vraible similariteMax
    idDoc = None  # initialisation de la variable idDoc
    for i in range(0, matval):
        similariteCourante = calcul_similarité(vecteur_tf_idf_question,
                                               matrice_tf_idf[i])  # appel de la fonction de la calcul similarite
        if (
                similariteCourante > similariteMax):  # attribue à similarité max la plus grande valeur du calcul de similarité
            similariteMax = similariteCourante
            idDoc = i

    return liste_noms_fichiers[idDoc]  # renvoie le fichier correspondant à ce calcul


def meilleur_tf_idf(chemin, liste_mot_question, matrice_tf_idf):
    vecteur_question = calcul_vecteur_tf_idf_question(chemin, liste_mot_question, matrice_tf_idf,
                                                      True)  # Appel de la fonction calcul vecteur tf idf question
    tf_idf_max = 0
    mot_max = None
    for mot, valeur in vecteur_question.items(): #Parcours du dico vecteur question
        if (valeur > tf_idf_max): #Renvoie le mot du meilleur score tf idf du dico vecteur question
            tf_idf_max = valeur
            mot_max = mot
        # print("Avant: ", valeur, mot)

    return mot_max


def reponse_pertinente(fichier, mot):
    fichier_ouvert = open(fichier, "r", encoding='UTF-8')
    lignes = fichier_ouvert.readlines() #Transforme les lignes de fichier en liste
    phrase_pertinente = ""
    for ligne in lignes: #Parcours des lignes
        if ligne.find(mot) > -1: #Quand le mot pertinent est trouvé pour la première fois il renvoie la ligne entière où il apparait
            phrase_pertinente = ligne
            break
    if phrase_pertinente:  # Vérifie si la chaîne n'est pas vide
        premier_caractere = phrase_pertinente[0].lower()  # Premier caractère en minuscule
        reste_de_la_phrase = phrase_pertinente[1:]  # Le reste de la chaîne
        return premier_caractere + reste_de_la_phrase
    else:
        return phrase_pertinente


def generation_reponse(phrase_pertinente, question):
    questions_genere = { #Création d'un dico afin de générer des réponses plus vivantes
        "Comment": "Après analyse, ",
        "Pourquoi": "Car, ",
        "Peux-tu": "Oui, bien sûr! ",
        "comment": "Après analyse, ",
        "pourquoi": "Car, ",
        "peux-tu": "Oui, bien sûr! "
    }

    for mot, reponse in questions_genere.items(): #Parcours du dico
        "reponse_genere = None"
        if mot in question: #Condition de si la clé du dico est dans la question posé par l'utilsateur alors ça met renvoie la valeur de clé plus la phrase pertinente
            reponse_genere = questions_genere[mot] + phrase_pertinente
            return reponse_genere
        else :
            reponse_genere = phrase_pertinente
            if reponse_genere:  #Met une majuscule à la première lettre de la phrase si elle a trouve l'une des clés du dico dans la question
                premier_caractere = reponse_genere[0].upper()
                reste_de_la_phrase = reponse_genere[1:]
                return premier_caractere + reste_de_la_phrase
            else:
                return reponse_genere
