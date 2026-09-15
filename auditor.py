inventory_units = 0
total_units_processed = 0
number_of_failed_attempts = 0

while True:
    user_input=input("Enter stock quantity or 'quit' to exit: ")

    if user_input=="quit":
            break
    elif not user_input.isdigit():
        print("Invalid input. Please enter a valid stock quantity or 'quit' to exit")
        continue
    elif int(user_input) <0:
        print("Invalid input. Please enter a non-negative stock quantity or 'quit' to exit")
        continue
    else:
        if inventory_units + int(user_input)>500:
            print("Overstock alert! You cannot add " + str(user_input)+ " items. Maximum capacity is 500.")
        else:
            inventory_units+=int(user_input)
            print("Added " + str(user_input) + " items to the inventory. " + "Total inventory: " + str(inventory_units))

    

