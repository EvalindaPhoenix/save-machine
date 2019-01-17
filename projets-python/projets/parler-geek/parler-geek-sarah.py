#!/usr/local/bin/python3
#--*-- coding:utf8 --*--
"""
Programme qui traduit une phrase ou un mot en langage geek.
Traducteur : https://github.com/floft/leetspeak
"""
Dico={"A":"4","B":"8","C":"(","D":"d","E":"3","F":"f","G":"6","H":"#","I":"1","J":"j","K":"k","L":"1","M":"m","N":"n","O":"0","P":"p","Q":"q","R":"2","S":"5","T":"7","U":"u","V":"v","W":"w","X":"x","Y":"y","Z":"z"}
phrase=input('Veuillez entrer une phrase\n')
phraseM=phrase.upper()
longueur=len(phraseM)
i = 0
while i < longueur:
   if phraseM[i]==" ":
       lettre=" "
   else:
       lettre = Dico[phraseM[i]]
   print(lettre,end="")
   i = i + 1
print('\n')
