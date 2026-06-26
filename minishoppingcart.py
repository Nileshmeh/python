menu = {"lays":10,
        "kurkure":20,
        "doritos":35,
        "bingo":30,
        "puffcorn":60
        }

cart = []
total = 0

print("------ MENU ------")
for key , value in menu.items():
    print(F"{key:10} {value:2f}")
    print()
print("----------------------")

while True:
    food_item = input("what food items you want Sir/Man(or you can press q to quit): ").lower()
    if food_item =="q":
        break
    elif menu.get(food_item) is not None:
        cart.append(food_item)

print("----------BILL----------")

for food_item in cart:
    total += menu.get(food_item)
    print(food_item, end=" ")
print()
print(f"total is: {total:2f}" )
print("-------------------------")