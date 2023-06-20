def shopper():
    shoppingList = {}
    product = ""
    
    total = 0
 

    while product != "stop":

        #ask user for an item that they want to add
        product = input("Enter a product you want to buy: ")

        #ask user for price
        price = float(input("Enter the price of the product:"))
        total += price

        shoppingList[product] = price

    shoppingList.pop("stop")

    print(shoppingList)
    print(total)


    #add item to shoppingList
    #print total


shopper()
