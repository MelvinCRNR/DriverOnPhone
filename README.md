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

![Untitled](https://user-images.githubusercontent.com/43339150/211201802-0d03620f-e398-43b5-b1f9-df5ce7401f35.png)

# Lancement de l’application via le NoteBook

Récupérer le dossier git. Ouvrer le grâce à un NoteBook et lancer les cellules du fichier driveronphone.ipynb. Une fois cela fait, pour changer de photo à tester, charger la photo voulu dans le dossier et préciser son nom dans la dernière cellule.

![Untitled 1](https://user-images.githubusercontent.com/43339150/211201835-33194b50-8e1b-44c0-9fa7-0a69eb94fbc1.png)

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

![Untitled 2](https://user-images.githubusercontent.com/43339150/211201862-8c45a5dc-b767-4833-a818-e7357694119f.png)

### Résultat

![Untitled 3](https://user-images.githubusercontent.com/43339150/211201890-5faa3e9b-fbe0-49f3-8aef-6f189561852c.png)

---

## Automobiliste utilisant son téléphone

## Photo

![Untitled 4](https://user-images.githubusercontent.com/43339150/211201900-42658d1a-9596-4797-b3e2-398f27e63150.png)

## Résultat

![Untitled 5](https://user-images.githubusercontent.com/43339150/211201916-4fba6fe2-aab1-439d-a7ed-b2d10e23ab3e.png)
