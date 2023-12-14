# Builder Pattern:
# Separates the construction of a complex object from its representation, allowing the same construction process to create various representations.

class Computer:
    def __init__(self, cpu, memory, storage, gpu):
        self.cpu = cpu
        self.memory = memory
        self.storage = storage
        self.gpu = gpu

    def __str__(self):
        return f"Computer: CPU={self.cpu}, Memory={self.memory}, Storage={self.storage}, GPU={self.gpu}"

class ComputerBuilder:
    def set_cpu(self, cpu):
        pass
    
    def set_memory(self, memory):
        pass

    def set_storage(self, storage):
        pass

    def set_gpu(self, gpu):
        pass

    def get_computer(self):
        pass


class GamingComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer(cpu=None, memory=None, storage=None, gpu=None)

    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def set_memory(self, memory):
        self.computer.memory = memory
        return self

    def set_storage(self, storage):
        self.computer.storage = storage
        return self

    def set_gpu(self, gpu):
        self.computer.gpu = gpu
        return self

    def get_computer(self):
        return self.computer

class ComputerDirector:
    def construct(self, builder):
        return builder.set_cpu("Intel i9").set_memory("32GB").set_storage("1TB SSD").set_gpu("NVIDIA RTX 3080").get_computer()


gaming_computer_builder = GamingComputerBuilder()
computer_director = ComputerDirector()

gaming_computer = computer_director.construct(gaming_computer_builder)
print(gaming_computer)