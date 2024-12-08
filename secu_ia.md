# **Exercice : Optimisation de la sécurité serveur avec l’IA**

## **Contexte**
La sécurité des serveurs est une priorité pour tout administrateur système. Dans cet exercice, vous allez analyser les fichiers logs d’un serveur Linux pour détecter des anomalies de sécurité, telles que des tentatives de brute-force ou des connexions suspectes.

Vous utiliserez ensuite un outil d’IA pour automatiser cette détection, proposer des recommandations de sécurité, et générer un rapport structuré.

---

## **Objectifs pédagogiques**
1. **Comprendre et analyser les logs système** pour identifier des comportements suspects.
2. **Utiliser un modèle d’IA** pour automatiser la détection d’anomalies et proposer des solutions.
3. **Automatiser la génération d’un rapport de sécurité.**
4. **Renforcer vos connaissances sur la sécurité des serveurs.**

---

## **Scénario**
En tant qu’administrateur système, vous devez :
1. Explorer les fichiers de logs (`/var/log/auth.log`, par exemple).
2. Identifier les tentatives d’accès suspectes ou non autorisées.
3. Automatiser la détection des anomalies à l’aide d’un script Python et d’un modèle d’IA.
4. Générer un rapport de sécurité qui inclut :
   - Les anomalies détectées.
   - Les recommandations d’amélioration.

---

## **Fichiers fournis**
Un exemple de fichier de logs système anonymisé (`auth.log.sample`) contenant des échecs de connexion, des connexions réussies, et des comportements potentiellement suspects.

---

## **Parties de l'exercice**

### **1. Analyse manuelle des logs**
- Parcourez le fichier `auth.log.sample`.
- Identifiez les lignes pertinentes (par exemple, celles contenant "Failed password" ou des adresses IP inhabituelles).
- **Livrable attendu** : Une liste des IP suspectes et des observations sur les comportements identifiés.

---

### **2. Automatisation avec Python**
- Complétez le script de base fourni pour :
  1. Lire un fichier de logs.
  2. Extraire les informations suivantes :
     - Adresses IP associées aux tentatives échouées.
     - Nombre de tentatives par adresse IP.
     - Heure des tentatives.

- Fournissez un résumé statistique :
  - Nombre total d’échecs.
  - Les 5 IP les plus actives.
  - Les heures avec le plus d’activité suspecte.

**Script de base fourni** :
```python
import re

def parse_logs(log_file):
    with open(log_file, "r") as f:
        logs = f.readlines()
    failed_attempts = []
    for line in logs:
        if "Failed password" in line:
            failed_attempts.append(line)
    return failed_attempts

log_file_path = "auth.log.sample"
failed_logs = parse_logs(log_file_path)
print(f"Number of failed attempts: {len(failed_logs)}")
```


### **3. Intégration de l’IA**

- Modifiez votre script pour inclure un appel à une API d’IA capable d’analyser les logs.

- Fournissez à l’IA un résumé ou des extraits significatifs des logs.
- L’IA devra :
  1. Identifier les anomalies (adresses IP suspectes, heures critiques).
  2. Proposer des recommandations pour améliorer la sécurité du serveur.

**Exemple d’appel API simulé** :
```python
import openai

openai.api_key = "VOTRE_CLE_API"

def analyze_with_ai(logs):
    prompt = "Voici des logs système. Identifie les comportements suspects et propose des solutions de sécurité :\n\n" + logs
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500
    )
    return response.choices[0].text

sample_logs = "Failed password for invalid user admin from 192.168.1.1 port 22"
ai_analysis = analyze_with_ai(sample_logs)
print(ai_analysis)

```

---

### **4. Génération d’un rapport de sécurité**

- Ajoutez une fonction pour générer un rapport structuré au format `.txt` ou `.md`.
- Ce rapport devra contenir :
  1. **Résumé des logs analysés** :
     - Total des tentatives échouées.
     - Liste des IP suspectes.
     - Les heures critiques avec une activité inhabituelle.
  2. **Anomalies détectées par l’IA** :
     - Adresses IP ou comportements signalés comme suspects.
  3. **Recommandations proposées par l’IA** :
     - Actions à entreprendre pour renforcer la sécurité du serveur.

**Exemple de génération d’un rapport :**
```python
def generate_report(log_summary, ai_findings, output_file="security_report.md"):
    with open(output_file, "w") as report:
        report.write("# Rapport de sécurité\n\n")
        report.write("## Résumé des logs analysés\n")
        report.write(f"- Tentatives échouées : {log_summary['failed_attempts']}\n")
        report.write(f"- IP suspectes : {', '.join(log_summary['suspicious_ips'])}\n")
        report.write(f"- Heures critiques : {', '.join(log_summary['critical_hours'])}\n\n")
        
        report.write("## Anomalies détectées par l’IA\n")
        report.write(f"{ai_findings}\n\n")
        
        report.write("## Recommandations de sécurité\n")
        report.write("Renforcez la configuration SSH, utilisez un pare-feu, etc.\n")
```

---

## **Livrables attendus**
1. **Script Python fonctionnel**, capable de :
   - Lire les fichiers logs.
   - Identifier et résumer les anomalies.
   - Intégrer une API d’IA pour enrichir l’analyse.
   - Générer un rapport structuré.
2. **Rapport final** au format `.txt` ou `.md`, contenant :
   - Les anomalies détectées.
   - Les recommandations de sécurité.
   - Un retour sur les limites du script et les améliorations possibles.

---

## **Ressources**
- [Documentation OpenAI](https://platform.openai.com/docs/)
- [Guide sur la gestion des logs Linux](https://linuxconfig.org/how-to-view-and-analyze-system-log-files-on-linux)
- [Python re module (regex)](https://docs.python.org/3/library/re.html)
- [PEP 8 - Style Guide for Python Code](https://peps.python.org/pep-0008/)

---

## **Temps estimé**
- Analyse manuelle des logs : **20 min**
- Automatisation avec Python : **40 min**
- Intégration de l’IA : **30 min**
- Génération du rapport et finalisation : **30 min**