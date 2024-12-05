#### Imports et définition des variables globales
"""
Module pour encoder une chaîne de caractères en tuples (caractère, nombre d'occurrences) 
en utilisant deux algorithmes : itératif (artcode_i) et récursif (artcode_r).

Fonctions :
- artcode_i(s): Encodage itératif.
- artcode_r(s): Encodage récursif.

Variables globales :
- sys.setrecursionlimit(1100): Augmente la limite de récursion.

Exemple :
    Pour la chaîne 'MMMMaaacXolloMM', les deux fonctions renvoient :
    [('M', 4), ('a', 3), ('c', 1), ('X', 1), ('o', 2), ('l', 1), ('o', 1), ('M', 2)].
"""
import sys

sys.setrecursionlimit(1100)


#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument selon un 
    algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """

    #votre code ici

    c = [s[0]]
    o = [1]
    for k in range(1,len(s)) :
        if s[k] == s[k-1]:
            o[-1]+= 1
        else :
            c.append(s[k])
            o.append(1)
    return list(zip(c,o))



def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument selon un 
    algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    # votre code ici
    # cas de base
    if not s :
        return []
    char = s[0]
    index = 1
    # recherche nombre de caractères identiques au premier
    while index < len(s) and s[index] == char:
        index+=1
    l=[(char,index)]
    # appel récursif
    return l + artcode_r(s[index:])

#### Fonction principale


def main():
    """Point d'entrée principal du programme.

    Cette fonction affiche le résultat de l'encodage d'une chaîne de caractères en utilisant 
    les deux algorithmes (itératif et récursif) définis ci-dessus.

    Exemple:
        artcode_i('MMMMaaacXolloMM') et artcode_r('MMMMaaacXolloMM')
        Affichent le même résultat encodé de manière itérative et récursive.
    """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
