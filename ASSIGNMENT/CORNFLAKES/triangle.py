# collect input from the user to determine the amount of star loops to print
# use for loop to print out the pattern

user = int(input("enter a number: "))
for number in range (user + 1):
    for value in range (number):
        print("*", end=" ")
    print(" ")
