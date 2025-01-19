"""Write a program to take 3 integers and find their difference between sum and average. 

Sample Run: 


Enter the first integer: 10 

Enter the second integer: 15 

Enter the third integer: 12 


The difference between the sum and average is: 24.666666 """


first= int(input("Enter the first integer "))  

second= int(input("Enter the second integer "))  

third= int(input("Enter the third integer ")) 

total= first+second+third  

average= total/3  

difference= total-average  

print ("The difference between the sum and the average is", difference) 