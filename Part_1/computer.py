class Computer:

    def __init__(self, make, model, serial_num):
        self.make = make
        self.model = model
        self.serial_num = serial_num

    def get_description(self):
        print(f'This computer is a {self.make} model {self.model} and serial number: {self.serial_num}')

    def upgrade_computer(self, model, serial_num):
        self.serial_num = serial_num
        self.model = model
        


new_computer = Computer('hp', 'gs450', 10001)

new_computer.get_description()

new_computer.upgrade_computer('gs550', 10002)

new_computer.get_description()

