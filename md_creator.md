
## Titre de l’exercice : Génération automatisée de README.md
### Contexte : 
Vous êtes chargé de développer un script Python qui analyse une application existante pour générer automatiquement un fichier README.md. Ce README doit suivre une structure définie par un fichier de recommandations.

---

## Partie 1 : Débuter avec l’analyse de fichiers

### Objectif : Lire un fichier Python et extraire les docstrings.

#### Tâches :

1. Implémentez une fonction extract_docstrings(file_path) qui ouvre un fichier Python, identifie les docstrings (texte entre """), et les retourne sous forme de liste.
2. Testez votre fonction sur un fichier Python fourni (ou généré par les participants).

#### Fichier de départ :
Un fichier Python simple avec plusieurs fonctions contenant des docstrings. Exemple :

```python
Copier le code
"""Module principal."""

def addition(a, b):
    """Cette fonction additionne deux nombres."""
    return a + b

class Exemple:
    """Classe exemple avec une méthode."""
    def methode(self):
        """Méthode de démonstration."""
        pass
```

## Partie 2 : Parcourir l’arborescence du projet

### Objectif : Analyser une structure de projet et collecter les informations des fichiers Python.

#### Tâches :

1. Écrivez une fonction analyze_project(project_path) qui parcourt les fichiers d’un répertoire donné et applique extract_docstrings à chaque fichier Python.
2. Retournez un dictionnaire contenant les noms des fichiers et leurs docstrings.

---

## Partie 3 : Générer le fichier README.md

### Objectif : Structurer les données collectées en contenu Markdown.

#### Tâches :

1. Lisez un fichier recommendations.txt contenant les sections à inclure dans le README (exemple fourni ci-dessous).
2. Complétez une fonction generate_readme(project_data, recommendations_path) qui crée un fichier README.md en se basant sur les données collectées et le fichier de recommandations.

#### Exemple de fichier recommendations.txt :

```shell
Copier le code
# Introduction
Décrivez brièvement le projet.

# Installation
Listez les étapes nécessaires pour installer le projet.

# Utilisation
Donnez un exemple d'utilisation ou une commande de test.

# Structure du projet
Insérez ici la structure analysée.
```

## Partie 4 : Personnalisation avancée (Challenge)

### Objectif : Ajouter des fonctionnalités avancées au script.

#### Tâches :

1. Détectez si un fichier requirements.txt est présent dans le projet et incluez les dépendances dans le README.
2. Analysez les imports dans les fichiers Python pour générer une section "Dépendances principales".
3. Formatez le README pour inclure des liens vers les fichiers analysés.