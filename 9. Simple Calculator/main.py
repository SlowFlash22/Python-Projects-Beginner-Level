from clear import clean
from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  if n2 !=0:
    return n1 / n2
  else: 
    return 

def remainder(n1,n2):
    return n1 % n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
  "%": remainder
}

def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
  should_continue = True
 
  while should_continue:
    for symbol in operations:
      print(symbol)
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    answer = 0
    if operation_symbol in operations:
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
    choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to restart the calculator, or Type 'x' to exit: ")
    if choice == 'y':
      num1 = answer
    elif choice == 'n':
      should_continue = False
      clean()
      calculator()
    else:
        should_continue = False
        print("Thanks for using this program...")
        print("Exiting...")

calculator()
