"""Write a program to input 3 integers and find the sum of the last digit of each integer. 

Example: 

Enter a number: 23 

Enter a number: 44 

Enter a number: 12 

Sum of last Digits = 9""" 


first= int(input("Enter a number "))  
second= int(input("Enter a number "))  
third= int(input("Enter a number " ))  

first= (first%10)  

second= (second%10)  

third= (third%10) 

sum= first + second + third  
print (sum) 