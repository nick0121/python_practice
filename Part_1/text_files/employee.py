class Employee:

    def __init__(self, fname, lname, an_salary):
        self.first = fname
        self.last = lname
        self.salary = an_salary
    
    def give_raise(self, amount=5000):
        new_salary = self.salary + amount
        return new_salary

    