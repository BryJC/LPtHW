## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a(n) animal
class Dog(Animal):

    def __init__(self, name):
        ## class Dog has-a(n) attribute name set to name
        self.name = name

## Cat is-a(n) animal
class Cat(Animal):

    def __init__(self, name):
        ## class Cat has-a(n) attribute name set to name
        self.name = name

## Person is-a(n) object
class Person(object):

    def __init__(self, name):
        ## Person has-a(n) attribute name set to name
        self.name = name

        ## Person has-a(n) attribute pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## class Employee has-a(n) attribute name set to name (from Person class) ??
        super(Employee, self).__init__(name)
        ## class Employee has-a(n) attribute salary set to salary
        self.salary = salary

## class Fish is-a(n) object
class Fish(object):
    pass

## class Salmon is-a Fish
class Salmon(Fish):
    pass

## class Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
## set satan equal to an instance of class Cat that takes self, "Satan" parameters
satan = Cat("Satan")

## Mary is-a Person
## set mary equal to an instance of class Person that takes self, "Mary" parameters
mary = Person("Mary")

## mary has-a satan
## from (instance of class Person:) mary, get the pet attribute and set it to satan
mary.pet = satan

## frank is-a Employee
## set frank equal to an instance of class Employee that takes self, "Frank", and 120000 arguments
frank = Employee("Frank", 120000)

## frank has-a rover
## from (instance of class Employee:) frank, get the pet attribute (from superclass Person) and set it to rover
frank.pet = rover

## flipper is-a Fish
## set flipper to an instance of class Fish that takes parameter self
flipper = Fish()

## crouse is-a Salmon
## set crouse equal to an instance of class Salmon that takes parameter self
crouse = Salmon()

## harry is-a Halibut
## set harry equal to an instance of class Halibut that takes parameter self
harry = Halibut()
