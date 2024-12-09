# Installation et utilisation d'un LLM local
### Objectifs
1. Apprendre à installer les outils nécessaires pour travailler avec des LLM en local.
2. Découvrir comment charger un modèle Hugging Face.
3. Comprendre les bases de l’interaction avec un LLM.

---

## Étape 1 : Installer les outils requis
### Prérequis
1. Python 3.8 ou supérieur installé.
2. Une connexion Internet pour télécharger les modèles.

### Installation des bibliothèques
Exécutez les commandes suivantes dans votre terminal ou votre environnement VSCode :

```bash
pip install transformers torch
```

---

## Étape 2 : Chargement d’un modèle Hugging Face
### Exemple avec GPT-Neo 125M
Voici un script Python simple pour télécharger et utiliser un modèle :

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

# Télécharger le tokenizer et le modèle
model_name = "EleutherAI/gpt-neo-125M"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Exemple de question
input_text = "What is artificial intelligence?"
inputs = tokenizer(input_text, return_tensors="pt")

# Générer une réponse
outputs = model.generate(inputs["input_ids"], max_length=50, num_return_sequences=1)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

### Ce que fait le script :
1. Télécharge le modèle et le tokenizer depuis Hugging Face.
2. Transforme une question en entrée compatible avec le modèle.
3. Génère une réponse et l’affiche.

---

## Étape 3 : Exercices pratiques
### Exercice 1 : Modifier le texte d'entrée
Modifiez le texte d’entrée pour poser des questions différentes, par exemple :

```text
"What is the capital of France?"
"Explain machine learning in simple terms."
```

### Questions : 
1. Qu'observez-vous dans les réponses générées ?
2. Sont-elles cohérentes ?

---

### Exercice 2 : Modifier les paramètres de génération
Ajoutez des paramètres comme temperature et top_k pour explorer l’effet sur les réponses générées :

```python
outputs = model.generate(
    inputs["input_ids"],
    max_length=50,
    num_return_sequences=1,
    temperature=0.7,
    top_k=50
)
```

### Questions : 
- Comment les paramètres influencent-ils la créativité et la précision des réponses ?

---

### Exercice 3 : Personnaliser le modèle
Essayez de remplacer EleutherAI/gpt-neo-125M par d’autres modèles légers, comme :

- distilbert-base-uncased (pour de l’analyse de texte).
- EleutherAI/gpt-neo-1.3B (si vous avez une machine avec un GPU).
### Questions : 
1. Quels modèles fonctionnent le mieux dans votre environnement local ?
2. Pourquoi ?

---

### Étape 4 : Aller plus loin
#### Charger un modèle quantifié (Challenge)
Si les ressources matérielles sont limitées, vous pouvez tester un modèle quantifié (e.g., LLaMA 2 7B 4-bit).

```bash
pip install bitsandbytes
```

Modifiez le script pour utiliser une quantification :

```python
Copier le code
model = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-2-7b-chat-hf",
    device_map="auto",
    load_in_4bit=True
)
```

## Fichiers disponibles

### 1. Script de base : `load_llm.py`
Un fichier Python contenant un script prêt à l'emploi pour charger et interagir avec un modèle léger (`gpt-neo-125M`). 
- Ce script guide les apprenants à poser une question au modèle et recevoir une réponse générée.

### 2. Exemples de questions : `questions.txt`
Un fichier texte listant des questions types que les apprenants peuvent poser au modèle. Ces exemples permettent de tester différentes capacités de génération du modèle.

### 3. Exercice avancé : `llm_experiments.py`
Un fichier Python conçu pour expérimenter avec des paramètres avancés de génération tels que `temperature` et `top_k`. 
- Idéal pour explorer comment ces paramètres influencent les réponses générées.

### 4. Modèle quantifié : `quantized_model.py`
Un fichier Python permettant de charger un modèle quantifié en 4-bit (ex : LLaMA 2 7B) pour une utilisation sur des machines avec ressources limitées.

## Téléchargements

- Fichiers individuels :
  - [Script de base](./load_llm.py)
  - [Exemples de questions](./questions.txt)
  - [Exercice avancé](./llm_experiments.py)
  - [Modèle quantifié](./quantized_model.py)

- Archive complète :
  - [Télécharger le fichier ZIP](./llm_support_files.zip)