
def prime_checker(number):
  is_prime= True
  if number<=1 :
    is_prime= False
  for i in range(2, number):    
    if number % i == 0 :
      is_prime=False
  if is_prime:
    print("Its a Prime number")
  else:
    print("It's not a prime number.")


n= int(input("what number do you wish to check: "))

prime_checker(number=n)





