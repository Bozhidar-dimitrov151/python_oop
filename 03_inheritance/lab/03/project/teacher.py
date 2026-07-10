from person import Person
from employee import Employee

class Teacher(Person, Employee):
    def sleep(self):
        return "teaching..."

