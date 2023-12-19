import os
from os import listdir
from os.path import isfile, join
from Fonctions import *

nom_repertoire = 'Speeches'

# Effectuer une liste des nom des fichiers du dossier "Speeches"
liste_fichiers = [f for f in listdir(nom_repertoire) if
           isfile(join(nom_repertoire, f))]
for i in range(len(liste_fichiers)):
    convertir_fichier(liste_fichiers[i])




#fonctionalité 1: affichage des mots les moins importants
tf_idf_cleaned=tf_idf('Cleaned')#tf_idf du fichier cleaned
liste_mot_non_important=[]#liste mot non important
#ajout des mots non importants dans liste_mot_non_important
for mot, valeur in tf_idf_cleaned.items():
    if tf_idf_cleaned[mot]==[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]:
        liste_mot_non_important.append(mot)




#fonctionnalité 2:Affichage les mots avec le score TD-IDF le plus élevé"
tf_idf_cleaned = tf_idf('Cleaned')#tf_idf du fichier cleaned
liste_mot_important=[]
#somme des tf-idf de chaque mot
for mot in tf_idf_cleaned.keys():
    liste_tf_idf=tf_idf_cleaned[mot]#recuperation de la valeur(liste tf-idf) de la clé(du mot)
    #recuperation de la somme de tf_idf de chaque mot
    somme_tf_idf = sum(liste_tf_idf)
    #ajout du mot et de la somme de ses tf-idf
    if liste_mot_important==[]:
        liste_mot_important.append((mot,somme_tf_idf))
    #si la somme tf_idf du prochain mot est superieur a celle du mot deja dans list_mot_important il est écrasé par le nouveau
    elif somme_tf_idf > liste_mot_important[0][1]:
        liste_mot_important=[(mot,somme_tf_idf)]
    #si la somme tf_idf du prochain mot est egale a celle du mot deja dans list_mot_important il est ajouté
    elif somme_tf_idf== liste_mot_important[0][1]:
        liste_mot_important.append((mot,somme_tf_idf))


#fonction 3: mot le plus prononcé par chirac
tf_idf_cleaned = tf_idf('Cleaned')  # tf_idf du fichier cleaned
liste_mot_plus_repete_chirac = []
# somme des tf-idf des mots répétés par chirac
for mot in tf_idf_cleaned.keys():
    liste_tf_idf = tf_idf_cleaned[mot]  # recuperation de la valeur(liste tf-idf) de la clé(du mot)
    liste_tf_idf=liste_tf_idf[:2]#recuperation du tf idf du mot dans les fichier de chirac
    #recuperation de la somme des tf-idf de chaque mot
    somme_tf_idf = sum(liste_tf_idf)
    #ajout du mot et de la somme de ses tf-idf des fichiers chirac
    if mot not in liste_mot_non_important:
        if liste_mot_plus_repete_chirac==[] :
                liste_mot_plus_repete_chirac.append((mot,somme_tf_idf))
    #si la somme tf_idf du prochain mot est superieur a celle du mot deja dans  liste_mot_plus_repete_chirac il est écrasé par le nouveau
        elif somme_tf_idf > liste_mot_plus_repete_chirac[0][1]:
            liste_mot_plus_repete_chirac = [(mot, somme_tf_idf)]

    #si la somme tf_idf du prochain mot est egale a celle du mot deja dans liste_mot_plus_repete_chirac il est ajouté
        elif somme_tf_idf == liste_mot_plus_repete_chirac[0][1]:
            liste_mot_plus_repete_chirac.append((mot, somme_tf_idf))


#fonction 4:  le(s) nom(s) du (des) président(s) qui a (ont) parlé de la « Nation » et celui qui l’a répété le plus de fois
# Recuperation du chemin du dossier où se trouve le script Python
chemin_script = os.path.dirname(os.path.realpath(__file__))

# Construction du chemin vers le dossier de corpus en supposant qu'il se trouve au même niveau que le script
dossier_corpus = os.path.join(chemin_script, 'Cleaned')

# dico pour stocker les tf de nation par fichier
frequences_nation_par_president = {}
liste_des_presidents= afficher_liste_de_nom(liste_fichiers)
#association de la frequence de "nation" a chaque president
for fichier in listdir(dossier_corpus):
    if isfile(join(dossier_corpus, fichier)):

        frequence_mots = tf(join(dossier_corpus, fichier))
        fichier = extraire_nom(fichier)#pour extraire les noms des fichiers
        # Trouve le nom du président dans le nom de fichier
        nom_president = next((president for president in liste_des_presidents if president in fichier), None)#recherche du nom du president dans "liste_des_presidents"
        if nom_president is None:
            continue  # Si aucun nom de président n'est trouvé, passer au fichier suivant

        # Cumulation des fréquences pour chaque président
        if 'nation' in frequence_mots:
            frequences_nation_par_president[nom_president] = frequences_nation_par_president.get(nom_president, 0) + frequence_mots['nation']
# Initialisation des variables pour suivre le président avec la fréquence la plus élevée
president_max = None
frequence_max = 0

    # Parcourir le dictionnaire pour trouver le président avec la fréquence la plus élevée
for president, frequence in frequences_nation_par_president.items():
    if frequence > frequence_max:
        frequence_max = frequence
        president_max = president

#fonction 5: Indiquer le(s) nom(s) du (des) président(s) qui a (ont) parlé du climat et/ou de l’écologie

# Définition du chemin vers le dossier de corpus
chemin_script = os.path.dirname(os.path.realpath(__file__))  # Chemin du dossier contenant le script
dossier_corpus = os.path.join(chemin_script, 'Cleaned')  # Chemin du dossier contenant les fichiers nettoyés

# Champ lexical pour le thème de l'écologie et du climat
champ_lexical_ecologie = [
    'écologie', 'environnement', 'durable',
    'réchauffement global', 'écologique', 'biodiversité',
    'changement climatique', 'énergies renouvelables',
    'empreinte carbone', 'développement durable', 'durabilité',
    'climat'
]

# Dictionnaire pour enregistrer les présidents ayant parlé de sujets liés à l'écologie et au climat
presidents_climat_ecologie = {}

# Parcourir chaque fichier du dossier_corpus
for fichier in listdir(dossier_corpus):
    if isfile(join(dossier_corpus, fichier)):
        # Vérification que l'élément est bien un fichier
        frequence_mots = tf(join(dossier_corpus, fichier)) # Appel de la fonction tf pour obtenir les fréquences des mots
        fichier = extraire_nom(fichier)#extraire le nom des fichiers
        nom_president = next((president for president in liste_des_presidents if president in fichier), None)  # Extraction du nom du président du nom du fichier
        if nom_president is None:
            continue  # Si aucun nom de président n'est trouvé, passer au fichier suivant

        # Vérifier si l'un des mots du champ lexical est présent dans le fichier
        if any(mot in frequence_mots for mot in champ_lexical_ecologie):
            presidents_climat_ecologie[nom_president] = True  # Enregistrer le président comme ayant parlé de ces sujets

#choix du mode
mode=int(input("tapez 1 pour utiliser lancer le mode fonctionnalité ou tapez 2 pour lancer le mode chatbot: "))
#saisie sécurisée
"""while mode !=1 or mode!=2:
    mode=int(input("tapez 1 pour utiliser lancer le mode fonctionnalité ou tapez 2 pour lancer le mode chatbot: "))"""
#mode fonctionnalité
if mode==1:
    # FONCTIONALITE
    print("1. Afficher les mots moins importants")
    print("2. Afficher les mots avec le score TD-IDF le plus élevé")
    print("3. Indiquer les mots les plus répétés par Chirac")
    print("4. Indiquer les noms des présidents qui ont parlé de la Nation et celui qui l'a répété le plus ")
    print("5. Indiquer le premier président qui a parler du climat et/ou de l'écologie")
    #boucle pour executer les fonctionnalités
    recommencer="oui"
    while recommencer=="oui":
        # demande a l'utilisateur de choisir une fonctionalité
        numero = int(input("Pour éxécuter l'une des fonctionnalité suivante entrez tapez le numéro qui précède la fonctionnalité: "))
        # saisie securise
        while not 1 <= numero < 6:
            numero = int(input("Veuillez rentrer un numero parmi ceux proposer: "))
        if numero==1:
            print(f"Vous avez tapez {numero}")
            print("Les mots les moins importants dans le corpus sont:")
            for mot in liste_mot_non_important:
                if mot != liste_mot_non_important[-1]:
                    print(mot, end=",")
                else:
                    print(mot)
        elif numero==2:
            print(f"Vous avez tapez {numero}")
            print("Le ou les mots avec avec le score TD-IDF le plus élevé dans le corpus sont:")
            for mot in liste_mot_important:
                if mot != liste_mot_important[-1][0] and len(liste_mot_important)!=1:
                    print(mot[0], end=",")
                else:
                    print(mot[0])
        elif numero==3:
            print(f"Vous avez tapez {numero}")
            print("Le ou les mots les plus répétés par le président Chirac sont:")
            for mot in liste_mot_plus_repete_chirac:
                print(mot[0])
        elif numero==4:
            print(f"Vous avez tapez {numero}")
            print("Les présidents qui ont parlé de 'Nation' sont:")
            for nom_president in frequences_nation_par_president.keys():
                print(nom_president)
            print(f"Le président qui a le plus parlé de 'Nation' est {president_max} avec {frequence_max} mentions.")
        elif numero==5:
            print(f"Vous avez tapez {numero}")
            if presidents_climat_ecologie:
                print("Présidents ayant parlé du climat et/ou de l'écologie :")
                for president in presidents_climat_ecologie.keys():
                    print(president)
            else:
                print("Aucun président n'a mentionné le climat ou l'écologie.")
        recommencer=input("Si vous voulez tester d'autres fonctionnalités entrez 'oui' sinon entrez 'non': ")
#mode chatbot
else:
    print("Bonjour je suis votre chatbot spécialisé dans les discours des présidents")
    question = str(input("Posez moi votre question : "))
    matrice = tf_idf(nom_repertoire, True)
    liste_question = tokenisation_question( question)
    vecteur_question = calcul_vecteur_tf_idf_question(nom_repertoire, liste_question, tf_idf(nom_repertoire))
    doc_pertinent = calcul_document_pertinent(matrice, vecteur_question, liste_fichiers)
    mot_pertinent = meilleur_tf_idf(nom_repertoire, liste_question, tf_idf(nom_repertoire))
    phrase_pertinente =  reponse_pertinente("./{}/{}".format(nom_repertoire, doc_pertinent), mot_pertinent)
    reponse_genere = generation_reponse(phrase_pertinente, question)
    print(reponse_genere)


