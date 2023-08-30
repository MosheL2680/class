import logging

# Configure logging
logging.basicConfig(filename='function_usage.log', level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def summ():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    result = a + b
    print("Sum:", result)
    logging.info(f"Summation: {a} + {b} = {result}")

def kefel():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    result = a * b
    print("Product:", result)
    logging.info(f"Multiplication: {a} * {b} = {result}")

def hiluk():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    if b != 0:
        result = a / b
        print("Division:", result)
        logging.info(f"Division: {a} / {b} = {result}")
    else:
        print("Cannot divide by zero")

# Call the functions
summ()
kefel()
hiluk()
