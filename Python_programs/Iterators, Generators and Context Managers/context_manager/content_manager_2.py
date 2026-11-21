"""
Scenario: When printing debug logs or outputs to the terminal,
it is helpful to wrap special messages inside a visual banner or box made of characters (like dashes --- or asterisks ***)
to make them stand out.
"""


class Logs:
    def __init__(self, message, char):
        self.message = message
        self.char = char

    def __enter__(self):
        print("\n\n")
        for i in range(20):
            print(self.char, end=" ")
        print(f"\n{self.message}")
        return self

    def __exit__(self, a, b, c):
        for i in range(20):
            print(self.char, end=" ")
        return self


message = "Critical message: \nServer needs to be checked"
with Logs(message, "*") as l:
    pass

message = "Problem: \nOverheating about 80 degree"
with Logs(message, "-") as l:
    pass
