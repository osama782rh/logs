import matplotlib.pyplot as plt

f = open("dataBB.log.txt", "r")
print(type(f))
count = 0

entree = input("Entrer un mail\n")

tente_connexion = entree + " is attempting to login"
if '@' in entree:
    quitte_salle = entree + " has left"
    ouvre_salle = entree + " is starting room"
    liste = [quitte_salle, ouvre_salle, tente_connexion]
elif '-' in entree:
    quitte_salle = "has left " + entree
    ouvre_salle = "is starting room " + entree

    liste = [quitte_salle, ouvre_salle, tente_connexion]

nbtentation = 0
nbouverture = 0

if '@' in entree:
    while True:
        count += 1
        line = f.readline()

        if not line:
            print(f"{entree} pas présent dans la liste")
            break
        if liste[0] in line:
            salle = line[-15:]
            print(entree + " à quitter la salle :" + salle + " le :" + line[0:11] + " à " + line[11:19] + "\n")
        if liste[1] in line:
            salle = line[-15:]
            print(entree + " à ouvert la salle :" + salle + " le :" + line[0:11] + " à " + line[11:19] + "\n")
            print(f'Durée de connexion : ')
            nbouverture += 1
        if liste[2] in line:
            salle = line[-15:]
            print(entree + " à tenter de se connecter à la salle  :" + salle + " le :" + line[0:11] +
                  " à " + line[11:19] + "\n")
            nbtentation += 1

elif '-' in entree:
    line = f.readline()
    while True:
        if not line:
            print(f"{entree} cette salle n'est pas présent dans la liste")
            break
        elif liste[0] in line:
            duree = 0
            prof = line[-58:]
            print(f'{prof} à accéder à la salle {entree} le {line[0:11]} à {line[11:19]} durant {duree}')
        elif liste[1] in line:
            prof = line[-50]
            print(f'{prof} à quitter la salle {entree} le {line[0:11]} à {line[11:19]}')
        elif liste[2] in line:
            prof = line[-58]
            print(f'{prof} à tenter de se connecter à  la salle {entree} le {line[0:11]} à {line[11:19]}')

f.close()

''' 
annina.liddell@gmail.com 
macamuscio@gmail.com
'''