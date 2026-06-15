#Sopping list Program
shopping_list = []
while True:
    print("....Shopping List Manager....")
    print("1.Add Item in List")
    print("2.Display Items in List")
    print("3.Search Item in List")
    print("4.Remove Item in List")
    print("5.Count Items in List")
    print("6.Exit")
    choice =int(input("Enter your choice:"))
    if choice == 1:
        item=input("Entered item Name is:")
        shopping_list.append(item)
        print("Item added successfully.")

    elif choice == 2:
        print("Shopping List is:")
        for item in shopping_list:
            print(item)

    elif choice == 3:
        item = input("Enter item name to be searched:")
        if item in shopping_list:
            print("Item found in shopping list.")
        else:
            print("Item not found in shopping list.")

    elif choice == 4:
        item = input("Enter item name to be remove:")
        if item in shopping_list:
            shopping_list.remove(item)
            print(item,"This Item removed successfully.")
        else:
            print("Item not found in Shopping List.")
    elif choice == 5:
        print("Total items in shopping list is:", len(shopping_list))

    elif choice == 6:
        print("Exiting program.")
        break
    else:
        print("Invalid choice.")