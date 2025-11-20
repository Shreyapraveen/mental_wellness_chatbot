# ---- SAFETY & CRISIS DETECTION MODULE ----

CRISIS_KEYWORDS = [
    "suicide", "kill myself", "end my life", "end it all",
    "self harm", "hurt myself", "i want to die", "can't go on",
    "hopeless", "life is pointless", "want to harm someone",
    "i feel like dying", "cut myself"
]

def is_crisis_message(text: str) -> bool:
    """
    Returns True if user message contains high-risk or crisis words.
    """
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in CRISIS_KEYWORDS)


def get_crisis_response() -> str:
    """
    Returns a safe and supportive crisis response.
    """
    return (
        "I'm really sorry you're feeling this way. "
        "You are not alone, and your feelings are valid. "
        "Please consider reaching out to someone you trust or contacting a local helpline immediately. "
        "I care about your safety, but I'm just an AI and cannot provide emergency help."
    )
