
print(r'''
             ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
          jgs |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
      
      
      ''')





print("\n        Welcome to treasure hunt!\n        Your Mission is to find the Hidden treasure!\n\n")
crossroad= input("\n You are at a crossroad,which way will you take? left or right:  ").lower()
if crossroad == "right":
  print("\n Oops! That Road contained wildebeast and you were stumbled to death,Game over!")
  
elif crossroad=="left":
  
  lake_Option= input("\n You find a lake, will you wait for a boat or swim across ? type swim or wait: ").lower()
  
  if lake_Option =="swim":
    print("\n Oops! You were grabbed by an alligator, Game Over!")
    
  elif lake_Option=="wait":
    door_option=input("\n You arrive atthe island safely. There is a mansion with three colored doors. One red, yellow and blue. Which color are you picking? ").lower()
    
    if door_option== "yellow":
      print("\n Congratulations You found the treasure! You are now Rich")
      
    elif door_option =="red":
      print("\n Oops! That door contained lava and you are burned to death, Game Over!")
      
    elif door_option== "blue":
      print("\n Oops! That door was holding too much water, You drowned, Game Over!")
    else:
      print("\n Check your input, Game Over!")
  else:
     print("\n Check your input, Game Over!")   
    
       
      
else:
  print("\n Check your input, Game Over!")   
    

  