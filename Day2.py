class Car:
    def __init__(self,name):
        self._name= name

    @property
    def name(self):
        print("in the gettho")
        return self._name
    @name.setter
    def name(self,name):
        print("in the setto")
        self._name = name

    @name.deleter
    def name(self,name):
        print("im in delulu")
        del self.name

my_car = Car("Jimmywho")
print(my_car.name)
my_car.name = "step bro"
print(my_car.name)