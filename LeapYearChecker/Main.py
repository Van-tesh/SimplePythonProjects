year= int(input("Which Year Do you want to check? "))

DivisibleBy4= year % 4
DivisibleBy100= year % 100
DivisibleBy400 = year % 400 

if DivisibleBy4 == 0 :
  if DivisibleBy100 == 0:
   if DivisibleBy400 == 0:
    print(f"{year} is a leap year")
   else:
     print(f"{year} is a not leap year")
  else:
   print(f"{year} is  a leap year")  
else:
  print(f"{year} is not a leap year")  
