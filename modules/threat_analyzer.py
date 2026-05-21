import re

phishing_keywords = [

    "urgent",
    "verify",
    "password",
    "bank",
    "login",
    "otp",
    "credit card",
    "click here",
    "suspended",
    "security alert",
    "reset password",
    "confirm account",
    "limited time",
    "unauthorized access"
]

def analyze_message(message):

    score = 0

    detected = []

    text = message.lower()

    for keyword in phishing_keywords:

        if keyword in text:

            score += 10

            detected.append(keyword)

    # Detect URLs

    urls = re.findall(
        r'(https?://\S+)',
        message
    )

    if urls:

        score += 20

        detected.append("Suspicious URLs")

    # Detect urgency language

    urgency_words = [
        "immediately",
        "urgent",
        "now",
        "asap"
    ]

    for word in urgency_words:

        if word in text:

            score += 10

            detected.append("Urgency Tactics")

    # Final classification

    if score >= 60:
        risk = "HIGH RISK"

    elif score >= 30:
        risk = "SUSPICIOUS"

    else:
        risk = "SAFE"

    return {
        "score": score,
        "risk": risk,
        "detected": detected
    }