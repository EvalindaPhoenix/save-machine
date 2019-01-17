#!/usr/local/bin/python3
#--*-- coding:utf8 --*--
"""Ce script va nous permettre de chiffrer grace a l'algorithme de vigenere une
phrase qui se trouvera dans un fichier texte
Le resultat du chiffrement se trouvera dans un autre fichier texte"""
# demande de la clef de chiffrement
clef=input('Entrez la cle de chiffrement\n')
# lecture du fichier messageclair.txt
fichier=open('messageclair.txt','r')
texteclair=fichier.read()
fichier.close()
# initialisation du texte chiffre textechiffre=' '
textechiffre=''
# chiffrement selon l'algorithme de vigenere
for i in range(0,len(texteclair)): # parcours de la phrase lettre par lettre
    if 97<=ord(texteclair[i])<=122: # si la lettre est comprise entre a et z ascii
        caractere=texteclair[i] # récupère le caractere dans la variable
        #print(caractere)
        code=ord(caractere)-97 # le caractere est positionne dans l'alphabet
        #print(code)
        decalage=ord(clef[i%len(clef)])-97 # calcul du decalage modulo longueur cle
        #print(decalage)
        codechiffre=(code+decalage)%26 # code + decalage sans dépasser 25
        #print(codechiffre)
        caracterechiffre=chr(codechiffre+97) # code ascii
        #print(caracterechiffre)
        textechiffre=textechiffre+caracterechiffre # fabrication du texte chiffre
        #print('\n')
    else:
        textechiffre=textechiffre+' ' # un caractere qui n'existe pas est remplace par un espace
# ecriture dans le fichier messagechiffre.txt
fichier=open('messagechiffre.txt','w')
fichier.write(textechiffre)
fichier.close()
