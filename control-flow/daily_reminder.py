task = input("Enter your task:")
priority = input ("Priority (high/medium/low):")
time_bound = input ("Is it time-bound? (yes/no):")

match priority:
  case "high":
    result = f"'{task}' is a {priority} priority task"
  case "medium": 
    result = f"'{task}' is a {priority} priority task"
  case "low":
    result = f"'{task}' is a {priority} priority task"
    
if time_bound == "yes":
    reminder = "that requires immediate attention today!"
else:
    reminder = ". Consider completing it when you have free time."
print(result, reminder) 
  
