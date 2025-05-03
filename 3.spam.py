spam_keywords = [
    "win", "free", "prize", "click here", "buy now", "urgent",
    "money", "lottery", "congratulations", "offer", "limited time"
]

def is_spam(email_text):
    email_text_lower = email_text.lower()
    for keyword in spam_keywords:
        if keyword in email_text_lower:
            return True
    return False

email_input = input("Enter your email content:\n")

if is_spam(email_input):
    print("\nResult: This email is likely SPAM.")
else:
    print("\nResult: This email is NOT SPAM.")
