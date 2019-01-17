#!/usr/local/bin/python3
#--*-- coding:utf8 --*--

cle=input("Veuillez entrer la cle\n")
file=open('messageclair.txt','r')
texteclair=file.read()
file.close()
textechiffre=' '
for i in range(0,len(texteclair)):
    if 97<=ord(texteclair[i])<=122:
        caractere=texteclair[i]
        code=ord(caractere)-97
        decalage=ord(cle[i%len(cle)])-97
        codechiffre=(code+decalage)%26
        caracterechiffre=chr(codechiffre+97)
        textechiffre=textechiffre+caracterechiffre
    else:
        textechiffre=textechiffre+' '
file=open('messagechiffre.txt','w')
texteclair=file.write(textechiffre)
file.close()
