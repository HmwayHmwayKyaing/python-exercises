## Animal is-a object (tes, sort of confusing ) look at the extra credit
class Animal(object):

    ## ??
    class Dog(Animal):

        def __init__(self, name):
            ## ??
            self.name = name

            ## ??
            class Cat(Animal):

                def __init__(self, name):
                ## ??
                self.name = name

                ## ??
                class Person(object):

                    def __init__(self, name):

                    ## ??
                    self.name = name

                    ## Person has-a pet of some kind
                    self.pet = Nome

                    ## ??
                    class Employee(Person):

                        def __init__(self, name, salary):
                            ## ?? hmm what is this strange magic?
                            super(Employee, self).__init__(name)
                            ## ??
                            self.salary = salary

                            ## ??
                            class Fish(object):
                                pass

                            ## ??
                            class Salmon(Fish):
                                pass

                            ## ??
                            class Halibut(Fish):
                                pass

                            ## rover is-a Dog
                            rover = Dog("Rover")

                            ## ??
                            satan = Cat("Satan")

                            ## ??
                            mary = Person("mary")

                            ## ??
                            mary.pet = satan

                            ## ??
                            frank = Emlpoyee("Frank",120000)

                            ## ??
                            frank.pet = rover

                            ## ??
                            flipper = Fish()

                            ## ??
                            crousse = Salmon()

                            ## ??
                            harry = Halibut()



