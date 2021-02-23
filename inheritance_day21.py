# class Animal:
#     def __init__(self):
#         self.num_eyes = 2
#
#     def breathe(self):
#         print("Inhale, exhale.")
#
#
# class Fish(Animal):
#     def __init__(self):
#         super().__init__()
#
#     def breathe(self):
#         super().breathe()
#         print("doing this in underwater.")
#
#     def swim(self):
#         print("moving in water.")
#
#
#
# nemo = Fish()
# nemo.breathe()


class Person:

    def __init__(self):
        self.name = "Ram"
        self.age = 34

    def man(self):
        print("Man well be men.")


class Object(Person):

    def __init__(self):
        super().__init__()

    def man(self):
        super().man()
        print("Man well be Man")


things = Object()
things.man()
