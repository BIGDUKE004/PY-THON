#collect input 
#reverse the number 
#create a variable to store the reversed number
#compare the reversed number with his original value


number = int(input("enter a number: "))
digit = 0
reverse_number = 0
clone = number
while number > 0:
    digit = number % 10
    reverse_number = digit + reverse_number * 10
    number = number // 10
if clone ==  reverse_number:
    print("it is a palindrom")
else:
    print("it is not a palindrome")
