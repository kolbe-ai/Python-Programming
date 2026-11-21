"""
9. Create a University class and a Student class using aggregation. A
university should maintain references to students. Demonstrate that
deleting the University object does not delete the Student objects.
"""

class University:
    def __init__(self,u_name):
        self.u_name = u_name
        self.batch = []
    def add_student(self,name):
        self.batch.append(name)
    def display(self):
        for i in self.batch:
            print(f"Class: {i.batch}\tUniversity: {i.u_name.u_name}")


class Student_C:
    def __init__(self,batch,u_name):
        self.batch = batch
        self.u_name = u_name

    def display(self):
        print(f"Class: {self.batch}\tUniversity: {self.u_name.u_name}")

uni = University("IIT")
batch1 = Student_C("Batch1",uni)
uni.add_student(batch1)
batch2 = Student_C("Batch2",uni)
uni.add_student(batch2)
batch3 = Student_C("Batch3",uni)
uni.add_student(batch3)
batch4 = Student_C("Batch4",uni)
uni.add_student(batch4)

print(f"\n\nBatches is: \n")
uni.display()

#deleting uni
del uni

##printing again to verify aggregation
print(f"\n\nAfter Deleting UNIVERSITY CLASS \nBatches is: \n")
batch1.display()
batch2.display()
batch3.display()
batch4.display()