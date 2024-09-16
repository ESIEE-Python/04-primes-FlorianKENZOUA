"""
Module isprime()
"""

from math import sqrt

#### Fonction secondaire


def isprime(p):

    """
    Retourne si p est premier ou non.

    Args :
        p : valeur entière positive
    
    Returns :
        isprime(p) : False or True
    """

    if p == 1 :
        return False

    if p == 4 :
        return False

    rac = int(sqrt(p)) # On optimise le nombre de diviseurs potentiels
    for i in range(2, rac) :
        div = p / i
        ent = int(div)
        if div - ent == 0 : # On regarde si le diviseur est entier ou non
            return False

    return True


#### Fonction principale


def main():

    """
    permet l'appel de isprime()
    """

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

if __name__ == "__main__":
    main()
