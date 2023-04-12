
class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name 
        self.price = price 

    def __str__(self) -> str:
        return "<{} {}>".format(self.id, self.name)
    
    def serialize(self):
        return {
            'id': self.id, 
            'name': self.name,
            'price': self.price
        }
    

if __name__ == '__main__':
    product = Product(1, "Monitor", 120.5)
    print(product)
    print(product.serialize())

