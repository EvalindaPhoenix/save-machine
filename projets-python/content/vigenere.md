# Projet Vigenere

<!-- toc -->

## Objectif

Chiffrer grâce à l'algorithme de Vigenère un texte écrit dans un fichier "`messageclair.txt`" et écrire ce résultat dans un autre fichier texte "`messagechiffre.txt`".

## Principe

### ROT13

Décalage de chaque lettre de 13 vers la droite dans l'alphabet. Si les lettres de l'alphabet sont numérotées de 0 à 25, il s'agirait d'ajouter 13 à leur rang et de s'assurer qu'il reste compris entre 0 et 25 avec le modulo 26.

![Chiffré avec ROT13, le mot « HELLO » devient « URYYB » (et inversement).](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/ROT13.png/440px-ROT13.png	)

Peut-être plus simplement en python 2 :

```python
import string
rot13 = string.maketrans(
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
string.translate("Hello World!", rot13)
# 'Uryyb Jbeyq!'
```

Et en python 3 :

```python
rot13 = str.maketrans(
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
"Hello World!".translate(rot13)
#'Uryyb Jbeyq!'
```


```python
import string
```

[Source](https://stackoverflow.com/questions/3269686/short-rot13-function-python)

## Algortithme de Vigenère

Pour casser le code Rot13 il suffit de tester les 26 décalages possibles. [L'algortithme de Vigenère](https://fr.wikipedia.org/wiki/Cryptanalyse_du_chiffre_de_Vigen%C3%A8re) consiste à introduire une clé rendant le décalage variable selon la position du caractère dans le message.

Message clair | c   | i   | s   | c   | o   | s   | y   | s   | t   | e   | m   | s
---| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---
n# du message clair | 2   | 8   | 18  | 2   | 14  | 18  | 24  | 18  | 19  | 4   | 12  | 18
Clé répétée | **a**   | **b**   | **c**   | **d**   | a   | b   | c   | d   | a   | b   | c   | d
n# de clé (décalage) | 0   | 1   | 2   | 3   | 0   | 1   | 2   | 3   | 0   | 1   | 2   | 3
Résultat n# + n# | 2   | 9   | 20  | 5   | 14  | 19  | 0   | 21  | 19  | 5   | 14  | 21
Message chiffré | c   | j   | u   | f   | o   | t   | a   | v   | t   | f   | o   | v

```bash
echo "ciscosystems" > messageclair.txt

```

## Résultat attendu

```bash
if [ -f messagechiffre.txt ] ; then rm messagechiffre.txt ; fi ; ./vigenere.py && cat messagechiffre.txt ; echo " "
Entrez la cle de chiffrement
abcd
cjufotavtfov

```

## En pratique

* Opérations arithmétiques
* manipulation de fichier
* créer automatiquement une plage de nombres, de lettres
* commentaires et documentation
* Mise en fonction
* Fonction native [`ord()`](https://docs.python.org/fr/3/library/functions.html#ord) et [`chr()`](https://docs.python.org/fr/3/library/functions.html#chr)
* Boucle `for`
* Fonction `range()`

## Références

* Source de départ : [Apprendre Python 3 - Franck Ebel](http://python3.moneformation.fr/), pp.
* Voir aussi [1A.algo - Casser le code de Vigenère](http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/notebooks/expose_vigenere.html)
