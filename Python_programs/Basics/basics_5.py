"""
Write student_card(name, **details) that prints each detail as key -> value.
"""


def student_card(name,**details):
  print("Name: ",name)
  for i,j in details.items():
    print(f"{i}: {j}")


student_card("Arun",age = 20,blood_group = 'A',grade = 12)