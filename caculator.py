# This is the way we can Instantiate the class in object oriented
class Calculator:
    """ This is the default result property"""
    result = 0

    # Here is the constructor Method
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    # here are the methods below
    def add(self):
        return self.number1 + self.number2

    def subtract(self):
        return self.number1 - self.number2

    def multiply(self):
        return self.number1 * self.number2

    def devide(self):
        return self.number1 / self.number2

    # Example of User Choosen method we can call is as Recursion
    def decision(self, user_decision):
        if user_decision == '+':
            return self.add()
        elif user_decision == '-':
            return self.subtract()
        elif user_decision == '*':
            return self.multiply()
        elif user_decision == '/':
            return self.devide()


user_input = ' 2 + 2 '
user_input = user_input.strip().split(" ")  # This will split the input into pieces and strip all the white space
print(type(user_input))  # we can check the type of input
print(user_input)  # this will output us the input

number_1 = int(user_input[0])
number_2 = int(user_input[2])
decision = user_input[1]

# It's the example of Polymorphism
cal = Calculator(number_1, number_2)
print(cal.decision(decision))

# This is the way we can Instantiate a method in a class
cal = Calculator(1, 3)
print(cal.add())

cal1 = Calculator(1, 3)
print(cal.subtract())

cal2 = Calculator(1, 3)
print(cal.multiply())

cal3 = Calculator(1, 3)
print(cal.devide())


