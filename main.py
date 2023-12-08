import csv

class Item:
    pay_rate = 0.8 
    all = []
    def __init__(self, name: str , price: float, quantity: int) -> None:
        # Run validations to the recived arguments
        assert price >=0, f" Price {price} isn't greater than zero"
        assert quantity >= 0, f"Quantity {quantity} isn't greater than zero"
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        # Actions to execute
        Item.all.append(self)
    def calculte_total_price(self):
        return self.price * self.quantity
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name= item.get('name'),
                price = float(item.get('price')),
                quantity= int(item.get('quantity'))
            )
    @staticmethod    
    def is_integer(num):
        # We will count out the floats that are point zero
        
        if isinstance(num,float):
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False
        
    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})"

print(Item.is_integer(7.0))