# task 1
class Facade:
    pass

facade_1 = Facade()
facade_1_type = type(facade_1)

print(facade_1_type)

#task 2

class Grade:
    minimum_passing = 65

class Rules:
    def washing_brushes(self):
        return "Point bristlestowards the basin while washing your brushes."
        # в задании написано возвращает, а не выводит в терминал))

class Circle:
    pi = 3.14

    def area(self,radius):
        return self.pi * radius ** 2
    