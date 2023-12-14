# Prototype Pattern:
# Creates new objects by copying an existing object, known as the prototype.
import copy


class Prototype:
    def clone(self):
        pass


class ConcretePrototype(Prototype):
    def __init__(self, data):
        self.data = data

    def clone(self):
        return copy.copy(self) 


if __name__ == "__main__":
    original_object = ConcretePrototype(data="Original Data")

    cloned_object = original_object.clone()

    print("Original Object Data:", original_object.data)
    print("Cloned Object Data:", cloned_object.data)
    print(original_object is cloned_object) # returns False