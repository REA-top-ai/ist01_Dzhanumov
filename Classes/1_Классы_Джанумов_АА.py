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
    
# task 3


class Circle:
    
    def __init__(self,diameter):
        print(f'New circle with diameter: {diameter}')

    pi = 3.14

    def area(self,radius):
        return self.pi * radius ** 2
    

teaching_table = Circle(36)

# task 4

class Circle:
    
    def __init__(self,diameter: int):
        print(f'New circle with diameter: {diameter}')
        self.radius = diameter / 2
    pi = 3.14

    def area(self,radius):
        return self.pi * radius ** 2
    
    def circumference(self):
        return 2 * self.pi * self.radius
    
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())

# task 5 

print(dir(5))

def this_function_is_an_object(*args, **kwargs):
    return "Функция тоже объект!"

print(dir(this_function_is_an_object))

# task 5

class Circle:
    
    def __init__(self,diameter: int):
        print(f'New circle with diameter: {diameter}')
        self.radius = diameter / 2
    pi = 3.14

    def area(self,radius):
        return self.pi * radius ** 2
    
    def circumference(self):
        return 2 * self.pi * self.radius
    
    def __repr__(self):
        return f'Circle with radius {self.radius}'


medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza,
      teaching_table,
      round_room)
