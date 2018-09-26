total_list = []
grocery_items = []
shop_list = []
count = 0

class Grocery_item:

    def __init__(self,item):
        self.item = item
        self.item_id = count 

    def __repr__(self):
        return '%s' % (self.item)

class ShoppingList():

    def __init__(self,title,description):
        self.title = title
        self.description = description
        self.grocery_items = []
        self.list_id = len(shop_list) + 1

    def __repr__(self):
        return  '%s %s, %s' % (self.title, self.description, self.grocery_items)

       
    
while True:
    shopping_title = input("Enter shopping list title: ")
    description_list = input("Enter simple list description: ")
    new_item = input("Enter grocery item: ")

    shopping_list = ShoppingList(shopping_title,description_list)
    
    shop_list.append(shopping_list)
    # print("-",shopping_list.title)
    # print(shopping_list.description)

    grocery_item = Grocery_item(new_item)
    count += 1
    shopping_list.grocery_items.append(grocery_item)
    #print(grocery_item.item_id,".",grocery_item.item)
    total_list.append(shop_list + grocery_items)

    quit_or_view = input("Enter (q) to EXIT or press (v) to view list: ")
    if (quit_or_view == "q"):
        break
    elif (quit_or_view == "v"):
        for i in total_list:
            print(i)
        # print("-",shopping_list.title)
        # print(shopping_list.description)
        # print(count,".",grocery_item.item)

        add_another_list = input("Please press (Y) if you would like to add another list or press (N) to quit the app: ")
        if (add_another_list == "Y"):
            continue

        else:
            break

       
print("Thank you for using the app!")


  