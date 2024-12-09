from transformers import AutoTokenizer, AutoModelForCausalLM

# Choix d'un modèle quantifié
model_name = "meta-llama/Llama-2-7b-chat-hf"

# Charger le modèle avec quantification 4-bit
print("Téléchargement et chargement du modèle quantifié...")
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",
    load_in_4bit=True
)
print("Modèle quantifié prêt à l'emploi.")

# Interaction avec le modèle
input_text = input("Posez une question au modèle : ")
inputs = tokenizer(input_text, return_tensors="pt").to("cuda")
outputs = model.generate(inputs["input_ids"], max_length=50)
response = tokenizer.decode(outputs[0], skip_special_tokens=True)

print("\n--- Réponse du modèle ---")
print(response)
