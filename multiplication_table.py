print("MULTIPLICATION TABLE \n")

user_number = int(input("which table you want : "))

multiplier = 1

while( multiplier <= 10):
    print ( str(user_number) + " X "+ str(multiplier) +" = "+ str(user_number*multiplier) )
    multiplier += 1

print("")
print("Thank you for using my application")
