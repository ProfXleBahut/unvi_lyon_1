from transformers import AutoTokenizer, AutoModelForCausalLM

# Choix du modèle
model_name = "EleutherAI/gpt-neo-125M"

# Téléchargement du tokenizer et du modèle
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Fonction pour générer une réponse
def generate_response(input_text, temperature=0.7, top_k=50):
    inputs = tokenizer(input_text, return_tensors="pt")
    outputs = model.generate(
        inputs["input_ids"],
        max_length=50,
        num_return_sequences=1,
        temperature=temperature,
        top_k=top_k
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Tester différents paramètres
print("=== Expérimentation avec le modèle ===")
questions = [
    "What is artificial intelligence?",
    "Explain reinforcement learning.",
    "What are the benefits of AI in healthcare?"
]

for question in questions:
    print(f"\nQuestion : {question}")
    print("Réponse standard :")
    print(generate_response(question))
    print("\nRéponse créative :")
    print(generate_response(question, temperature=1.0, top_k=100))
