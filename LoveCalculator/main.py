print("Welcome to love calculator!")
name1= input("What is your Name? \n").lower()
name2= input('What is your soulmates name? \n').lower()

combined_Names= name1 + name2

T=combined_Names.count("t")
R=combined_Names.count("r")
U=combined_Names.count("u")
E=combined_Names.count("e")
 
True1= T+R+U+E

L=combined_Names.count("l")
O=combined_Names.count("o")
V=combined_Names.count("v")
E=combined_Names.count("e")

love= L+O+V+E

total= str(True1) + str(love)

if (total < "10") or (total > "90"):
  print(f"Your score is {total}, You are incompatible")
  
elif (total >= "40") and (total <= "75"):
  print(f"Your score is {total}, You are ok together ")
    
else:
  print(f"Your score is {total}")  
