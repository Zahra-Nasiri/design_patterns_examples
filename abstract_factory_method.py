# Abstract Factory Pattern
# Provides an interface for creating families of related or dependent objects without specifying their concrete classes.

class Chair:
    def sit_on(self):
        pass

class ModernChair(Chair):
    def sit_on(self):
        return "Sitting on a modern chair"

class VictorianChair(Chair):
    def sit_on(self):
        return "Sitting on a Victorian chair"

class Table:
    def put_item(self):
        pass

class ModernTable(Table):
    def put_item(self):
        return "Putting item on a modern table"

class VictorianTable(Table):
    def put_item(self):
        return "Putting item on a Victorian table"

class FurnitureFactory:
    def create_chair(self):
        pass

    def create_table(self):
        pass

class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return ModernChair()

    def create_table(self):
        return ModernTable()

class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return VictorianChair()

    def create_table(self):
        return VictorianTable()


def create_furniture(factory):
    chair = factory.create_chair()
    table = factory.create_table()
    return chair, table


modern_factory = ModernFurnitureFactory()
modern_chair, modern_table = create_furniture(modern_factory)

print(modern_chair.sit_on()) 
print(modern_table.put_item())

victorian_factory = VictorianFurnitureFactory()
victorian_chair, victorian_table = create_furniture(victorian_factory)

print(victorian_chair.sit_on())  
print(victorian_table.put_item())  