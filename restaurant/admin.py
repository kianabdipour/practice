from menu import Menu
from super_admin import SupperAdmin
from customer import list_information_login_customer
from category import Category
from item import Item


class Admin:
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.admin_code = None

    # This method is for login admin with a code that super admin set
    def admin_login(self):

        print("Enter your admin code")
        input_admin_code = input(": ")

        # Make type safe
        try:
            int_input_admin_code = int(input_admin_code)

        except ValueError:
            return print("ValueError: You should just type number")

        condition_of_login_admin = False
        for admin in SupperAdmin.list_admin:
            if admin[2] == int_input_admin_code:
                condition_of_login_admin = True
                self.first_name = admin[0]
                self.last_name = admin[1]
                self.admin_code = admin[2]

        if condition_of_login_admin:
            print("\n", self.first_name, self.last_name, "welcome to your admin panel\n")

        else:
            print("Admin code not found")
        return condition_of_login_admin

    # This method append food to list_food in menu class
    # With name food append a price of food by integer type
    @staticmethod
    def add_food():
        print("Enter number of type item \n1 -- food\n2 -- appetizer\n3 -- drink")
        input_number_type_of_item = input(": ")

        print("Enter name of item")
        input_name_of_item = input(": ")

        print("Enter price of {name_item} the currency of money is dollar".format(name_item=input_name_of_item))
        input_price_of_item = input(": ")

        try:
            int_input_price_of_item = int(input_price_of_item)

        except ValueError:
            return print("ValueError: You should type just number")

        if input_number_type_of_item == "1":
            category = Category("food")
            item = Item(input_name_of_item, category.name, int_input_price_of_item)
            category.list_items.append(item)
            Menu.list_categories.append(category)

        elif input_number_type_of_item == "2":
            category = Category("appetizer")
            item = Item(input_name_of_item, category.name, int_input_price_of_item)
            category.list_items.append(item)
            Menu.list_categories.append(category)

        elif input_number_type_of_item == "3":
            category = Category("drinks")
            item = Item(input_name_of_item, category.name, int_input_price_of_item)
            category.list_items.append(item)
            Menu.list_categories.append(category)

    # This method remove the food that user want
    @staticmethod
    def remove_food():
        for item in Menu.list_item:
            print(Menu.list_item.index(item) + 1, " -- ", "(", item.name_item, "price: ", item.price_item, ")",
                  "type: ", item.type_item)

        #input_number_food_for_remove = input(": ")
        ## Make type safe
        #try:
        #    int_input_number_food_for_remove = int(input_number_food_for_remove)

        #except ValueError:
        #    return print("ValueError: You should just type number")

        #condition_of_remove = False
        #for item in Menu.list_name_items:
        #    if Menu.list_name_items.index(item) + 1 == int_input_number_food_for_remove:
        #        Menu.list_name_items.pop(int_input_number_food_for_remove - 1)
        #        condition_of_remove = True

        #if condition_of_remove:
        #    print("Remove food was successful")

        #else:
        #    print("Remove food was unsuccessful")

    # This method is clear and show the all food that we have in list_food
    @staticmethod
    def display_menu():
        print("Enter a number \n1 -- all menu\n2 -- all type that are in menu\n3 -- number each type")
        input_number_display_menu = input(": ")
        if input_number_display_menu == "1":
            number_item = 0
            for category in Menu.list_categories:
                for item in category.list_items:
                    number_item += 1
                    print(number_item, " -- ", "(", item.name, "type:", item.category_name, ")"
                          " price: ", item.price)

        if input_number_display_menu == "2":
            for category in Menu.list_categories:
                print(Menu.list_categories.index(category) + 1, " -- ", category.name)

        elif input_number_display_menu == "2":
            print("1")

    # This method confirm the orders
    # First check that we have orders or not then get the username that admin want to confirm the order
    # After by a nested loop pop all orders that are in customer list and customer list is in list_information_login_
    # customer
    @staticmethod
    def confirmation_the_active_transaction():
        progress = True
        while progress:
            number_account_that_have_orders = 0
            print("Please enter username of user that you want to confirm his orders")
            for customer in list_information_login_customer:
                if len(customer) > 3:
                    print(list_information_login_customer.index(customer) + 1, " -- ", customer[0])
                    number_account_that_have_orders += 1

            input_username_for_admin = input(": ")
            if number_account_that_have_orders > 0:
                for customer in list_information_login_customer:
                    if len(customer) > 3 and input_username_for_admin == customer[0]:
                        while len(customer) != 3:
                            list_information_login_customer[list_information_login_customer.index(customer)].pop()
                print("Confirmation was successful")

            else:
                print("Now we don't have any order")

            if input_username_for_admin == "q":
                progress = False

    # This method show the customer that have already order
    @staticmethod
    def display_orders_of_user():
        number_account_that_have_orders = 0
        for customer in list_information_login_customer:
            if len(customer) > 3:
                print(list_information_login_customer.index(customer) + 1, " -- ", customer[0])
                number_account_that_have_orders += 1

        if number_account_that_have_orders > 0:
            pass

        else:
            print("Now we don't have any order")
