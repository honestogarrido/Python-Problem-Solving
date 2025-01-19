"""Write a program to take the temperature in Fahrenheit and change it to Celsius. 

Formula: C = (F-32) x (5/9)  


Write a program to input 3 integers and find the sum of the last digit of each integer. 

Example: 

Enter a number: 23 

Enter a number: 44 

Enter a number: 12 

Sum of last Digits = 9 """


a = int(input("Enter a number: ")) 

b = int(input("Enter a number: ")) 

c = int(input("Enter a number: ")) 

last_digit_a = a%10 

last_digit_b = b%10 

last_digit_c = c%10 

total = last_digit_a + last_digit_b + last_digit_c 
# print(last_digit_a, last_digit_b, last_digit_c) 

print("Sum of last digits: ", total) 