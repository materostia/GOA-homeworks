def vending_machine(products):
    count = 1


    for product in products:
        print(count, product)
        count = count + 1


    choose = int(input("Please Choose product: "))
    money = int(input("Please enter money: "))


    if choose == 1 and money >= 2:
        return "cola"
    elif choose == 2 and money >= 5:
        return "nabeglavi"
    elif choose == 3 and money >= 3:
        return "snickers"
    elif choose == 4 and money >= 3:
        return "fanta"
    elif choose == 5 and money >= 1:
        return "water"
    else:
        return "invalid option or not enough money"
    

print(vending_machine"cola 2.00", "nabeglavi 5.00", "snickers 3.00", "fanta 3.00", "water 1.00")

   
   