[![CircleCI](https://dl.circleci.com/status-badge/img/gh/Wil31/Python-OC-Lettings/tree/master.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/Wil31/Python-OC-Lettings/tree/master)

[![CircleCI](https://dl.circleci.com/insights-snapshot/gh/Wil31/Python-OC-Lettings/master/pipelineci/badge.svg?window=7d)](https://app.circleci.com/insights/github/Wil31/Python-OC-Lettings/workflows/pipelineci/overview?branch=master&reporting-window=last-7-days&insights-snapshot=true)

## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(oc_lettings_site_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from oc_lettings_site_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Déploiement sur Heroku

### Configuration

#### DockerHub

1. Créez un compte sur [Docker](https://hub.docker.com/signup/)
2. Créez un nouveau repo sur DockerHub
3. Remplacez le nom de repo [L44 de config.yml](https://github.com/Wil31/Python-OC-Lettings/blob/7c4e0ea9f24f19647ffb43bc971003cff79c5a4f/.circleci/config.yml#L44) ($DOCKERHUB_USERNAME/[votre-repo]) par votre repository.

Repo DockerHub utilisé pour le projet:
[hub.docker.com/r/wil91/oc-lettings-site](https://hub.docker.com/r/wil91/oc-lettings-site)

#### Sentry

Une surveillance de l’application et suivi des erreurs est effectué avec Sentry. 

1. Créez un compte [Sentry](https://sentry.io/signup/)
2. Créez un projet Django dans Sentry
3. Récupérez votre clé DSN du projet

#### Heroku

1. Créez un compte [Heroku](https://www.heroku.com/home)
2. Créez un nouvelle application Heroku
3. Récupérez votre token Heroku (API Key) dans les paramètres de votre compte
4. Dans les paramètres Heroku, dans Config Vars, configurer les variables suivantes:

| Clé               | Valeur               |
| ----------------- | -------------------- |
| ENV               | production           |
| DJANGO_SECRET_KEY | Token générée Django |
| SENTRY_DSN        | Token générée Sentry |

#### CircleCI 

1. Créer un compte sur [circleci.com](https://circleci.com/)
2. Commencer la configuration du projet https://circleci.com/docs/config-intro
3. Configurez CircleCI avec les variables d'environnement suivantes:

| Clé                | Valeur                        |
| ------------------ | ----------------------------- |
| DOCKERHUB_USERNAME | Votre identifiant Docker Hub  |
| DOCKERHUB_PASSWORD | Votre mot de passe Docker Hub |
| HEROKU_TOKEN       | Votre API key sur Heroku      |
| HEROKU_APP_NAME    | Le nom de l'app Heroku        |

#### Automatisation CI/CD

CircleCI permet d'automatiser les tests, la conteneurisation et le déploiement sur Heroku, grâce
au fichier config.yml se trouvant dans le dossier .circleci du projet. L'execution du pipeline CI/CD est déclenchée automatiquement lors d'un push sur la branch `master` 
sur GitHub.  
L'application est déployée vers le site [https://oc-lettings-docker-wil.herokuapp.com/](https://oc-lettings-docker-wil.herokuapp.com/).

## Déployer en local une image Docker du projet

La commande suivante récupère et déploie en local une image du projet:  
`docker run -d -p 8000:8000 wil91/oc-lettings-site:$TAG`  
Remplacer `wil91/oc-lettings-site` par votre docker hub.  
Prendre le dernier tag sur DockerHub:  
https://hub.docker.com/r/wil91/oc-lettings-site/tags
