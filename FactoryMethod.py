from abc import abstractmethod, ABCMeta


class Product(metaclass=ABCMeta):
    @abstractmethod
    def action(self):
        pass


class ProductA(Product):
    def action(self):
        print("this is productA's action! ")


class ProductB(Product):
    def action(self):
        print("this is productB's action! ")


class Factory(metaclass=ABCMeta):
    @abstractmethod
    def create_product(self):
        pass


class FactoryA(Factory):
    def create_product(self):
        f = ProductA()
        return f


class FactoryB(Factory):
    def create_product(self):
        f = ProductB()
        return f
