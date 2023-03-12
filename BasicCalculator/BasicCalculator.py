FirstNum = float(input("Enter First Number: "))
SecondNum= float(input("Enter Second Number: "))
Operator=input("Enter Operator: ")


if Operator == "+" :
  print(FirstNum + SecondNum)
elif Operator== '-':
   print(FirstNum - SecondNum)
elif Operator == '*':
  print(FirstNum * SecondNum)
  
elif Operator == '/':
  print(round(FirstNum / SecondNum , 3))
  
else:
  print(f"Error! The {Operator} Operator is invalid. ")     
  
