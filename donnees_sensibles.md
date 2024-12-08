# **Exercice : Sécuriser l'analyse de code avec un modèle IA (simulation locale)**

## **Contexte**
Dans cet exercice, vous devez analyser des fichiers de code tout en garantissant qu’aucune donnée sensible (comme des clés API, mots de passe ou logins) n’est exposée. Pour cela, nous allons simuler l’utilisation d’un modèle IA local en appelant une API externe. Avant chaque envoi, vous devrez anonymiser le code pour respecter les règles de confidentialité.

---

## **Objectifs pédagogiques**
1. Appliquer un processus d’anonymisation pour protéger les données sensibles dans le code.
2. Utiliser une IA pour analyser des conventions de codage ou détecter des incohérences.
3. Simuler un modèle local en utilisant une API tout en soulignant les défis liés à la sécurité.

---

## **Scénario**
Vous travaillez sur un projet où vous devez analyser des fichiers de code pour vérifier :
1. La cohérence des conventions utilisées (noms, indentation, documentation, etc.).
2. La présence éventuelle de données sensibles dans le code.

L’objectif est de :
1. Parcourir les fichiers d’un répertoire donné.
2. Anonymiser le code avant toute transmission à l’IA.
3. Transmettre le code anonymisé à une API simulant un modèle local.
4. Générer un rapport des observations et recommandations.

---

## **Étapes de l'exercice**

### **1. Lecture des fichiers**
- Parcourez tous les fichiers d’un répertoire donné en ciblant les extensions `.py`, `.js`, `.php` ou autres en fonction de vos usages.
- Chargez le contenu de chaque fichier pour analyse.

**Code de base :**
```python
import os

def list_code_files(directory, extensions):
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            if any(filename.endswith(ext) for ext in extensions):
                files.append(os.path.join(root, filename))
    return files

directory = "./project"
extensions = [".py", ".js", ".java"]
code_files = list_code_files(directory, extensions)
print(f"Found {len(code_files)} files: {code_files}")

```
---

### **2. Anonymisation des données sensibles**
- Développez une fonction pour détecter et masquer les données sensibles comme :
  - Clés API (exemple : `api_key`).
  - Mots de passe (exemple : `password`).
  - Logins (exemple : `login`).

- Exemple d’approche avec des expressions régulières :
  - Recherche des clés API avec un motif tel que : `api[_-]?key`.
  - Recherche des mots de passe : `password\s*[:=]\s*["'][^"\']+["']`.
  - Recherche des logins : `login\s*[:=]\s*["'][^"\']+["']`.

- Implémentez une fonction pour remplacer ces valeurs par un indicateur `[MASKED]`.
- Testez cette fonction sur plusieurs fichiers de code pour vérifier qu’aucune donnée sensible n’est laissée intacte.

**Tâche :**
- Intégrez cette étape dans le pipeline d’analyse avant tout envoi à l’IA.
- Validez que le code anonymisé est toujours lisible et prêt à être analysé.

---
### 3. Envoi du code anonymisé à l'IA
Simulez un modèle local en appelant une API IA (comme OpenAI) avec le code anonymisé.

L’IA devra analyser les conventions utilisées et signaler d’éventuelles incohérences.

Exemple d’appel API :
```python
import openai

openai.api_key = "VOTRE_CLE_API"

def analyze_code_with_ai(anonymized_code):
    prompt = (
        "Voici un extrait de code anonymisé. Analyse ses conventions de style et identifie les incohérences :\n"
        f"{anonymized_code}\n"
    )
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500
    )
    return response.choices[0].text

# Exemple d'utilisation
anonymized_code = "api_key: [MASKED]\ndef my_function():\n    pass"
ai_analysis = analyze_code_with_ai(anonymized_code)
print(ai_analysis)
```

---

### 4. Génération d’un rapport
Compilez les résultats pour chaque fichier dans un rapport structuré, incluant :

- Les conventions identifiées.
- Les incohérences signalées.
- Les recommandations de l’IA pour harmoniser le code.

Exemple de rapport attendu :

# Rapport d'analyse de code

## Résumé global
- Style d'indentation : 4 espaces (majorité des fichiers).
- Conventions de nommage :
  - Variables : snake_case.
  - Fonctions : camelCase (fichiers JavaScript).
- Documentation :
  - Présente dans 60 % des fichiers, mais incomplète.

## Détails par fichier
### Fichier : main.py
- Indentation : 4 espaces.
- Style de nommage : snake_case.
- Documentation : Aucune.

### Fichier : utils.js
- Indentation : 2 espaces.
- Style de nommage : camelCase.
- Documentation : Présente, mais non standardisée.

## Recommandations
1. Uniformisez l'indentation à 4 espaces dans tout le projet.
2. Appliquez snake_case pour les variables et fonctions.
3. Ajoutez des commentaires/docstrings pour chaque fonction.

---

### Livrables attendus
1. Un script Python fonctionnel capable de :
    - Lire les fichiers dans un répertoire.
    - Anonymiser les données sensibles.
    - Transmettre le code anonymisé à une API pour analyse.
    - Générer un rapport détaillé.
2. Un rapport .md ou .txt contenant :
    - Les conventions détectées.
    - Les incohérences identifiées.
    - Les recommandations pour harmoniser le style de code.

---

### Temps estimé
- Lecture et anonymisation des fichiers : 20 min
- Analyse avec l’IA : 30 min
- Compilation du rapport : 30 min