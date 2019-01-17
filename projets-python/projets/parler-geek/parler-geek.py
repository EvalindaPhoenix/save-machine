#!/usr/local/bin/python3
#--*-- coding:utf8 --*--
"""
Programme qui traduit une phrase ou un mot en langage geek.
Traducteur : https://github.com/floft/leetspeak
Leet speak : https://fr.wikipedia.org/wiki/Leet_speak
"""
dico={"A":"4","B":"8","C":"(","D":"d","E":"3","F":"f","G":"6","H":"#","I":"1","J":"j","K":"k","L":"1","M":"m","N":"n","O":"0","P":"p","Q":"q","R":"2","S":"5","T":"7","U":"u","V":"v","W":"w","X":"x","Y":"y","Z":"z"}
message_clair=input("entrez votre phrase\n")
msg=message_clair.upper()
i=0
while i<len(msg):
    for cle,valeur in dico.items():
        if cle==msg[i]:
            print(valeur,end="")
        elif msg[i]==" ":
            print(" ",end="")
            break
    i=i+1
print("\n")
