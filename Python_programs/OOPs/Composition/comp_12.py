"""
12. Create a Computer class containing CPU and RAM objects using
composition. Demonstrate that the CPU and RAM are components of
the Computer and are managed as part of the Computer object.
"""

class CPU:
    def __init__(self,cpu):
        self.cpu = cpu
class Memory:
    def __init__(self,ram):
        self.ram = ram

class Computer:
    def __init__(self,system):
        self.system = system
        self.comp = CPU("Intel")
        self.memory = Memory("DDR5")
    def display(self):
        print(f"\nSystem: {self.system} \tCPU: {self.comp.cpu}  \tMemory: {self.memory.ram}")

c = Computer ("Windows")
c.display()
del c
c.display()
