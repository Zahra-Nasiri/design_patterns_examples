# Factory Method Pattern:
# Defines an interface for creating an object, but leaves the choice of its type to the subclasses, creating an instance of one of the several possible classes.

class Animal:
    def speak(self):
        raise NotImplementedError("Subclasses must implement the 'create_animal' method.")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    def create_animal(self):
        raise NotImplementedError("Subclasses must implement the 'create_animal' method.")

class DogFactory:
    def create_animal(self):
        return Dog()

class CatFactory:
    def create_animal(self):
        return Cat()


def main():
    dog_factory = DogFactory()
    cat_factory = CatFactory()

    dog = dog_factory.create_animal()
    cat = cat_factory.create_animal()

    print(dog.speak())  # Output: Woof!
    print(cat.speak())  # Output: Meow!

if __name__ == "__main__":
    main()