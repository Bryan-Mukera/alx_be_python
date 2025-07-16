purchase_amount = float(input("Enter your purchase amount:"))

if purchase_amount >= 1000:
  discount = 0.1 * purchase_amount
elif purchase_amount >= 500: 
  discount = 0.05 * purchase_amount
else: 
    discount = 0
final_price = int(purchase_amount - discount)
print (f"Final price after discount: ${final_price}")