class Calculator:
    def add(self, a, b):
        return int(a + b)

    def subtract(self, a, b):
        return int(a - b)

    def multiply(self, a, b):
        result = 0
        for i in range(abs(b)):
            result = self.add(result, a)
        return result if b >= 0 else -result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cann't divide by zero")
        result = 0
        while a >= abs(b):
            a = self.subtract(a, abs(b))
            result += 1
        return int(result) if b > 0 else int(-result)

    def modulo(self, a, b):
        if b == 0:
            raise ValueError("Cann't divide by zero")
        while a>= abs(b):
            a = self.subtract(a, abs(b))
        return int(a)


# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(3, 3))
    print("Example: division: ", calc.divide(10, 3))
    print("Example: modulo: ", calc.modulo(23, 5))