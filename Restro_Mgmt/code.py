menu={
    'Pizza':40,
    'Pasta':50,
    'Burger':60,
    'Salad':70,
    'Coffee':80,
}
print("Welcom to Python Restaurants:");
print("Our Menu:");
print("Pizza:40\nPasta:50\nBurger:60\nSalad:70\nCoffee:80\n");
order_total=0
item_1=input("Enter the item you want to add:")
if item_1 in menu:
    order_total+=menu[item_1]
    print("You item",item_1," has been added in your order");
else:
    print("please order something from thw menu ",item_1," is currently not available");
another_item=input("Do you want to add another item in your order:(Yes/No)?");
if another_item=="Yes":
    item_2=input("Enter your second item to be added in order:");
    if  item_2 in menu:
        order_total+=menu[item_2]
        print("Your item has been added to the order");
    else:
        print("Ordered item is not currently available!!");
print("total bill:",order_total);
print("Ordered Items:",item_1,"and",item_2);
print("Thanks for the Order Visit Again")
