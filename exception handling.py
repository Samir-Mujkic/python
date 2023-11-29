# exceptiom = events detected during execution that interruput the flow of a program

#example

try:
  numerator = int(input("enter a number to divide"))
  denominator = int(input("enter a number to divide by"))
  result = numerator / denominator
  print(result)
except ZeroDivisionError as e:
  print("Your cant divide by zero")

except ValueError as e:
  print("Enter only number please")
except Exception as e:
  print("somethin went wrong")
else:
  print(result)
finally:
  print('This will always execute')
