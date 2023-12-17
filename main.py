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
"""tf_idf_cleaned = tf_idf('Cleaned')  # tf_idf du fichier cleaned
liste_mot_plus_repete_chirac = []
# somme des tf-idf des mots répétés par chirac
for mot in tf_idf_cleaned.keys():
    liste_tf_idf = tf_idf_cleaned[mot]  # recuperation de la valeur(liste tf-idf) de la clé(du mot)
    liste_tf_idf=liste_tf_idf[:2]#recuperation du tf idf du mot dans les fichier de chirac
    #recuperation de la somme des tf-idf de chaque mot
    somme_tf_idf = sum(liste_tf_idf)
    #ajout du mot et de la somme de ses tf-idf des fichiers chirac
    if liste_mot_plus_repete_chirac==[] and mot not in liste_mot_non_important:
        liste_mot_plus_repete_chirac.append((mot,somme_tf_idf))
    #si la somme tf_idf du prochain mot est superieura celle du mot deja dans  liste_mot_plus_repete_chirac il est écrasé par le nouveau
    elif somme_tf_idf > liste_mot_plus_repete_chirac[0][1] and mot not in liste_mot_non_important:
        liste_mot_plus_repete_chirac=[(mot,somme_tf_idf)]
    #si la somme tf_idf du prochain mot est egale a celle du mot deja dans liste_mot_plus_repete_chirac il est ajouté
    elif somme_tf_idf == liste_mot_plus_repete_chirac[0][1]:
        liste_mot_plus_repete_chirac.append((mot,somme_tf_idf))
"""
"""
#fonction 4:  le(s) nom(s) du (des) président(s) qui a (ont) parlé de la « Nation » et celui qui l’a répété le plus de fois
# Recuperation du chemin du dossier où se trouve le script Python
chemin_script = os.path.dirname(os.path.realpath(__file__))

# Construisez le chemin vers le dossier de corpus en supposant qu'il se trouve au même niveau que le script
dossier_corpus = os.path.join(chemin_script, 'Cleaned')

# dico pour stocker les tf de nation par fichier
frequences_nation_par_president = {}
liste_des_presidents= afficher_liste_de_nom(liste_fichiers)
#association de la frequence de "nation" a chaque president
for fichier in listdir(dossier_corpus):
    if isfile(join(dossier_corpus, fichier)):
        frequence_mots = tf(join(dossier_corpus, fichier))
        # Trouve le nom du président dans le nom de fichier
        nom_president = next((president for president in liste_des_presidents if president in fichier), None)#recherche du nom du president dans "liste_des_presidents"
        if nom_president is None:
            continue  # Si aucun nom de président n'est trouvé, passer au fichier suivant

        # Cumuler les fréquences pour chaque président
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
    if isfile(join(dossier_corpus, fichier)):  # Vérification que l'élément est bien un fichier
        frequence_mots = tf(join(dossier_corpus, fichier))  # Appel de la fonction tf pour obtenir les fréquences des mots
        nom_president = next((president for president in liste_des_presidents if president in fichier), None)  # Extraction du nom du président du nom du fichier
        if nom_president is None:
            continue  # Si aucun nom de président n'est trouvé, passer au fichier suivant

        # Vérifier si l'un des mots du champ lexical est présent dans le fichier
        if any(mot in frequence_mots for mot in champ_lexical_ecologie):
            presidents_climat_ecologie[nom_president] = True  # Enregistrer le président comme ayant parlé de ces sujets
"""


question = "Je suis décidé à placer le septennat qui commence ?"

vecteur_question = calcul_tf_idf('Cleaned', tf_idf_question(question), tf_idf('Cleaned'))
print(vecteur_question)
matrice = tf_idf("Cleaned")
print(matrice)
print("Test len :",len(matrice.values()))
matval = len(matrice.values())
for i in range(0, matval):
    print(calcul_similarité(vecteur_question, list(matrice.values())[0]), "\n")

#print("Test : ",test)
"""
>>>>>>> d599b19 (Fonctions Calcul vecteur TF-IDF, Calcul de la similarité fonctionnelles)
#demande a l'utilisateur de choisir une fonctionalité
numero=int(input("Pour éxécuter l'une des fonctionnalité suivante entrez tapez le numéro qui précède la fonctionnalité: "))
#saisie securise
while not 1<=numero<=6:
    numero=int(input("Veuillez rentrer un numero parmi ceux proposer: "))
if numero==1:
    print(liste_mot_non_important)
elif numero==2:
    print(liste_mot_important)
elif numero==3:
    print(liste_mot_plus_repete_chirac)
elif numero==4:
    print(f"Le président qui a le plus parlé de 'Nation' est {president_max} avec {frequence_max} mentions.")
elif numero==5:
    if presidents_climat_ecologie:
        print("Présidents ayant parlé du climat et/ou de l'écologie :")
        for president in presidents_climat_ecologie:
            print(president)
    else:
        print("Aucun président n'a mentionné le climat ou l'écologie.")

"""


