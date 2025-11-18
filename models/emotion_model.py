from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Path to your saved model folder
MODEL_PATH = "saved_models/emotional_model"

# Load tokenizer and model only ONCE (faster)
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)

# Put the model in evaluation mode
model.eval()

def detect_emotion(text: str):
    """
    Detects emotion from a given text using the saved HuggingFace model.
    Returns:
        - predicted_label (str)
        - confidence_score (float)
    """

    # Tokenize the input
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)

    # Run the model
    with torch.no_grad():
        outputs = model(**inputs)

    # Get prediction
    logits = outputs.logits
    probabilities = torch.softmax(logits, dim=1)
    confidence_score, predicted_class = torch.max(probabilities, dim=1)

    # Convert class index → label
    label = model.config.id2label[predicted_class.item()]
    confidence = confidence_score.item()

    return label, confidence
