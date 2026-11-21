# view.py

class SimpleView:
    def display_list(self, items):
        print("\n--- Current Languages ---")
        for item in items:
            print(f"• {item}")

    def get_user_input(self):
        return input("\nEnter a new programming language: ")
