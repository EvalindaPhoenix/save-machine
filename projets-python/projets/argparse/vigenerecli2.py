#!/usr/local/bin/python3
#--*-- coding:utf8 --*--
"""Ce script va nous permettre de chiffrer grace a l'algorithme de vigenere une
phrase qui se trouvera dans un fichier texte
Le resultat du chiffrement se trouvera dans un autre fichier texte"""

import argparse
import sys
import random
import string

def vigenere(cle,clair):
    """Fonction de chriffrement"""
    crypt=''
    for i in range(0,len(clair)): # parcours de la phrase lettre par lettre
        if 97<=ord(clair[i])<=122: # si la lettre est comprise entre a et z ascii
            caractere=clair[i] # récupère le caractere dans la variable
            code=ord(caractere)-97 # le caractere est positionne dans l'alphabet
            decalage=ord(cle[i%len(cle)])-97 # calcul du decalage modulo longueur cle
            codechiffre=(code+decalage)%26 # code + decalage sans dépasser 25
            caracterechiffre=chr(codechiffre+97) # code ascii
            crypt=crypt+caracterechiffre # fabrication du texte chiffre
        else:
            crypt=crypt+' ' # un caractere qui n'existe pas est remplace par un espace
    return crypt

def ouvrir_source(source):
    """lecture du fichier source à chiffrer"""
    fichier=open(source,'r')
    message=fichier.read()
    fichier.close()
    return message

def ecrire_destination(dest,contenu):
    """ecriture du resultat chiffre"""
    fichier=open(dest,'w')
    fichier.write(contenu)
    fichier.close()

def check_arg(args=None):
    """Récolte les arguments de la ligne de commande"""
    parser = argparse.ArgumentParser(description='Script to cipher a text with vigenere')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-k', '--key',
                        help='vigenere key',
                        default='abcd')
    group.add_argument("-r", "--random",
                        action="store_true",
                        help="use a random key")
    parser.add_argument('-s', '--source',
                        help='clear source file',
                        default='./messageclair.txt')
    parser.add_argument('-d', '--destination',
                        help='ciphered destination file',
                        default='./messagechiffre.txt')

    results = parser.parse_args()
    return (results.key, results.random,results.source, results.destination)

def random_key(number):
    keyr=''
    for i in range(number):
        keyc=random.choice(string.ascii_lowercase)
        keyr=keyr+keyc
    return keyr

if __name__ == '__main__':
    """Programme principal"""
    args = check_arg()
    cle=args[0]
    source=args[2]
    destination=args[3]
    if args[1]:
        cle=random_key(4)
        print("la clé est :", cle)
    message=ouvrir_source(source)
    messagex=vigenere(cle,message)
    ecrire_destination(destination,messagex)
