#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute() -> float:
    mon_nombre = float(input('Veuillez entrer un nombre: ')
    if mon_nombrer < 0 
      mon_nombre=-mon_nombre
    return mon_nombre


def use_prefixes() -> List[str]:
    prefixes, suffixes = 'JKLMNOP', 'ack'
    resultat = []
    for prefixe in prefixes:
        nom = prefixe + suffixe
        resultat.append(nom)
    return resultat


def prime_integer_summation() -> int:
    nombrePremier = 0
    nombre = 2
    sommes = 0
    while(nombrePremier < 100):
        for i in range(1, nombre+1):
            if (nombre % i == 0 and i != 1 and i != nombre):
            break
        elif(i == nombre):
            nombrePremier += 1
            sommes += nombre
    nombre += 1
    return sommes
    
           


def factorial(number: int) -> int:
    result = 1
    if number == 0:                   
        return result
    else:
       for i in range(number):
            result *= (number -i)
       return result                


def use_continue() -> None:
    for chiffre in rang(1, 11):
        if chiffre == 5
            continue
        print ( chiffre)
        else:
                       


def main() -> None:
    print(f"La valeur absolue du nombre est {convert_to_absolute()}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des nombres de 0 à 100 est: {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()


if __name__ == '__main__':
    main()
