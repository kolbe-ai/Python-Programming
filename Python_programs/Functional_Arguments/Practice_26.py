"""
26. Create broadcast_message(*recipients, **personalized) that sends a personalized message if one is provided,
otherwise the default “Hello from University!”.
Example: broadcast_message("Alice","Bob","Charlie", Alice="Your library books are due.", Charlie="Exam schedule updated.") should print:
To Alice: Your library books are due.
To Bob: Hello from University!
To Charlie: Exam schedule updated.
"""

def broadcast_message (*recipients, **personalized):
    for i in recipients:
        if i in personalized:
            print(f"To {i}: {personalized[i]}")
        if i not in personalized:
            print(f"To {i}: Hello from University!")

broadcast_message("Alice","Bob","Charlie",Alice = "Your libraary book are due",Charlie= "Exam schedule updated")