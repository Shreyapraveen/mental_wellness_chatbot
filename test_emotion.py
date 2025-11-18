from models.emotion_model import detect_emotion

if __name__ == "__main__":
    text = "I am feeling very low and tired today."
    label, confidence = detect_emotion(text)
    print("Text:", text)
    print("Predicted emotion:", label)
    print("Confidence:", confidence)
