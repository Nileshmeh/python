
inventory = { "potato" : 30,
 "onion" : 10,
 "cauliflower" : 60,
 "tomato" : 50,
 "spinach" : 5,
 "mango" : 80,
 "strawberry" : 150,
 "pineapple" : 60,
 "papaya" : 35,
 "cucumber" : 15,
 "lettuce" : 10,
 "apple" : 250,
}

cart = {}

print("Welcome to nigger's shop")
print("Items that are available are:")
print(", ".join(inventory.keys()))
print("press Q to quit anypart of shopping")

print("-" * 40)

while True:
    user_choice = input("add the items you want to add to the cart: ").strip().lower()
    
    if user_choice == "q":
        print("proceeding to checkout")
        break
    
    if user_choice in inventory:
        price_per_unit = inventory[user_choice]
        print(f"your {user_choice} will cost you {price_per_unit} per item")

        quantity_input = (input(f"In how much amount do you want {user_choice}:  "))

        if quantity_input.lower() == "q":
         print("proceeding to checkout")
         break

        if quantity_input.isdigit() and int(quantity_input) > 0:
           quantity = int(quantity_input)
           item_total_price = quantity * price_per_unit

           if user_choice in cart:
                cart[user_choice]['quantity'] += quantity
                cart[user_choice]['total_price'] += item_total_price  # <-- MUST use 'item_total_price'
           else:
                cart[user_choice] = {
                   'quantity' : quantity,
                   'total_price' : item_total_price
                }

           print(f"\n[ADDED] {quantity}x {user_choice.capitalize()} to your cart.")
           print(f"Current unique items in cart: {', '.join(cart.keys())}")

        
        else:
             print("invalid qunatity")

    else:
       print(f"sorry the {user_choice} is not available in the store. choose something else!")


print("-" * 40)
print("       Your final reciept     ")
print("-" * 40)

if not cart:
   print("your cart is empty you total bill is 0")

else:
    grand_total = 0
    print(f"{'Item':<15} | {'Quantity':<10} | {'Subtotal':<10}")
    print("-" * 40)
    for item, details in cart.items():
        print(f"{item.capitalize():<15} | {details['quantity']:<10} | {details['total_price']:<10}")
        grand_total += details['total_price']
    print("-" * 40)
    print(f"Grand Total: {grand_total}")
           

       
           
              

       
        
    



