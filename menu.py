import matplotlib.pyplot as plt


def open_fichier() -> object:
    """
    Cette méthode ouvre et retourne le fichier générale contenant toutes les informations en gérant des cas d'érreurs
    :return: Le fichier dans une variable
    """
    try:
        f = open("dataBB.log.txt", "r")
    except IOError:
        print("Désolé quelque chose ne c'est pas passé comme prévu : Vérifier l'éxistance du fichier")
        raise
    return f


def retour():
    print('\n' * 3)


fichier = open_fichier()


def cree_liste_prof(entree):
    type_saisie = ''
    if '@' in entree:
        type_saisie = 'email'
        quitte_salle = entree + " has left"
        ouvre_salle = entree + " is starting room"
        tente_connexion = entree + " is attempting to login"
        liste = [quitte_salle, ouvre_salle, tente_connexion]

    elif '-' in entree:
        type_saisie = 'salle'
        quitte_salle = "has left " + entree
        ouvre_salle = " is starting room " + entree
        tente_connexion = "is attempting to login"
        liste = [quitte_salle, ouvre_salle, tente_connexion]
    return liste, type_saisie


def detail_connexion_prof(mail_or_nbSalle):
    """
    Cette méthode prends en paramètre un email ou le nombre d'une salle et renvoie
    :param mail_or_nbSalle:
    :return:
    """
    liste = cree_liste_prof(saisie)
    line = fichier.readline()
    nb_tentation = 0
    nb_ouverture = 0
    nb_faild = 0
    count = 0
    if '@' in saisie:
        while True:
            count += 1
            if not line:
                print(f"{saisie} : cette personne n'est pas présent dans la liste")
                break
            elif liste[0] in line:
                salle = line[-15:]
                print(saisie + " à quitter la salle :" + salle + " le :" + line[0:11] + " à " + line[11:19] + "\n")
            elif liste[1] in line:
                salle = line[-15:]
                print(saisie + " à ouvert la salle :" + salle + " le :" + line[0:11] + " à " + line[11:19] + "\n")
                nb_ouverture += 1
            elif liste[2] in line:
                salle = line[-15:]
                print(saisie + " à tenter de se connecter à la salle  :" + salle + " le :" + line[0:11] +
                      " à " + line[11:19] + "\n")
                nb_tentation += 1
        retour()
    elif '-' in saisie:
        while True:
            if not line:
                print(f"{saisie} cette salle n'est pas présent dans la liste")
                break
            elif liste[0] in line:
                duree = 0
                prof = line["?"]
                print(f'{prof} à accéder à la salle {saisie} le {line["?"]} à {line["?"]} durant {duree} jusqu\'à'
                      f' {line["?"]}')
            elif liste[1] in line:
                prof = line["?"]
                print(f'{prof} à quitter la salle {saisie} le {line["?"]} à {line["?"]}')
            elif liste[2] in line:
                prof = line["?"]
                print(f'{prof} à tenter de se connecter à  la salle {saisie} le {line["?"]} à {line["?"]}')


def detail_connexion_eleve(saisie):
    """
    Cette méthode prend en paramètre un mail ou le nb salle et renvoie une liste d'élève avec la durée de connexion
    chaque fois que le prof a ouvert la salle
    :param saisie:
    :return: liste [nom élève, durée de connexion]
    """
    line = fichier.readline()
    liste = ["is joining room " + saisie, saisie + "is joining room"]
    if liste[0] in line:
        salle = line[-15:]
        print(f'L\élève {line["?"]} à rejoint la salle {salle} le {line[0:11]} à  {line[11:19]} \n')
    elif liste[1] in line:
        eleve = line["?"]


def volume_horaire_prof():
    """
    :param :
    :return:
    """


def volume_horaire_eleve():
    """

    :return:
    """


def horaires_journaliers_prof():
    """
    Cette méthode permet de retourner les horaires journaliers où il y a des pics d'activités donc le nb de connexion
    par jour
    :return:
    """


# Menu principal
choix = ""
while choix != "Q" and choix != "q":
    print("1.. : Si vous souhaitez pouvoir rentrer l'email d'un prof ou le numero de sa salle et obtenir le détail de "
          "ses connexions (tentative de connexion, jour et heure avec durée de la connexion (entre l'entrée et la "
          "sortie) en minutes ) jour par jour ")

    print("2.. : Si vous souhaitez pouvoir rentrer l'email d'un prof ou le numero de sa salle et savoir quel "
          "eleve s'est connecté et la durée de la connexion de l'eleve pour chaque fois que le prof a ouvert sa salle")

    print("3.. : Si vous souhaitez pouvoir rentrer l'email d'un prof ou le numero de sa salle et pouvoir visualiser "
          "le volume horaire travaillé par jour (un histogramme avec la date et la durée journaliere")

    print("4.. : Si vous souhaitez pouvoir rentrer l'identifiant d'un eleve (son nom/email etc....) pouvoir "
          "visualiser le volume horaire travaillé par jour (un histogramme avec la date et la durée journaliere")

    print("5.. : Si vous souhaitez tout prof confondu évalué les horaires journaliers où il y a des pics d'activités "
          "donc visualiser le nombre de connexion simultanées par heure par jour")

    print("Quitter...................................Q")
    choix = input("Votre choix                      : ")

    # Menu Principal
    if choix == "1":
        saisie = input("Saisir l'émail d'un prof ou le numéro de salle :  ")
        detail_connexion_prof(saisie)
    elif choix == "2":
        saisie = input("Saisir l'émail d'un prof ou le numéro de salle :  ")
        detail_connexion_eleve(saisie)
    elif choix == "3":
        saisie = input("Saisir l'émail d'un prof ou le numéro de salle :  ")
        volume_horaire_prof(saisie)
    elif choix == "4":
        saisie = input("Saisir l'émail d'un prof ou le numéro de salle :  ")
        volume_horaire_eleve(saisie)
    elif choix == "5":
        saisie = input("Saisir l'émail d'un prof  :  ")
        horaires_journaliers_prof(saisie)
