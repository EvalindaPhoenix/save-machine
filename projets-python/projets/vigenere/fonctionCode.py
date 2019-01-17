#!/usr/local/bin/python3
# -*- coding:Utf-8 -*

message=input("Entrez un message à coder: ")
clef=input("Entrez un mot de chiffrement: ")
fichier=input("Nom du fichier d'ecriture: ")

def chiffrement(message,clef):
   i=0
   j=0
   traduction=""
   while len(clef)<len(message):
       clef=clef+clef
   for i in range(0,len(message)):
       somme=ord(message[i])+ord(clef[j])-96
       if 97<=somme<=122:
           traduction=traduction+chr(somme)
           j=j+1
       elif somme>122:
           traduction=traduction+chr(somme-26)
           j=j+1
       else:
           traduction=traduction+message[i]
       i=i+1
   return traduction

txt=chiffrement(message,clef)

def ecritureDansFichier(fichier,txt):
   file = open(fichier,"w")
   file.write(txt+"\n")
   file.close()
   
ecritureDansFichier(fichier,txt)
print("la traduction est dans le fichier défini")
