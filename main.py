import json
import os
from orders import create_order_promo
from storage import ensure_storage_structure
from storage import load_json
from storage import save_json
from storage import backup_file
from storage import tax_rate
from storage import discount_list
from catalog import load_products
from catalog import save_products
from catalog import update_product_stock
from catalog import add_new_product
from catalog import search_product
from catalog import filter_by_category
from cart import add_to_cart
from cart import remove_from_cart
from cart import update_quantity
from cart import calculate_total
from cart import apply_promo_code
from orders import create_order
from orders import save_order
from orders import generate_receipt
from orders import update_inventory_after_order
from orders import load_order
from orders import list_past_orders


Promo = {"P001": [0.5, [200, 300, 400, 500, 600]]}
cart = {}

main_flag = True
while main_flag:
    exit_flag = False
    Registeredornot = (str(input("Welcome to the app! Are you registered? Yes, No or Admin? (type 0 to exit):")))
    if Registeredornot.upper() not in ("0","YES","NO","ADMIN"):
        print("Invalid input. Please try again.")
        exit_flag = True

    elif Registeredornot.upper() == "ADMIN":
        admin_flag = True
        while admin_flag:
            admins_id = str(input("Please enter your admin id:"))
            with open("Admin.json",mode="r",encoding="utf-8") as f:
                data = json.load(f)
            for key, value in data.items():
                if key == admins_id:

                    print("Welcome admin")
                    admin_flag = False
                else:
                    print("Invalid admin id try again")
        adminfleg=True
        while adminfleg:
            print("1) Update product stock ")
            print("2) Add new product ")
            print("3) Top-selling products")
            print("4) Promo update ")
            print("5) Exit ")


            Admin_choice = input("Please enter your choice:")

            if Admin_choice == "1":
                print("Updating product stock")



            elif Admin_choice == "2":
                print("Adding new product to cart")




            elif Admin_choice == "3":
                print("Top-selling products")



            elif Admin_choice == "4":
                print("Promo update products")




            elif Admin_choice == "5":
                adminfleg = False



            else:
                print("Invalid choice try again")






    elif Registeredornot == "0":
        main_flag = False
    else:
        if Registeredornot.upper() == "NO"   :
            print("Please sign up!")
            users_name=str(input("Please enter your name and surname:"))
            users_email=str(input("Please enter your email address:"))
            users_address=str(input("Please enter your address:"))
            with open("Customers.json",mode= "r",encoding="utf-8") as file:
                data = json.load(file)
            Customer_list = []
            if  len(data) == 0 :
                c = {1:[users_name,users_email,users_address]}
                Customer_list.append(c)
            else:
                i=1
                for item in data:
                    i =i+1
                    Customer_list.append(item)
                c = {i: [users_name, users_email, users_address]}
                Customer_list.append(c)
                print(f"Your user id is:{i}")



            with open("Customers.json",mode="w",encoding="utf-8") as file:
                    json.dump(Customer_list,file,indent=4)






        elif Registeredornot.upper() == "YES": # Hiçbi kullanıcı yokken yes diyince sapıtıyo

            userflag = True
            while userflag:

                users_id = str(input("Please enter your user id:"))
                with open("Customers.json",mode="r",encoding="utf-8") as file:
                    data = json.load(file)
                found_flag= False
                for item in data:
                    for key, value in item.items():
                        if users_id==key:
                            found_flag=True


                if found_flag:
                    print(f"Welcome user {users_id}! ")
                    userflag = False
                else:
                    print("Sorry, user not found.")




        while not exit_flag :
            print("To increase your shopping experience we have added some features from our app as shortcuts. Please use them as you wish.  ")
            print("1) See the whole catalog")
            print("2) Search products")
            print("3) Search products by filtering category")
            print("4) Buy products")
            print("5) Cart")
            print("6) Create an order")
            print("7) Previous orders")
            print("8) Exit the app")


            Customers_choice=str(input("Please enter the feature you wish for:"))
            if Customers_choice.upper()=="EXIT":
                os.system('cls')
                exit_flag = True

            if Customers_choice=="1":
                print("                                                                   Catalog        ")
                print("-" * 140)
                loaded_products = load_products("products.json")

                for item in loaded_products:
                    print(f"{item["name"]},price:{item["price"]}TL,stock:{item["stock"]}")
                print("-" * 140)
            elif Customers_choice=="2":
                loaded_products = load_products("products.json")
                Customers_productnamechoice=str(input("Please enter the product name you wish to search:"))
                SP_list = search_product(loaded_products,Customers_productnamechoice)
                print("-"*60)
                for item in SP_list:
                    print(f"{item["name"]},price:{item["price"]}TL,stock:{item["stock"]}")
                print("-"*60)
            elif Customers_choice=="3":
                loaded_products = load_products("products.json")
                Tempset =set()
                for item in loaded_products:
                    Tempset.add(item["category"])
                print(Tempset)


                Customers_categorynamechoice=str(input("Please enter the category you want to filter:"))
                CP_list = filter_by_category(loaded_products,Customers_categorynamechoice)
                print("-" * 60)
                for item in CP_list:
                    print(f"{item["name"]},price:{item["price"]}TL,stock:{item["stock"]}")
                print("-" * 60)

            elif Customers_choice=="4":
                loaded_products = load_products("products.json")

                buyflag = True
                while buyflag  :
                    i=1
                    for item in loaded_products:
                        i= i+1
                        print(f"Press {item["id"]} to buy {item['name']}  price:{item['price']}TL, stock:{item['stock']}")
                    Customerbuyingchoice=int(input("Please choose what you want to buy (Type 0 to return to main menu):"))
                    if Customerbuyingchoice<=i :

                        if Customerbuyingchoice==0:
                            os.system('cls')
                            buyflag = False


                        else:
                            hm = int(input("How many would you like to buy?"))
                            if hm <= loaded_products[Customerbuyingchoice - 1]["stock"]:
                                add_to_cart(cart, loaded_products[Customerbuyingchoice - 1], hm)
                                print(cart)

                            else:
                                print("Sorry we have not enough stock to buy. please try again later.")


                    else:
                        print("Unknown product id please try again.")


            elif Customers_choice=="5":
                #print(cart.keys())
                if len(cart) != 0:
                    print(f"The content of the cart: {cart}")
                    Customer_cart_choice=str(input("Do you want to remove products from the cart? Yes or No:"))

                    if Customer_cart_choice=="Yes":
                        cart_remove_id = str(input("Please enter the id of the product you want to remove:"))
                        remove_from_cart(cart,cart_remove_id)
                        print(f"Contents of the new cart:{cart}")

                else:
                    print("Cart is empty.")





            elif Customers_choice=="6":
                loaded_products = load_json("products.json")
                if len(cart) != 0:
                    Payment = str(input("Please enter the payment method you wish to use (Credit card or Iban) :"))
                    Customer_find_json = str(input("Please enter your user id:"))
                    if Payment == "Credit card" or Payment == "Iban":
                        with open("Customers.json",mode="r",encoding="utf-8") as file:
                            data = json.load(file)
                        for item in data:
                            for key, value in item.items():
                                if key == Customer_find_json:
                                    promo_flag = True
                                    while promo_flag:
                                        pcode = str(input("Do you have the promo code (Yes or No):"))
                                        if pcode == "Yes":
                                            promo_code = str(input("Please enter the promo code:"))
                                            if promo_code == "P001":
                                                order=create_order_promo(cart,item,Payment)
                                                save_order("order.json", order)
                                                generate_receipt(order, "Receipts.json")
                                                update_inventory_after_order(loaded_products, order)
                                                backup_file("products.json", "products_backup.json")
                                                cart = {}
                                                print("Order is saved.")
                                                promo_flag = False

                                            else:
                                                print("There is no such promo code.")
                                                promo_flag = False

                                        elif pcode == "No":
                                            order=create_order(cart,item,Payment)
                                            save_order("order.json", order)
                                            generate_receipt(order, "Receipts.json")
                                            update_inventory_after_order(loaded_products, order)
                                            backup_file("products.json", "products_backup.json")
                                            cart = {}
                                            print("Order is saved.")
                                            promo_flag = False

                                        else:
                                            promo_flag = False






                    else:
                        print("Invalid payment method.")
                else:
                    print("Cart is empty.")


            elif Customers_choice=="7":
                customer_mail = str(input("Please enter your email address:"))
                data = load_order("orders.json")
                Clist= list_past_orders(data,customer_mail)
                if len(Clist) != 0:
                    for item in Clist:
                        print(item)
                else:
                    print("Invalid email address.")


            elif Customers_choice=="8":
                exit_flag=True

            else:
                print("Invalid answer, please try again.")








