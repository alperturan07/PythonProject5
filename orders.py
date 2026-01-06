from storage import Product
import time
import json
from storage import load_json
from storage import save_json
from cart import calculate_total
from storage import tax_rate
from storage import discount_list
from catalog import update_product_stock
import os
from cart import apply_promo_code

def create_order(cart:dict,customer:dict,payment_method:str):
    ts = time.time()
    Total=calculate_total(cart, tax_rate(), discount_list())
    for key,value in customer.items():
        order_last = {key : [value,ts,payment_method,Total,cart]}


    return order_last


def create_order_promo(cart:dict,customer:dict,payment_method:str):
    with open("Promo.json",mode="r",encoding="utf-8") as f:
        data = json.load(f)
    for key,value in data.items():
        promo_key = key
    ts = time.time()
    Total=apply_promo_code(cart, promo_key, data)
    for key,value in customer.items():
        order_last = {key : [value,ts,payment_method,Total,cart]}


    return order_last


#CART = {"1":10,"2":10}
#Customer = {"C001":["Alper Turan","alptur19@gmail.com","kurtkoy"]}

#print(create_order(CART,Customer,"credit card"))


def save_order(path:str,order:dict):
    Order_S = []
    with open(path,mode='r',encoding="utf-8") as file:
        data = json.load(file)
    for item in data:
        Order_S.append(item)

    Order_S.append(order)

    with open(path,mode='w',encoding="utf-8") as file:
        json.dump(Order_S,file,indent=4)

#E={'3': [['soner Turan', 'sontur19@gmail.com', 'kurtkoy'], 1766604762.7219923, 'credit card', {'Lenovo': 373500.0, 'Excalibur': 298500.0},{"1":10,"2":10}]}



#save_order("order.json",E)


def generate_receipt(order: dict, path: str):
    Receipts = []
    with open(path,mode='r',encoding="utf-8") as file:
        data = json.load(file)
    for item in data:
        Receipts.append(item)
    Receipts.append(order)
    with open(path,mode='w',encoding="utf-8") as file:
        json.dump(Receipts,file,indent=4)


#generate_receipt(E,"Receipts.json")



def update_inventory_after_order(Products: list, order: dict):

    for key,value in order.items():
        for K,V in value[4].items():
            update_product_stock(Products,K, V)
    save_json("products.json",Products)
    return Products



#test = load_json("products.json")
#update_inventory_after_order(test,E)

def load_order(path:str):
    loaded_order = []
    with open(path,mode='r',encoding="utf-8") as file:
        data = json.load(file)
    for item in data:
        loaded_order.append(item)
    return loaded_order

#print(load_order("order.json"))

def list_past_orders(orders:list,email : str):
    order_list = []
    for item in orders:
        for key,value in item.items():
            for A in value[0]:
                if A == email:
                    order_list.append(item)

    return order_list

#print(list_past_orders(load_order("order.json"),"ozlozdtur19@gmail.com"))













