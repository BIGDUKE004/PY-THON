# collect input from the user
# place a condition that if the mark is more than the pass mark 
# it should keep count of the pass mark
count = 0
for number in range (1, 16):
    score = int(input("enter a number: "))
    if score > 45:
        count += 1
        print(f"number of student with pass mark:  {count}")
