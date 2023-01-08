# Driver On Phone

# Introduction

Ce projet à pour but de déterminer si un automobiliste est en train d’utiliser son téléphone en conduisant ou non. Il est développé à la demande du ministère de l’intérieur qui veut mettre en place des radars de contrôles d’automobiliste étant dans l’illégalité en utilisant leur téléphone au volant. 

# Technologies utilisées

Pour développer ce projet, nous allons les technologies suivantes :

- Python3
- FastAi
- FastBook
- JupyterLab pour utiliser des Notebook de développer le programme de reconnaissance
- Flask (Pour le développement d’un site minimaliste permettant de tester l’application)

J’ai préféré utiliser FastAi à Yolo, car, Yolo détecte les objets et, la plupart des automobilistes au téléphone cache une partie de leur téléphone avec leur main, ce qui peut empêcher le bon fonctionnement de cet algorithme. Par ailleurs, la position des automobilistes est similaires lorsqu’ils sont au téléphone, c’est pour cela que préfère partir sur FastAi.

# Développement

Afin d’entrainer notre algorithme, nous avons créer 2 dossiers possédants, pour le premier, d’automobilistes n’utilisant pas leur téléphone. Dans le second dossier, des automobilistes utilisant leur téléphone. Nous avons 50 photos dans chaque dossier. Ce nombre de photo est un peu léger pour bien entrainer l’algorithme mais s’avère suffisant. De plus, en termes de rapidité, 50 photos nous permet d’avoir un traitement et un entrainement rapide au moment de l’exécution. Un diagramme de répartition des données n’est pas pertinent dans notre cas car nous utilisons un nombre de données fixe.

![Untitled](Driver%20On%20Phone%20f6273493baad4cf39fc3fd423b2cf7d7/Untitled.png)

# Lancement de l’application via le NoteBook

Récupérer le dossier git. Ouvrer le grâce à un NoteBook et lancer les cellules du fichier driveronphone.ipynb. Une fois cela fait, pour changer de photo à tester, charger la photo voulu dans le dossier et préciser son nom dans la dernière cellule.

![Untitled](Driver%20On%20Phone%20f6273493baad4cf39fc3fd423b2cf7d7/Untitled%201.png)

# Lancement de l’application avec Flask en local

Télécharger le dossier, ouvrez un terminal, lancer l’environnement virtuel grâce à la commande suivante :

```python

source venv/bin/activate
```

Une fois l’environnement lancé, faites la commande suivante :

```python
flask run
```

Cliquez sur le lien donné et vous voilà dans l’application

# Lancement de l’application avec Docker

Tout d’abord, lancer la commande suivante pour créer l’image Docker :

```bash
sudo docker build --tag flask-driver-on-phone .
```

Lancer ensuite la commande qui suit pour lancer l’application :

```bash
sudo docker run --name flask-driver-on-phone -p 5001:5001 flask-driver-on-phone
```

Rendez-vous sur l’adresse suivante pour avoir accès à l’application :

```bash
0.0.0.0:5001
```

# Mise en production avec Azure

# Tests

## Automobiliste n’utilisant pas son téléphone

### Photo

![Untitled](Driver%20On%20Phone%20f6273493baad4cf39fc3fd423b2cf7d7/Untitled%202.png)

### Résultat

![Untitled](Driver%20On%20Phone%20f6273493baad4cf39fc3fd423b2cf7d7/Untitled%203.png)

---

## Automobiliste utilisant son téléphone

## Photo

![Untitled](Driver%20On%20Phone%20f6273493baad4cf39fc3fd423b2cf7d7/Untitled%204.png)

## Résultat

![Untitled](Driver%20On%20Phone%20f6273493baad4cf39fc3fd423b2cf7d7/Untitled%205.png)