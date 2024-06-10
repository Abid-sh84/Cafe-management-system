menu={
    'pizza':100,
    'coffee':80,
    'salad':70,
    'burgur':250,
    'water-bottel':50,
    'pasta':50,
}
print("Welcome to my restaurent")
print("pizza: Rs100\n coffee: Rs80\n salad: Rs70\n burgur: Rs250\n water-bottel: Rs50\n pasta: Rs50")
order_total=0
item_1=input("Enter the name of the item you want to order=")
if item_1 in menu:
    order_total+=menu[item_1]
    print(f"your item{item_1} has been added to your order" )
else:
    print(f"order item{item_1} is not available yet")
another_order=input("do you want to add another item ?(Yes/No)")
if another_order=="Yes":
    item_2=input("Enter the name of the second item=")
    if item_2 in menu:
        order_total+=menu[item_2]
    print(f"your item{item_2} has been added to your order" )
else:
    print(f"order item{item_2} is not available yet")
print(f"total amout to be pay is{order_total}")

