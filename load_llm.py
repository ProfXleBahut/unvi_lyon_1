from transformers import AutoTokenizer, AutoModelForCausalLM

# Définir le modèle à utiliser
model_name = "EleutherAI/gpt-neo-125M"  # Modèle léger de Hugging Face

# Télécharger le tokenizer et le modèle
print("Téléchargement du modèle...")
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
print("Modèle téléchargé avec succès !")

# Exemple de question
input_text = input("Posez une question au modèle : ")

# Préparer l'entrée pour le modèle
inputs = tokenizer(input_text, return_tensors="pt")

# Générer une réponse
print("Génération de la réponse...")
outputs = model.generate(inputs["input_ids"], max_length=50, num_return_sequences=1)
response = tokenizer.decode(outputs[0], skip_special_tokens=True)

# Afficher la réponse
print("\n--- Réponse du modèle ---")
print(response)
