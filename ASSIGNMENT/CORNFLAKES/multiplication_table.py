# use one loop for the range of 1-10
# collect the user input and multiply it with the loop

user = int(input("enter a number: "))
for number in range(1, 11):
    print(f"{user} * {number} = {user * number}")
