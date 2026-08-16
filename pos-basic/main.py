#██╗   ██╗██████╗ ██╗███████╗██╗      ███████╗ █████╗ 
#██║   ██║██╔══██╗██║██╔════╝██║      ██╔════╝██╔══██╗
#██║   ██║██████╔╝██║█████╗  ██║      ███████╗███████║
#██║   ██║██╔══██╗██║██╔══╝  ██║      ╚════██║██╔══██║
#╚██████╔╝██║  ██║██║███████╗███████╗███████║ ██║  ██║
 #╚═════╝ ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚══════╝ ╚═╝  ╚═╝

import datetime;

class Product:
    
    def __init__(self, code, name, price, stock):
        self.code = code
        self.name = name
        self.price = price
        self.stock = stock
        
class Sale:
    
    def __init__(self):
        self.items = []
        self.date = datetime.datetime.now()
        
    def add_products(self, product, amount):
        self.product = product
        self.amount = amount
        
        if product.stock >= amount:
            self.items.append({"product": product, "amount": amount})
            product.stock -= amount
            print(f"✅ Agregado: {product.name} (x{amount})")
        else:
            print(f"Stock insufficient {product.name}")
            
    def calculate_cut(self):
       return sum(item["product"].price * item["amount"] for item in self.items)
   
#we created a catalog

p1 = Product("1", "Pepsi 600", 25, 5)

#starting sale

new_sale = Sale()
new_sale.add_products(p1, 2)

#calculated

print(f"Charge: ${new_sale.calculate_cut()}")
