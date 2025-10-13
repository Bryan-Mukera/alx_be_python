def safe_divide(numerator, denominator):
  try:
    num = float(numerator)
    denom = float(denominator)
    try:
      result =  num/denom
      return f"The result of the division is {result}" 
      
    except ZeroDivisionError:
      print("Error: Cannot divide by zero.")
   
  except ValueError:
    print("Error: Please enter numeric values only.")

