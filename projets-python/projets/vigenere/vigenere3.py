#!/usr/local/bin/python3
#--*-- coding:utf8 --*--
"""Ce script va nous permettre de chiffrer grace a l'algorithme de vigenere une
phrase qui se trouvera dans un fichier texte
Le resultat du chiffrement se trouvera dans un autre fichier texte"""

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

source='messageclair.txt'
destination='messagechiffre.txt'
cle='abcd'

message=ouvrir_source(source)
messagex=vigenere(cle,message)
ecrire_destination(destination,messagex)
