# collect input from the user
#  use loop to iterate over the number
#create a variable to store the number
# divde the number with modulos
# divide with 10 to get the whole number 
# print 


number = int(input("enter a number: "))
digit = 0
while number > 0:
    digit = number % 10
    print(digit, end="")
    number = number  // 10

