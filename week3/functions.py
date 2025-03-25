def calculate_discount(price, discount_percent):

  #Discount only applies if the price is 20% or higher
  if discount_percent >= 20:
    discounted_price = (price * (discount_percent/100))
    final_price = price - discounted_price
    return final_price
  else:
    return price

#Prompting price and discount percentage from user  
price = float(input("Please enter a price "))
discount_percent = float(input("please enter the discount percentage "))


#calculate final price
final_price = calculate_discount(price, discount_percent)
 
#print the result
if final_price == price:
  print(f"No dicscount applied. The price due is {price:.2f}")
else:
  print(f"You got a discount and the price due is {final_price:.2f} ")