
num = int(input("Enter the number: "))
fact = 1
if num < 0 :
    print("factorial of 0 does not exist")
    
if num == 0 :
    print("factorial of 0 is ",1 )
if num > 0:
    for i in range (1,num+1):
        fact = fact * i
    print("The factorial of given number is ",fact)