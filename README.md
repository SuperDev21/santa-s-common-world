# Santa's Common World Project

Ce projet est ma première application web ! J'ai créé une petite API qui renvoie des données à partir de fichier `data.py` avec le framework Flask.

## Objectifs du projet

* Comprendre le fonctionnement du routage
* Comprendre ce qu'est une API
* Familiarisez-vous avec le format de données JSON
  
## Lancer le projet

* Lancer le serveur dans le terminal avec la commande `python3 run.py`
* Ouvrir un autre terminal pour exécuter les requêtes

### Quelques commandes (requêtes) pour tester l'API

#### Toys

* La route /toys `curl http://127.0.0.1:5000/toys`

* La route /toys/<toy_id>  `curl http://127.0.0.1:5000/toys/2`

* La route /toys avec la méthode POST `curl -d "name=Minesweeper&description=Home computer classic&price=0&category_id=0" -X POST http://127.0.0.1:5000/toys`

* La route pour mettre à jour /toys/<toy_id> avec la méthode PUT `curl -d "name=Checkers" -X PUT http://127.0.0.1:5000/toys/4`

* La route pour supprimer /toys/<toy_id> avec la méthode DELETE `curl -X DELETE http://127.0.0.1:5000/toys/4`

#### Categories

* La route /categories `curl http://127.0.0.1:5000/categories`

* La route /categories/<category_id> `curl http://127.0.0.1:5000/categories/0`

* La route /categories avec la méthode POST  `curl -d "name=Water Games" -X POST http://127.0.0.1:5000/categories`

* La route pour mettre à jour /categories/<category_id> avec la méthode PUT  `curl -d "name=Old School Games" -X PUT  http://127.0.0.1:5000/categories/1`

* La route pour supprimer /categories/<category_id> avec la méthode DELETE `curl -X DELETE http://127.0.0.1:5000/categories/3`

* La route /categories/< name>/toys qui renvoie tous les jouets d'une catégorie donnée `curl http://127.0.0.1:5000/categories/Boardgames/toys`
