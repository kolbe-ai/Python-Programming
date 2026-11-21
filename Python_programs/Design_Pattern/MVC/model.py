# model.py

class SimpleModel:
    def __init__(self):
        # A simple list acting as our database
        self.data_list = ["Python", "Java", "C++"]

    def get_items(self):
        return self.data_list

    def add_item(self, new_item):
        self.data_list.append(new_item)
