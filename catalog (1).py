from storage import Product
import json

from storage import load_json
from storage import save_json



def load_products(path:str):
    return load_json(path)

def save_products(path:str,Updated_Products:list):
    return save_json(path,Updated_Products)

#test = load_json("products.json")


def update_product_stock(Updated_stock: list, product_id: str, delta: int):
    for item in Updated_stock:
        clss = Product(item["id"], item["name"], item["category"], item["sub_category"], item["price"], item["stock"], item["description"])
        if clss.to_dict()["id"]==product_id:

            stock = clss.to_dict()["stock"]
            clss.to_dict()["stock"]=stock-delta
            item["stock"]=stock-delta
            return True

    return False



#update_product_stock(test,"1",15)
#for item in test:
    #clss = Product(item["id"], item["name"], item["category"], item["sub_category"], item["price"], item["stock"],item["description"])
    #print(clss.to_dict())
#save_products("products.json",test)


def add_new_product(New_Product: list, product_data: dict):
    New_Product.append(Product(product_data["id"],product_data["name"],product_data["category"],product_data["sub_category"],product_data["price"],product_data["stock"],product_data["description"]).to_dict())
    save_products("products.json",New_Product)
    return New_Product

#a = {"id":55,"name":"alper","category":"Electronics","sub_category":"Computer","price":100,"stock":100,"description":" Computer"}
#print(add_new_product(test,a))




def search_product(SProducts: list, keyword: str):
    Search_list =[]
    for item in SProducts:
        clss = Product(item["id"], item["name"], item["category"], item["sub_category"], item["price"], item["stock"],item["description"])

        if clss.contains((keyword.upper())):
            Search_list.append(item)
    return(Search_list)



#for item in search_product(test,"w"):
    #clss = Product(item["id"], item["name"], item["category"], item["sub_category"], item["price"], item["stock"], item["description"])
    #print(clss.to_dict())

def filter_by_category(CProducts: list, category: str):
    Filtered_Products = []
    for item in CProducts:
        clss = Product(item["id"], item["name"], item["category"], item["sub_category"], item["price"], item["stock"],item["description"])

        if clss.to_dict()["category"]==(category.title()):
            Filtered_Products.append(item)
    return(Filtered_Products)




#for item in filter_by_category(test,"ELECTRONICS"):
     #clss = Product(item["id"], item["name"], item["category"], item["sub_category"], item["price"], item["stock"],item["description"])
     #print(clss.to_dict())
a = {"2007":"Alper Turan"}
with open("Admin.json",mode="w",encoding="utf-8") as file:
    json.dump(a,file,indent=4)

