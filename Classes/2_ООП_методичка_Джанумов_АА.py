# task 1

class Employee:
    new_id = 1
    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1

    def say_id(self):
        print(f'My id is {self.id}')

e1 = Employee()
e2 = Employee()

e1.say_id()
e2.say_id()

# task 2 

class Admin(Employee):

    def say_id(self):
        print('I am an Admin')

e3 = Admin()
e3.say_id()

#task 3
class Admin(Employee):
    def say_id(self):
        super().say_id()       
        print('I am an Admin') 

e3 = Admin()
e3.say_id()


# task 4

class Manager(Admin):
    def say_id(self):
        super().say_id()
        print('It is my deal')

e4 = Manager()
e4.say_id()

class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

    def say_user_info(self):
        print(f'Username: {self.username}, Role: {self.role}')


class Admin(Employee, User):
    def __init__(self):
        Employee.__init__(self)
        User.__init__(self, self.id, "Admin")

    def say_id(self):
        super().say_id()
        print('I am an Admin')


e3 = Admin()
e3.say_user_info()

# task 5
meeting = [Employee(), Admin(), Manager()]

for person in meeting:
    person.say_id()


# task 6
class Meeting:
    def __init__(self):
        self.attendees = []

    def __add__(self, employee):
        self.attendees.append(employee)
        return self

    def __len__(self):
        return len(self.attendees)


m1 = Meeting()

m1 = m1 + e1
m1 = m1 + e2
m1 = m1 + e3

print(len(m1))


# task 7
from abc import ABC, abstractmethod

class AbstractEmployee(ABC):
    new_id = 1

    def __init__(self):
        self.id = AbstractEmployee.new_id
        AbstractEmployee.new_id += 1

    @abstractmethod
    def say_id(self):
        pass


class Employee(AbstractEmployee):
    def say_id(self):
        print(f'My id is {self.id}')


e1 = Employee()
e1.say_id()


# task 8
class Employee(AbstractEmployee):
    def __init__(self):
        super().__init__()
        self._id = self.id
        self.__id = "hidden"

    def say_id(self):
        print(f'My id is {self.id}')


e = Employee()
print(dir(e))


# task 9
class Employee(AbstractEmployee):
    def __init__(self, name=None):
        super().__init__()
        self._name = name

    def say_id(self):
        print(f'My id is {self.id}')

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        if isinstance(new_name, str):
            self._name = new_name
        else:
            raise TypeError

    def del_name(self):
        del self._name


e1 = Employee()
print(e1.get_name())

e1.set_name("Alex")
print(e1.get_name())

e1.del_name()