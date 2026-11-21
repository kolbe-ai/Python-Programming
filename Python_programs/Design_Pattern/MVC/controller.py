# controller.py
from model import SimpleModel
from view import SimpleView


class SimpleController:
    def __init__(self):
        self.model = SimpleModel()  # Create the Data Specialist
        self.view = SimpleView()  # Create the Screen Specialist

    def run_app(self):
        # 1. Ask the Model for the current data
        current_data = self.model.get_items()

        # 2. Tell the View to print that data
        self.view.display_list(current_data)

        # 3. Ask the View to get a new item from the user
        new_language = self.view.get_user_input()

        # 4. Give that new item to the Model to save it
        self.model.add_item(new_language)

        # 5. Get the updated data and show it again to prove it saved!
        updated_data = self.model.get_items()
        self.view.display_list(updated_data)


if __name__ == "__main__":
    # Start the manager
    app = SimpleController()
    app.run_app()
