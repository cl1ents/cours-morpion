# DEBUT

# On admet une fonction `clear` qui efface tout le texte affiché
# On admet une fonction `lower` qui met une chaine de caractere en minuscule

# On admet une fonction `input` avec un argument `Text`:
    # Afficher la valeur de `Text`
    # Attendre que l'utilisateur entre une chaine de caractère, puis la renvoyer

# Definir `playerSymbols` comme une liste avec les caracteres '.', 'X' et 'O'
# Definir `abc` comme une liste avec les caracteres 'a', 'b' et 'c'
# Definir `ott` comme une liste avec les caracteres '1', '2' et '3'
    
# Definir une fonction `createGrid`:
    # Renvoyer une liste de trois listes, qui elles sont remplies par trois 0.

# Definir une fonction `printGrid` qui prend pour argument une liste `grid`:
    # Definir une chaine de caractere vide `output`
    # Mettre `output` en tant que concatenation de `output` et "    A B C\n    _ _ _\n"
    # Pour `i` prenant toutes les valeurs entre 0 et la longueur de grid - 1:
        # Mettre `output` en tant que concatenation de `output`, de l'élement `i` de `ott` et de " | "
        # Pour `element` prenant toutes les valeurs dans l'élement `i` de `grid`:
            # Mettre `output` en tant que concatenation de `output` et l'élement `element` de `playerSymbols` et " "
        # Mettre `output` en tant que concatenation de `output` et "\n"
    
    # Afficher `output`

# Definir une fonction `testCoordinate` qui prend pour argument une liste `grid`, et deux nombres `x` et `y`:
    # Renvoyer True si `x` et `y` sont entre 0 et 3, sinon renvoyer False

# Definir une fonction `getValue` qui prend pour argument une liste `grid`, et deux nombres `x` et `y`:
    # Si `testCoordinate` avec les arguments `grid`, `x` et `y` renvoye True,
        # Alors renvoyer l'élement d'index `x` de l'élement `y` de `grid`
    # Sinon,
        # Renvoyer 0

# Definir une fonction `setValue` qui prend pour argument une liste `grid`, et trois nombres `x`, `y` et `value`:
    # Si `testCoordinate` avec les arguments `grid`, `x` et `y` renvoye True,
        # Alors mettre l'élement d'index `x` de l'élement `y` de `grid` en tant que `value`
        # Et renvoyer True
    # Sinon,
        # Renvoyer False

# Definir une fonction `toCoordinates` qui prend pour argument une chaine de caractere `coord`:
    # Mettre `coord` en miniscule
    # Si la longueur de `coord` est égale a 2, alors:
        # Si le premier caractere de `coord` est dans `abc` et si le deuxieme caractere de `coord` est dans `ott`:
            # Alors renvoyer une liste qui contient l'index du premier caractere de `coord` dans abc, et l'index du deuxieme caractere de `coord` dans ott
        # Sinon si le deuxieme caractere de `coord` est dans `abc` et si le premier caractere de `coord` est dans `ott`:
            # Alors renvoyer une liste qui contient l'index du deuxieme caractere de `coord` dans abc, et l'index du premier caractere de `coord` dans ott
    # Renvoyer une liste qui contient -1 et -1

# Definir une fonction `customInput` qui prend pour argument une chaine de caractere `txt`:
    # Tant que True:
        # Definir `enteredInput` en tant que la valeur renvoyée par `input` avec l'argument `txt`
        # Si `enteredInput` en minuscule est égal a "exit", alors:
            # Si la valeur renvoyée par `input` avec l'argument "Are you sure? (yes/no) > " en minuscule est égale a "yes":
                # Appeler la fonction `exit`
        # Sinon,
            # Renvoyer `enteredInput`

# Definir une fonction `isWinner` qui prend pour argument une liste `grid` et un nombre entier `player`:
    # Pour `i` prenant toutes les valeurs entre 0 et 2:
        # Definir une variable `col` qui a pour valeur 0
        # Definir une variable `row` qui a pour valeur 0
        # Definir une variable `diag` qui a pour valeur 0
        # Definir une variable `reverseDiag` qui a pour valeur 0
        # Pour `y` prenant toutes les valeurs entre 0 et 2:
            # Si la valeur renvoyée par `grid` avec les arguments `grid`, `y` et `i` est égal a `player`,
                # Alors incrementer `col` par 1
            # Si la valeur renvoyée par `grid` avec les arguments `grid`, `i` et `y` est égal a `player`,
                # Alors incrementer `row` par 1
            # Si la valeur renvoyée par `grid` avec les arguments `grid`, `y` et `y` est égal a `player`,
                # Alors incrementer `diag` par 1
            # Si la valeur renvoyée par `grid` avec les arguments `grid`, `y` et 2-`y` est égal a `player`,
                # Alors incrementer `reverseDiag` par 1
            
            # Si `row` == 3 ou `row` == 3 ou `diag` == 3 ou `reverseDiag` == 3,
                # Alors renvoyer True
    # Renvoyer False

# Definir une fonction `isDraw` qui prend en argument une liste `grid`:
    # Initaliser la variable `filled` a 0
    # Pour `row` prenant toutes les valeurs dans `grid`:
        # Pour `element` prenant toutes les valeurs dans `row`:
            # Si `element` est different de 0, incrementer `filled` de 1
    # Renvoyer la valeur de l'assertion (`filled` === 9)

# Definir une fonction `round` qui prend en argument une liste `grid` et un entier `player`
    # Initaliser la liste `coordinates` qui contient -1 et -1
    # Tant que coordinates est une liste qui contient -1 et -1
        # Alors appeler la fonction `clear`
        # Appeler la fonction `printGrid` avec comme argument `grid`
        # Afficher la concatenation de "\nITS PLAYER ", `player` en tant que chaine de caractere, "'s TURN! (", l'élement d'index `player` de playerSymbols et ")"
        # Definir une variable `playerInput` en tant que la chaine de caractere renvoyée par `customInput` prenant pour argument "Enter coordinates (e.g: A2) > "
        # Definir une variable `coordinates` en tant que la liste renvoyée par `toCoordinates` prenant pour argument `customInput`

        # Si la valeur renvoyée par `getValue` avec comme arguments `grid` et l'élement 0 puis 1 de `coordinates` est differente de 0,
            # Alors mettre `coordinates` en tant que liste qui contient -1 et -1
        
    # Appeler la fonction `setValue` avec comme arguments `grid`, l'élement 0 puis 1 de `coordinates` et `player`


# Appeler la fonction `clear`
# Afficher le message:
"""----
Welcome to MORPION!!
----
Le but du jeu est simple:
Il suffit d'aligner, avant son adversaire, 3 symboles identiques horizontalement, verticalement ou en diagonale sur une grille de 3x3.
Le joueur ayant aligné 3 symboles gagne la partie.
Le joueur 1 a le symbole X et le joueur 2 a le symbole O
Pour jouer, le joueur indique les coordonnées de la case dans laquelle il veut jouer, par exemple "C2"

"""
# Appeler la fonction `input` avec comme argument "(Appuyez sur entrer pour continuer.)"

# Initialiser la variable `grid` en tant que la liste renvoyée par `createGrid`
# Initialiser la variable `turn` a 2
# Initialiser la variable `playing` a True

# Tant que `playing == True`
    # Redefinir turn en tant que (`turn` modulo 2) + 1
    # Appeler la fonction `round` avec comme argument `grid` et `turn`
    
    # Si la valeur renvoyée par `isWinner` avec comme argument `grid` et `turn` est égale a True,
        # Alors appeler la fonction `clear`
        # Appeler la fonction `printGrid` avec comme argument `grid`
        # Afficher la concatenation de "\nPLAYER ", `turn` en tant que chaine de caractere et " WINS!\n"
        # Appeler la fonction `input` avec comme argument "(Appuyez sur entrer pour continuer.)"
        # Mettre `playing` a False
    # Sinon si la valeur renvoyée par `isDraw` avec comme argument `grid` est égale a True,
        # Alors appeler la fonction `clear`
        # Appeler la fonction `printGrid` avec comme argument `grid`
        # Afficher "\nDRAW!\n"
        # Appeler la fonction `input` avec comme argument "(Appuyez sur entrer pour continuer.)"
        # Mettre `playing` a False

    
# FIN