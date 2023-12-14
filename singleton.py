# Singleton Pattern:
# Ensures a class has only one instance and provides a global point of access to it.

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

instance_1 = Singleton()
instance_2 = Singleton()

