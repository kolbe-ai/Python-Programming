#24. Use arbitrary keyword arguments (**kwargs) in a function that collects customer details and displays them as key: value pairs.




def customer(**kwargs):
    for i,j in kwargs.items():
        print(f"Key:{i}\t Value: {j}")

dist = {"101" : "Ravi" , "102" : "Raju"}
customer(**dist)