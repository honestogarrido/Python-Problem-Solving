"""Write a Python program to calculate the Body Mass Index (BMI) of a person. Prompt the user to enter their weight (in kilograms) and height (in meters), and then display the calculated BMI. 

Formula: 

BMI=Weight / (Height**2) 

Sample Run 

Welcome to the BMI Calculator! 

Please enter your weight (in kg): 70 

Please enter your height (in meters): 1.75 


Your BMI is approximately: 22.86 """ 

weight= int(input("Please enter your weight "))  

height= float(input("Please enter your height "))  

bmi= (weight)/(height**2)  

print("Your BMI is: ", bmi) 