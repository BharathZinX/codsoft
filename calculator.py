class Calculator:
    def __init__(self):
        self.choice = None
        self.num1 = None
        self.num2 = None

    def get_user_input(self):
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        self.choice = input("Enter choice (1/2/3/4): ")

        try:
            self.num1 = float(input("Enter first number: "))
            self.num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            self.num1 = None
            self.num2 = None

    def perform_operation(self):
        if self.choice == '1':
            print(f"{self.num1} + {self.num2} = {self.add()}")
        elif self.choice == '2':
            print(f"{self.num1} - {self.num2} = {self.subtract()}")
        elif self.choice == '3':
            print(f"{self.num1} * {self.num2} = {self.multiply()}")
        elif self.choice == '4':
            if self.num2 == 0:
                print("Cannot divide by zero!")
            else:
                print(f"{self.num1} / {self.num2} = {self.divide()}")
        else:
            print("Invalid choice.")

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2 if self.num2 != 0 else None

    def run_calculator(self):
        while True:
            self.get_user_input()
            if self.num1 is None or self.num2 is None:
                continue
            self.perform_operation()
            next_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
            if next_calculation != "yes":
                print("Exiting calculator.")
                break


if __name__ == "__main__":
    calculator = Calculator()
    calculator.run_calculator()
