"""
Q26. Create a function broadcast_message(*recipients, **personalized) that:

Sends a personalized message if available in **kwargs
Otherwise, sends the default message: "Hello from University!"
"""

def broadcast_message(*recipients, **personalized):
    for i in recipients:
        if i in personalized:
            print(f"Hello {i}, {personalized[i]}")
        else:
            print(f"Hello {i} from University!")

broadcast_message("Alice","Bob","John",Alice= "Marks available",John="Collect Books")