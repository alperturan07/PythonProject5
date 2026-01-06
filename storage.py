import json
class Product:

    def __init__(self,id,name,category,sub_category,price,stock,description):
        self.id = id
        self.name = name
        self.category = category
        self.sub_category = sub_category
        self.price = price
        self.stock = stock
        self.description = description
        self.id : str
        self.name : str
        self.category : str
        self.sub_category : str
        self.price : float
        self.stock : int
        self.description : str

    def to_dict(self):
        return {"id":self.id,"name":self.name,"category":self.category,"sub_category":self.sub_category,"price":self.price,"stock":self.stock,"description":self.description}

    def contains(self,L1):
        index = self.name.upper().find(L1)
        if index != -1:
            return True
        else:
            return False

def ensure_storage_structure(base_dir:str):
    Lenovo = Product("1","Lenovo","Electronics","Computers",25000,100,"Laptop")
    Excalibur = Product("2","Excalibur" ,"Electronics","Computers",20000,100,"Laptop")
    Apple_Macbook = Product("3","Apple Macbook","Electronics","Computers",40000,100,"Laptop")
    Samsung = Product("4","Samsung","Electronics","Telephones",15000,100,"Telephone")
    Apple = Product("5","Apple","Electronics","Telephones",25000,100,"Telephone")
    Huawei = Product("6","Huawei","Electronics","Telephones",20000,100,"Telephone")
    JBL = Product("7","JBL","Electronics","Headphones",3000,100,"Headphone")
    Steelseries = Product("8","Steelseries","Electronics","Headphones",2500,100,"Headphone")
    Logitech = Product("9","Logitech","Electronics","Headphones",3000,100,"Headphone")
    Levis = Product("10","Levis","Clothing","T-shirts",300,100,"T-shirt")
    Hummle = Product("11","Hummle","Clothing","T-shirts",250,100,"T-shirt")
    Lacoste = Product("12","Lacoste","Clothing","T-shirts",350,100,"T-shirt")
    Under_Armour = Product("13","Under Armour","Clothing","Shorts",200,100,"Shorts")
    Nike = Product("14","Nike","Clothing","Shorts",300,100,"Shorts")
    Adidas = Product("15","Adidas","Clothing","Shorts",250,100,"Shorts")
    Boyner = Product("16","Boyner","Clothing","Pants",400,100,"Pants")
    Mudo = Product("17","Mudo","Clothing","Pants",450,100,"Pants")
    Zara = Product("18","Zara","Clothing","Pants",400,100,"Pants")
    Lc_Waikiki = Product("19","Lc Waikiki","Clothing","Coats",800,100,"Coat")
    Bershka = Product("20","Bershka","Clothing","Coats",1200,100,"Coat")
    Oysho = Product("21","Oysho","Clothing","Coats",1000,100,"Coat")
    Pull_Bear = Product("22","Pull Bear","Clothing","Jackets",1250,100,"JAcket")
    Benetton = Product("23","Benetton","Clothing","Jackets",1400,100,"Jacket")
    Nocturne = Product("24","Nocturne","Clothing","Jackets",1200,100,"Jacket")
    Mavi = Product("25","Mavi","Clothing","Jeans",800,100,"Jeans")
    Les_Benjamins = Product("26","Les Benjamins","Clothing","Jeans",1600,100,"Jeans")
    Balenciaga = Product("27","Balenciaga","Clothing","Jeans",2000,100,"Jeans")
    Decathlon = Product("28","Decathlon","Clothing","Sports T-shirts",350,100,"Sports t-shirt")
    North_Face = Product("29","North Face","Clothing","Sports T-shirts",325,100,"Sports t-shirt")
    Colombia = Product("30","Colombia","Clothing","Sports T-shirts",400,100,"Sports t-shirt")
    Puma = Product("31","Puma","Clothing","Sports Shorts",250,100,"Sports short")
    New_Balance = Product("32","New Balance","Clothing","Sports Shorts",250,100,"Sports short")
    Vans = Product("33","Vans","Clothing","Sports Shorts",350,100,"Sports short")
    Selin = Product("34","Selin","Cosmetics","Colognes",50,100,"Cologne")
    Duru = Product("35","Duru","Cosmetics","Colognes",40,100,"Cologne")
    Axe = Product("36","Axe","Cosmetics","Deodorants",80,100,"Deodorant")
    Nivea = Product("37","Nivea","Cosmetics","Deodorants",100,100,"Deodorant")
    Burberry = Product("38","Burberry","Cosmetics","Deodorants",120,100,"Deodorant")
    Calvin_Klein = Product("39","Calvin Klein","Cosmetics","Parfumes",300,100,"Parfume")
    Chanel = Product("40","Chanel","Cosmetics","Parfumes",320,100,"Parfume")
    Jimmy_Choo = Product("41","Jimmy Choo","Cosmetics","Parfumes",300,100,"Parfume")
    Narnia = Product("42", "Narnia","Books","Adventure Books",70,100,"Adventure book")
    Jurassic_Park = Product("43","Jurassic Park","Books","Adventure Books",80,100,"Adventure book")
    Hunger_Games = Product("44","Hunger Games","Books","Science-Fiction Books",100,100,"Science-Fiction book")
    Dune = Product("45","Dune","Books","Science-Fiction Books",100,100,"Science-Fiction book")
    Deep_End = Product("46","Deep End","Books","Romance Books",80,100,"Romance book")
    Happy_Place = Product("47","Happy Place","Books","Romance Books",90,100,"Romance book")
    Hot_Wheels = Product("48","Hot Wheels","Toys","Toy Cars",150,100,"Car")
    Cararama = Product("49","Cararama","Toys","Toy Cars",120,100,"Car")
    Lego_Classic  = Product("50","Lego Classical","Toys","Legos",150,100,"Lego")
    Lego_Technic = Product("51","Lego Technic","Toys","Legos",225,100,"Lego")
    Batman_Figure = Product("52", "Batman Figure","Toys","Figures",300,100,"Figure")
    Superman_Figure = Product("53", "Superman Figure","Toys","Figures",300,100,"Figure")

    Products = [Lenovo.to_dict(),Excalibur.to_dict(),Apple_Macbook.to_dict(),Samsung.to_dict(),Apple.to_dict(),Huawei.to_dict(),JBL.to_dict(),Steelseries.to_dict(),Logitech.to_dict(),Levis.to_dict(),Hummle.to_dict(),Lacoste.to_dict(),Under_Armour.to_dict(),Nike.to_dict(),Adidas.to_dict(),Boyner.to_dict(),Mudo.to_dict(),Zara.to_dict(),Lc_Waikiki.to_dict(),Bershka.to_dict(),Oysho.to_dict(),Pull_Bear.to_dict(),Benetton.to_dict(),Nocturne.to_dict(),Mavi.to_dict(),Les_Benjamins.to_dict(),Balenciaga.to_dict(),Decathlon.to_dict(),North_Face.to_dict(),Colombia.to_dict(),Puma.to_dict(),New_Balance.to_dict(),Vans.to_dict(),Selin.to_dict(),Duru.to_dict(),Axe.to_dict(),Nivea.to_dict(),Burberry.to_dict(),Calvin_Klein.to_dict(),Chanel.to_dict(),Jimmy_Choo.to_dict(),Narnia.to_dict(),Jurassic_Park.to_dict(),Hunger_Games.to_dict(),Dune.to_dict(),Deep_End.to_dict(),Happy_Place.to_dict(),Hot_Wheels.to_dict(),Cararama.to_dict(),Lego_Classic.to_dict(),Lego_Technic.to_dict(),Batman_Figure.to_dict(),Superman_Figure.to_dict()]

    with open(base_dir, mode= "w", encoding ="utf-8") as f:
        json.dump(Products,f,indent=4)
#ensure_storage_structure("products.json")

def load_json(path:str):
    Product_list = []
    product_list_last =[]

    with open(path, mode= "r", encoding = "utf-8") as f:
        data = json.load(f)
    for item in data:
        try:
            Product_list.append(Product(item["id"],item["name"],item["category"],item["sub_category"],item["price"],item["stock"],item["description"]))
            #print(item["id"],item["name"],item["category"],item["sub_category"],item["price"],item["stock"],item["description"])
        except Exception as exc:
            print(f"Error: {exc} in item: {item}")


    for item in Product_list:
        product_list_last.append(item.to_dict())
    return product_list_last

#print(load_json("products.json"))


def save_json(path:str,Updated_Products:list):
    Updated_Products_new = []
    for item in Updated_Products:
        clss = Product(item["id"], item["name"], item["category"], item["sub_category"], item["price"], item["stock"],  item["description"])
        Updated_Products_new.append(clss.to_dict())

    with open(path, mode = "w", encoding = "utf-8") as f:
        data = json.dump(Updated_Products_new,f,indent = 4)

#test = load_json("products.json")
#test_son = []
#for item in test:
    #test_son.append(item.__dict__)


#for item in test:
    #if item.__dict__["name"]== "Lenovo":
        #if item.__dict__["name"]=="Lenovo":
            #item.__dict__["stock"]=item.__dict__["stock"]-1



#save_json("products.json",test)


def backup_file(source_path: str, backup_dir: str):
    with open(source_path, mode = "r", encoding = "utf-8") as f:
        data = json.load(f)
    with open(backup_dir, mode = "w", encoding = "utf-8") as f:
        json.dump(data,f,indent = 4)


#backup_file("products.json","products_backup.json")

def tax_rate():
     return 0.5

#print(tax_rate())

def discount_list():
    return [100,200,300,400,500]

#print(discount_list())
