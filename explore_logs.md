# **Exercice : Création d'une application d'exploration et de visualisation des logs système**

## **Contexte**
Dans cet exercice, vous allez travailler sur une application Python qui explore les répertoires d'un serveur pour identifier les fichiers logs, afficher leurs métadonnées, et permettre leur visualisation dans une interface graphique.

Le script de base fourni est fonctionnel, mais il n'est ni structuré, ni optimisé. Votre mission consistera à transformer ce prototype en une application robuste et bien conçue, tout en appliquant les meilleures pratiques de développement.

---

## **Objectifs pédagogiques**
1. **Comprendre la gestion des fichiers logs sur un serveur.**
2. **Appliquer les principes de refactorisation pour structurer une application Python en plusieurs modules.**
3. **Utiliser des conventions de codage standard (ex. : PEP 8).**
4. **Collaborer avec une IA pour améliorer le code et enrichir ses fonctionnalités.**

---

## **Fichiers fournis**
- Un script Python de base nommé `log_viewer.py`.
- Ce script :
  - Explore les répertoires à la recherche de fichiers contenant "log" dans leur nom.
  - Affiche une liste des fichiers logs trouvés (avec leur taille et leur date de modification).
  - Permet de visualiser le contenu d'un fichier log sélectionné.

---

## **Parties de l'exercice**

### **1. Analyse du script existant**
- Examinez le fichier `log_viewer.py`.
- Identifiez :
  - Les fonctionnalités principales.
  - Les failles ou manques dans le code (structure, conventions, gestion des erreurs).

---

### **2. Refactorisation**
1. **Division en modules :**
   - Séparez le code en plusieurs fichiers pour une meilleure lisibilité et maintenabilité :
     - `main.py` : Contiendra le point d'entrée de l'application.
     - `ui.py` : Contiendra la gestion de l'interface utilisateur.
     - `file_explorer.py` : Gèrera la logique d'exploration des répertoires et de récupération des métadonnées.
   - Mettez en place une structure claire et logique.

2. **Amélioration de la lisibilité :**
   - Ajoutez des commentaires explicatifs dans chaque fonction.
   - Adoptez des noms de variables et de fonctions explicites.

3. **Application des conventions :**
   - Utilisez PEP 8 pour formater le code.
   - Corrigez les incohérences dans les indentations, espaces, et structures conditionnelles.

---

### **3. Ajout de nouvelles fonctionnalités**
1. **Lecture partielle des fichiers volumineux :**
   - Implémentez une méthode pour afficher uniquement les 100 premières lignes des fichiers trop grands.
   - Ajoutez un bouton permettant de charger la suite du fichier.

2. **Filtres de recherche :**
   - Ajoutez un champ permettant de filtrer les logs par nom ou date de modification.

3. **Gestion des erreurs :**
   - Affichez des messages d'erreur clairs si un fichier ne peut pas être lu ou si le répertoire est inaccessible.

---

### **4. Collaboration avec une IA**
1. **Optimisation :**
   - Utilisez un outil d'IA (ex. : OpenAI ou autre) pour analyser et améliorer le code.
   - Demandez des suggestions pour améliorer les performances ou ajouter des fonctionnalités avancées.

2. **Rédaction de documentation :**
   - Utilisez l'IA pour rédiger une documentation utilisateur ou développeur.

---

## **Livrables attendus**
À la fin de l'exercice, chaque participant devra fournir :
1. Une application Python refactorisée, composée de plusieurs modules.
2. Une documentation technique expliquant :
   - L'architecture de l'application.
   - Les principales fonctionnalités.
   - Les améliorations apportées.
3. Les suggestions d'améliorations ou de fonctionnalités proposées par l'IA.


---

## **Ressources supplémentaires**
- [Documentation Tkinter](https://docs.python.org/3/library/tkinter.html)
- [PEP 8 - Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [Python OS Module](https://docs.python.org/3/library/os.html)
- [Python Open File Function](https://docs.python.org/3/library/functions.html#open)

---

## **Temps estimé**
- Analyse et refactorisation : **30 minutes**
- Ajout de fonctionnalités : **30 minutes**
- Collaboration avec l'IA : **20 minutes**
- Documentation et finalisation : **20 minutes**

Bon courage ! 🚀
