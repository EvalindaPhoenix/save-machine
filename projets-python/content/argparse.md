# Projet argparse

<!-- toc -->

## Objectif

Fournir le support des options et des commandes en ligne de commande avec la librairie argparse.

## Exemple

```bash
./vigenerecli.py -h
usage: vigenerecli.py [-h] -k KEY [-s SOURCE] [-d DESTINATION]

Script to cipher a text with vigenere

optional arguments:
  -h, --help            show this help message and exit
  -k KEY, --key KEY     vigenere key
  -s SOURCE, --source SOURCE
                        clear source file
  -d DESTINATION, --destination DESTINATION
                        ciphered destination file
./vigenerecli.py -k abcd
Fichier 'messagechiffre.txt' créé et encodé.
```

## Documentation

* [Argparse Tutorial](https://docs.python.org/3/howto/argparse.html)
* [What is argparse?](https://www.bogotobogo.com/python/python_argparse.php)
* [argparse — Parser for command-line options, arguments and sub-commands](https://docs.python.org/3/library/argparse.html)

## En pratique

* Script avec fonction main
* Reprise du code original ou import ?
* Existence du fichier source
* Proposer une clé aléatoire

```bash
./vigenerecli2.py -h
usage: vigenerecli2.py [-h] [-k KEY | -r] [-s SOURCE] [-d DESTINATION]

Script to cipher a text with vigenere

optional arguments:
  -h, --help            show this help message and exit
  -k KEY, --key KEY     vigenere key
  -r, --random          use a random key
  -s SOURCE, --source SOURCE
                        clear source file
  -d DESTINATION, --destination DESTINATION
                        ciphered destination file
./vigenerecli2.py -r
la clé est : cxrc
Fichier 'messagechiffre.txt' créé et encodé.

```
