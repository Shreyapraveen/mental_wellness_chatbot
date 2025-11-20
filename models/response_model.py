# ---- FINAL RESPONSE MODEL FILE ----

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load model (DistilGPT2)
try:
    MODEL_NAME = "distilgpt2"
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
    MODEL_AVAILABLE = True
except:
    MODEL_AVAILABLE = False

# Templates for empathetic responses
TEMPLATES = {
    "sadness": "I’m sorry you’re going through this. If you want, I can stay here and listen.",
    "anger": "It makes sense to feel angry about that. If you want, tell me more.",
    "fear": "That must be scary. I’m here and I can listen if you want to share more.",
    "joy": "I’m so happy for you — that sounds great!"
}

# Main Response Function
def generate_response(user_text, emotion):
    # If emotion has a predefined template
    if emotion in TEMPLATES:
        return (
            f"{TEMPLATES[emotion]}  I’m an AI, not a professional. If this is an emergency, please reach out to local services.",
            {"strategy": "template"}
        )

    # Fallback to GPT-2 generation
    if MODEL_AVAILABLE:
        input_text = f"User is feeling {emotion}: {user_text}\nAI:"
        inputs = tokenizer.encode(input_text, return_tensors="pt")
        outputs = model.generate(inputs, max_length=80, do_sample=True, temperature=0.7)
        text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return text, {"strategy": "gpt"}

    # If model fails
    return "I’m here for you. Tell me more about what you're feeling.", {"strategy": "fallback"}
