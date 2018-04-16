# fluotracker

The purpose of this repository is to extract and analyse tracks of nanoparticles from
fluorescent microscopy movies of neurons.

TODO: add background info (lab, links to publications, etc.)

# Setup

## 1 - Télécharger le code

```
$ git clone https://github.com/BenjaminHabert/fluotracker.git
$ cd fluotracker
```

Si le projet a déjà été téléchargé, penser à le **mettre à jour**

```
$ git pull
$ git checkout master
```


## 2 - mettre en place un environnement python

Nous recommandons d'utiliser un environnement virtuel local. La bonne pratique: un projet = un
environment virtuel. De cette manière tout le monde utilise la même version de python
et les mêmes libraires.

### 2.1 préambule: avoir la bonne version de python sur sa machine

On veut avoir python3 (version > 3.3) sans anaconda pour se simplifier la vie.

Ici c'est ok: on peut passer directement au point 2.2

```
$ which python3
/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
```

Ici ça ne va pas:

```
$ which python3
/Users/benjaminhabert/anaconda/bin/python3
```


#### 2.1.1 J'ai anaconda et je ne veux plus l'utiliser!

Quand on tappe `$ python3` dans un terminal l'OS va regarder dans plusieurs endroits pour vérifier
si l'exécutable existe. On peut modifier les chemins d'accès en regardant le fichier de configuration
`.bash_profile` (parfois `.profile`, `.bashrc`, etc) qui est situé dans votre `home`.


```
# Quels fichiers dans mon home ?
$ ls -lah ~/
....
-rw-r--r--@    1 benjaminhabert  staff   2,5K 16 avr 21:46 .bash_profile
...

# Il y a bien un fichier .bash_profile; je l'ouvre dans un éditeur de texte
$ open ~/.bash_profile
```

Dans le fichier `.bash_profile` on va trouver une ligne qui indique où trouver le `python` de
anaconda: on peut la commenter (possible d'inverser ce choix plus tard).

```
# file: ~/.bash_profile

# added by Anaconda3 4.0.0 installer
export PATH="/Users/benjaminhabert/anaconda/bin:$PATH"

# En général je rajoute cette ligne à la fin ou au début du fichier pour m'assurer qu'il est bien lu
echo "Reading config from ~/.bash_profile"

# Souvent je me rajoute aussi un truc pratique pour passer rapidement dans un dossier
# sur lequel je travail:
alias fluo="cd /Users/benjaminhabert/Documents/FluotrackerProject/fluotracker/"
```

Après avoir **sauvegardé et fermé** le fichier, pour que les modifications soient prisent en compte il faut
**démarrer un nouveau terminal**

```
# astuce:
$ fluo
$ pwd
/Users/benjaminhabert/Documents/FluotrackerProject/fluotracker

$ which python
/usr/local/bin/python3
$ python3 --version
Python 3.6.5
```

Dans mon cas j'ai bien un exécutable python disponible après avoir "désactivé" la version de
anaconda. Si ce n'est pas le cas il faut installer python 3 depuis
[python.org](https://www.python.org/downloads/). Une fois que l'installation est terminée
on peut vérifier le contenu du fichier `.bash_profile`:

```
$ open ~/.bash_profile

# fichier ~/.bash_profile
# L'installation a ajouté les lignes suivantes:

# Setting PATH for Python 3.6
# The original version is saved in .bash_profile.pysave
PATH="/Library/Frameworks/Python.framework/Versions/3.6/bin:${PATH}"
export PATH
```

Et si on vérifie la version de python dont on dispose:

```
$ which python3
/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
$ python3 --version
Python 3.6.5
```

Ok! on est prêt pour l'étape suivante: créer un environnement de python qui ne servira que
pour le projet fluotracker.

*Note pour les curieux*: comme on l'a vu c'est la variable `PATH` qui est utilisée pour
savoir quel exécutable sera lancé par une commande dans le terminal. Le `PATH` est composé de
répertoires séparés par `:`. Par exemple

```
$ echo $PATH
/Library/Frameworks/Python.framework/Versions/3.6/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
```

Il faut savoir que le `PATH` est parcouru en commençant par les premiers répertoires. Donc si
un exécutable `python` existe dans plusieurs des répertoires du `PATH` c'est le premier qui sera
utilisé.

### 2.2 Créer un environment virtuel local

Maintenant qu'on a la bonne version de Python:

```
# J'utilise l'alias "fluo" que j'ai définit dans ~/.bash_profile (voir plus haut)
$ fluo
$ pwd
/Users/benjaminhabert/Documents/FluotrackerProject/fluotracker

$ python3 -m venv venv-fluo
$ ls venv-fluo
```

Cette commande créé un dossier `venv-fluo` qui contient une installation complète de python.
C'est cette version qu'on va utiliser pour lancer les codes et c'est ici qu'on va installer
des librairies.

### 2.3 Activer son environnement

Dans un nouveau terminal, il faut dire explicitement qu'on veut utiliser le nouveal environment
qu'on vient de créer. Il faut répéter cette étape à chaque fois qu'on revient sur le projet.

```
$ . activate.sh

# Alternativement, on peut utiliser faire directement
$ source venv-fluo/bin/activate
# Mais le fichier activate.sh met aussi à jour la variable PYTHONPATH, ce qui sera utile
# plus tard

(venv-fluo) $ which python
/Users/benjaminhabert/Documents/FluotrackerProject/fluotracker/venv-fluo/bin/python
```

Quand on tappe `python` ça pointe donc maintenant vers notre environnement local. A noter:
le nom de l'environnement virtuel est ajouté au début de la ligne de commande.

Pour désactiver cet environment virtuel (pour travailler sur un autre projet par exemple):

```
(venv-fluo) $ deactivate
$ which python
/usr/bin/python
```

## 3 Installer les dépendances python

On utiliser `pip` pour installer des librairies. On s'assure de les installer dans notre python
local:

```
$ . activate.sh
$ which pip
/Users/benjaminhabert/Documents/FluotrackerProject/fluotracker/venv-fluo/bin/pip

# mise à jour de pip
(venv-fluo) $ pip install --upgrade pip

# installer une seule librairie
(venv-fluo) $ pip install numpy

# installer toutes les dépendances du projet
(venv-fluo) $ pip install -r requirements.txt
```

Le fichier `requirements.txt` est utilisé pour lister l'ensemble des dépendances du projet. Il
faudra le mettre à jour au fur et à mesure qu'on trouve de nouvelles librairies à utiliser.


On a maintenant un environnement virtuel local qu'on peut activer / désactiver au besoin. On est
prêt à utiliser cet environnement pour lancer notre code.

# Lancer le code

Le script principal du projet est le module python `fluotracker/extraction/run_extraction.py`.
Pour le lancer on s'assure d'utiliser l'environnement virtuel local:

```
$ fluo
$ . activate.sh
(venv-fluo)$ python fluotracker/extraction/run_extraction.py
```

Ce script principal a pour vocation de rester simple. Il faut appel à d'autres fonctions définies
ailleurs dans le projet.

Par ailleurs, lorsqu'on est en train de tester des fonctions, on peut utiliser les **notebooks**.
Pour les lancer:

```
(venv-fluo)$ jupyter notebook
```

Pour y accéder il faut utiliser son navigateur (chrome ?) et aller sur http://localhost:8000.



# Conventions

## Data Management

All data files are stored in the `data/` folder. These files **should not me comitted** to the
repository. The module `fluotracker.io.files` provides convenient functions to load and save
files from the folder.


## Editor setup

Use what you want as an editor. We suggest using [atom](https://atom.io/) with the following plugins:

- python-indent
- minimap

Make sure to configure your editor to use **4-spaces indentation** and not tabs for Python files!
(to test this: press "tab" in a python file and checks wether a tab or spaces were inserted).

Once your are more familiar with Python / atom, you can also use:

- linter-flake8
- linter-pydocstyle
- kite plugin (requires installation of [kite](http://help.kite.com/article/53-quickstart)).
This provides code completion! You can configure kite itself to whitelist the repository
(which allows code inspection not only for basic python packages but also modules degined here)


## Using git

TODO
