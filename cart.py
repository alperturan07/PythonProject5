from storage import Product
import json

from storage import load_json
from storage import save_json
from storage import tax_rate
from storage import discount_list





def add_to_cart(cart:dict,cartproduct:dict,quantity:int):
    sub_dicttionary = {}
    sub_dicttionary[cartproduct["id"]] = quantity
    i = 0
    found_fleg = False
    for key, value in cart.items():
        i = i+1
        if key == cartproduct["id"]:
            found_fleg = True
            cart.update({key: value+quantity})

    if i == 0 or not found_fleg:
        cart.update(sub_dicttionary)



    return cart
#a = {"id":54,"name":"alper","category":"Electronics","sub_category":"Computer","price":100,"stock":100,"description":" Computer"}
#C = {}
#add_to_cart(C,a,5)

def remove_from_cart(cart:dict,product_id:str):
    cart.pop(product_id)
    return cart

#C = {"50":5}
#print(C)
#remove_from_cart(C,"50")
#print(C)

def update_quantity(cart:dict,product_id:str,quantity:int):
    sub_dicttionary = {}
    sub_dicttionary[product_id] = quantity
    cart.update(sub_dicttionary)
    return cart

#update_quantity(C,"50",1)
#print(C)

def calculate_total(cart:dict,tax_rate: float, discounts: list):
    cart_totals = {}
    total_discount = 0
    p_list = []
    p_list = load_json("products.json")
    total_discount= sum(discounts)


    for id,quantity in cart.items():
        total_price = 0

        for product in p_list:

            if product["id"] == id:
                total_price =product["price"] + product["price"] * tax_rate
                total_price = (total_price * quantity) - total_discount
                cart_totals[product["name"]] = total_price




    return cart_totals


#W = {"1":10,"3": 12,"5":20}

#D = [100,200,300,400,500]

#print(calculate_total(W,tax_rate(),discount_list()))


def apply_promo_code(cart: dict, code: str, promo_rules: dict):
    return(calculate_total(cart,promo_rules[code][0], promo_rules[code][1]))   # In promo rules the value is a list in that list there are 2 values first value is the tax rate and the second one is discount list




#T = {"1":10,"3": 12,"5":20}
#P = {"P001": [0.5,[100,200,300,400,500]],"P002": [0.3,[100]]}
#print(apply_promo_code(T,"P002",P))






















