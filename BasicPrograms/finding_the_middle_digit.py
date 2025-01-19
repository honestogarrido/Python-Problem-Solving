"""Write a program to find the middle digit of a five digit number 

Example: 

Enter a number: 24680 

Middle digit = 6 """ 

number= int(input("Enter a number ")) 

division= number//100 

print ("The middle digit is", division%10)  