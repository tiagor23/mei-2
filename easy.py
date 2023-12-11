def add_numbers(result, a, b):
    
    result += a + b
    return result

def multiply_numbers(result, a, b):
    
    result += a * b
    return result

def main():
    result = 0
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    result = add_numbers(result, num1, num2)
    print(f"Sum: {result}")

    product_result = multiply_numbers(result, num1, num2)
    print(f"Product: {product_result}")

if __name__ == "__main__":
    main()
