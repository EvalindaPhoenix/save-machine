#!/usr/local/bin/python3
#--*-- coding:utf8 --*--
dico={"A":"4","B":"8","C":"(","D":"[)","E":"3","F":"|=","G":"6","H":"#","I":"1","J":"_|","K":"|<","L":"£","M":"|v|","N":"|v","O":"0","P":"|*","Q":"()_","R":"2","S":"5","T":"7","U":"|_|","V":"\/","W":"\/\/","X":"><","Y":"'/","Z":"~/_"}
message=input("Entrez votre texte a traduire: \n").upper()
for key,value in dico.items():
    message=message.replace(key,value)
print(message)
print("\n")
