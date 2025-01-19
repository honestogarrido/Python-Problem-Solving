"""Question: Write a Python program to calculate the speed of a vehicle. Prompt the user to enter the distance travelled (in kilometres) and the time taken (in hours), and then display the calculated speed. 

Formula: 

Speed=Distance/Time 

 
Sample Run 

Welcome to the Speed Calculator! 

Please enter the distance traveled (in kilometers): 300 

Please enter the time taken (in hours): 5 

The speed of the vehicle is approximately 60.0 km/h""" 


print("Welcome to the Speed Calculator!")  
distance= int(input("Enter your distance travelled "))  
time= int(input("Enter the time taken "))  
speed= distance/time  

print(speed) 