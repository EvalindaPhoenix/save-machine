# Notes Installtion Mkdcos

## Premiers essai

Sur un container de build

```
docker run -it -v $HOME:/root/mkdocs-test python:2.7
pip install mkdocs-material
cd /root/mkdocs-test
mkdocs build
```

Sur un conteneur de service HTTP :

```
docker run -dit -v $PWD/site:/usr/local/apache2/htdocs -p 8080:80 httpd
```

## Suite

```
git clone lerepo
cd lerepo
docker run --rm -it -v ${PWD}:/docs squidfunk/mkdocs-material build
docker run -dit -p 8080:80 -v "$PWD/site":/usr/local/apache2/htdocs/ httpd
```
